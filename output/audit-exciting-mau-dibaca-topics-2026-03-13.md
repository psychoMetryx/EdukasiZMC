# Audit "Exciting dan Mau Dibaca" untuk `topics/*.html`

Tanggal: 13 Maret 2026  
Scope: 12 halaman HTML di `topics/`  
Tujuan: mencari apa yang sudah bikin halaman terasa hidup, apa yang masih menahan minat baca, lalu merumuskan revisi yang reusable untuk batch berikutnya.

## Definisi Kerja

Untuk halaman edukasi klinis, "exciting" bukan berarti ramai atau promosi. Yang kita cari adalah halaman yang:

- cepat terasa relevan;
- gampang discan tanpa bikin mata capek;
- punya ritme baca yang hidup;
- terasa langsung berguna;
- cukup khas sehingga tidak terasa template AI;
- tetap tenang, akurat, dan klinis.

## Metode Singkat

- Baca source semua file di `topics/*.html`.
- Pakai artefak render yang sudah ada di `assets/qa/` untuk cek kesan nyata di layar.
- Pakai audit internal sebelumnya di `output/audit-kebacotan-penat-mata-topics-2026-03-13.md` sebagai baseline pendukung.
- Fokus audit ini: hook, scanability, ritme, utilitas, kehangatan tone, dan karakter halaman.
- Audit ini tidak mengulang validasi medis, keyboard, offline, atau print secara penuh.

## Ringkasan Eksekutif

Repo ini sudah punya fondasi yang kuat: brand konsisten, CTA klinik jelas, materi inti tebal, dan sebagian halaman sudah mulai menemukan bentuk editorial yang enak dibaca. Masalah utamanya bukan "konten kurang", tetapi "banyak konten penting masih tampil dengan bobot visual dan pola pembuka yang terlalu mirip".

Kalau diringkas:

- Potensi terbesar repo: `asam-urat-dewasa.html`, `hipertensi-dewasa.html`, `gorengan-harian.html`.
- Potensi paling besar untuk naik kelas bila direvisi: `gizi-anak-6bulan-5tahun.html`, `tipes.html`, `demam-berdarah-dbd.html`, `batuk-pilek-anak.html`.
- Pola paling mengurangi rasa "exciting": hero + ringkasan + chips + section-head + lead formulaik + grid card yang berulang terlalu sering.

## Yang Sudah Kuat

### 1. Relevansi topik terasa dekat

Banyak judul dan angle sudah terasa membumi, misalnya:

- `asam-urat-dewasa.html`: berangkat dari salah fokus lokal yang nyata.
- `gorengan-harian.html`: topiknya spesifik, dekat dengan kebiasaan sehari-hari.
- `hipertensi-dewasa.html`: langsung menautkan risiko dengan kebiasaan rumah.
- `tipes.html`: langsung bicara "cukup dipantau di rumah" vs "harus diperiksa".

Ini penting karena halaman edukasi mulai menarik saat pembaca merasa, "ini ngomongin hidup saya", bukan cuma menjelaskan penyakit.

### 2. CTA klinik dan orientasi dasar sudah disiplin

Hampir semua halaman sudah punya:

- sticky header yang jelas;
- CTA `WhatsApp Klinik` dan `Instagram Klinik`;
- quick chips anchor;
- section red flags / kapan ke dokter;
- referensi di bagian akhir.

Secara kegunaan, repo ini tidak kehilangan arah.

### 3. Beberapa halaman sudah punya signature yang kuat

- `asam-urat-dewasa.html` unggul karena sudut masuknya tajam dan tidak bertele-tele.
- `hipertensi-dewasa.html` unggul karena variasi komponennya paling sehat: ada icon grid, scan row, figure, agenda, measure, dan signal card.
- `demam-berdarah-dbd.html` punya section fase hari `1-7` yang terasa seperti bagian khas, bukan section generik.
- `gorengan-harian.html` kuat karena scope topiknya sempit dan copy-nya hemat.

