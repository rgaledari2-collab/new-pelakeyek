import subprocess

# Let's inspect image_0.webp
# Check dimensions, size
print("image_0.webp:")
info = subprocess.check_output(["identify", "-verbose", "public/image_0.webp"]).decode("utf-8")
for l in info.splitlines():
    if any(k in l for k in ["Format", "Geometry", "Resolution", "Filesize", "Colorspace"]):
        print(" ", l.strip())

# Let's check image_1.webp
print("\nimage_1.webp:")
info1 = subprocess.check_output(["identify", "-verbose", "public/image_1.webp"]).decode("utf-8")
for l in info1.splitlines():
    if any(k in l for k in ["Format", "Geometry", "Resolution", "Filesize", "Colorspace"]):
        print(" ", l.strip())
