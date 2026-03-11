# SVG to AI Image Audit Plan

## Goal

Tujuan plan ini bukan mengganti semua SVG besar menjadi AI image. Untuk use case "HTML dikirim ke pasien", strategi yang lebih aman adalah:

- ganti hanya visual orientasi atau hero yang tugasnya membangun kesan awal,
- pertahankan visual yang membawa instruksi, alur keputusan, checklist, atau label medis,
- simpan aset gambar utama secara lokal di `assets/topics/<slug>/` agar halaman tetap aman saat offline,
- pakai host permanen **Cloudinary** untuk URL publik, tetapi selalu pertahankan local fallback.

## Decision Rules

- `Replace with AI image`: cocok bila visual sekarang lebih berfungsi sebagai orientasi atau mood-setting daripada menyampaikan detail yang harus dibaca.
- `Keep as SVG/HTML`: cocok bila visual berisi langkah, proporsi, hotspot, timeline, atau checklist yang harus presisi dan mudah dipindai.
- `Remove/Merge`: cocok bila visual hanya mengulang informasi yang sudah ada di tempat lain.

## Audit Summary

- Total visual besar yang diaudit: `26`
- Kandidat diganti AI image: `6`
- Sebaiknya tetap SVG atau dibangun ulang sebagai HTML infografik: `19`
- Sebaiknya dihapus atau digabung: `1`

## Replace with AI Image

| File | Line | Visual | Why replace | Guardrail |
| --- | ---: | --- | --- | --- |
| `topics/diabetes-melitus-tipe-2-fixed.html` | 269 | Hero `4 fokus harian` | Fungsi utamanya orientasi awal. Konten 4 fokus sudah bisa tetap hidup di teks hero dan section bawah. | Jangan pindahkan teks 4 fokus ke dalam gambar. |
| `topics/hipertensi-dewasa.html` | 310 | Hero `cek tensi rutin` | Lebih cocok jadi foto/ilustrasi editorial pasien cek tensi di rumah. | Catat-tulis-kontrol tetap harus tampil di HTML, bukan di image. |
| `topics/lambung.html` | 880 | Hero `pemicu lambung + posisi lambung` | Visual sekarang campuran anatomi dan label pemicu, tetapi peran utamanya orientasi. Bisa jadi image editorial yang lebih natural. | Label pemicu tetap di HTML sebagai chips/callout, jangan dibakar ke image. |
| `topics/menurunkan-berat-badan.html` | 276 | Hero `plate + gerak + tidur` | Ini visual ringkas gaya poster. AI image bisa memberi kesan lebih manusiawi tanpa mengganggu isi inti. | Hindari tubuh "fitness ad" yang terlalu ideal atau vibe promosi. |
| `topics/tipes-fixed.html` | 244 | Hero `kapan curiga tipes` | Hero lebih baik jadi visual situasional pasien demam + perut tidak nyaman, sementara pola gejala tetap dibaca di copy hero. | Triad gejala dan arahan cek medis tetap di teks, bukan image. |
| `topics/fixed/nyeri-badan-lansia-fixed.html` | 324 | Hero `area nyeri umum pada lansia` | Hero saat ini duplikatif dengan diagram tubuh di section isi. Lebih cocok jadi image orientasi lansia dengan keluhan gerak. | Biarkan diagram hotspot yang presisi tetap ada di body section. |

## Keep as SVG or HTML Infographic

| File | Line | Visual | Why keep | Better improvement |
| --- | ---: | --- | --- | --- |
| `topics/asam-urat-dewasa.html` | 347 | `langkah aman saat flare` | Ini checklist tindakan aman, bukan ilustrasi dekoratif. | Bila perlu, refactor ke HTML list dengan ikon lokal. |
| `topics/demam-berdarah-dbd.html` | 343 | `hari sakit demam berdarah` | Timeline fase DBD harus presisi dan cepat discan. | Ubah ke timeline HTML bila ingin lebih fleksibel. |
| `topics/demam-berdarah-dbd.html` | 501 | `pantau 4 hal di rumah` | Ini checklist pemantauan yang harus terbaca jelas. | Pertahankan sebagai checklist visual atau HTML panel. |
| `topics/demam-berdarah-dbd.html` | 651 | `checklist 3M Plus` | Fungsinya instruksional dan berbentuk daftar tindakan rumah. | Lebih cocok jadi checklist HTML print-friendly. |
| `topics/diabetes-melitus-tipe-2-fixed.html` | 335 | `3 sinyal awal diabetes` | Ini ringkasan gejala yang harus dibaca, bukan dilihat sekilas saja. | Bisa jadi stack card HTML. |
| `topics/diabetes-melitus-tipe-2-fixed.html` | 389 | `isi piring diabetes` | Proporsi piring lebih aman bila tetap diagram terkontrol. | Boleh hybrid dengan foto lokal, tapi label tetap di HTML. |
| `topics/diabetes-melitus-tipe-2-fixed.html` | 540 | `cek kaki 4 hal` | Pemeriksaan kaki butuh label yang spesifik dan aman dibaca. | Bila diganti, gunakan diagram statis plus overlay HTML, bukan AI murni. |
| `topics/gizi-anak-6bulan-5tahun.html` | 188 | `proporsi isi piring anak` | Ini edukasi proporsi, jadi presisi lebih penting daripada estetika. | Bisa dibikin versi HTML/CSS agar lebih responsif. |
| `topics/hipertensi-dewasa.html` | 548 | `garam tersembunyi di dapur` | Isi utamanya daftar contoh makanan dan pengganti rasa. | Ubah ke 2 kolom HTML dengan heading tegas. |
| `topics/hipertensi-dewasa.html` | 603 | `1 hari yang lebih ramah tensi` | Timeline kebiasaan harian lebih efektif sebagai diagram atau HTML. | Pertahankan scan-first structure. |
| `topics/lambung-saat-puasa.html` | 601 | `alur buka -> makan -> tegak` | Ini alur perilaku yang jelas, dan lebih kuat sebagai flowchart. | Boleh dipindah ke HTML flow strip agar print lebih rapi. |
| `topics/menurunkan-berat-badan.html` | 443 | `visual isi piring` | Sama seperti topik gizi dan diabetes, ini soal proporsi. | Keep as controlled infographic. |
| `topics/menurunkan-berat-badan.html` | 581 | `cek kebiasaan harian` | Checklist mingguan lebih berguna bila teksnya tetap tajam. | Refactor ke checklist HTML bila mau lebih ringan. |
| `topics/tipes-fixed.html` | 335 | `jalur penularan tifoid` | Ini menjelaskan rantai penularan, bukan sekadar hiasan. | Bisa dibuat sebagai flow HTML dengan 3 node besar. |
| `topics/tipes-fixed.html` | 416 | `alur kapan memeriksakan dugaan tipes` | Ini decision flow; AI image tidak cocok untuk logika keputusan. | Pertahankan flowchart yang mudah discan. |
| `topics/tipes-fixed.html` | 457 | `pantau di rumah` | Checklist pemantauan harus tetap eksplisit. | Rebuild as checklist HTML bila perlu. |
| `topics/fixed/nyeri-badan-lansia-fixed.html` | 402 | `area nyeri umum pada lansia` | Ini diagram hotspot yang lebih presisi daripada AI image. | Jadikan satu-satunya diagram tubuh utama jika hero diganti. |
| `topics/fixed/nyeri-badan-lansia-fixed.html` | 652 | `latihan ringan aman` | Pose latihan harus aman dan konsisten; AI mudah salah postur. | Lebih aman tetap diagram atau foto referensi yang dikurasi. |
| `topics/fixed/nyeri-badan-lansia-fixed.html` | 772 | `checklist rumah aman` | House safety butuh penanda yang bisa dibaca cepat. | HTML floor tips atau diagram statis tetap lebih aman. |

