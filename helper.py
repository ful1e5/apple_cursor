import shutil
import json
import sys

from config import name, temp_folder, bitmaps_dir, win_out, x11_out
from os import path, listdir


package_dir = "./packages"
x11_out_dir = path.join(package_dir, x11_out)
win_out_dir = path.join(package_dir, win_out)


def init_build() -> None:
    """
        Print build version.
        Remove previously built packages && Check Bitmaps.
    """
    with open("./package.json", "r") as package_file:
        data = json.loads(package_file.read())
        version = data['version']
        print("⚡ Build Version %s" % version)

    # cleanup old packages
    if path.exists(package_dir):
        shutil.rmtree(package_dir)

    # Checking Bitmaps directory
    if not path.exists(bitmaps_dir):
        print(
            "⚠ BITMAPS NOT FOUND.\n\n`yarn install && yarn render` to Generates Bitmaps")
        sys.exit(1)


def pack_it() -> None:
    """
        Create Crisp 📦 Packages for Windows & X11 Cursor Theme.
    """
    # Rename directory
    shutil.move(path.join(temp_folder, name, "x11"), x11_out_dir)
    shutil.move(path.join(temp_folder, name, "win"), win_out_dir)

    # Packaging
    #  - .tar archive for X11
    #  - .zip archive for Windows
    shutil.make_archive(x11_out_dir, "tar", x11_out_dir)
    shutil.make_archive(win_out_dir, "zip", win_out_dir)

    # Clenaup
    shutil.rmtree(temp_folder)
    for f in listdir(package_dir):
        f_path = path.join(package_dir, f)
        if path.isdir(f_path):
            shutil.rmtree(f_path)