Ini tanda bahwa repo sudah punya bibit "exciting" yang benar: bukan gimmick, tapi bentuk yang pas dengan isi.

## Yang Masih Menahan Minat Baca

### 1. Terlalu banyak halaman membuka section dengan formula yang sama

Masalah paling konsisten adalah pembuka section yang terasa seperti template editorial:

- `Konteks: ...`
- `Langkah praktis: ...`
- `Kapan evaluasi medis ...`

Pola ini membantu secara isi, tetapi kalau dipakai di hampir semua section, pembaca cepat merasa sedang membaca format yang sama terus.

Sinyal paling jelas:

- `tipes.html`: 12 dari 12 pembuka section sangat formulaik.
- `gizi-anak-6bulan-5tahun.html`: banyak section dibuka pola serupa, lalu diteruskan ke card lagi.
- `demam-berdarah-dbd.html`: hampir semua section memakai ritme pembuka yang sangat seragam.
- `batuk-pilek-anak.html`: masalah utamanya lebih ke scripted opening daripada struktur inti.

Efeknya: halaman tetap informatif, tetapi rasa "mau lanjut baca" turun karena kejutan editorialnya kecil.

### 2. Terjadi "over-carding"

Saat terlalu banyak poin penting masuk ke box dengan gaya serupa, semua hal terasa sama penting. Itu bikin hierarchy melemah.

Sinyal source yang paling menonjol:

- `gizi-anak-6bulan-5tahun.html`: 70 block `card` untuk 18 section.
- `batuk-pilek-anak.html`: 27 `card`.
- `nyeri-badan-lansia.html`: 27 `card`.
- `pusing-dewasa.html`: 23 `card`.
- `demam-berdarah-dbd.html`: 23 `card`.

Card bukan masalah. Yang jadi masalah adalah ketika card berubah dari alat bantu scan menjadi default container untuk hampir semua hal.

### 3. Rasa halaman lintas topik masih terlalu seragam di layar pertama

Pola yang sering muncul:

1. header
2. hero
3. `Ringkas 1 kalimat`
4. chips anchor
5. section card pertama

Struktur ini rapi dan aman, tetapi bila hampir semua halaman membuka dengan urutan dan bobot visual yang sama, rasa khas topik berkurang. Halaman hipertensi, DBD, tipes, dan MPASI seharusnya boleh terasa satu keluarga, tetapi tidak harus terasa saudara kembar.

### 4. Visual breaker belum cukup merata dan belum selalu datang di momen yang tepat

Beberapa halaman sudah terbantu visual, tetapi sebagian masih terlalu text-first pada titik yang seharusnya bisa lebih cepat dipindai.

Approximate source signal:

- `hipertensi-dewasa.html`: 5 figure-ish block, 16 icon card, 7 scan row.
- `tipes.html`: 4 figure-ish block, tetapi 0 scan row.
- `demam-berdarah-dbd.html`: 4 figure-ish block, tetapi opening section tetap terasa verbal.
- `gizi-anak-6bulan-5tahun.html`: hanya 1 figure-ish block untuk topik yang sangat padat.
- `batuk-pilek-anak.html`: 0 figure-ish block.
- `gorengan-harian.html`: 0 figure-ish block, tetapi masih tertolong karena copy-nya ringkas.

Artinya, masalah utama bukan semata "kurang gambar", tetapi "kurang visual fungsional di titik yang paling membantu orientasi".

### 5. Beberapa hero masih mengambil terlalu banyak napas

Dari audit sebelumnya, hero mobile yang paling mengganggu ritme awal:

- `menurunkan-berat-badan.html`: 308px
- `gizi-anak-6bulan-5tahun.html`: 278px
- `batuk-pilek-anak.html`: 273px
- `lambung.html`: 201px mobile dan 315px desktop

Pada halaman edukasi, layar pertama harus terasa cepat, bukan terasa seperti pembukaan yang masih minta waktu.

## Matriks Cepat per Halaman

