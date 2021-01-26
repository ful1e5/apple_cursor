import { resolve } from "path";
import { readdirSync, existsSync } from "fs";

// Source Directory
const staticCursorsDir = resolve(__dirname, "svg", "static");
const animatedCursorsDir = resolve(__dirname, "svg", "animated");

if (!existsSync(staticCursorsDir) || !existsSync(animatedCursorsDir)) {
  throw new Error("svg directory not found");
}

// Out Directory
const bitmapsDir = resolve(__dirname, "../", "bitmaps");

//  Cursors
const staticCursors = readdirSync(staticCursorsDir).map((f) =>
  resolve(staticCursorsDir, f)
);
const animatedCursors = readdirSync(animatedCursorsDir).map((f) =>
  resolve(animatedCursorsDir, f)
);

export { staticCursors, animatedCursors, bitmapsDir };
