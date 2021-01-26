import "module-alias/register";

import fs from "fs";
import path from "path";
import Pixelmatch from "pixelmatch";

import { PNG } from "pngjs";
import puppeteer, { ElementHandle, Page } from "puppeteer";

import { animatedCursors, bitmapsDir, staticCursors } from "./config";
import { getFrameName } from "./utils/getFrameName";
import { toHTML } from "./utils/toHTML";

const getSVGElement = async (page: Page) => {
  const svg = await page.$("#container svg");

  if (!svg) {
    throw new Error("svg element not found!");
  }
  return svg;
};

const screenshot = async (element: ElementHandle<Element>): Promise<Buffer> => {
  return await element.screenshot({
    omitBackground: true,
    encoding: "binary",
  });
};

const saveFrame = (key: string, frame: Buffer) => {
  const out_path = path.resolve(bitmapsDir, key);
  fs.writeFileSync(out_path, frame, { encoding: "binary" });
};

const main = async () => {
  const browser = await puppeteer.launch({
    ignoreDefaultArgs: ["--single-process", "--no-sandbox"],
    headless: true,
  });

  if (!fs.existsSync(bitmapsDir)) {
    fs.mkdirSync(bitmapsDir);
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
    const out = path.join(bitmapsDir, key);

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

    let index = 1;
    let breakRendering = false;

    // Rendering 1st frame
    const img1 = await screenshot(svg);
    const key1 = getFrameName(index, svgFilePath);

    console.log("Saving", key1, "...");
    saveFrame(key1, img1);

    // Rendering frames till `imgN` matched to `img1`
    while (!breakRendering) {
      ++index;
      const imgN = await screenshot(svg);
      const keyN = getFrameName(index, svgFilePath);

      console.log("Saving", keyN, "...");
      saveFrame(keyN, imgN);

      const { data: img1Data, width, height } = PNG.sync.read(img1);
      const { data: imgNData } = PNG.sync.read(imgN);

      const diff = Pixelmatch(img1Data, imgNData, null, width, height);

      if (diff <= 100) {
        breakRendering = !breakRendering;
      }
    }

    await page.close();
  }
  await browser.close();
};

main();
