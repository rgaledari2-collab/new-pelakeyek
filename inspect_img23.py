import subprocess

for img in ["public/image_2.png", "public/image_3.png"]:
    info = subprocess.check_output(["identify", img]).decode().strip()
    print(img, ":", info)
    # Check non-transparent bounding box
    bbox = subprocess.check_output(["convert", img, "-trim", "-format", "%wx%h%O", "info:"]).decode().strip()
    print("  trimmed bounding box:", bbox)
