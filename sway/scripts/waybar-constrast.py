import json
import os

wal_cache = os.path.expanduser("/home/pave/.cache/wal/colors.json")
out_file = os.path.expanduser("/home/pave/dotfiles/waybar/colors-waybar-contrast.css")

def get_contrast(hex_color):
    hex_color = hex_color.lstrip('#')
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    
    luminance = (0.299 * r + 0.587 * g + 0.114 * b) / 255
    
    return "#282828" if luminance > 0.5 else "#ebdbb2"


with open(wal_cache, 'r') as f:
    data = json.load(f)

colors = data['colors']
colors['background'] = data['special']['background']

with open(out_file, 'w') as f:
    for name, hex_val in colors.items():
        contrast_hex = get_contrast(hex_val)
        f.write(f"@define-color {name}_contrast {contrast_hex};\n")
