import fs from "fs";
import path from "path";

import { generateRenderTemplate } from "./helpers/htmlTemplate";
// import { renderSvg } from "./helpers/render";
import { staticSvgs, bitmapsDir } from "./config";

const generateStaticSvgBitmaps = (svg: string) => {
  fs.readFile(svg, "utf8", (error, data) => {
    if (error) {
      return console.log(error);
    }

    // Generating HTML Template
    generateRenderTemplate(data);

    // rendering svg
    let bitmap = path.parse(svg).base;
    bitmap = path.resolve(bitmapsDir, bitmap);
    console.log(bitmap);
  });
};

(async () => {
  // iterate over all .svg files
  staticSvgs.forEach((svg) => {
    generateStaticSvgBitmaps(svg);
  });
})();
