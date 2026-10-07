import subprocess

# Let's check where the features are in image_0 (895x762)
# Center: x=447, y=381 (50%, 50%)
# Red marker: x=753, y=447 (84%, 58%) -> This is a key tagged location in the user's photo!
print("Red marker in image_0: left: 84%, top: 58%")

# Let's check brightness in 3x3 grid of image_0
for r in range(3):
    for c in range(3):
        x = c * 298
        y = r * 254
        crop = f"298x254+{x}+{y}"
        out = subprocess.check_output(["convert", "public/image_0.webp", "-crop", crop, "-scale", "1x1!", "-colorspace", "Gray", "txt:-"]).decode()
        val = float(out.splitlines()[-1].split("(")[1].split(",")[0].replace("%",""))
        print(f"Grid ({r},{c}) at [{x},{y}]: gray={val:.1f}")
