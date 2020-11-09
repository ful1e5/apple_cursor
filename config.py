import tempfile
import json

# Build Config
delay = 50
name = "macOSBigSur"
sizes = [22, 24, 28, 32, 40, 48, 56, 64, 72, 80, 88, 96]

bitmaps_dir = "./bitmaps"
package_dir = "./themes"
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
    "right_ptr.cur": "Alternate.cur",
    "wait.ani": "Busy.ani",
    "crosshair.cur": "Cross.cur",
    "left_ptr.cur": "Default.cur",
    "bd_double_arrow.cur": "Diagonal_1.cur",
    "fd_double_arrow.cur": "Diagonal_2.cur",
    "pencil.cur": "Handwriting.cur",
    "dnd-ask.cur": "Help.cur",
    "sb_h_double_arrow.cur": "Horizontal.cur",
    "hand2.cur": "Link.cur",
    "hand1.cur": "Move.cur",
    "xterm.cur": "Text.cur",
    "circle.cur": "Unavailiable.cur",
    "sb_v_double_arrow.cur": "Vertical.cur",
    "left_ptr_watch.ani": "Work.ani",
}

# Windows install.inf file content
with open("./scripts/windows.inf") as f:
    data = f.read()
    window_install_inf_content = data.replace(
        "<inject_theme_name>", name + " Cursors"
    ).replace("<inject_author_name>", author)
