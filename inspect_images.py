import subprocess, os

imgs = [
    "public/image_0.webp",
    "public/image_1.webp",
    "public/image_2.png",
    "public/image_3.png",
    "public/map_user_upload.jpg",
    "public/main_map_final.jpg"
]

for img in imgs:
    if os.path.exists(img):
        # get size and dimensions
        dim = subprocess.check_output(["identify", "-format", "%w x %h, format: %m, size: %b", img]).decode("utf-8").strip()
        print(f"=== {img} === ({dim})")
