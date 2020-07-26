import fs from "fs";
import path from "path";

import { generateRenderTemplate } from "./helpers/htmlTemplate";
// import { renderSvg } from "./helpers/render";
import { staticSvgs, bitmapsDir } from "./config";

const generateStaticSvgBitmaps = async (svg: string) => {
  fs.readFile(svg, "utf8", (error, data) => {
    if (error) {
      return console.log(error);
    }

    // Generating HTML Template
    generateRenderTemplate(data);

    // preparing paths
    let bitmap = path.parse(svg).base;
    bitmap = path.resolve(bitmapsDir, bitmap);

    console.log(bitmap);
  });
};

// iterate over satic .svg files
staticSvgs.forEach(async (svg) => {
  await generateStaticSvgBitmaps(svg);
});
