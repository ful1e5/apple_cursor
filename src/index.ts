import fs from "fs";

import { generateRenderTemplate } from "./helpers/htmlTemplate";
import { svgs } from "./config";

(async () => {
  // iterate over all .svg files
  svgs.forEach((svg) => {
    // reading file
    fs.readFile(svg, "utf8", (error, data) => {
      if (error) {
        return console.log(error);
      }

      // Generating HTML Template
      const template = generateRenderTemplate(data);

      console.log(template);
    });
  });
})();
