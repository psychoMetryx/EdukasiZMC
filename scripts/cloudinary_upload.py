#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import mimetypes
import os
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Dict, Optional

try:
    import winreg  # type: ignore
except ImportError:  # pragma: no cover - non-Windows hosts
    winreg = None


ENV_VARS = (
    "OPENAI_API_KEY",
    "CLOUDINARY_CLOUD_NAME",
    "CLOUDINARY_API_KEY",
    "CLOUDINARY_API_SECRET",
)


def read_windows_user_env(name: str) -> Optional[str]:
    if winreg is None:
        return None
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Environment") as key:
            value, _ = winreg.QueryValueEx(key, name)
    except FileNotFoundError:
        return None
    except OSError:
        return None
    return value or None


def get_env(name: str) -> Optional[str]:
    return os.environ.get(name) or read_windows_user_env(name)


def build_signature(params: Dict[str, str], api_secret: str) -> str:
    joined = "&".join(f"{key}={params[key]}" for key in sorted(params))
    return hashlib.sha1(f"{joined}{api_secret}".encode("utf-8")).hexdigest()


def multipart_payload(fields: Dict[str, str], file_path: Path) -> tuple[bytes, str]:
    boundary = f"----ZMCCloudinary{int(time.time())}"
    chunks: list[bytes] = []
    for key, value in fields.items():
        chunks.extend(
            [
                f"--{boundary}\r\n".encode("utf-8"),
                f'Content-Disposition: form-data; name="{key}"\r\n\r\n'.encode("utf-8"),
                str(value).encode("utf-8"),
                b"\r\n",
            ]
        )

    mime_type = mimetypes.guess_type(file_path.name)[0] or "application/octet-stream"
    chunks.extend(
        [
            f"--{boundary}\r\n".encode("utf-8"),
            f'Content-Disposition: form-data; name="file"; filename="{file_path.name}"\r\n'.encode("utf-8"),
            f"Content-Type: {mime_type}\r\n\r\n".encode("utf-8"),
            file_path.read_bytes(),
            b"\r\n",
            f"--{boundary}--\r\n".encode("utf-8"),
        ]
    )
    return b"".join(chunks), boundary


def upload_with_curl(endpoint: str, fields: Dict[str, str], file_path: Path) -> str:
    curl_bin = shutil.which("curl.exe") or shutil.which("curl")
    if not curl_bin:
        raise RuntimeError("curl is not available for Cloudinary fallback upload")

    command = [curl_bin, "--silent", "--show-error", "--fail", "-X", "POST", endpoint]
    for key, value in fields.items():
        command.extend(["-F", f"{key}={value}"])
    command.extend(["-F", f"file=@{file_path}"])

    completed = subprocess.run(
        command,
        check=False,
        capture_output=True,
        text=True,
    )
    if completed.returncode != 0:
        raise RuntimeError(completed.stderr.strip() or "curl upload failed")
    return completed.stdout


def check_command() -> int:
    status: Dict[str, Dict[str, bool]] = {}
    for name in ENV_VARS:
        process_value = os.environ.get(name)
        user_value = read_windows_user_env(name)
        effective = process_value or user_value
        status[name] = {
            "process": bool(process_value),
            "user": bool(user_value),
            "effective": bool(effective),
        }

    status["notes"] = {
        "cloudinary_helper_uses_stdlib_only": True,
        "restart_may_be_needed_for_other_tools": True,
    }
    print(json.dumps(status, indent=2))
    return 0


def upload_command(args: argparse.Namespace) -> int:
    file_path = Path(args.file).resolve()
    if not file_path.is_file():
        print(json.dumps({"error": f"File not found: {file_path}"}))
        return 1

    cloud_name = get_env("CLOUDINARY_CLOUD_NAME")
    api_key = get_env("CLOUDINARY_API_KEY")
    api_secret = get_env("CLOUDINARY_API_SECRET")
    missing = [
        name
        for name, value in (
            ("CLOUDINARY_CLOUD_NAME", cloud_name),
            ("CLOUDINARY_API_KEY", api_key),
            ("CLOUDINARY_API_SECRET", api_secret),
        )
        if not value
    ]
    if missing:
        print(json.dumps({"error": "Missing Cloudinary env vars", "missing": missing}))
        return 1

    public_id = args.public_id or f"zmc/{args.slug}/{args.slug}-{args.role}"
    timestamp = str(int(time.time()))
    signed_params = {
        "overwrite": "true" if args.overwrite else "false",
        "public_id": public_id,
        "timestamp": timestamp,
    }
    signature = build_signature(signed_params, api_secret)

    fields = {
        **signed_params,
        "api_key": api_key,
        "signature": signature,
    }
    payload, boundary = multipart_payload(fields, file_path)
    endpoint = f"https://api.cloudinary.com/v1_1/{cloud_name}/image/upload"
    request = urllib.request.Request(
        endpoint,
        data=payload,
        headers={"Content-Type": f"multipart/form-data; boundary={boundary}"},
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=90) as response:
            body = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        error_body = exc.read().decode("utf-8", errors="replace")
        print(
            json.dumps(
                {
                    "error": "Cloudinary upload failed",
                    "status": exc.code,
                    "body": error_body,
                }
            )
        )
        return 1
    except urllib.error.URLError as exc:
        try:
            body = upload_with_curl(endpoint, fields, file_path)
        except RuntimeError as curl_exc:
            print(
                json.dumps(
                    {
                        "error": "Cloudinary upload failed",
                        "reason": str(exc.reason),
                        "curl_fallback": str(curl_exc),
                    }
                )
            )
            return 1

    try:
        parsed = json.loads(body)
    except json.JSONDecodeError:
        print(json.dumps({"error": "Unexpected Cloudinary response", "body": body}))
        return 1

    result = {
        "public_id": parsed.get("public_id"),
        "secure_url": parsed.get("secure_url"),
        "bytes": parsed.get("bytes"),
        "format": parsed.get("format"),
        "width": parsed.get("width"),
        "height": parsed.get("height"),
        "resource_type": parsed.get("resource_type"),
        "source_file": str(file_path),
    }
    print(json.dumps(result, indent=2))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Cloudinary helper for the ZMC AI image workflow.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("check", help="Check AI image workflow prerequisites.")

    upload_parser = subparsers.add_parser("upload", help="Upload a local file to Cloudinary.")
    upload_parser.add_argument("--file", required=True, help="Local image file path.")
    upload_parser.add_argument("--slug", required=True, help="Topic slug, for example hipertensi-dewasa.")
    upload_parser.add_argument("--role", default="hero", help="Asset role, defaults to hero.")
    upload_parser.add_argument("--public-id", help="Override the default Cloudinary public ID.")
    upload_parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Allow Cloudinary to overwrite an existing public ID.",
    )
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    if args.command == "check":
        return check_command()
    if args.command == "upload":
        return upload_command(args)
    parser.error(f"Unknown command: {args.command}")
    return 2


if __name__ == "__main__":
    sys.exit(main())
