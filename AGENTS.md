# AGENTS.md

## Mission
Bangun halaman edukasi klinis HTML untuk **Zihan Medical Center Wanaraja** yang:
- kontennya akurat dan mudah dipahami pasien,
- desainnya khas, tetapi tidak generik dan tidak terasa seperti template AI,
- aman untuk mobile Android dan desktop,
- siap print ke PDF,
- tetap berguna saat offline.

## Non-Negotiables
- UI boleh berubah, tetapi materi inti tidak boleh dipangkas, dipindah keluar dari isi edukasi utama, atau diringkas berlebihan hanya demi tampilan.
- Area yang paling berat dibaca harus tetap hampir murni teks.
- Ikon, visual, dan callout dipakai untuk membantu pembacaan isi utama, bukan sekadar dekorasi tombol atau footer.
- Jangan menyelesaikan masalah "halaman terasa plain" dengan memindahkan materi menjadi teks panjang di dalam kartu, box, atau SVG.

## Default Workflow
### 1. Research internet dulu
- Wajib pakai sumber kredibel dan terbaru.
- Prioritas sumber: Kemenkes RI, WHO, UNICEF, IDAI, CDC.
- Simpan tautan rujukan di akhir konten.

### 2. Susun konten medis
- Bahasa Indonesia awam, target SMA, tidak menggurui.
- Nuansa lokal Sunda ringan boleh dipakai bila membantu.
- Tiap section minimal memuat konteks singkat, langkah praktis, dan kapan evaluasi medis.
- Wajib ada bagian `Kapan harus ke dokter/IGD`.
- Tambahkan catatan untuk kondisi khusus seperti prematur, penyakit kronis, atau alergi berat.
- Saat revisi UI, pertahankan semua materi penting dan urutan logika edukasi.

### 3. Bangun HTML single-file
- Vanilla HTML/CSS/JS.
- Mobile-first, responsive, aksesibel keyboard.
- Offline-ready dengan fallback logo, ikon, dan visual.
- Fokus utama tetap pada scanability isi edukasi, bukan pada dekorasi layout.

## QA terpisah dari flow bikin HTML
- QA dilakukan setelah HTML stabil, bukan disatukan dengan proses menyusun konten dan layout.
- Jangan anggap halaman selesai hanya karena file HTML sudah jadi.
- Tahap QA wajib mencakup viewport, keyboard, print preview / Save PDF, mode offline, dan fallback ikon.
- Gunakan skill `playwright`, `pdf`, dan `screenshot` saat tahap QA memang membutuhkan itu.

## Large File Write Strategy
- Jika patch gagal karena ukuran input, tulis file secara chunked.
- Jangan memendekkan atau menghapus detail hanya karena batas tooling.
- Urutan fallback wajib: kerangka -> section inti -> section lanjutan -> script -> QA.
- Setelah chunked write selesai, cek ulang anchor, heading, dan nomor section.

## Design Direction
Nama gaya dasar: **Poster Merah ZMC**

Artinya:
- merah-putih tetap dominan dan brand-fit,
- headline tegas dan kontras tinggi,
- aksen hitam/navy tipis boleh dipakai seperlunya,
- tetapi layout harus terasa seperti halaman edukasi klinis, bukan landing page promosi.

### Editorial Clinical Default
Untuk implementasi UI, gunakan guardrail `uncodixify` sebagai standar praktis:
- pilih layout yang normal, bersih, dan mudah dipindai,
- gunakan satu keluarga font sans lokal/offline yang konsisten,
- pakai radius kecil, border jelas, shadow tipis,
- section title langsung ke isi tanpa copy dekoratif,
- visual harus fungsional dan mendukung edukasi.

### Hard Rules
- Jangan pakai hero SaaS generik.
- Jangan pakai wallpaper yang tile atau repeating.
- Jangan memaksa 3 kolom di layar sempit.
- Jangan biarkan CTA kecil; target sentuh minimal sekitar `44px`.
- Gunakan satu mode warna terang saja; kontras wajib lolos.
- Jangan buat varian tema kedua atau kontrol pergantian tema.
- Tombol `Print / Save PDF` harus berada di bawah sebagai secondary CTA.
- Ilustrasi wajib reproducible tanpa API key dan tetap tampil saat offline.
- Hero wajib compact:
  - mobile `150-180px`
  - desktop `220-260px`
- Pelanggaran hero compact dianggap QA fail.
- Jangan pakai hero art besar yang mendorong konten terlalu jauh ke bawah.

