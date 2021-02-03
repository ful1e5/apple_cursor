#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from pathlib import Path

from applbuild.generator import build, wbuild, xbuild

parser = argparse.ArgumentParser(
    prog="apple_builder",
    description="'macOSBigSur' cursor build python script.",
)

# Positional Args.
parser.add_argument(
    "platform",
    choices=("windows", "unix", "all"),
    default="all",
    const="all",
    nargs="?",
    help="Set package type, Which you want to build. (default: '%(default)s')",
)


# Optional Args.
parser.add_argument(
    "-p",
    "--png-dir",
    dest="png_dir",
    metavar="PNG",
    type=str,
    default="../bitmaps",
    help="To change pngs directory. (default: %(default)s)",
)

parser.add_argument(
    "-o",
    "--out-dir",
    dest="out_dir",
    metavar="OUT",
    type=str,
    default="../themes",
    help="To change output directory. (default: %(default)s)",
)


# Preparing build
args = parser.parse_args()

bitmaps_dir = Path(args.png_dir)
x_out_dir = Path(args.out_dir) / "macOSBigSur"
win_out_dir = Path(args.out_dir) / "macOSBigSur_Windows"

if args.platform == "unix":
    xbuild(bitmaps_dir, x_out_dir)
elif args.platform == "windows":
    wbuild(bitmaps_dir, win_out_dir)
else:
    build(bitmaps_dir, x_out_dir, win_out_dir)
