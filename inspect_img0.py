import subprocess

# Let's see if there are any strings or metadata inside image_0.webp
with open("public/image_0.webp", "rb") as f:
    data = f.read()

# WebP chunks
print("image_0.webp length:", len(data))
print("First 100 bytes:", data[:100])

with open("public/image_1.webp", "rb") as f:
    data1 = f.read()
print("image_1.webp length:", len(data1))
print("First 100 bytes:", data1[:100])
