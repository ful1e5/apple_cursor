#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from typing import Any, Dict

from clickgen.builders import WindowsCursor, XCursor
from clickgen.core import CursorAlias
from clickgen.packagers import WindowsPackager, XPackager

from applbuild.constants import AUTHOR, COMMENT, THEME_NAME, URL
from applbuild.symlinks import add_missing_xcursor


def xbuild(
    config: Dict[str, Dict[str, Any]],
    x_out_dir: Path,
) -> None:
    """Build `macOSBigSur` cursor theme for only `X11`(UNIX) platform.

    :config: (Dict) `macOSBigSur` configuration.

    :x_out_dir: (Path) Path to the output directory, Where the `X11` cursor theme package will generate. It also creates a directory if not exists.
    """

    for _, item in config.items():
        png = item.get("png")
        hotspot = item.get("hotspot")
        x_sizes = item.get("x_sizes")
        delay = item.get("delay")

        with CursorAlias.from_bitmap(png, hotspot) as alias:
            x_cfg = alias.create(x_sizes, delay)
            print(f"Building '{x_cfg.stem}' XCursor...")
            XCursor.create(x_cfg, x_out_dir)

    add_missing_xcursor(x_out_dir / "cursors")
    XPackager(x_out_dir, THEME_NAME, COMMENT)


def wbuild(config: Dict[str, Dict[str, Any]], win_out_dir: Path) -> None:
    """Build `macOSBigSur` cursor theme for only `Windows` platforms.

    :config: (Dict) `macOSBigSur` configuration.

    :win_out_dir: (Path) Path to the output directory, Where the `Windows` cursor theme package will generate. It also creates a directory if not exists.
    """

    for _, item in config.items():
        png = item.get("png")
        hotspot = item.get("hotspot")
        x_sizes = item.get("x_sizes")
        delay = item.get("delay")

        with CursorAlias.from_bitmap(png, hotspot) as alias:
            alias.create(x_sizes, delay)

            if item.get("win_key"):
                position = item.get("position")
                win_size = item.get("win_size")
                win_key = item.get("win_key")
                canvas_size = item.get("canvas_size")
                win_delay = item.get("win_delay")

                win_cfg = alias.reproduce(
                    win_size, canvas_size, position, delay=win_delay
                ).rename(win_key)
                print(f"Building '{win_cfg.stem}' Windows Cursor...")
                WindowsCursor.create(win_cfg, win_out_dir)

    WindowsPackager(win_out_dir, THEME_NAME, COMMENT, AUTHOR, URL)


def build(
    config: Dict[str, Dict[str, Any]], x_out_dir: Path, win_out_dir: Path
) -> None:
    """Build `macOSBigSur` cursor theme for `X11` & `Windows` platforms.

    :config: (Dict) `macOSBigSur` configuration.

    :x_out_dir: (Path) Path to the output directory, Where the `X11` cursor theme package will generate. It also creates a directory if not exists.

    :win_out_dir: (Path) Path to the output directory, Where the `Windows` cursor theme package will generate. It also creates a directory if not exists.
    """

    def win_build(item: Dict[str, Any], alias: CursorAlias) -> None:
        position = item.get("position")
        win_size = item.get("win_size")
        win_key = item.get("win_key")
        canvas_size = item.get("canvas_size")
        win_delay = item.get("win_delay")

        win_cfg = alias.reproduce(
            win_size, canvas_size, position, delay=win_delay
        ).rename(win_key)
        print(f"Building '{win_cfg.stem}' Windows Cursor...")
        WindowsCursor.create(win_cfg, win_out_dir)

    for _, item in config.items():
        png = item.get("png")
        hotspot = item.get("hotspot")
        x_sizes = item.get("x_sizes")
        delay = item.get("delay")

        with CursorAlias.from_bitmap(png, hotspot) as alias:
            x_cfg = alias.create(x_sizes, delay)
            print(f"Building '{x_cfg.stem}' XCursor...")
            XCursor.create(x_cfg, x_out_dir)

            if item.get("win_key"):
                win_build(item, alias)

    add_missing_xcursor(x_out_dir / "cursors")
    XPackager(x_out_dir, THEME_NAME, COMMENT)

    WindowsPackager(win_out_dir, THEME_NAME, COMMENT, AUTHOR, URL)
