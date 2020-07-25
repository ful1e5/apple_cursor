import path from "path";
import fs from "fs";

// Source Directory
const svgsDir = path.resolve(__dirname, "svg");

// .svg
let svgs = fs
  .readdirSync(svgsDir)
  .filter((file) => path.extname(file) === ".svg");
svgs = svgs.map((svg: string) => path.resolve(svgsDir, svg));

const animatedCursor = ["watch", "left_ptr_watch"];

// Out Directory
const bitmapsDir = path.resolve(process.cwd(), "bitmaps");

export { svgs, animatedCursor, bitmapsDir };
