# AGENTS.md

## Mission
Bangun halaman edukasi klinis HTML untuk **Zihan Medical Center Wanaraja** yang:
- kontennya akurat dan mudah dipahami pasien,
- desainnya khas (bukan template generik),
- aman untuk mobile Android + desktop,
- siap print ke PDF,
- tetap berguna saat offline.

## Default Workflow
1. **Research internet dulu**
   - Wajib gunakan sumber kredibel dan terbaru.
   - Prioritas sumber: Kemenkes RI, WHO, UNICEF, IDAI, CDC (jika relevan).
   - Simpan tautan rujukan di bagian akhir konten.
2. **Susun konten medis**
   - Bahasa Indonesia awam (target SMA), kalimat singkat, tidak menggurui.
   - Nuansa lokal Sunda ringan boleh dipakai agar lebih dekat ke pasien Garut.
   - Konten tetap elaboratif, jangan dipendekkan berlebihan.
   - Untuk topik utama, konten harus padat-elaboratif dan tidak terasa seperti ringkasan tipis.
   - Setiap section harus punya tujuan unik; hindari repetisi pesan yang sama lintas section.
   - Tiap section minimal memuat konteks singkat, langkah praktis, dan kapan perlu evaluasi medis.
   - Wajib ada bagian `Kapan harus ke dokter/IGD` (red flags).
   - Sertakan catatan: jika ada kondisi khusus (prematur, penyakit kronis, alergi berat), konsultasi dulu.
3. **Bangun HTML single-file**
   - Vanilla HTML/CSS/JS.
   - Mobile-first, responsive, aksesibel keyboard.
   - Footer klinik di bagian bawah, bukan fokus utama halaman.
4. **QA + bugfix pass**
   - Uji lebar 360px, 768px, 1366px.
   - Uji print preview (Save PDF).
   - Uji mode offline (asset fallback).
   - Gunakan skill `playwright` untuk validasi UI lintas viewport + interaksi keyboard.
   - Gunakan skill `pdf` untuk verifikasi hasil print (A4/Save PDF) dan potensi konten terpotong.
   - Gunakan skill `screenshot` untuk bukti QA (mobile, tablet, desktop) setelah bugfix.

## Large File Write Strategy (Hard Rule)
- Jika patch/tool gagal karena ukuran input, WAJIB tulis file secara chunked (append per bagian).
- Dilarang menyingkat, menghapus, atau mereduksi detail konten hanya karena batas tooling.
- Pertahankan target kedalaman konten sesuai section yang diminta user.
- Jika penulisan dipecah, urutan kerja wajib: kerangka -> section inti -> section lanjutan -> script -> QA.
- Setelah chunked write selesai, WAJIB lakukan verifikasi integritas: nomor section, anchor, dan heading tidak rusak.
- Jika terjadi fallback teknis, jelaskan singkat di update progres bahwa metode diubah ke chunked write, bukan ringkasan.

## Design Direction (Default)
Nama gaya: **Poster Merah ZMC**

Signatures:
- Dominan merah-putih, brand-fit dengan logo dan referensi IG ZMC.
- Headline tegas, kontras tinggi, tetap nyaman dibaca untuk konten panjang.
- Aksen hitam/navy tipis + detail dot/grid halus non-repeating.
- Jangan pakai tampilan SaaS generik.

### Hard Rules
- Jangan pakai pola hero SaaS generik.
- Jangan pakai wallpaper yang tile/berulang.
- Jangan memaksa 3 kolom di layar sempit.
- Jangan biarkan CTA kecil (target sentuh minimal ~44px).
- **Light theme wajib lolos kontras**: larang teks terang di background terang.
- Tombol `Print / Save PDF` diposisikan di area bawah (secondary CTA), bukan fokus utama header.
- Ilustrasi wajib reproducible tanpa API key dan tetap tampil saat offline.
- Hero wajib compact:
  - mobile `150-180px`
  - desktop `220-260px`
- Jangan pakai hero art besar yang mendorong konten terlalu jauh ke bawah.

## Mandatory Clinic Config
Setiap HTML wajib punya blok config JS berikut:

```js
const ZMC = {
  name: "Zihan Medical Center",
  tagline: "#ZMCGakNyuekinKamu",
  logoLocal: "zmc-logo.jpeg",
  logoFallback: "https://i.imgur.com/jzuguQE.jpeg",
  maps: "https://maps.app.goo.gl/CYpDhM1bGBnSf7D77",
  whatsapp: "https://api.whatsapp.com/send/?phone=%2B6282217180432&type=phone_number&app_absent=0&wame_ctl=1",
  instagram: "https://www.instagram.com/zihanmedicalcenter/?hl=en",
  address: "Jl. Kudang, Wanajaya, Wanaraja, Wanajaya, Garut, Kabupaten Garut, Jawa Barat 44183",
  phone: "+62 822-1718-0432",
  hours: "Senin - Minggu: 24 Jam"
};
```

## Localization Rule
- Gunakan bahasa Indonesia sederhana.
- Hindari jargon medis rumit tanpa penjelasan singkat.
- Masukkan contoh konteks lokal Sunda jika relevan, terutama pada pola makan/kebiasaan harian.

