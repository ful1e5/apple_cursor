import json
from clickgen import build_cursor_theme

from config import name, sizes, delay, bitmaps_dir, temp_folder
from helper import init_build, pack_it


def build() -> None:
    init_build()
    with open('./hotspots.json', 'r') as hotspot_file:
        hotspots = json.loads(hotspot_file.read())
        build_cursor_theme(name, image_dir=bitmaps_dir,
                           cursor_sizes=sizes, out_path=temp_folder, hotspots=hotspots, archive=False, delay=delay)
    pack_it()


if __name__ == "__main__":
    build()