| File | Yang Sudah Potensial | Yang Menahan | Arah revisi berikutnya |
| --- | --- | --- | --- |
| `asam-urat-dewasa.html` | Angle kuat, bahasa langsung, tidak terasa cerewet | Visual breaker masih bisa diperkaya di isi tengah | Pertahankan tone lugas, tambah 1 visual bantu di mid-flow |
| `batuk-pilek-anak.html` | Topik dekat dengan kebutuhan keluarga | Hero tinggi, section opening terlalu scripted, minim visual orientasi | Ubah ke symptom ladder dan home-check flow |
| `demam-berdarah-dbd.html` | Topik penting, fase hari `1-7` sudah khas | Banyak lead formulaik, callout dan card sama-sama ramai | Jadikan section fase sebagai model, pangkas lead lain |
| `diabetes-melitus-tipe-2.html` | Materi kaya, bisa sangat berguna | Paragraf cenderung menjelaskan dulu baru membantu scan | Pecah jadi decision strip, monitor board, diet compare |
| `gizi-anak-6bulan-5tahun.html` | Flagship content, struktur lengkap | 70 card, ritme sangat padat, visual breaker terlalu sedikit | Rebuild ritme tanpa memangkas isi |
| `gorengan-harian.html` | Scope tajam, nada ringan, tidak terasa template | Visual fungsional di tubuh halaman masih minim | Jadikan referensi tone, bukan referensi density |
| `hipertensi-dewasa.html` | Variasi komponen paling sehat, paling hidup | Masih ada sedikit rasa template di beberapa lead | Jadikan acuan sistem komponen lintas repo |
| `lambung.html` | Materi cukup fokus | Hero agak besar, callout terlalu dominan untuk halaman pendek | Ringankan opening, gabungkan warning yang berdekatan |
| `menurunkan-berat-badan.html` | Bisa terasa memotivasi dan sangat actionable | Hero terlalu makan ruang, section tengah masih naratif | Kecilkan hero, percepat masuk ke agenda praktis |
| `nyeri-badan-lansia.html` | Sudah cukup hidup, visual ada | Masih ada section yang membuka terlalu lebar | Ringkas pembuka, tonjolkan scan-first lebih dini |
| `pusing-dewasa.html` | Scan row membantu, ritme lumayan tertolong | Masih ada beberapa bagian yang terasa padat | Pertajam hierarchy antar tingkat bahaya dan sebab umum |
| `tipes.html` | Hero dan tema sebenarnya sangat kuat untuk decision-led content | Lead formulaik sangat dominan, ritme verbal | Ubah pembuka tiap section menjadi format yang berbeda |

## Halaman Referensi Positif

### `asam-urat-dewasa.html`

Ini contoh bahwa halaman bisa terasa kuat tanpa harus ramai. Yang bekerja di sini:

- angle pembukanya spesifik dan membantah miskonsepsi nyata;
- chips dan section title terasa langsung;
- card dipakai untuk menegaskan, bukan untuk menampung semua isi;
- user cepat tahu "salah fokusnya di mana".

Pelajaran reusable: satu sudut yang tajam lebih menarik daripada pengantar yang sangat lengkap tetapi datar.

### `hipertensi-dewasa.html`

Ini referensi terbaik untuk ritme. Halaman terasa lebih hidup karena:

- tidak cuma mengandalkan satu jenis komponen;
- banyak titik scan-first yang benar-benar bantu keputusan;
- visual di desktop tidak terasa tempelan;
- halaman panjang tetap punya jeda.

Pelajaran reusable: halaman panjang tidak masalah kalau bentuk bacaannya bervariasi.

### `gorengan-harian.html`

Halaman ini memperlihatkan pentingnya scope yang sempit dan copy yang hemat. Ia tidak terlalu "wah", tetapi terasa mau dibaca karena tidak memaksa pembaca melewati banyak pengantar.

