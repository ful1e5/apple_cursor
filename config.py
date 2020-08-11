import tempfile
import json

# Build Config
delay = 35
name = "macOSBigSur"
sizes = [24, 28, 32, 40, 48, 56, 64, 72, 80, 88, 96]

bitmaps_dir = "./bitmaps"
temp_folder = tempfile.mkdtemp()

# Cleanup Configs
x11_out = name
win_out = name + "_Windows"

# getting author name
with open("./package.json") as f:
    data = json.loads(f.read())
    author = data["author"]

# Windows Cursors Config
windows_cursors = {
    "sb_up_arrow.cur": "alt-select.cur",
    "bd_double_arrow.cur": "diagonal-resize-1.cur",
    "bottom_left_corner.cur": "diagonal-resize-2.cur",
    "pencil.cur": "handwriting.cur",
    "dnd-ask.cur": "help-select.cur",
    "right_side.cur": "horizontal-resize.cur",
    "hand2.cur": "link-select.cur",
    "all-scroll.cur": "move.cur",
    "left_ptr.cur": "normal-select.cur",
    "X_cursor.cur": "pirate.cur",
    "crosshair.cur": "precision-select.cur",
    "xterm.cur": "text-select.cur",
    "circle.cur": "unavailable.cur",
    "bottom_side.cur": "vertical-resize.cur",
    "wait.ani": "busy.ani",
    "left_ptr_watch.ani": "working-in-background.ani"
}

# Windows install.inf file content
with open("./scripts/windows.inf") as f:
    data = f.read()
    window_install_inf = data.replace(
        "<inject_theme_name>", name+" Cursors").replace("<inject_author_name>", author)
