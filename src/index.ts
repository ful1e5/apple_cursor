import fs from "fs";
import path from "path";
import puppeteer from "puppeteer";

import { generateRenderTemplate } from "./helpers/htmlTemplate";
import { staticSvgs, bitmapsDir } from "./config";

// --------------------------- Main
(async () => {
  const browser = await puppeteer.launch({
    ignoreDefaultArgs: process.env.IS_LOCAL ? [" --single-process "] : [],
    executablePath: process.env.IS_LOCAL ? "/usr/bin/google-chrome-stable" : "",
    headless: true,
  });

  // Rendering satic .svg files
  for (let svg of staticSvgs) {
    fs.readFile(svg, "utf8", async (error, data) => {
      if (error) throw new Error(`${error}`);

      // Generating HTML Template
      const template = generateRenderTemplate(data);

      // config
      const bitmap = `${path.basename(svg, ".svg")}.png`;
      const out = path.resolve(bitmapsDir, bitmap);

      // Render
      try {
        const page = await browser.newPage();
        await page.setContent(template);

        await page.waitForSelector("#container");
        const svgElement = await page.$("#container svg");

        if (!svgElement) throw new Error("svg element not found");

        await svgElement.screenshot({ omitBackground: true, path: out });
        console.log(`Static Cursor rendered at ${out}`);

        await page.close();
      } catch (error) {
        console.error(error);
      }
    });
  }
})();
