#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Dict, List, Tuple

# Info
THEME_NAME = "macOSBigSur"
COMMENT = "macOS Big Sur Pointers"
AUTHOR = "Kaiz Khatri"
URL = "https://github.com/ful1e5/apple_cursor"

# XCursor
X_DELAY: int = 10
X_SIZES: List[Tuple[int, int]] = [
    (22, 22),
    (24, 24),
    (28, 28),
    (32, 32),
    (40, 40),
    (48, 48),
    (56, 56),
    (64, 64),
    (72, 72),
    (80, 80),
    (88, 88),
    (96, 96),
]


# Windows Cursor
WIN_DELAY = 1
WIN_CANVAS_SIZE = (32, 32)
WIN_SIZE = (24, 24)

X_CURSORS_CFG: Dict[str, Dict[str, int]] = {
    ##########
    # Static #
    ##########
    "all-scroll.png": {"xhot": 100, "yhot": 100},
    "bottom_left_corner.png": {"xhot": 100, "yhot": 100},
    "bottom_right_corner.png": {"xhot": 100, "yhot": 100},
    "bottom_tee.png": {"xhot": 98, "yhot": 137},
    "center_ptr.png": {"xhot": 100, "yhot": 70},
    "context-menu.png": {"xhot": 43, "yhot": 61},
    "copy.png": {"xhot": 67, "yhot": 46},
    "cross.png": {"xhot": 100, "yhot": 100},
    "crossed_circle.png": {"xhot": 67, "yhot": 46},
    "crosshair.png": {"xhot": 100, "yhot": 100},
    "dnd_no_drop.png": {"xhot": 100, "yhot": 100},
    "dotbox.png": {"xhot": 100, "yhot": 100},
    "hand1.png": {"xhot": 94, "yhot": 72},
    "hand2.png": {"xhot": 67, "yhot": 46},
    "left_ptr.png": {"xhot": 69, "yhot": 56},
    "left_side.png": {"xhot": 100, "yhot": 100},
    "left_tee.png": {"xhot": 100, "yhot": 100},
    "link.png": {"xhot": 120, "yhot": 55},
    "ll_angle.png": {"xhot": 100, "yhot": 100},
    "lr_angle.png": {"xhot": 100, "yhot": 100},
    "move.png": {"xhot": 80, "yhot": 71},
    "pencil.png": {"xhot": 81, "yhot": 117},
    "plus.png": {"xhot": 98, "yhot": 100},
    "question_arrow.png": {"xhot": 99, "yhot": 99},
    "right_ptr.png": {"xhot": 136, "yhot": 66},
    "right_tee.png": {"xhot": 98, "yhot": 99},
    "sb_down_arrow.png": {"xhot": 100, "yhot": 100},
    "sb_h_double_arrow.png": {"xhot": 100, "yhot": 100},
    "sb_left_arrow.png": {"xhot": 100, "yhot": 100},
    "sb_right_arrow.png": {"xhot": 100, "yhot": 100},
    "sb_up_arrow.png": {"xhot": 100, "yhot": 100},
    "sb_v_double_arrow.png": {"xhot": 100, "yhot": 100},
    "top_side.png": {"xhot": 100, "yhot": 100},
    "top_tee.png": {"xhot": 100, "yhot": 100},
    "ul_angle.png": {"xhot": 100, "yhot": 100},
    "ur_angle.png": {"xhot": 100, "yhot": 100},
    "vertical-text.png": {"xhot": 96, "yhot": 99},
    "wayland-cursor.png": {"xhot": 100, "yhot": 100},
    "X_cursor.png": {"xhot": 100, "yhot": 100},
    "xterm.png": {"xhot": 100, "yhot": 104},
    "zoom-in.png": {"xhot": 100, "yhot": 100},
    "zoom-out.png": {"xhot": 100, "yhot": 100},
    ############
    # Animated #
    ############
    # Note: Animated cursors don't need an extension and frame numbers.
    "left_ptr_watch": {"xhot": 67, "yhot": 46},
    "wait": {"xhot": 100, "yhot": 100},
}

WIN_CURSORS_CFG: Dict[str, Dict[str, str]] = {
    ##########
    # Static #
    ##########
    "right_ptr.png": {"to": "Alternate", "position": "top_right"},
    "cross.png": {"to": "Cross"},
    "left_ptr.png": {"to": "Default", "position": "top_left"},
    "bottom_left_corner.png": {"to": "Diagonal_1"},
    "bottom_right_corner.png": {"to": "Diagonal_2"},
    "pencil.png": {"to": "Handwriting"},
    "question_arrow.png": {"to": "Help", "position.png": "top_left"},
    "sb_h_double_arrow.png": {"to": "Horizontal"},
    "xterm.png": {"to": "IBeam", "position": "top_left"},
    "hand2.png": {"to": "Link", "position": "top_left"},
    "hand1.png": {"to": "Move"},
    "crossed_circle.png": {"to": "Unavailiable", "position": "top_left"},
    "sb_v_double_arrow.png": {"to": "Vertical"},
    ############
    # Animated #
    ############
    # Note: Animated cursors don't need frame numbers.
    "left_ptr_watch": {"to": "Work", "position": "top_left"},
    "wait": {"to": "Busy", "size": WIN_CANVAS_SIZE},
}
