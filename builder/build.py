#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from pathlib import Path

from applbuild.configure import get_config
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


parser.add_argument(
    "-xs",
    "--xsizes",
    dest="xsizes",
    metavar="INT",
    nargs="+",
    default=[
        22,
        24,
        28,
        32,
        40,
        48,
        56,
        64,
        72,
        80,
        88,
        96,
    ],
    type=int,
    help="Set pixel-size for xcursor. (default: %(default)s)",
)


parser.add_argument(
    "-ws",
    "--win-size",
    dest="win_size",
    metavar="INT",
    default=24,
    type=int,
    help="Set pixel-size for Windows cursors. (default: %(default)s)",
)


parser.add_argument(
    "-wcs",
    "--win-canvas-size",
    dest="win_canvas_size",
    metavar="INT",
    default=32,
    type=int,
    help="Set pixel-size for Windows cursor's canvas. (default: %(default)s)",
)

# Preparing build
args = parser.parse_args()

bitmaps_dir = Path(args.png_dir)

x_out_dir = Path(args.out_dir) / "macOSBigSur"
win_out_dir = Path(args.out_dir) / "macOSBigSur_Windows"

# Windows Canvas & Cursor sizes
win_size: int = args.win_size
win_canvas_size: int = args.win_canvas_size
if win_canvas_size < win_size:
    win_canvas_size = win_size


config = get_config(
    bitmaps_dir,
    x_sizes=args.xsizes,
    win_canvas_size=win_canvas_size,
    win_size=win_size,
)

if args.platform == "unix":
    xbuild(config, x_out_dir)
elif args.platform == "windows":
    wbuild(config, win_out_dir)
else:
    build(config, x_out_dir, win_out_dir)
