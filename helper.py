import shutil
import json
import sys

from config import name, temp_folder, bitmaps_dir, win_out, x11_out, window_install_inf_content, windows_cursors
from os import path, listdir, rename, remove


package_dir = "./themes"
x11_out_dir = path.join(package_dir, x11_out)
win_out_dir = path.join(package_dir, win_out)


def window_bundle() -> None:
    # Remove & Rename cursors
    # If Key found => Rename else Remove
    for cursor in listdir(win_out_dir):
        old_path = path.join(win_out_dir, cursor)

        try:
            new_path = path.join(win_out_dir, windows_cursors[cursor])
            rename(old_path, new_path)
        except KeyError:
            remove(old_path)

    # creating install.inf file
    install_inf_path = path.join(win_out_dir, "install.inf")
    with open(install_inf_path, "w") as file:
        file.write(window_install_inf_content)


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

    # create install.inf file in Windows Theme
    window_bundle()

    # # Packaging
    # #  - .tar archive for X11
    # #  - .zip archive for Windows
    # shutil.make_archive(x11_out_dir, "tar", x11_out_dir)
    # shutil.make_archive(win_out_dir, "zip", win_out_dir)

    # # Clenaup
    # shutil.rmtree(temp_folder)
    # for f in listdir(package_dir):
    #     f_path = path.join(package_dir, f)
    #     if path.isdir(f_path):
    #         shutil.rmtree(f_path)
