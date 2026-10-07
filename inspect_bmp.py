import struct

def inspect_bmp(path):
    with open(path, "rb") as f:
        header = f.read(54)
        width, height = struct.unpack("<ii", header[18:26])
        bpp = struct.unpack("<h", header[28:30])[0]
        print(f"{path}: width={width}, height={height}, bpp={bpp}")
        
        # Read all pixels (BGR 24-bit)
        f.seek(54)
        row_size = ((width * 3 + 3) // 4) * 4
        
        # Count color ranges:
        # Greenish (vegetation/palms)
        # Sandy/Brownish (desert/soil/buildings)
        # Blueish (water/canals)
        # White/light (roads/buildings)
        # Dark
        green, sand, blue, white, dark, other = 0, 0, 0, 0, 0, 0
        total = 0
        
        # Sample every 5th row, 5th col
        for y in range(0, abs(height), 4):
            f.seek(54 + y * row_size)
            row_data = f.read(row_size)
            for x in range(0, width, 4):
                b = row_data[x*3]
                g = row_data[x*3 + 1]
                r = row_data[x*3 + 2]
                total += 1
                
                # classify
                if r > 200 and g > 200 and b > 200:
                    white += 1
                elif r < 40 and g < 40 and b < 40:
                    dark += 1
                elif g > r + 15 and g > b + 15:
                    green += 1
                elif b > r + 15 and b > g + 15:
                    blue += 1
                elif r > g and g > b:
                    sand += 1
                else:
                    other += 1
        
        print(f"  Distribution: sand={sand/total:.1%}, green={green/total:.1%}, blue={blue/total:.1%}, white={white/total:.1%}, dark={dark/total:.1%}, other={other/total:.1%}")

inspect_bmp("/tmp/img0.bmp")
inspect_bmp("/tmp/img1.bmp")
