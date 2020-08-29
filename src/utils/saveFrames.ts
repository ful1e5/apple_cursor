import fs from "fs";
import path from "path";
import { bitmapsDir } from "../config";

export interface Frames {
  [fileName: string]: {
    buffer: Buffer;
  };
}

interface SaveFramesArguments {
  fileName: string;
  frames: Frames;
}

export const saveFrames = (frames: SaveFramesArguments) => {
  for (let [fileName, { buffer }] of Object.entries(frames.frames)) {
    const out_path = path.resolve(bitmapsDir, fileName);
    fs.writeFileSync(out_path, buffer, { encoding: "binary" });
  }
};
