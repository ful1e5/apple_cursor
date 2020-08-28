import fs from "fs";
import { PNG } from "pngjs";
import pixelmatch from "pixelmatch";

export const matchImages = (img1Path: string, img2Path: string) => {
  const img1 = PNG.sync.read(fs.readFileSync(img1Path));
  const img2 = PNG.sync.read(fs.readFileSync(img2Path));
  const { width, height } = img1;
  const diff = new PNG({ width, height });

  return pixelmatch(img1.data, img2.data, diff.data, width, height, {
    threshold: 0.3,
  });
};
