# Audit Kebacotan dan Penat Mata `topics/*.html`

Tanggal: 13 Maret 2026  
Lokasi audit: `topics/`  
Jumlah file: 12 HTML

## Cakupan

- Fokus audit ini sempit: kebacotan copy, density visual, ritme section, dan potensi penat mata.
- Audit ini tidak menilai ulang akurasi medis, keyboard flow, print, atau offline fallback.
- Temuan di bawah menggabungkan baca source HTML dan render headless pada `1366x768` serta `360x800`.

## Metode Singkat

- Struktur: total kata, jumlah section, jumlah lead section, rata-rata panjang lead, pola lead formulaik, jumlah blok card/callout.
- Render: tinggi hero desktop/mobile, overflow horizontal, dorongan konten utama ke bawah, dan variasi signature section.
- Interpretasi:
  - `Kebacotan` tinggi = isi cenderung membuka section dengan lead formulaik/panjang, atau paragraf penjelas terlalu sering mengulang fungsi visual.
  - `Penat mata` tinggi = hierarchy visual terlalu rata, hero terlalu berat, atau terlalu banyak blok dengan bobot visual setara.

## Ringkasan Eksekutif

- Prioritas revisi tertinggi: `gizi-anak-6bulan-5tahun.html`, `demam-berdarah-dbd.html`, `tipes.html`.
- Prioritas menengah: `batuk-pilek-anak.html`, `diabetes-melitus-tipe-2.html`, `menurunkan-berat-badan.html`, `nyeri-badan-lansia.html`, `lambung.html`.
- Relatif paling rapi dan paling anti-bacot saat ini: `asam-urat-dewasa.html`, `gorengan-harian.html`.
- Paling seimbang antara konten panjang dan ritme baca: `hipertensi-dewasa.html`, lalu `pusing-dewasa.html`.

## Temuan Lintas Halaman

1. Pola lead `Konteks: ... Langkah praktis: ... Kapan evaluasi medis ...` adalah penyumbang kebacotan terbesar. Saat dipakai di hampir semua section, halaman terasa seperti membaca template editorial yang diulang.
2. Banyak halaman sudah punya visual edukasi, tetapi visual breaker belum selalu datang cukup awal. Akibatnya pembaca tetap bertemu blok lead dan card sebelum dapat orientasi scan-first yang tegas.
3. Beberapa halaman panjang sebenarnya masih nyaman karena variasi komponennya tinggi. Masalah utama repo ini bukan panjang semata, tetapi panjang yang dibagi ke blok-blok dengan bobot visual mirip.
4. Hero mobile masih sering melampaui guardrail compact. Ini memperberat kesan pertama bahkan sebelum user masuk ke isi edukasi utama.
5. Halaman terbaik di repo ini cenderung memakai bahasa langsung, lead singkat, dan pola compare/strip/decision yang cepat dipindai tanpa terasa seperti deretan kartu identik.

## Hero Compact Fail yang Berkontribusi ke Penat Mata

- `batuk-pilek-anak.html`: hero mobile `273px`
- `gizi-anak-6bulan-5tahun.html`: hero mobile `278px`
- `lambung.html`: hero mobile `201px`, hero desktop `315px`
- `menurunkan-berat-badan.html`: hero mobile `308px`
- `hipertensi-dewasa.html`: hero mobile `193px` (mild fail, bukan yang paling berat)

## Ranking Cepat per Halaman

| File | Kebacotan | Penat mata | Sinyal utama |
| --- | --- | --- | --- |
| `gizi-anak-6bulan-5tahun.html` | Tinggi | Sangat tinggi | `3125` kata, `15` lead formulaik, `69` blok card-like, hero mobile `278px` |
| `demam-berdarah-dbd.html` | Tinggi | Tinggi | `2573` kata, `11/11` lead formulaik, callout sangat banyak, signature section berulang |
| `tipes.html` | Tinggi | Tinggi | `2909` kata, `12/12` lead formulaik, `23` blok card-like, ritme section terlalu seragam |
| `batuk-pilek-anak.html` | Sedang | Sedang-tinggi | `10/10` lead formulaik, hero mobile `273px`, layout cukup variatif tapi pembuka terlalu scripted |
| `diabetes-melitus-tipe-2.html` | Sedang-tinggi | Sedang | `2636` kata, paragraf cukup panjang, ritme visual masih tertolong variasi layout |
| `menurunkan-berat-badan.html` | Sedang-tinggi | Sedang-tinggi | hero mobile `308px`, beberapa blok tengah panjang, visual breaker belum cukup cepat |
| `nyeri-badan-lansia.html` | Sedang | Sedang | pembuka section tertentu terlalu panjang, tetapi variasi visual bagus |
| `lambung.html` | Sedang | Sedang | hero terlalu tinggi, callout padat, section sedikit tapi opening masih cukup berat |
| `pusing-dewasa.html` | Sedang | Rendah-sedang | banyak paragraf, tetapi scan-grid/track-grid cukup membantu ritme |
| `hipertensi-dewasa.html` | Rendah-sedang | Rendah-sedang | konten panjang, tetapi variasi komponen paling sehat di repo |
| `asam-urat-dewasa.html` | Rendah | Rendah | bahasa langsung, lead singkat, compare-strip efektif |
| `gorengan-harian.html` | Rendah | Rendah | ritme paling hemat, scope jelas, hampir tidak ada kesan template |

