import fs from "fs";
import path from "path";

import { generateRenderTemplate } from "./helpers/htmlTemplate";
import { staticSvgs, bitmapsDir } from "./config";

import { renderSvg } from "./helpers/render";

const generateStaticSvgBitmaps = async (svg: string) => {
  fs.readFile(svg, "utf8", (error, data) => {
    if (error) {
      return console.log(error);
    }

    // Generating HTML Template
    const template = generateRenderTemplate(data);

    // rendering with frames=1 beacause of static
    const bitmap = `${path.basename(svg, ".svg")}.png`;
    renderSvg(template, 1, bitmap, bitmapsDir);
  });
};

// iterate over satic .svg files
staticSvgs.forEach(async (svg) => {
  await generateStaticSvgBitmaps(svg);
});
