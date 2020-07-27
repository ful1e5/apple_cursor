import fs from "fs";
import path from "path";
import puppeteer from "puppeteer";

import { generateRenderTemplate } from "./helpers/htmlTemplate";
import { staticSvgs, bitmapsDir, svgsDir, animatedCursors } from "./config";

// --------------------------- Helpers
const pad = (number: number, length: number) => {
  var str = "" + number;
  while (str.length < length) {
    str = "0" + str;
  }
  return str;
};

// --------------------------- Main
(async () => {
  const browser = await puppeteer.launch({
    ignoreDefaultArgs: process.env.IS_LOCAL ? [" --single-process "] : [],
    executablePath: process.env.IS_LOCAL ? "/usr/bin/google-chrome-stable" : "",
    headless: true,
  });

  try {
    console.log("📸 Rendering Static Cursors...");
    // Rendering satic .svg files
    for (let svg of staticSvgs) {
      const buffer = fs.readFileSync(path.resolve(svgsDir, svg), "utf8");
      if (!buffer) throw new Error(`${svg} File Read error`);

      const data = buffer.toString();
      // Generating HTML Template
      const template = generateRenderTemplate(data);

      // config
      const bitmap = `${path.basename(svg, ".svg")}.png`;
      const out = path.resolve(bitmapsDir, bitmap);

      // Render
      const page = await browser.newPage();
      await page.setContent(template);

      await page.waitForSelector("#container");
      const svgElement = await page.$("#container svg");

      if (!svgElement) throw new Error("svg element not found");

      await svgElement.screenshot({ omitBackground: true, path: out });
      // console.log(`Static Cursor rendered at ${out}`);

      await page.close();
    }

    console.log("🎥 Rendering Animated Cursors...");

    // Rendering animated .svg files
    for (let [svg, { frames }] of Object.entries(animatedCursors)) {
      const buffer = fs.readFileSync(path.resolve(svgsDir, svg), "utf8");
      if (!buffer) throw new Error(`${svg} File Read error`);

      const data = buffer.toString();
      // Generating HTML Template
      const template = generateRenderTemplate(data);

      const page = await browser.newPage();
      await page.setContent(template);

      await page.waitForSelector("#container");
      const svgElement = await page.$("#container svg");

      if (!svgElement) throw new Error("svg element not found");

      // Render Frames
      for (let index = 1; index <= frames; index++) {
        // config
        const padIndex = pad(index, frames.toString().length);
        const bitmap =
          frames == 1
            ? `${path.basename(svg, ".svg")}.png`
            : `${path.basename(svg, ".svg")}-${padIndex}.png`;

        const out = path.resolve(bitmapsDir, bitmap);

        // Render
        await svgElement.screenshot({ omitBackground: true, path: out });
        // console.log(`${svg} frame ${padIndex}/${frames} rendered at ${out}`);
      }

      await page.close();
    }
  } catch (error) {
    console.error(error);
  } finally {
    console.log(`\nBitmaps stored at ${bitmapsDir}\n\n🎉 Render Done.`);
    process.exit(0);
  }
})();
