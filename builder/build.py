#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from applbuild.generator import xbuild, wbuild

bitmaps_dir = Path("../pngs")
x_out_dir = Path("../themes") / "macOSBigSur"
win_out_dir = Path("../themes") / "macOSBigSur-Windows"

xbuild(bitmaps_dir, x_out_dir)
wbuild(bitmaps_dir,win_out_dir)