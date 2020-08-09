import tempfile
import json

# Build Config
delay = 50
name = "MacOSBigSur"
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

# Windows install.inf file content
with open("./scripts/windows.inf") as f:
    data = f.read()
    window_install_inf = data.replace(
        "<inject_theme_name>", name+" Cursors").replace("<inject_author_name>", author)

print(window_install_inf)