## Audit Per File

### Prioritas Tinggi

#### `gizi-anak-6bulan-5tahun.html`

- Halaman ini paling rentan terasa melelahkan karena panjangnya memang besar dan ritme visualnya belum cukup memecah beban baca.
- Masalah utamanya bukan materi terlalu banyak, tetapi terlalu banyak section dibuka dengan lead formulaik lalu dilanjutkan grid card lagi.
- `69` blok card-like untuk satu halaman membuat banyak poin penting tampil dengan bobot visual yang mirip.
- Hero mobile `278px` membuat opening terasa penuh sebelum user benar-benar masuk ke isi inti.
- Arah revisi:
  - pertahankan seluruh struktur wajib, tetapi pendekkan lead menjadi 1 kalimat bila scan-first sudah ada;
  - bedakan section berat dengan pola selain grid card, misalnya strip langkah, scan row, split text, atau accordion terarah;
  - jangan biarkan `growth`, `development`, `resep`, `anemia`, `kebersihan` semuanya terasa seperti blok saudara kembar.

#### `demam-berdarah-dbd.html`

- Materinya kuat, terutama section fase hari `1-7`, tetapi hampir semua pembuka section memakai formula yang sama dan panjang.
- `11/11` lead section formulaik membuat ritme editorial terasa mekanis.
- Kombinasi callout, grid, dan section-head yang sama bobotnya membuat halaman cepat terasa "serius terus" tanpa cukup jeda.
- Section fase adalah contoh yang relatif berhasil karena punya struktur khusus dan tidak sekadar grid card biasa.
- Arah revisi:
  - pertahankan detail medis, tetapi pangkas pembuka yang mengulang isi callout atau diagram;
  - gunakan lebih banyak scan-first sebelum paragraf penjelas;
  - beri kontras hierarchy lebih tegas antara fase, red flags, rawat rumah, dan pencegahan.

#### `tipes.html`

- Ini halaman yang sangat informatif, tetapi terasa verbal dan formulaik hampir di semua section penting.
- `12/12` lead section memakai pola serupa, dan beberapa lead mencapai `34-47` kata sebelum user mendapat elemen scan-first.
- Mid-page juga cukup padat karena banyak block edukasi masih dibuka dengan narasi konteks dulu, baru decision/grid.
- Halaman ini tidak seburuk `gizi` secara jumlah card, tetapi rasa repetitifnya lebih terasa karena nada pembuka tiap section sangat mirip.
- Arah revisi:
  - ringkas lead ke kalimat pembeda yang benar-benar perlu;
  - pindahkan sebagian fungsi orientasi ke strip/decision summary;
  - pertahankan seluruh topik, tetapi variasikan bentuk pembuka antarsection.

### Prioritas Menengah

#### `batuk-pilek-anak.html`

- Layout dasarnya cukup variatif, jadi problem utamanya lebih ke kebacotan pembuka daripada monoton layout.
- `10/10` lead section formulaik membuat halaman terasa sangat "diceramahkan" di awal tiap blok.
- Hero mobile `273px` ikut menambah beban opening.
- Arah revisi:
  - potong formula `Konteks / Langkah praktis / Kapan evaluasi` di sebagian besar section;
  - jaga orientasi cepat lewat cek napas, durasi, dan red flag, bukan lewat lead yang panjang.

#### `diabetes-melitus-tipe-2.html`

- Halaman ini tidak terlalu monoton secara layout; signature antarsection cukup beragam.
- Masalah utamanya adalah beberapa paragraf dan lead cukup panjang, sehingga bacaannya lebih berat daripada yang perlu.
- Section diet, kaki, dan kondisi khusus cukup kaya isi, tetapi masih terasa "jelaskan dulu baru scan".
- Arah revisi:
  - pecah paragraf panjang menjadi poin scan-first;
  - pertahankan detail penting, tetapi kurangi kalimat transisi yang mengulang pesan card/callout.

#### `menurunkan-berat-badan.html`

- Hero mobile `308px` adalah masalah visual paling jelas di halaman ini.
- Section tengah seperti `mulai`, `gerak`, dan `pantau` cukup panjang secara narasi sebelum ritmenya benar-benar lega.
- Variasi layout ada, tetapi belum cukup cepat menyelamatkan opening dan beberapa section panjang.
- Arah revisi:
  - kecilkan hero secara nyata;
  - lebih cepat masuk ke scan list atau agenda;
  - kurangi kalimat pengantar di blok yang sudah punya checklist atau metric panel.

