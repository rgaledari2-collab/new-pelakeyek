import subprocess

# Let's check what kind of image image_0.webp is vs image_1.webp
# We can check color histograms or edge detection
out0 = subprocess.check_output(["identify", "-format", "%[colorspace] - %[mean] - %[standard_deviation]", "public/image_0.webp"]).decode("utf-8")
out1 = subprocess.check_output(["identify", "-format", "%[colorspace] - %[mean] - %[standard_deviation]", "public/image_1.webp"]).decode("utf-8")
out_map = subprocess.check_output(["identify", "-format", "%[colorspace] - %[mean] - %[standard_deviation]", "public/map_user_upload.jpg"]).decode("utf-8")

print("image_0.webp:", out0)
print("image_1.webp:", out1)
print("map_user_upload.jpg:", out_map)
