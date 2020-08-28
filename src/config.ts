import path from "path";
import fs from "fs";
import { staticCursors, animatedCursors, animatedClip } from "./cursors.json";

// Source Directory
const svgsDir = path.resolve(__dirname, "svg");

// Out Directory
const bitmapsDir = path.resolve(process.cwd(), "bitmaps");
if (!fs.existsSync(bitmapsDir)) fs.mkdirSync(bitmapsDir);

export { staticCursors, animatedCursors, svgsDir, bitmapsDir, animatedClip };
