import path from "path";
import { staticCursors } from "./cursors.json";

// Source Directory
const svgsDir = path.resolve(__dirname, "svg");

// Resolve Paths for svg
const staticSvgs = staticCursors.map((svg: string) =>
  path.resolve(svgsDir, svg)
);

// Out Directory
const bitmapsDir = path.resolve(process.cwd(), "bitmaps");

export { staticSvgs, bitmapsDir };
