const http = require('http');
const fs = require('fs');
const path = require('path');
const mime = {'.html':'text/html; charset=utf-8','.jpeg':'image/jpeg','.jpg':'image/jpeg','.png':'image/png','.webp':'image/webp','.css':'text/css','.js':'text/javascript','.svg':'image/svg+xml'};
const root = process.cwd();
const server = http.createServer((req,res)=>{
  const clean = decodeURIComponent((req.url || '/').split('?')[0]);
  let filePath = path.join(root, clean === '/' ? 'topics/menurunkan-berat-badan.html' : clean.replace(/^\//,''));
  if (!filePath.startsWith(root)) { res.statusCode = 403; res.end('forbidden'); return; }
  fs.readFile(filePath, (err, data) => {
    if (err) { res.statusCode = 404; res.end('not found'); return; }
    res.setHeader('Content-Type', mime[path.extname(filePath).toLowerCase()] || 'application/octet-stream');
    res.end(data);
  });
});
server.listen(4173, '127.0.0.1');
setInterval(()=>{}, 1 << 30);
