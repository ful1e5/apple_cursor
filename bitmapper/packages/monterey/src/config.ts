import { Colors } from "core/src/types";

interface Config {
  themeName: string;
  color: Colors;
}

const black = "#000000";
const white = "#FFFFFF";

const config: Config[] = [
  {
    themeName: "macOSMonterey",
    color: {
      base: black,
      outline: white,
    },
  },
  {
    themeName: "macOSMonterey-White",
    color: {
      base: white,
      outline: black,
    },
  },
];

export { config };
