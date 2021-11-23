#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from glob import glob

ignore_files = ["center_ptr.svg", "context-menu.svg", "left_ptr.svg", "right_ptr.svg"]


def link_svg_dir(src_dir, dst_dir) -> None:
    for src_path in glob(f"{src_dir}/*"):
        file_name = os.path.basename(src_path)
        if file_name not in ignore_files:
            dst = os.path.join(dst_dir, file_name)
            if os.path.exists(dst):
                print(f"Removing old symlink of '{file_name}'")
                os.remove(dst)
            print(f"Creating symlink of '{file_name}'")
            os.symlink(
                os.path.relpath(src_path, f"{dst_dir}/"),
                dst,
            )
        else:
            print(f"Ignoring file '{file_name}'")


link_svg_dir("bigsur/static", "monterey/static")
link_svg_dir("bigsur/animated", "monterey/animated")
