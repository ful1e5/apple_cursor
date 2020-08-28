import fs from "fs";
import path from "path";
import puppeteer from "puppeteer";

import { generateRenderTemplate } from "./helpers/htmlTemplate";
import {
  staticCursors,
  bitmapsDir,
  svgsDir,
  animatedCursors,
  animatedClip,
} from "./config";

// --------------------------- Helpers
const frameNumber = (number: number, length: number) => {
  var str = "" + number;
  while (str.length < length) {
    str = "0" + str;
  }
  return str;
};

// --------------------------- Main

const main = async () => {
  const browser = await puppeteer.launch({
    ignoreDefaultArgs: [" --single-process ", "--no-sandbox"],
    headless: true,
  });

  try {
    console.log("📸 Rendering Static Cursors...");
    // Rendering satic .svg files
    for (let svg of staticCursors) {
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
        const frame = frameNumber(index, frames.toString().length);
        const bitmap =
          frames == 1
            ? `${path.basename(svg, ".svg")}.png`
            : `${path.basename(svg, ".svg")}-${frame}.png`;

        const out = path.resolve(bitmapsDir, bitmap);

        // Render
        await svgElement.screenshot({
          omitBackground: true,
          path: out,
          clip: animatedClip,
        });
        // console.log(`${svg} frame ${frame}/${frames} rendered at ${out}`);
      }

      await page.close();
    }
  } catch (error) {
    console.error(error);
  } finally {
    console.log(`\nBitmaps stored at ${bitmapsDir}\n\n🎉 Render Done.`);
    process.exit(0);
  }
};

main();
