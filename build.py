import json
import shutil
import tempfile

from os import path, listdir
from clickgen import build_cursor_theme

# Config
name = "MacOS Big Sur"
sizes = [24, 28, 32, 40, 48, 56, 65, 72, 80, 88, 96]
temp_folder = tempfile.mkdtemp()
package_dir = "./packages"
x11_out_dir = path.join(package_dir, "macOSBigSur")
win_out_dir = path.join(package_dir, "macOSBigSur_Windows")

# Building Cursor Theme
with open('./hotspots.json', 'r') as hotspot_file:
    config = json.loads(hotspot_file.read())
    build_cursor_theme(name, image_dir="./bitmaps",
                       cursor_sizes=sizes, out_path=temp_folder, archive=False, delay=30)

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
