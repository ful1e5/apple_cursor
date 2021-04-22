#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This module provides build methods for ``macOSBigSur``."""

from pathlib import Path
from typing import Any, Dict

from applbuild.constants import AUTHOR, COMMENT, THEME_NAME, URL
from applbuild.symlinks import add_missing_xcursor
from clickgen.builders import WindowsCursor, XCursor
from clickgen.core import CursorAlias
from clickgen.packagers import WindowsPackager, XPackager


def xbuild(config: Dict[str, Dict[str, Any]], x_out_dir: Path) -> None:
    """Build `macOSBigSur` cursor theme for only `X11`(UNIX) platform.

    :param config: `macOSBigSur` configuration.
    :type config: Dict

    :param x_out_dir: Path to the output directory,\
                Where the `X11` cursor theme package will generate.\
                It also creates a directory if not exists.
    :type x_out_dir: Path

    :param info: Content theme name & comment
    :type info: Info
    """

    for _, item in config.items():
        with CursorAlias.from_bitmap(item["png"], item["hotspot"]) as alias:
            x_cfg = alias.create(item["x_sizes"], item["delay"])

            print(f"Building '{x_cfg.stem}' XCursor...")
            XCursor.create(x_cfg, x_out_dir)

    add_missing_xcursor(x_out_dir / "cursors")
    XPackager(x_out_dir, THEME_NAME, COMMENT)


def wbuild(config: Dict[str, Dict[str, Any]], win_out_dir: Path) -> None:
    """Build `macOSBigSur` cursor theme for only `Windows` platforms.

    :param config: `macOSBigSur` configuration.
    :type config: Dict

    :param win_out_dir: Path to the output directory,\
                  Where the `Windows` cursor theme package will generate.\
                  It also creates a directory if not exists.
    :type win_out_dir: Path

    :param info: Content theme name & comment
    :type info: Info
    """

    for _, item in config.items():
        with CursorAlias.from_bitmap(item["png"], item["hotspot"]) as alias:
            alias.create(item["x_sizes"], item["delay"])

            if item.get("win_key"):
                win_cfg = alias.reproduce(
                    size=item["win_size"],
                    canvas_size=item["canvas_size"],
                    position=item["position"],
                    delay=item["win_delay"],
                ).rename(item["win_key"])

                print(f"Building '{win_cfg.stem}' Windows Cursor...")
                WindowsCursor.create(win_cfg, win_out_dir)

    WindowsPackager(win_out_dir, THEME_NAME, COMMENT, AUTHOR, URL)


def build(
    config: Dict[str, Dict[str, Any]], x_out_dir: Path, win_out_dir: Path
) -> None:
    """Build `macOSBigSur` cursor theme for `X11` & `Windows` platforms.

    :param config: `macOSBigSur` configuration.
    :type config: Dict

    :param x_out_dir: Path to the output directory,\
                Where the `X11` cursor theme package will generate.\
                It also creates a directory if not exists.
    :type x_out_dir: Path

    :param win_out_dir: Path to the output directory,\
                  Where the `Windows` cursor theme package will generate.\
                  It also creates a directory if not exists.
    :type win_out_dir: Path

    :param info: Content theme name & comment
    :type info: Info
    """

    for _, item in config.items():

        with CursorAlias.from_bitmap(item["png"], item["hotspot"]) as alias:
            x_cfg = alias.create(item["x_sizes"], item["delay"])

            print(f"Building '{x_cfg.stem}' XCursor...")
            XCursor.create(x_cfg, x_out_dir)

            if item.get("win_key"):
                win_cfg = alias.reproduce(
                    size=item["win_size"],
                    canvas_size=item["canvas_size"],
                    position=item["position"],
                    delay=item["win_delay"],
                ).rename(item["win_key"])

                print(f"Building '{win_cfg.stem}' Windows Cursor...")
                WindowsCursor.create(win_cfg, win_out_dir)

    add_missing_xcursor(x_out_dir / "cursors")
    XPackager(x_out_dir, THEME_NAME, COMMENT)

    WindowsPackager(win_out_dir, THEME_NAME, COMMENT, AUTHOR, URL)