Pelajaran reusable: topik sederhana sering justru menang karena langsung ke kebiasaan, salah kaprah, dan tindakan.

## Halaman dengan Potensi Kenaikan Terbesar

### `gizi-anak-6bulan-5tahun.html`

Ini kandidat paling besar untuk naik kelas. Isinya kaya dan penting, tetapi ritmenya paling berisiko melelahkan.

Kunci revisi:

- pertahankan semua struktur wajib MPASI;
- kurangi rasa "semua poin harus masuk box";
- beda-beda-kan opening section;
- letakkan visual bantu lebih awal di alur berat;
- ubah beberapa blok menjadi plain text zone yang rapi, bukan card lagi.

### `tipes.html`

Topik ini sebenarnya ideal untuk dibuat sangat menarik karena punya tegangan keputusan yang jelas: pantau atau periksa, aman di rumah atau perlu evaluasi cepat.

Kunci revisi:

- mulai section dari keputusan atau kesalahpahaman yang paling relevan;
- ganti sebagian lead dengan compare row atau warning strip;
- jangan jelaskan semua konteks sebelum memberi pegangan tindakan.

### `demam-berdarah-dbd.html`

DBD punya urgensi alami. Itu sudah merupakan modal excitement. Yang perlu diperbaiki adalah cara menyajikannya agar urgensi itu terasa terarah, bukan sekadar berat.

Kunci revisi:

- jadikan section fase sebagai anchor pola;
- pangkas pembuka yang hanya mengulang isi callout;
- buat hierarchy lebih tegas antara tanda bahaya, rawat rumah, dan pencegahan.

### `batuk-pilek-anak.html`

Ini topik yang sangat sering dicari keluarga. Potensinya besar sekali untuk jadi halaman yang "langsung kepakai", tetapi sekarang belum cukup ditolong oleh orientasi visual.

Kunci revisi:

- bikin symptom ladder atau cek napas yang langsung terlihat;
- pakai visual bantu sederhana untuk demam, napas, minum, dan durasi;
- pendekkan opening supaya keluarga cepat sampai ke bagian "sekarang saya harus cek apa".

## Pola Revisi yang Sebaiknya Dipakai Next Time

### 1. Jangan buka semua section dengan paragraf meta

Kalau section sudah punya scan aid, tabel, strip, atau figure, pembukanya harus makin pendek. Jangan tetap diawali dengan paragraf tiga fungsi.

Lebih baik pakai salah satu dari ini secara bergantian:

- decision strip;
- compare row;
- warning list;
- myth correction;
- langkah cek cepat;
- agenda harian;
- FAQ-style opener.

### 2. Kurangi jumlah box, naikkan ketepatan box

Prinsip baru yang perlu dijaga:

- kalau satu poin cukup jadi paragraf plain text, biarkan jadi plain text;
- kalau tiga box bilang bobot yang hampir sama, ubah satu atau dua jadi list biasa;
- card dipakai untuk hal yang memang perlu dibedakan, bukan default semua isi.

### 3. Setiap halaman perlu satu "signature move"

Bukan gimmick visual, tetapi bentuk yang terasa khas untuk topik itu. Contoh:

- DBD: timeline fase demam turun;
- batuk pilek anak: cek cepat napas, minum, dan durasi;
- tipes: alur "curiga - pantau - periksa";
- MPASI: tab usia yang benar-benar jadi alat kerja, bukan cuma daftar data;
- hipertensi: ritme rumah, dapur, ukur, kontrol.

Tanpa signature move, halaman yang rapi tetap akan terasa mirip template.

### 4. Hero harus jadi orientasi, bukan mini-bab pembuka

Checklist cepat:

- headline singkat;
- 1 ringkasan pendek;
- 2-3 poin inti saja;
- CTA tetap jelas;
- jangan pakai hero untuk menampung materi yang seharusnya ada di body.

### 5. Pakai lebih banyak visual fungsional di konten inti

Yang dibutuhkan bukan dekorasi, tetapi visual yang mengurangi beban baca:

