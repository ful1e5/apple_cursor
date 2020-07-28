import json
import os
from clickgen import build_cursor_theme

sizes = [24, 28]
with open('./hotspots.json') as hotspot_file:
    file_data = json.loads(hotspot_file.read())
    hotspots = file_data["hotspots"]
    print(hotspots)
