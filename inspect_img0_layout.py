import subprocess

# Let's inspect image_0.webp in detail
# Dimensions: 895x762
# Let's check the corners and center to see what kind of map this is:
# e.g., is there a road passing through? Where are the settlements?
print("Copying image_0.webp to pol_now_map.webp and generating pol_now_map.jpg...")
subprocess.run(["cp", "public/image_0.webp", "public/pol_now_map.webp"])
subprocess.run(["convert", "public/image_0.webp", "-quality", "95", "public/pol_now_map.jpg"])
subprocess.run(["cp", "public/pol_now_map.webp", "dist/pol_now_map.webp"])
subprocess.run(["cp", "public/pol_now_map.jpg", "dist/pol_now_map.jpg"])
print("Files copied successfully!")
