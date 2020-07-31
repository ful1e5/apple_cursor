import tempfile

# Build Config
delay = 50
name = "MacOSBigSur"
sizes = [24, 28, 32, 40, 48, 56, 65, 72, 80, 88, 96]

bitmaps_dir = "./bitmaps"
temp_folder = tempfile.mkdtemp()

# Cleanup Configs
x11_out = "macOSBigSur"
win_out = "macOSBigSur_Windows"