### Explicit UI Bans
- gradient dekoratif besar yang hanya jadi hiasan,
- glassmorphism, glow, blur shell, atau floating panel,
- pill overload,
- mixed heading fonts atau serif-premium shortcut,
- eyebrow labels, `small` header dekoratif, atau status chip non-fungsional,
- hover transform,
- kartu "premium" dengan shadow dramatis,
- dashboard AI look seperti KPI grid, control room, atau right rail dekoratif.

## Hero Guardrail
- Hero hanya untuk orientasi cepat.
- Isi hero dibatasi ke headline singkat, ringkasan pendek, dan maksimal 2-3 poin inti.
- Jangan isi hero dengan paragraf panjang, checklist kedua, note tambahan, ilustrasi besar, atau rangkuman ulang dari section-section bawah.
- Jika hero sudah membuat user terasa "buka file lalu langsung disuruh baca banyak", berarti komposisinya gagal.

## Rhythm and Density Guardrail
- Jangan ulang pola visual section yang sama terus-menerus.
- Variasikan hierarchy antarsection dengan perbedaan density, layout, accent bar, list emphasis, atau callout placement.
- Tidak semua section harus mengikuti pola "judul + paragraf pengantar + grid kartu + callout".
- Jika semua border, radius, shadow, dan warna permukaan terasa sama terus, hierarchy visual dianggap datar.

## Main Content Guardrail
- Isi edukasi utama tetap didominasi teks yang rapi dan mudah dipindai.
- Gunakan ikon CDN/fallback di konten inti seperti cek napas, cek minum, tanda bahaya, rawat rumah, dan kapan ke dokter/IGD bila itu membantu pembacaan cepat.
- Jangan menaruh hampir semua ikon hanya di toolbar, CTA bawah, atau footer.
- Jika perlu visual bantuan, letakkan sebagai pemecah beban baca di tengah alur teks, bukan sebagai blok besar yang mengulang isi.

## Illustration + Icon Rules
- Minimal 1 visual edukasi per halaman; 2-4 lebih ideal bila memang membantu.
- Utamakan SVG/CSS handcrafted lokal atau foto lokal yang sudah ada.
- Visual harus tetap tampil saat file dibuka langsung (`file://`).
- Bootstrap Icons CDN boleh dipakai, tetapi ikon kritikal wajib punya fallback inline SVG.
- Wajib ada runtime check untuk mengaktifkan mode fallback ikon jika CDN gagal.
- Visual harus memecah beban baca, bukan memindahkan teks panjang ke dalam kotak atau SVG.
- Hindari ilustrasi dengan terlalu banyak label kecil yang sulit dibaca di mobile.
- Dorong diagram sederhana, pointer, langkah cek cepat, atau highlight risiko yang bisa dipahami sekilas.

## Mandatory Clinic Config
Setiap HTML wajib punya blok config ini:

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
- Hindari jargon medis tanpa penjelasan singkat.
- Masukkan konteks lokal Sunda jika relevan, terutama untuk pola makan dan kebiasaan harian.

## Page Structure Standard
1. Sticky header
2. Ringkasan 1 kalimat
3. Quick chips anchor
4. Isi edukasi utama
5. Red flags
6. FAQ singkat bila perlu
7. CTA bawah termasuk `Print / Save PDF`
8. Footer klinik

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
- Gunakan heading berurutan `h1 -> h2 -> h3`.
- Fokus keyboard harus terlihat.
- Tab, accordion, dan tombol harus bisa dioperasikan keyboard.
- Tambahkan `@media print` untuk:
  - sembunyikan kontrol non-esensial,
  - hindari pemotongan kartu dengan `break-inside: avoid`,
  - naikkan kontras teks.

