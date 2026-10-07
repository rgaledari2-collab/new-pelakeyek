import subprocess

for img in ["public/image_0.webp", "public/image_1.webp", "public/image_2.png", "public/image_3.png", "public/map_user_upload.jpg"]:
    # Let's crop middle and check colors / or convert to txt
    # ImageMagick can output txt: format for a 5x5 sample
    out = subprocess.check_output(["convert", img, "-resize", "10x10!", "txt:-"]).decode("utf-8")
    lines = [l for l in out.splitlines() if not l.startswith("#")]
    sample_colors = [l.split()[-1] for l in lines[:5]]
    print(f"{img}: sample colors -> {sample_colors}")
