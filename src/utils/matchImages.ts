import fs from "fs";
import path from "path";
import { PNG } from "pngjs";
import pixelmatch from "pixelmatch";

export const matchImages = (img1Buff: Buffer, img2Buff: Buffer) => {
  const img1 = PNG.sync.read(img1Buff);
  const img2 = PNG.sync.read(img2Buff);
  const { width, height } = img1;

  const diff = new PNG({ width, height });

  const out = pixelmatch(img1.data, img2.data, diff.data, width, height, {
    threshold: 0.3,
  });

  fs.writeFileSync(
    path.resolve(process.cwd(), "diff", `${out}.png`),
    diff.data
  );
  return out;
};