## Illustration Integration
- Minimal 1 visual edukasi per halaman; direkomendasikan 2-4.
- Sumber visual default: SVG/CSS handcrafted lokal atau foto lokal yang sudah ada.
- Jika pakai ilustrasi visual, utamakan tanpa teks keras agar teks bisa dikontrol di HTML.
- Wajib punya fallback lokal agar tetap tampil saat offline.
- Dilarang memakai image generation API sebagai pipeline default.

## Icon Integration
- Default icon set: **Bootstrap Icons CDN**.
- Ikon kritikal wajib punya fallback lokal (inline SVG): warning, check, telepon, lokasi, rumah sakit.
- Tampilan konten tidak boleh rusak jika CDN ikon gagal dimuat.
- Terapkan runtime check: jika icon font CDN tidak terbaca, aktifkan mode fallback lokal otomatis.

## Page Structure Standard
1. Sticky header (logo + judul topik + tombol tema)
2. Ringkasan 1 kalimat
3. Quick chips (anchor section)
4. Isi edukasi utama (cards/checklist/callouts/accordion)
5. Red flags (kapan ke dokter/IGD)
6. FAQ singkat (opsional)
7. CTA bawah termasuk tombol `Print / Save PDF`
8. Footer klinik (WA, Maps, IG, alamat, jam)

## Mandatory Structure for MPASI/Tumbuh Kembang
1. Ringkasan singkat
2. Red flags
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
13. FAQ
14. Rujukan

## Accessibility + Print
- Gunakan heading berurutan (`h1` -> `h2` -> `h3`).
- Fokus keyboard harus terlihat.
- Komponen interaktif (tab/accordion) harus bisa keyboard.
- Tambahkan `@media print`:
  - sembunyikan kontrol non-esensial,
  - hindari pemotongan kartu (`break-inside: avoid`),
  - naikkan kontras teks.

## QA Bugfix Checklist
1. Wallpaper/texture tidak repeating.
2. Grid pakai `repeat(auto-fit, minmax(...))`.
3. Tidak ada overflow horizontal.
4. Tinggi kartu tidak fixed jika tidak perlu.
5. Tab/accordion punya ARIA + keyboard support.
6. Print tidak memotong bagian penting.
7. Link footer berfungsi: WA, Maps, Instagram.
8. Dark/light theme parity valid (kontras teks aman).
9. Tombol print berada di area bawah halaman.
10. Visual lokal tetap tampil saat offline (dengan fallback).
11. Tidak ada ketergantungan external image API.
12. Ilustrasi tetap tampil saat file lokal dibuka langsung (`file://`).
13. Ikon tampil normal saat online, dan fallback ikon tampil saat CDN gagal.
14. Hero height sesuai rentang compact.
15. Artefak QA tersimpan: screenshot viewport + file PDF hasil print check.
16. Jika memakai chunked write, validasi semua section tetap utuh dan tidak ada bagian terpotong.

## Playwright Integration
- Skill `playwright` dianggap aktif untuk tugas QA halaman HTML.
- Minimum skenario otomatis:
  1. Buka halaman lokal topik di `topics/*.html`.
  2. Uji viewport `360x800`, `768x1024`, `1366x768`.
  3. Verifikasi tidak ada horizontal scroll.
  4. Navigasi keyboard (`Tab`, `Shift+Tab`, `Enter`, `Space`) pada elemen interaktif.
  5. Simpan screenshot final tiap viewport ke folder `assets/qa/`.
- Jika ada regresi aksesibilitas atau layout, lakukan bugfix lalu ulangi test Playwright.

## PDF Integration
- Skill `pdf` dianggap aktif untuk verifikasi layout cetak.
- Minimum skenario:
  1. Jalankan print check untuk mode `@media print` dan ekspor ke PDF.
  2. Validasi bagian penting tidak terpotong antar halaman.
  3. Validasi heading, body text, dan callout tetap kontras saat dicetak.
  4. Simpan PDF bukti uji ke folder `assets/qa/`.

## Screenshot Integration
- Skill `screenshot` dianggap aktif untuk dokumentasi hasil akhir QA.
- Minimum artefak:
  1. Screenshot viewport `360x800` (mobile).
  2. Screenshot viewport `768x1024` (tablet).
  3. Screenshot viewport `1366x768` (desktop).
  4. Nama file disarankan: `slug-mobile.png`, `slug-tablet.png`, `slug-desktop.png`.

## Output Format per Task
Saat diminta membuat halaman baru, hasilkan:
1. Design direction singkat (2-6 baris).
2. Potongan token CSS utama.
3. Blueprint section.
4. Full `index.html` (satu code block).
5. Catatan penggunaan singkat.

## Repository Notes
- Simpan halaman topik di folder `topics/`.
- Simpan aset lokal di folder `assets/`.
- Untuk visual topik, gunakan `assets/topics/<slug>/`.
- Gunakan nama file slug, contoh: `diare-anak.html`, `dbd-dewasa.html`.
