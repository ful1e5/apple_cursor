#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from applbuild.generator import xbuild

bitmaps_dir = Path("../pngs")
x_out_dir = Path("../themes") / "macOSBigSur"

xbuild(bitmaps_dir, x_out_dir)
