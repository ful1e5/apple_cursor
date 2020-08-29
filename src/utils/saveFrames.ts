import fs from "fs";
import { getOutPath } from "./getOutPath";

interface SaveFramesArguments {
  fileName: string;
  frames: Buffer[];
}
export const saveFrames = ({ fileName, frames }: SaveFramesArguments) => {
  let index = 1;
  const totalFrames = Buffer.length;
  for (let [frameBuffer] of Object.entries(frames)) {
    const out = getOutPath(index, totalFrames, fileName);
    fs.writeFileSync(out, frameBuffer);
    index++;
  }
};
