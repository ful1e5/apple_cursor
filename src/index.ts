import puppeteer from "puppeteer";

(async () => {
  const browser = await puppeteer.launch({
    ignoreDefaultArgs: process.env.IS_LOCAL ? [" --single-process "] : [],
    headless: true,
  });
  const page = await browser.newPage();
  await page.goto("https://google.com");
  await page.pdf({ path: "google.pdf" });

  await browser.close();
})();
