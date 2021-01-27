import path from "path";
import { readdirSync, existsSync } from "fs";

// Directory resolve
const projectRoot = path.resolve(__dirname, "../../");

const outDir = path.resolve(projectRoot, "pngs");
const staticSvgDir = path.resolve(projectRoot, "svg", "static");
const animatedSvgDir = path.resolve(projectRoot, "svg", "animated");

// Generate a svg list
if (!existsSync(staticSvgDir) || !existsSync(animatedSvgDir)) {
  throw new Error("svg directory not found");
}

const staticCursors = readdirSync(staticSvgDir).map((f) =>
  path.resolve(staticSvgDir, f)
);
const animatedCursors = readdirSync(animatedSvgDir).map((f) =>
  path.resolve(animatedSvgDir, f)
);

export { staticCursors, animatedCursors, outDir };
