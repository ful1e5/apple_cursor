import fs from "fs";
import path from "path";
import puppeteer from "puppeteer";

import { htmlTemplate } from "./utils/htmlTemplate";
import { staticCursors, bitmapsDir, animatedCursors } from "./config";
import { matchImages } from "./utils/matchImages";
import { saveFrames, Frames } from "./utils/saveFrames";
import { getFrameName } from "./utils/getFrameName";

const main = async () => {
  const browser = await puppeteer.launch({
    ignoreDefaultArgs: [" --single-process ", "--no-sandbox"],
    headless: true,
  });

  if (!fs.existsSync(bitmapsDir)) {
    fs.mkdirSync(bitmapsDir);
  }

  try {
    console.log("📸 Rendering Static Cursors...");

    for (let svgPath of staticCursors) {
      const buffer = fs.readFileSync(path.resolve(svgPath), "utf8");
      if (!buffer) throw new Error(`${svgPath} File Read error`);

      // Generating HTML Template
      const data = buffer.toString();
      const template = htmlTemplate(data);

      // config
      const bitmapName = `${path.basename(svgPath, ".svg")}.png`;
      const out = path.resolve(bitmapsDir, bitmapName);

      // Render
      const page = await browser.newPage();
      await page.setContent(template);

      await page.waitForSelector("#container");
      const svgElement = await page.$("#container svg");
      if (!svgElement) throw new Error("svg element not found");
      await svgElement.screenshot({ omitBackground: true, path: out });

      await page.close();
    }

    console.log("🎥 Rendering Animated Cursors...");

    for (let svgPath of animatedCursors) {
      const buffer = fs.readFileSync(svgPath, "utf8");
      if (!buffer) throw new Error(`${svgPath} File Read error`);

      // Generating HTML Template
      const data = buffer.toString();
      const template = htmlTemplate(data);

      const page = await browser.newPage();
      await page.setContent(template, { waitUntil: "networkidle2" });

      await page.waitForSelector("#container");
      const svgElement = await page.$("#container svg");
      if (!svgElement) throw new Error("svg element not found");

      // Render Config
      let index = 1;
      let breakRendering = false;
      const frames: Frames = {};
      const firstKey = getFrameName(index, svgPath);

      console.log("Rendering", path.basename(svgPath), "...");
      console.log(firstKey);

      // 1st Frame
      frames[firstKey] = {
        buffer: await svgElement.screenshot({
          omitBackground: true,
          encoding: "binary",
        }),
      };

      //  Pushing frames until it match to 1st frame
      index++;
      while (!breakRendering) {
        const newFrame = await svgElement.screenshot({
          omitBackground: true,
          encoding: "binary",
        });
        const key = getFrameName(index, svgPath);
        console.log(key);
        const diff = matchImages({
          img1Buff: frames[firstKey].buffer,
          img2Buff: newFrame,
        });

        if (!(diff < 700)) {
          frames[key] = { buffer: newFrame };
        } else {
          breakRendering = true;
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
