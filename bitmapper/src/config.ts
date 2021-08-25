import { Colors } from "./core/types";

interface Config {
  themeName: string;
  color: Colors;
}

const black = "#000000";
const white = "#FFFFFF";

const config: Config[] = [
  {
    themeName: "macOSBigSur",
    color: {
      base: black,
      outline: white,
    },
  },
  {
    themeName: "macOSBigSur-White",
    color: {
      base: white,
      outline: black,
    },
  },
];

export { config };