## Remove or Merge

| File | Line | Visual | Why remove or merge | Replacement direction |
| --- | ---: | --- | --- | --- |
| `topics/lambung-saat-puasa.html` | 538 | Hero `alur buka, jeda, tegak` | Informasinya mengulang flow figure di section `#alur`. Untuk hero compact, ini terlalu dekat dengan isi visual yang sama. | Hapus visual hero ini, atau ganti dengan 3 chips HTML singkat tanpa diagram besar. |

## Recommended Scope

### Wave 1

Fokus ke kandidat yang paling aman diganti tanpa menurunkan kualitas edukasi:

1. `topics/hipertensi-dewasa.html`
2. `topics/diabetes-melitus-tipe-2-fixed.html`
3. `topics/lambung.html`
4. `topics/menurunkan-berat-badan.html`

### Wave 2

Lanjut ke kandidat yang butuh perhatian lebih pada nuansa klinis:

1. `topics/tipes-fixed.html`
2. `topics/fixed/nyeri-badan-lansia-fixed.html`

### Do Not Batch-Replace

Jangan membuat prompt massal untuk semua visual checklist, timeline, alur keputusan, atau proporsi piring. Itu akan menurunkan scanability dan membuat file pasien jadi lebih "cantik" tapi kurang berguna.

## Asset Integration Plan

### File placement

- Simpan gambar final di `assets/topics/<slug>/`
- Gunakan format utama `webp`
- Sediakan fallback `jpg` atau `png` bila perlu
- Gunakan nama default `assets/topics/<slug>/<slug>-hero.webp`

### HTML integration

- Gunakan config `TOPIC_MEDIA.hero` dengan `remote` + `local`
- Pertahankan `alt` yang informatif
- Jangan taruh teks medis penting di dalam image
- Pertahankan ukuran hero compact sesuai guardrail repo
- Saat online, `remote` boleh diprioritaskan
- Saat offline atau remote gagal, `local` wajib dipakai otomatis

### Hosting

- Host permanen workflow ini adalah **Cloudinary**
- Gunakan helper `scripts/cloudinary_upload.py`
- Temporary host seperti `0x0.st` hanya untuk test drive
- Ambil `secure_url` dari output helper untuk dimasukkan ke HTML

### Workflow status

Workflow resmi repo sekarang:

1. generate dengan skill `imagegen`
2. simpan asset lokal final
3. upload ke Cloudinary
4. ambil hyperlink `secure_url`
5. pasang URL ke HTML sebagai `remote`
6. pertahankan asset lokal sebagai `local`

## Prompt Pack Plan

Langkah berikutnya adalah membuat prompt pack hanya untuk kandidat `Replace with AI image`, lalu menjalankan workflow resmi repo di atas.

Tiap prompt nantinya perlu memuat:

- subject utama,
- setting lokal dan nada klinis,
- framing rasio gambar,
- larangan teks di dalam gambar,
- larangan gaya promosi, rumah sakit mewah, dan stock-photo generik,
- arahan warna agar tetap cocok dengan gaya `Poster Merah ZMC`.

## QA After Replacement

- Cek viewport `360x800`, `768x1024`, `1366x768`
- Cek tidak ada horizontal scroll
- Cek hero tetap compact
- Cek print preview agar image tidak memotong section penting
- Cek online memakai `remote`
- Cek offline dengan aset lokal
- Cek fallback ketika `remote` gagal dimuat
- Simpan artefak QA ke `assets/qa/` dengan suffix yang sesuai
