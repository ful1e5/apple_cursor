import path from "path";
import fs from "fs";

// Source Directory
const svgsDir = path.resolve(__dirname, "svg");

let svgs = fs
  .readdirSync(svgsDir)
  .filter((file) => path.extname(file) === ".svg");
svgs = svgs.map((svg: string) => path.resolve(svgsDir, svg));

// Out Directory
const bitmapsDir = path.resolve(process.cwd(), "bitmaps");

export { svgs, bitmapsDir };
