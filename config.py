import tempfile
import json

# Build Config
delay = 50
name = "macOSBigSur"
sizes = [24, 28, 32, 40, 48, 56, 64, 72, 80, 88, 96]

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
    "left_ptr_watch.ani": "AppStarting.ani",
    "left_ptr.cur": "Arrow.cur",
    "crosshair.cur": "Cross.cur",
    "hand2.cur": "Hand.cur",
    "pencil.cur": "Handwriting.cur",
    "dnd-ask.cur": "Help.cur",
    "xterm.cur": "IBeam.cur",
    "circle.cur": "NO.cur",
    "all-scroll.cur": "SizeAll.cur",
    "bd_double_arrow.cur": "SizeNESW.cur",
    "sb_v_double_arrow.cur": "SizeNS.cur",
    "fd_double_arrow.cur": "SizeNWSE.cur",
    "sb_h_double_arrow.cur": "SizeWE.cur",
    "sb_up_arrow.cur": "UpArrow.cur",
    "wait.ani": "Wait.ani",
}

# Windows install.inf file content
with open("./scripts/windows.inf") as f:
    data = f.read()
    window_install_inf_content = data.replace(
        "<inject_theme_name>", name+" Cursors").replace("<inject_author_name>", author)