## QA Bugfix Checklist
1. Wallpaper/texture tidak repeating.
2. Grid pakai `repeat(auto-fit, minmax(...))`.
3. Tidak ada overflow horizontal.
4. Tinggi kartu tidak fixed jika tidak perlu.
5. Tab/accordion punya ARIA + keyboard support.
6. Hero tidak menyisakan dead space besar, panel kosong, atau beban baca berlebihan.
7. Hero tetap dalam rentang compact dan tidak memonopoli layar pertama.
8. Materi inti tidak hilang atau tergeser dari isi edukasi utama saat UI direvisi.
9. Section tidak terasa seperti deretan box identik dengan ritme visual datar.
10. Ikon masuk ke area konten inti bila memang membantu scanability.
11. SVG/visual tidak clipping, termasuk teks kecil di dalam ilustrasi.
12. Visual benar-benar memecah beban baca, bukan hanya teks dalam kotak.
13. Print tidak memotong bagian penting, termasuk hero atau callout utama.
14. Link footer berfungsi: WA, Maps, Instagram.
15. Tombol print berada di area bawah halaman.
16. Visual lokal tetap tampil saat offline.
17. Tidak ada ketergantungan external image API.
18. Ilustrasi tetap tampil saat file lokal dibuka langsung.
19. Ikon tampil normal saat online, dan fallback ikon aktif saat CDN gagal.
20. Copy medis, red flags, dan rujukan masih selaras dengan sumber resmi terbaru.
21. Artefak QA tersimpan: screenshot viewport + PDF print check.
22. Jika memakai chunked write, semua section tetap utuh.

## Common QA Failures
- `Layout rhythm`: hero kiri terlalu tinggi, panel kanan kosong, visual terlalu kecil, atau section setelah hero terasa seperti deretan box identik. Cek ulang proporsi hero, panjang headline, dan hierarchy antarsection sebelum menyatakan desain selesai.
- `Responsive/mobile`: chips, tabel, atau grid memaksa lebar layar; 3 kolom dipertahankan di viewport sempit; tombol terlalu kecil untuk disentuh. Uji di `360x800` dan turunkan kompleksitas layout bila scanability turun.
- `Illustration/SVG`: SVG terlihat aman di code, tetapi di browser jadi terlalu kecil, kepotong, atau teks internal tidak terbaca. Validasi ukuran aktual, clipping, dan apakah ilustrasi benar-benar membantu isi.
- `Accessibility`: komponen interaktif bisa diklik mouse tetapi focus ring tidak terlihat, state `aria-expanded` tidak sinkron, atau keyboard navigation berhenti di tengah. Uji `Tab`, `Shift+Tab`, `Enter`, `Space`, `ArrowUp/Down`, `Home`, `End`.
- `Print/PDF`: hero, callout, atau tabel pecah jelek antar halaman; kontrol non-esensial masih tercetak; kontras turun saat print. Jika perlu, sederhanakan versi print, bukan memaksa layout layar ikut tercetak utuh.
- `Offline/fallback`: halaman lolos di HTTP lokal tetapi gagal saat asset lokal hilang atau CDN ikon mati. Jangan hanya cek online; verifikasi fallback logo, ikon, dan ilustrasi lokal.
- `file:// caveat`: jika tooling browser memblokir `file://`, jangan anggap cek offline selesai. Lakukan verifikasi lewat asset lokal dan forced fallback query, lalu catat keterbatasannya di hasil QA.
- `Medical/content drift`: layout sudah rapi tetapi isi melenceng tipis dari sumber resmi, misalnya batas evaluasi gejala, red flags pneumonia, batas obat OTC anak, atau rujukan yang tidak benar-benar mendukung copy. QA akhir harus membaca ulang isi kritis, bukan hanya melihat tampilan.

## Tool-Specific QA
### Playwright
- Buka halaman lokal di `topics/*.html`.
- Uji viewport `360x800`, `768x1024`, `1366x768`.
- Verifikasi tidak ada horizontal scroll.
- Uji `Tab`, `Shift+Tab`, `Enter`, `Space` pada elemen interaktif.
- Simpan screenshot final ke `assets/qa/`.

### PDF
- Jalankan print check mode `@media print`.
- Validasi heading, body text, callout, dan tabel tetap kontras.
- Validasi bagian penting tidak terpotong antar halaman.
- Simpan PDF bukti uji ke `assets/qa/`.
- Jika print pecah jelek, sederhanakan layout versi print, terutama pada hero dan visual besar.

### Screenshot
- Simpan minimal:
  - `slug-mobile.png`
  - `slug-tablet.png`
  - `slug-desktop.png`

## Output Format per Task
Saat diminta membuat halaman baru, hasilkan:
1. Design direction singkat
2. Potongan token CSS utama
3. Blueprint section
4. Full `index.html`
5. Catatan penggunaan singkat

## Repository Notes
- Simpan halaman topik di `topics/`.
- Simpan aset lokal di `assets/`.
- Visual topik di `assets/topics/<slug>/`.
- Gunakan nama file slug, misalnya `diare-anak.html` atau `dbd-dewasa.html`.
