# ZMC Edukasi HTML

Project ini dipakai untuk membuat halaman edukasi klinis HTML untuk **Zihan Medical Center (Wanaraja)** yang ramah pasien, siap offline, dan siap print.

## Tujuan
- Konten medis akurat, tetap elaboratif, dan mudah dipahami masyarakat umum.
- Tampilan khas brand ZMC, bukan template generik.
- Aman dipakai di Android + desktop, termasuk mode offline.
- Hasil print PDF rapi untuk kebutuhan edukasi pasien.

## Target Audiens
- Masyarakat umum lokal Garut (minimal literasi setara SMA).
- Bahasa: Indonesia sederhana, kalimat pendek, tidak menggurui.
- Nuansa lokal: boleh pakai istilah/konteks Sunda ringan agar terasa dekat.

## Brand Direction (Default)
Nama gaya: **Poster Merah ZMC**
- Dominan merah-putih ala poster IG ZMC.
- Headline tebal, visual tegas, tetap nyaman untuk baca panjang.
- Aksen hitam/navy tipis untuk menjaga kontras.
- Detail dekoratif halus (dot/grid/shape), tidak berlebihan.

## Konten Makanan Lokal
- Untuk topik yang relevan (contoh: lambung), pakai contoh konkret makanan lokal.
- Contoh wajib muncul sesuai konteks: `bala-bala`, `gehu`, `pepes`, `seblak`, `kopi tubruk`, dll.
- Selalu bagi kategori jelas: **lebih aman** vs **perlu dibatasi**.

## Alur Kerja Standar
1. Riset topik medis dari sumber kredibel terbaru (Kemenkes, WHO, IDAI, CDC bila relevan).
2. Tulis konten edukasi pasien + bagian wajib red flags (`Kapan harus ke dokter/IGD`).
3. Bangun halaman single-file HTML (vanilla, aksesibel keyboard, mobile-first).
4. Tambahkan ilustrasi kontekstual dan fallback offline.
5. QA dan bugfix: viewport, dark/light theme, print PDF, dan mode offline.

## Standar Kedalaman Konten
- Untuk topik utama (mis. MPASI/tumbuh-kembang), konten wajib **padat-elaboratif**, tidak boleh terasa ringkasan tipis.
- Larangan repetisi: satu pesan utama tidak boleh diulang lintas section dengan wording yang sama.
- Setiap section wajib punya fungsi unik (contoh: red flags, feeding rules, GTM, growth, development).
- Cara jaga agar tidak terlalu singkat:
  - Tiap section minimal berisi: konteks singkat, langkah praktis, dan kapan perlu evaluasi medis.
  - Sertakan contoh lokal yang relevan (menu, kebiasaan harian, hambatan umum orang tua).
  - Tambahkan catatan kondisi khusus (prematur, kronis, alergi berat) pada bagian yang relevan.

## Struktur Wajib MPASI/Tumbuh Kembang
1. Ringkasan singkat
2. Red flags (kapan ke dokter/IGD)
3. 7 Pesan Emas
4. Tab usia MPASI
5. Feeding rules
6. Pengenalan makanan baru
7. GTM troubleshooting
8. Pemantauan pertumbuhan
9. Pemantauan perkembangan
10. Resep lokal + makanan dibatasi
11. Anemia + sanitasi
12. Mitos vs fakta
13. FAQ singkat
14. Rujukan

## Icon Strategy (Default)
- Gunakan **Bootstrap Icons CDN** untuk percepatan UI.
- Wajib siapkan **fallback ikon lokal** (inline SVG) untuk ikon kritikal.
- Pattern implementasi yang disarankan:
  - `<i class="bi bi-... icon-cdn" aria-hidden="true"></i>`
  - `<svg class="icon-local" aria-hidden="true"><use href="#icon-id"></use></svg>`
- Jika CDN gagal, aplikasi harus otomatis menampilkan ikon fallback lokal.

## Ilustrasi (Non-AI Workflow)
- Gunakan ilustrasi lokal berbasis SVG/CSS handcrafted atau icon-led cards.
- Simpan aset visual di `assets/topics/<slug>/` atau inline langsung di HTML.
- Utamakan aset lokal agar halaman tetap berguna saat offline.
- Hero default harus **compact**: mobile `150-180px`, desktop `220-260px`.
- Hindari hero art besar yang mendorong konten utama terlalu ke bawah.
- Hero boleh ringkas, tetapi isi edukasi utama di bawah hero harus tetap panjang dan lengkap.

## Larangan Pipeline Default
- Jangan gunakan image generation API untuk alur kerja standar project ini.
- Semua visual harus reproducible di mesin lokal tanpa API key.

## Struktur Repo
```text
codex_edukasi/
  README.md
  AGENTS.md
  topics/
  assets/
    zmc-logo.jpeg
    topics/
      <slug>/
```

## Standar Output Halaman
- Single file HTML (tanpa build tools).
- Header sticky (logo + judul + tombol tema).
- Quick chips, konten utama, red flags, FAQ (opsional), footer klinik.
- Tombol `Print / Save PDF` sebagai fitur sekunder di bagian bawah.
- `@media print` rapi, kontras cukup, dan tidak memotong bagian penting.
