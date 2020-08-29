import fs from "fs";
import path from "path";
import puppeteer from "puppeteer";

import { generateRenderTemplate } from "./utils/htmlTemplate";
import {
  staticCursors,
  bitmapsDir,
  svgsDir,
  animatedCursors,
  animatedClip,
} from "./config";
import { matchImages } from "./utils/matchImages";

const main = async () => {
  const browser = await puppeteer.launch({
    ignoreDefaultArgs: [" --single-process ", "--no-sandbox"],
    headless: true,
  });

  // Paths
  if (!fs.existsSync(svgsDir)) {
    console.log("Source .svg files not found");
  }
  if (!fs.existsSync(bitmapsDir)) {
    fs.mkdirSync(bitmapsDir);
  }

  try {
    console.log("📸 Rendering Static Cursors...");

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

    for (let [svg] of Object.entries(animatedCursors)) {
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

      // Render Config
      let index = 1;
      let breakLoop = false;
      const frames: Buffer[] = [];

      // 1st Frame
      frames.push(
        await svgElement.screenshot({
          omitBackground: true,
          clip: animatedClip,
          encoding: "binary",
        })
      );

      //  Pushing frames until it match to 1st frame
      index++;
      while (!breakLoop) {
        const newFrame = await svgElement.screenshot({
          omitBackground: true,
          clip: animatedClip,
          encoding: "binary",
        });
        const diff = matchImages(frames[0], newFrame);
        console.log(diff, "frames", 1, "--", index);
        if (diff < 3000) {
          breakLoop = true;
        }
        index++;
      }

      await page.close();
    }

    console.log(`\nBitmaps stored at ${bitmapsDir}\n\n🎉 Render Done.`);
    process.exit(0);
  } catch (error) {
    console.error(error);
    process.exit(1);
  }
};

main();
