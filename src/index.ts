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
import { saveFrames, Frames } from "./utils/saveFrames";
import { getKeyName } from "./utils/getKeyName";

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
      const frames: Frames = {};
      const firstKey = getKeyName(index, svg);
      console.log(firstKey);

      // 1st Frame
      frames[firstKey] = {
        buffer: await svgElement.screenshot({
          omitBackground: true,
          clip: animatedClip,
          encoding: "binary",
        }),
      };

      //  Pushing frames until it match to 1st frame
      index++;
      while (!breakLoop) {
        const newFrame = await svgElement.screenshot({
          omitBackground: true,
          clip: animatedClip,
          encoding: "binary",
        });
        const key = getKeyName(index, svg);
        console.log(key);
        const diff = matchImages({
          img1Buff: frames[firstKey].buffer,
          img2Buff: newFrame,
        });

        if (!(diff < 3000)) {
          frames[key] = { buffer: newFrame };
        } else {
          breakLoop = true;
        }
        index++;
      }

      saveFrames(frames);

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
