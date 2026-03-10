# ZMC Edukasi HTML

Repo ini dipakai untuk membangun halaman edukasi klinis HTML untuk **Zihan Medical Center Wanaraja**. Targetnya bukan landing page generik, tetapi lembar edukasi pasien yang akurat, enak dibaca, aman di Android dan desktop, siap print ke PDF, dan tetap berguna saat offline.

## Tujuan
- Konten medis akurat, jelas, dan mudah dipahami pasien.
- UI khas ZMC, tetapi tetap terasa normal, tenang, dan fungsional.
- Halaman single-file yang bisa dibuka lokal tanpa build step.
- Hasil print rapi untuk kebutuhan edukasi pasien.

## Prinsip Inti
- UI boleh berubah, tetapi materi inti tidak boleh dipangkas, dipindah keluar dari isi edukasi utama, atau diringkas berlebihan hanya demi tampilan.
- Area baca terberat tetap hampir murni teks agar mudah discan pasien dan keluarga.
- Visual, ikon, dan callout dipakai untuk membantu baca, bukan menggantikan isi utama.
- Halaman harus tetap berguna saat offline dan saat dibuka langsung dari `file://`.
- Repo ini memakai satu mode warna terang saja; jangan menambah parity tema atau toggle tema sebagai default.

## Audiens
- Pasien dan keluarga di Garut dengan target literasi setara SMA.
- Bahasa Indonesia sederhana, kalimat pendek, tidak menggurui.
- Konteks Sunda ringan boleh dipakai jika membantu pemahaman.

## Default Workflow
1. Riset internet dulu dari sumber resmi terbaru dan simpan tautan rujukan di akhir konten.
2. Susun konten medis lengkap tanpa memangkas materi penting, dengan section yang tidak repetitif secara isi maupun ritme baca.
3. Bangun HTML single-file yang mobile-first, aksesibel, dan offline-ready.
4. Lakukan QA sebagai tahap terpisah setelah HTML stabil, lalu perbaiki bug berdasarkan hasil verifikasi.

QA bukan bagian dari flow drafting HTML. Selesaikan konten dan layout dulu, lalu uji viewport, keyboard, print PDF, dan fallback offline/icon sebagai tahap verifikasi tersendiri.

## Sumber Prioritas
- Kemenkes RI / Ayo Sehat
- WHO
- UNICEF
- IDAI
- CDC

Simpan tautan rujukan di bagian akhir halaman. Untuk topik anak, utamakan red flags, durasi evaluasi, dan catatan kondisi khusus.

## Standar Konten
- Setiap section minimal memuat konteks singkat, langkah praktis, dan kapan perlu evaluasi medis.
- Wajib ada bagian `Kapan harus ke dokter/IGD`.
- Jika ada kondisi khusus seperti prematur, penyakit kronis, atau alergi berat, tambahkan catatan konsultasi.
- Topik besar seperti MPASI atau tumbuh kembang harus padat-elaboratif, bukan ringkasan tipis.
- Gunakan contoh lokal jika relevan, termasuk pola makan atau kebiasaan harian.
- Saat revisi UI, pertahankan urutan logika edukasi agar pasien tetap bisa mengikuti alur baca dari masalah ke tindakan.

## Arah UI
Gaya dasar repo ini tetap **Poster Merah ZMC**, tetapi eksekusinya harus lebih dekat ke **editorial klinis** daripada poster promosi.

Prioritas visual:
- Merah-putih tetap dominan dan cocok dengan identitas ZMC.
- Layout harus tenang, rapi, dan mudah dipindai.
- Heading tegas lewat hirarki dan bobot teks, bukan font display campur-campur.
- Surface flat dengan border jelas, radius kecil, dan shadow tipis.
- Gunakan satu mode warna terang saja; kontras wajib lolos.
- CTA klinik utama ada di hero: `WhatsApp Klinik` dan `Instagram Klinik`.
- CTA bawah tetap sekunder untuk `Print / Save PDF`; fokus utama tetap pada isi edukasi.

Guardrail anti-generik:
- Jangan pakai hero SaaS atau panel "premium".
- Jangan pakai gradient dekoratif besar, glassmorphism, glow, atau floating card shell.
- Jangan pakai pill berlebihan, eyebrow labels, atau status chip non-fungsional.
- Jangan pakai hover transform, animasi bouncy, atau layout yang terasa seperti dashboard AI.
- Jangan campur banyak keluarga font; pakai satu keluarga sans lokal/offline yang konsisten.

## Hero dan Ritme Section
- Hero hanya untuk orientasi cepat, bukan untuk memuat ulang seluruh isi halaman.
- Isi hero dibatasi ke headline singkat, ringkasan pendek, dan maksimal 2-3 poin inti.
- Hero wajib memuat maksimal 2 CTA klinik utama: `WhatsApp Klinik` dan `Instagram Klinik`.
- Jangan naikkan `Maps` atau `Print / Save PDF` ke hero.
- Hero tidak boleh berisi checklist kedua, note tambahan yang panjang, ilustrasi besar, atau rangkuman ulang section-section di bawahnya.
- Target hero tetap compact: mobile `150-180px`, desktop `220-260px`. Jika jauh melampaui ini, anggap sebagai kegagalan desain.
- Jangan ulang pola section yang sama terus-menerus. Variasikan hirarki dengan density, layout, accent bar, list emphasis, atau penempatan callout.
- Hindari semua section terasa seperti pola tetap "judul + paragraf + grid card + callout" dengan border, radius, shadow, dan surface yang sama terus.

