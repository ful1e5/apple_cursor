import path from "path";
import { cursors } from "./cursors.json";

// Source Directory
const svgsDir = path.resolve(__dirname, "svg");

// Resolve Paths for svg
const svgs = cursors.map((svg: string) => path.resolve(svgsDir, svg));

// Out Directory
const bitmapsDir = path.resolve(process.cwd(), "bitmaps");

export { svgs, bitmapsDir };
