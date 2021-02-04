#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from typing import Any, Dict, List, Tuple, Union

from clickgen.util import LikePath, PNGProvider

from applbuild.constants import (
    WIN_CANVAS_SIZE,
    WIN_CURSORS_CFG,
    WIN_DELAY,
    WIN_SIZE,
    X_CURSORS_CFG,
    X_DELAY,
    X_SIZES,
)


def get_config(bitmaps_dir: LikePath, **kwargs) -> Dict[str, Any]:
    """Return configuration of `macOSBigSur` pointers.

    Args:

    :bitmaps_dir: (str | Path) Path to .png file's directory.

    Keywords Args:

    :x_sizes: (List[Tuple[int, int]] | Tuple[int, int]) List or Tuple of xcursor sizes.

    :win_size: (Tuple[int, int]) Single size for Windows cursor.

    Example:

    ```python
        get_config("./bitmaps", x_sizes=[(24, 24), (32, 32)], win_size=(32, 32))
    ```
    """

    if kwargs.get("x_sizes"):
        x_sizes = kwargs.pop("x_sizes")
    else:
        x_sizes = X_SIZES

    if kwargs.get("win_size"):
        w_size = kwargs.pop("win_size")
    else:
        w_size = WIN_SIZE

    png = PNGProvider(bitmaps_dir)
    config: Dict[str, Any] = {}

    for key, item in X_CURSORS_CFG.items():
        x_hot: int = item.get("xhot", 0)
        y_hot: int = item.get("yhot", 0)
        hotspot: Tuple[int, int] = (x_hot, y_hot)

        delay: int = item.get("delay", X_DELAY)
        p: Union[List[Path], Path] = png.get(key)

        data = {
            "png": p,
            "x_sizes": x_sizes,
            "hotspot": hotspot,
            "delay": delay,
        }

        win_data = WIN_CURSORS_CFG.get(key)

        if win_data:
            win_key = win_data.get("to")

            position = win_data.get("position", "center")
            win_delay: int = win_data.get("delay", WIN_DELAY)

            canvas_size: Tuple[int, int] = win_data.get("canvas_size", WIN_CANVAS_SIZE)
            win_size: Tuple[int, int] = win_data.get("size", w_size)

            # Because provided cursor size is bigger than cursor's canvas.
            # Also, "position" settings will not effect on cursor because the cursor's canvas and cursor sizes are equals.
            if (win_size[0] > canvas_size[0]) or (win_size[1] > canvas_size[1]):
                canvas_size = win_size

            config[key] = {
                **data,
                "win_key": win_key,
                "position": position,
                "canvas_size": canvas_size,
                "win_size": win_size,
                "win_delay": win_delay,
            }
        else:
            config[key] = data

    return config
