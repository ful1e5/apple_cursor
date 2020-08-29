import fs from "fs";
import path from "path";
import { bitmapsDir } from "../config";

export interface Frames {
  [fileName: string]: {
    buffer: Buffer;
  };
}

export const saveFrames = (frames: Frames) => {
  for (let [fileName, { buffer }] of Object.entries(frames)) {
    const out_path = path.resolve(bitmapsDir, fileName);
    fs.writeFileSync(out_path, buffer, { encoding: "binary" });
  }
};
