import subprocess

# Let's see what is inside image_0.webp:
# Is image_0.webp a screenshot? A map? A photo of a village?
# Let's inspect unique colors or text blocks
out = subprocess.check_output(["identify", "-format", "%[colors]", "public/image_0.webp"]).decode().strip()
print("image_0.webp unique colors:", out)

out1 = subprocess.check_output(["identify", "-format", "%[colors]", "public/image_1.webp"]).decode().strip()
print("image_1.webp unique colors:", out1)

# Let's check image_2 and image_3
out2 = subprocess.check_output(["identify", "-format", "%[colors]", "public/image_2.png"]).decode().strip()
print("image_2.png unique colors:", out2)

out3 = subprocess.check_output(["identify", "-format", "%[colors]", "public/image_3.png"]).decode().strip()
print("image_3.png unique colors:", out3)
