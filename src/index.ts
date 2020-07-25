import fs from "fs";

import { generateRenderTemplate } from "./helpers/htmlTemplate";
import { staticSvgs } from "./config";

const generateStaticSvgBitmaps = (svg: string) => {
  fs.readFile(svg, "utf8", (error, data) => {
    if (error) {
      return console.log(error);
    }
    // Generating HTML Template
    generateRenderTemplate(data);
  });
};

(async () => {
  // iterate over all .svg files
  staticSvgs.forEach((svg) => {
    generateStaticSvgBitmaps(svg);
  });
})();
