#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from typing import Any, Dict, List, Tuple, Union

from clickgen.util import LikePath, PNGProvider

from applbuild.constants import *


def get_config(bitmaps_dir: LikePath) -> Dict[str, Any]:
    """Return configuration of `macOSBigSur` pointers.

    :bitmaps_dir: (str | Path) Path to .png file's directory.
    """

    png = PNGProvider(bitmaps_dir)
    config: Dict[str, Any] = {}

    for key, item in X_CURSORS_CFG.items():
        x_hot: int = item.get("x_hot", 0)
        y_hot: int = item.get("y_hot", 0)
        hotspot: Tuple[int, int] = (x_hot, y_hot)

        delay: int = item.get("delay", X_DELAY)
        p: Union[List[Path], Path] = png.get(key)

        data = {
            "png": p,
            "hotspot": hotspot,
            "delay": delay,
        }

        win_data = WIN_CURSORS_CFG.get(key)

        if win_data:
            win_key = win_data.get("to")

            position = win_data.get("position", "center")
            canvas_size: Tuple[int, int] = win_data.get("canvas_size", CANVAS_SIZE)
            size: Tuple[int, int] = win_data.get("size", SIZE)
            win_delay: int = win_data.get("delay", WIN_DELAY)

            config[key] = {
                **data,
                "win_key": win_key,
                "position": position,
                "canvas_size": canvas_size,
                "size": size,
                "win_delay": win_delay,
            }
        else:
            config[key] = data

    return config
