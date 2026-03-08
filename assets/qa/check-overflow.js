const { chromium } = require('playwright');
(async () => {
  const url = process.argv[2];
  const tests = [[360,800],[768,1024],[1366,768]];
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  for (const [w, h] of tests) {
    await page.setViewportSize({ width: w, height: h });
    await page.goto(url);
    await page.waitForTimeout(400);
    const data = await page.evaluate(() => ({
      scrollW: document.documentElement.scrollWidth,
      clientW: document.documentElement.clientWidth
    }));
    console.log(`${w}x${h} => scrollWidth=${data.scrollW}, clientWidth=${data.clientW}, overflow=${data.scrollW > data.clientW}`);
  }
  await browser.close();
})();
