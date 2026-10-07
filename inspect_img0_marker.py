import subprocess

# Let's crop around x=[738, 768], y=[428, 466] in image_0
# 895x762
# Let's crop 200x200 around that marker
subprocess.run(["convert", "public/image_0.webp", "-crop", "200x150+650+380", "/tmp/marker_crop.png"])
info = subprocess.check_output(["identify", "/tmp/marker_crop.png"]).decode()
print("Marker crop info:", info)

# Let's also check if there is text in image_0 by doing OCR or printing ASCII
# Let's see what ascii art shows around the marker
out = subprocess.check_output(["convert", "/tmp/marker_crop.png", "-resize", "40x20!", "-colorspace", "Gray", "txt:-"]).decode()
lines = [l for l in out.splitlines() if not l.startswith("#")]
grid = [[" " for _ in range(40)] for _ in range(20)]
chars = " .:-=+*#%@"
for l in lines:
    parts = l.split(":")
    coord = parts[0].strip().split(",")
    x, y = int(coord[0]), int(coord[1])
    val_str = parts[1].split("(")[1].split(",")[0].replace("%", "")
    val = float(val_str)
    norm = val / 100.0 if "%" in parts[1].split("(")[1] else val / 255.0
    char_idx = min(len(chars)-1, max(0, int(norm * len(chars))))
    grid[y][x] = chars[char_idx]

for row in grid:
    print("".join(row))
