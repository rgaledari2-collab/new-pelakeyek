import subprocess

for name, path in [("IMAGE 0", "public/image_0.webp"), ("IMAGE 1", "public/image_1.webp"), ("USER UPLOAD", "public/map_user_upload.jpg")]:
    print(f"================ {name} ({path}) ================")
    out = subprocess.check_output(["convert", path, "-resize", "50x24!", "-colorspace", "Gray", "txt:-"]).decode("utf-8")
    lines = [l for l in out.splitlines() if not l.startswith("#")]
    
    grid = [[" " for _ in range(50)] for _ in range(24)]
    chars = " .:-=+*#%@"
    for l in lines:
        parts = l.split(":")
        coord = parts[0].strip().split(",")
        x, y = int(coord[0]), int(coord[1])
        # val can be float
        val_str = parts[1].split("(")[1].split(",")[0].replace("%", "")
        val = float(val_str)
        # normalize 0..100 or 0..255
        if "%" in parts[1].split("(")[1]:
            norm = val / 100.0
        elif val > 1.0:
            norm = val / 255.0
        else:
            norm = val
        char_idx = min(len(chars)-1, max(0, int(norm * len(chars))))
        grid[y][x] = chars[char_idx]
    
    for row in grid:
        print("".join(row))