#### `nyeri-badan-lansia.html`

- Secara visual ini sebenarnya salah satu yang lebih hidup di repo.
- Masalahnya ada di pembuka tertentu yang terlalu panjang, terutama ringkasan awal dan beberapa section yang masih membuka dengan narasi lebar.
- Karena visual breaker cukup banyak, halaman ini tidak terasa sedatar `gizi` atau `tipes`.
- Arah revisi:
  - ringkas ringkasan awal;
  - pertajam section yang paling penting dulu dengan scan-first lebih awal.

#### `lambung.html`

- Jumlah section sedikit, jadi masalahnya bukan volume total, melainkan opening yang masih berat dan hero yang terlalu tinggi.
- Hero mobile `201px` dan desktop `315px` membuat kesan pertama lebih padat daripada yang perlu.
- Callout cukup banyak untuk halaman sesingkat ini, sehingga halaman bisa terasa "selalu mengingatkan" tanpa cukup ruang bernapas.
- Arah revisi:
  - kecilkan hero;
  - gabungkan beberapa callout yang fungsinya berdekatan;
  - percepat masuk ke pemisahan gejala dan red flags.

### Relatif Aman, Tetapi Tetap Bisa Dirapikan

#### `pusing-dewasa.html`

- Section pertama cukup panjang, tetapi penggunaan `track-grid`, `scan-grid`, dan `step-grid` menolong ritme baca.
- Ini contoh halaman yang masih panjang tetapi tidak terlalu membuat mata cepat lelah.
- Yang perlu dirapikan terutama pembuka section yang masih bisa dibuat lebih padat.

#### `hipertensi-dewasa.html`

- Ini salah satu referensi terbaik untuk ritme visual di repo.
- Walau kontennya panjang dan card-like block banyak, variasi komponennya paling sehat: metric, icon-grid, agenda, measure, signal, scan-row.
- Kekurangannya lebih minor: hero mobile `193px` masih sedikit terlalu tinggi, dan dua lead paling akhir masih terasa template.

### Referensi Positif

#### `asam-urat-dewasa.html`

- Bahasa paling langsung dan paling hemat.
- Hampir tidak ada rasa "meta lead" yang memaksa user melewati paragraf pembuka panjang dulu.
- Compare-strip dan pola plain-columns berhasil menjaga halaman tetap informatif tanpa jadi melelahkan.

#### `gorengan-harian.html`

- Ini salah satu halaman paling anti-bacot di repo.
- Scope topik jelas, lead singkat, dan pola compare/strip terasa pas dengan materi.
- Halaman ini bagus dijadikan referensi untuk tone yang lebih lugas dan tidak terlalu templated.

## Pola yang Perlu Dikurangi di Revisi Berikutnya

1. Jangan buka hampir semua section dengan kalimat tiga fungsi sekaligus: konteks, langkah praktis, dan kapan evaluasi.
2. Jangan biarkan visual utama section selalu jatuh ke `section-head + grid card + callout`.
3. Jangan pakai hero tinggi untuk "menampung ringkasan tambahan" yang sebenarnya bisa turun ke body content.
4. Jangan beri bobot visual yang sama ke semua pesan penting. Kalau semua pakai box, semuanya terasa sama penting, dan pembaca cepat lelah.
5. Kalau sudah ada tabel, scan row, timeline, signal grid, atau decision card, paragraf pengantarnya harus makin pendek, bukan ikut membesar.

## Pola yang Layak Dipakai Sebagai Acuan

1. Nada lugas ala `asam-urat-dewasa.html` dan `gorengan-harian.html`.
2. Variasi komponen ala `hipertensi-dewasa.html`.
3. Section spesifik yang benar-benar punya bentuk sendiri, seperti fase di `demam-berdarah-dbd.html`.
4. Visual breaker yang langsung membantu keputusan, bukan sekadar jadi ornamen sebelum paragraf panjang.

## Rekomendasi Urutan Backlog

1. Rapikan `gizi-anak-6bulan-5tahun.html`.
2. Rapikan `demam-berdarah-dbd.html`.
3. Rapikan `tipes.html`.
4. Perbaiki hero dan lead formulaik di `batuk-pilek-anak.html`.
5. Perbaiki hero dan section tengah di `menurunkan-berat-badan.html`.
6. Ringankan paragraf panjang di `diabetes-melitus-tipe-2.html`, `nyeri-badan-lansia.html`, dan `lambung.html`.

## Catatan Penutup

- Repo ini bukan kekurangan materi. Masalah utamanya adalah banyak halaman masih menyajikan materi yang benar dengan ritme yang terlalu seragam.
- Halaman panjang tidak otomatis gagal. Yang gagal adalah halaman panjang yang membuat pembaca merasa semua kalimat sama penting dan semua section dibuka dengan cara yang sama.
