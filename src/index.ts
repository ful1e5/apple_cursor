import path from "path";
import fs from "fs";
import puppeteer from "puppeteer";

import { bitmapsPath } from "./config";

(async () => {
  const browser = await puppeteer.launch({
    ignoreDefaultArgs: process.env.IS_LOCAL ? [" --single-process "] : [],
    headless: true,
  });
  const page = await browser.newPage();
  await page.goto("https://google.com");

  fs.mkdirSync(bitmapsPath);
  await page.pdf({ path: path.resolve(bitmapsPath, "google.pdf") });

  await browser.close();
})();
