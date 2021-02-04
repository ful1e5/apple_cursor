import fs from "fs";
import path from "path";
import puppeteer, { ElementHandle, Page } from "puppeteer";

import { animatedCursors, outDir, staticCursors } from "./config";
import { frameNumber } from "./utils/frameNumber";
import { matchImages } from "./utils/matchImages";
import { toHTML } from "./utils/toHTML";

const getSVGElement = async (page: Page) => {
  const svg = await page.$("#container svg");

  if (!svg) {
    throw new Error("svg element not found!");
  }
  return svg;
};

const screenshot = async (element: ElementHandle<Element>): Promise<Buffer> => {
  return element.screenshot({
    omitBackground: true,
    encoding: "binary",
  });
};

const stopAnimation = async (page: Page) => {
  // @ts-ignore
  await page._client.send("Animation.setPlaybackRate", {
    playbackRate: 0,
  });
};

const resumeAnimation = async (page: Page, playbackRate: number = 0.1) => {
  // @ts-ignore
  await page._client.send("Animation.setPlaybackRate", {
    playbackRate,
  });
};

const saveFrameImage = (key: string, frame: Buffer) => {
  const out_path = path.resolve(outDir, key);
  fs.writeFileSync(out_path, frame, { encoding: "binary" });
};

const main = async () => {
  const browser = await puppeteer.launch({
    ignoreDefaultArgs: ["--single-process", "--no-sandbox"],
    headless: true,
  });

  if (!fs.existsSync(outDir)) {
    fs.mkdirSync(outDir);
  } else {
    throw new Error(`out directory '${outDir}' already exists.`);
  }

  for (const svgFilePath of staticCursors) {
    const svgData = fs.readFileSync(svgFilePath, "utf-8");
    if (!svgData) {
      throw new Error(`${svgFilePath} File Read error`);
    }

    const page = await browser.newPage();
    const html = toHTML(svgData);

    await page.setContent(html);
    const svg = await getSVGElement(page);

    const key = `${path.basename(svgFilePath, ".svg")}.png`;
    const out = path.join(outDir, key);

    console.log("Saving", key, "...");
    await svg.screenshot({ omitBackground: true, path: out });
    await page.close();
  }

  for (const svgFilePath of animatedCursors) {
    const svgData = fs.readFileSync(svgFilePath, "utf8");
    if (!svgData) {
      throw new Error(`${svgFilePath} File Read error`);
    }

    const page = await browser.newPage();
    const html = toHTML(svgData);

    await page.setContent(html);
    const svg = await getSVGElement(page);
    await stopAnimation(page);

    let index = 1;
    const frameLimit = 300;
    let breakRendering = false;
    let prevImg: Buffer;

    // Rendering frames till `imgN` matched to `imgN-1` (When Animation is done)
    while (!breakRendering) {
      if (index > frameLimit) {
        throw new Error("Reached the frame limit.");
      }

      resumeAnimation(page);
      const img = await screenshot(svg);
      stopAnimation(page);

      if (index > 1) {
        // @ts-ignore
        const diff = matchImages(prevImg, img);
        if (diff <= 100) {
          breakRendering = !breakRendering;
        }
      }
      const frame = frameNumber(index, 3);
      const key = `${path.basename(svgFilePath, ".svg")}-${frame}.png`;

      console.log("Saving", key, "...");
      saveFrameImage(key, img);

      prevImg = img;
      ++index;
    }

    await page.close();
  }
  await browser.close();
};

main();
