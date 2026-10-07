import subprocess

# Let's use ImageMagick to threshold and find text connected components!
# convert image_0.webp -threshold 50% -define connected-components:verbose=true ...
out = subprocess.check_output([
    "convert", "public/image_0.webp",
    "-negate", "-threshold", "60%",
    "-define", "connected-components:verbose=true",
    "-define", "connected-components:area-threshold=50",
    "-connected-components", "objects.png",
    "null:"
]).decode("utf-8")

lines = out.splitlines()
print(f"Total components in image_0: {len(lines)}")
for l in lines[:20]:
    print(l)
