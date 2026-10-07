import subprocess

# Let's convert both to png to inspect
subprocess.run(["convert", "public/image_0.webp", "/tmp/img0.png"])
subprocess.run(["convert", "public/image_1.webp", "/tmp/img1.png"])

# Let's check if there are text boxes or recognizable features
# We can do edge detection or crop corners to see what text/labels are present!
# In ImageMagick, we can crop the top, bottom, center of both images:
# img0 is 895x762
# Let's check color histograms or text-like areas
print("img0 converted, size:", subprocess.check_output(["identify", "/tmp/img0.png"]).decode())
print("img1 converted, size:", subprocess.check_output(["identify", "/tmp/img1.png"]).decode())