- step diagram;
- body-area or pose visual;
- quick monitor board;
- compare plate / compare choices;
- "cek ini dulu" strip dengan ikon;
- simple decision flow.

Khusus halaman padat seperti MPASI, batuk pilek, dan tipes, visual bantu di awal section akan sangat menaikkan willingness to read.

### 6. Variasikan rasa "ringkas"

`Ringkas 1 kalimat` sudah berguna, tetapi jika selalu tampil sebagai strip yang sama, lama-lama jadi elemen standar yang kehilangan daya.

Alternatif pola:

- `Yang paling penting dulu`
- `Kalimat inti`
- `Kesalahan yang paling sering`
- `Pegangan cepat`
- `Jangan tunggu kalau...`

Artinya bukan harus ganti label tiap halaman, tetapi jangan otomatis mengulang treatment yang sama.

## Komponen yang Layak Masuk Library Revisi

Untuk batch berikutnya, kita bisa menganggap komponen ini sebagai arsenal inti:

1. `decision-strip`
   Ringkas, 2-3 cabang keputusan, cocok untuk DBD, tipes, batuk pilek, pusing.

2. `myth-correction-row`
   Kiri salah fokus, kanan fokus yang lebih benar. Cocok untuk asam urat, lambung, tipes, gorengan.

3. `watch-now-checklist`
   Checklist observasi rumah 24 jam. Cocok untuk demam, batuk pilek, DBD, tipes.

4. `local-routine-board`
   Agenda realistis sehari-hari, cocok untuk hipertensi, diabetes, berat badan, lambung.

5. `scan-row`
   Sudah terbukti membantu di hipertensi dan pusing. Layak dipakai lebih luas.

6. `figure-plus-caption`
   Bukan gambar besar, tetapi visual orientasi yang disambung caption dan 2-3 poin.

7. `plain-text-zone`
   Area yang sengaja lebih tenang untuk bagian yang memang harus dibaca pelan.

## Backlog Prioritas

### Tier 1

- `gizi-anak-6bulan-5tahun.html`
- `tipes.html`
- `demam-berdarah-dbd.html`

### Tier 2

- `batuk-pilek-anak.html`
- `menurunkan-berat-badan.html`
- `diabetes-melitus-tipe-2.html`

### Tier 3

- `lambung.html`
- `nyeri-badan-lansia.html`
- `pusing-dewasa.html`

### Jadikan Acuan

- `asam-urat-dewasa.html`
- `hipertensi-dewasa.html`
- `gorengan-harian.html`

## Aturan Singkat untuk "Next Time"

Sebelum halaman dianggap selesai, cek 8 pertanyaan ini:

1. Apakah layar pertama terasa cepat dipahami dalam 5 detik?
2. Apakah section pertama langsung memberi pegangan, bukan pengantar panjang?
3. Apakah tiap 1-2 screen ada perubahan ritme baca yang terasa?
4. Apakah semua poin penting benar-benar perlu masuk box?
5. Apakah halaman punya satu signature move yang khas topiknya?
6. Apakah visual membantu keputusan, bukan hanya menghias?
7. Apakah pembaca cepat tahu apa yang harus dipantau di rumah?
8. Apakah halaman ini masih terasa khas bila judul topiknya diganti?

Kalau jawaban nomor 8 adalah "iya, masih terasa sama saja", berarti halaman terlalu template.

## Penutup

Repo ini sudah punya bahan untuk jadi sangat kuat. Yang kita perlukan berikutnya bukan lebih banyak dekorasi, tetapi lebih banyak keberanian editorial:

- memilih apa yang discan dulu;
- membiarkan sebagian isi tetap jadi teks biasa;
- memberi tiap topik bentuk yang lebih khas;
- mengurangi pengulangan struktur yang terlalu aman.

Dengan arah itu, halaman akan tetap klinis dan rapi, tetapi lebih terasa hidup, lebih cepat masuk, dan lebih "mau dibaca".
