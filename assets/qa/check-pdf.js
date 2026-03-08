const fs = require('fs');
const pdf = require('pdf-parse');
const path = 'assets/qa/panduan-makanan-anak-print.pdf';
const data = fs.readFileSync(path);
const checks = [
  'kapan harus ke dokter/igd',
  '7 pesan emas',
  'tab usia mpasi',
  'feeding rules',
  'gtm troubleshooting',
  'pemantauan pertumbuhan',
  'pemantauan perkembangan',
  'resep lokal',
  'anemia + sanitasi',
  'mitos vs fakta',
  'faq singkat',
  'rujukan'
];

pdf(data)
  .then((r) => {
    const txt = (r.text || '').replace(/\s+/g, ' ').toLowerCase();
    const hit = checks.map((k) => ({ k, ok: txt.includes(k) }));
    console.log(JSON.stringify({ numpages: r.numpages, numrender: r.numrender, checks: hit }, null, 2));
  })
  .catch((e) => {
    console.error(e);
    process.exit(1);
  });
