import { resolve } from "path";
import { staticCursors, animatedCursors, animatedClip } from "./cursors.json";

// Source Directory
const svgsDir = resolve(__dirname, "svg");

// Out Directory
const bitmapsDir = resolve(__dirname, "bitmaps");

export { staticCursors, animatedCursors, svgsDir, bitmapsDir, animatedClip };
