import subprocess

# Let's crop several parts of img0 and see
# Is it a satellite map? Is it a hand-drawn map? Is it a road map? Is it a cadastral plan?
# Let's see corners and center
for region, crop in [
    ("top-left", "200x100+0+0"),
    ("top-right", "200x100+695+0"),
    ("center", "300x200+300+280"),
    ("bottom-left", "200x100+0+662"),
    ("bottom-right", "200x100+695+662")
]:
    out = subprocess.check_output(["convert", "/tmp/img0.png", "-crop", crop, "-scale", "10x5!", "-colorspace", "Gray", "txt:-"]).decode()
    lines = [l for l in out.splitlines() if not l.startswith("#")]
    avg_gray = sum(float(l.split("(")[1].split(",")[0].replace("%","")) for l in lines) / len(lines)
    print(f"img0 {region} ({crop}): avg_gray={avg_gray:.1f}")

for region, crop in [
    ("top-left", "400x200+0+0"),
    ("top-right", "400x200+2000+0"),
    ("center", "600x400+900+800"),
    ("bottom-left", "400x200+0+1833"),
    ("bottom-right", "400x200+2000+1833")
]:
    out = subprocess.check_output(["convert", "/tmp/img1.png", "-crop", crop, "-scale", "10x5!", "-colorspace", "Gray", "txt:-"]).decode()
    lines = [l for l in out.splitlines() if not l.startswith("#")]
    avg_gray = sum(float(l.split("(")[1].split(",")[0].replace("%","")) for l in lines) / len(lines)
    print(f"img1 {region} ({crop}): avg_gray={avg_gray:.1f}")
