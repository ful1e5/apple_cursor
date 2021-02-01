#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from typing import Any

from clickgen.builders import WindowsCursor, XCursor
from clickgen.core import CursorAlias
from clickgen.packagers import WindowsPackager, XPackager
from clickgen.util import LikePath

from applbuild.configure import get_config
from applbuild.constants import *
from applbuild.symlinks import add_missing_xcursor

#
# 📝 Note: All CONSTANT variables are imported from `applbuild.constants` module.
#


def xbuild(bitmaps_dir: LikePath, x_out_dir: Path) -> None:
    """Build `macOSBigSur` cursor theme for only `X11`(UNIX) platform.

    :bitmaps_dir: (str | Path) Path to .png file's directory.

    :x_out_dir: (Path) Path to output directory, Where X11 cursor theme package store. Created automatically if not exists.
    """

    config = get_config(bitmaps_dir)

    # Building
    for _, item in config.items():
        png = item["png"]
        hotspot = item["hotspot"]
        delay = item["delay"]

        with CursorAlias.from_bitmap(png, hotspot) as alias:
            x_cfg = alias.create(X_SIZES, delay)
            XCursor.create(x_cfg, x_out_dir)

    add_missing_xcursor(x_out_dir / "cursors")
    XPackager(x_out_dir, THEME_NAME, COMMENT)


def wbuild(bitmaps_dir: LikePath, win_out_dir: Path) -> None:
    """Build `macOSBigSur` cursor theme for only `Windows` platforms.

    :bitmaps_dir: (str | Path) Path to .png file's directory.

    :win_out_dir: (Path) Path to output directory, Where Windows Cursor theme package store. Created automatically if not exists.
    """

    config = get_config(bitmaps_dir)

    # Building
    for _, item in config.items():
        png = item["png"]
        hotspot = item["hotspot"]
        delay = item["delay"]

        with CursorAlias.from_bitmap(png, hotspot) as alias:
            alias.create(X_SIZES, delay)

            if item.get("win_key"):
                position = item["position"]
                size = item["size"]
                win_key = item["win_key"]
                canvas_size = item["canvas_size"]

                win_cfg = alias.reproduce(size, canvas_size, position, delay=3).rename(
                    win_key
                )
                WindowsCursor.create(win_cfg, win_out_dir)

    WindowsPackager(win_out_dir, THEME_NAME, COMMENT, AUTHOR, URL)


def build(bitmaps_dir: LikePath, x_out_dir: Path, win_out_dir: Path) -> None:
    """Build `macOSBigSur` cursor theme for `X11` & `Windows` platforms.

    :bitmaps_dir: (str | Path) Path to .png file's directory.

    :x_out_dir: (Path) Path to output directory, Where X11 cursor theme package store. Created automatically if not exists.

    :win_out_dir: (Path) Path to output directory, Where Windows Cursor theme package store. Created automatically if not exists.
    """

    def win_build(item: Any, alias: CursorAlias) -> None:
        position = item["position"]
        size = item["size"]
        win_key = item["win_key"]
        canvas_size = item["canvas_size"]

        win_cfg = alias.reproduce(size, canvas_size, position, delay=3).rename(win_key)
        WindowsCursor.create(win_cfg, win_out_dir)

    config = get_config(bitmaps_dir)

    # Building
    for _, item in config.items():
        png = item["png"]
        hotspot = item["hotspot"]
        delay = item["delay"]

        with CursorAlias.from_bitmap(png, hotspot) as alias:
            x_cfg = alias.create(X_SIZES, delay)
            XCursor.create(x_cfg, x_out_dir)

            if item.get("win_key"):
                win_build(item, alias)

    add_missing_xcursor(x_out_dir / "cursors")
    XPackager(x_out_dir, THEME_NAME, COMMENT)

    WindowsPackager(win_out_dir, THEME_NAME, COMMENT, AUTHOR, URL)