## Density / Anti-Bacot
- Jangan buka section dengan paragraf meta panjang lalu diikuti 2-3 paragraf penjelas sebelum ada elemen scan-first.
- Kalau callout, card, strip, atau visual sudah menyampaikan poin inti, pangkas paragraf pengantar yang mengulang.
- Jangan beri bobot visual yang sama ke semua kalimat penting; pembaca harus cepat tahu mana yang perlu discan dulu.
- Mobile hero wajib tetap punya scan aid yang terlihat tanpa menunggu breakpoint desktop.
- Jangan biarkan semua pembuka section jatuh ke pola tetap "judul panjang + paragraf lead + grid + callout".
- Ikon CDN/fallback harus dipakai di body content bila membantu ritme baca, bukan menumpuk di header, CTA, dan footer.

## Ikon dan Visual Edukasi
- Minimal 1 visual edukasi per halaman; 2-4 lebih ideal bila memang membantu.
- Ikon CDN/fallback harus membantu isi edukasi utama, bukan hanya tombol/footer.
- Masukkan ikon pada area seperti cek napas, cek minum, rawat rumah, tanda bahaya, dan kapan ke dokter/IGD bila itu membantu scanability.
- Visual harus memecah beban baca, bukan memindahkan paragraf panjang ke dalam box atau SVG.
- Hindari SVG dengan terlalu banyak label kecil yang sulit dibaca di mobile.
- Utamakan diagram sederhana, pointer, langkah cek cepat, atau highlight risiko yang bisa dipahami sekilas.
- Ilustrasi harus reproducible tanpa API key dan tetap tampil offline.
- Bootstrap Icons CDN boleh dipakai, tetapi ikon kritikal wajib punya fallback inline SVG dan runtime check untuk mode fallback.

## Struktur Halaman
1. Sticky header
2. Hero / ringkasan singkat
3. CTA hero: `WhatsApp Klinik` + `Instagram Klinik`
4. Quick chips anchor
5. Isi edukasi utama
6. Red flags
7. FAQ singkat bila perlu
8. CTA bawah termasuk `Print / Save PDF`
9. Footer klinik

## Teknis Wajib
- Vanilla HTML/CSS/JS.
- Single file di `topics/`.
- Konfigurasi klinik wajib memakai `const ZMC`.
- `ZMC.whatsapp` dan `ZMC.instagram` dipakai untuk CTA hero dan footer.
- Bootstrap Icons CDN boleh dipakai, tetapi ikon kritikal wajib punya fallback inline SVG.
- Ilustrasi harus reproducible tanpa API key.
- `@media print` wajib menghindari card terpotong dan menjaga kontras.
- Logo, ikon, dan visual penting harus tetap berguna saat file dibuka lokal.

## Struktur Repo
```text
EdukasiZMC/
  README.md
  AGENTS.md
  topics/
    <slug>.html
    fixed/
      <slug>.html
    zmc-logo.jpeg
  assets/
    qa/
    topics/
      <slug>/
```

## QA Minimum
- Viewport `360x800`, `768x1024`, `1366x768`
- Tidak ada horizontal scroll
- Fokus keyboard terlihat
- Accordion/tab bisa dioperasikan keyboard
- CTA hero `WhatsApp Klinik` dan `Instagram Klinik` tampil jelas di mobile dan desktop
- Tombol `Print / Save PDF` tetap hanya ada di area bawah sebagai CTA sekunder
- Footer link WA, Maps, Instagram berfungsi
- Ikon CDN dan fallback lokal sama-sama aman
- Offline/fallback diverifikasi, termasuk caveat bila tooling memblokir `file://`
- Hero tetap compact dan tidak memonopoli tinggi layar
- Materi inti tetap utuh setelah revisi UI
- Section tidak terasa monoton secara ritme visual
- Visual edukasi membantu scanability, bukan sekadar teks dalam kotak
- Print A4 tidak memotong bagian penting
- Artefak QA disimpan di `assets/qa/`
- Skill `playwright`, `pdf`, dan `screenshot` dipakai saat QA memang butuh browser automation, print check, dan artefak visual

## Artefak Akhir
Untuk halaman yang selesai dikerjakan, minimal hasil akhirnya mencakup:
- file HTML di `topics/`
- screenshot mobile, tablet, desktop di `assets/qa/`
- PDF hasil print check di `assets/qa/`

Untuk revisi yang masih tahap review:
- simpan versi baru di `topics/fixed/`
- bedakan artefak QA dengan suffix `-fixed`
- biarkan file baseline di `topics/` tetap ada sampai versi staging disetujui

## Evaluasi 10 Maret 2026
- Beberapa halaman terbaru terasa penat karena density terlalu rata; terlalu banyak kalimat penting muncul dengan bobot visual serupa.
- Pembuka section masih sering terlalu panjang sebelum user mendapat elemen scan-first yang membantu orientasi cepat.
- Visual sudah ada, tetapi belum cukup memecah beban baca di bagian awal section.
- Ikon masih terlalu banyak terkonsentrasi di header, CTA, dan footer; body content perlu lebih aktif memakai ikon fungsional.
