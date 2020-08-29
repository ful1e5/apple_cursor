import path from "path";
import { bitmapsDir } from "../config";

export const getOutPath = (number: number, length: number, svgFile: string) => {
  let frame = "" + number;
  while (frame.length < length) {
    frame = "0" + frame;
  }

  const bitmap = `${path.basename(svgFile, ".svg")}-${frame}.png`;

  return path.resolve(bitmapsDir, bitmap);
};
