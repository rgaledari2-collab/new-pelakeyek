import struct

with open("/tmp/img1.bmp", "rb") as f:
    header = f.read(54)
    width, height = struct.unpack("<ii", header[18:26])
    row_size = ((width * 3 + 3) // 4) * 4
    
    markers = []
    for y in range(0, height, 4):
        f.seek(54 + (height - 1 - y) * row_size)
        row_data = f.read(row_size)
        for x in range(0, width, 4):
            b, g, r = row_data[x*3], row_data[x*3+1], row_data[x*3+2]
            if r > 200 and g > 180 and b < 100:
                markers.append(('yellow', x, y))
            elif r > 200 and g < 80 and b < 80:
                markers.append(('red', x, y))
            elif b > 200 and r < 80 and g < 150:
                markers.append(('blue', x, y))

    print(f"img1: yellow pixels={len([m for m in markers if m[0]=='yellow'])}, red={len([m for m in markers if m[0]=='red'])}, blue={len([m for m in markers if m[0]=='blue'])}")
    if markers:
        for color in ['yellow', 'red', 'blue']:
            c_markers = [m for m in markers if m[0] == color]
            if c_markers:
                min_x = min(m[1] for m in c_markers)
                max_x = max(m[1] for m in c_markers)
                min_y = min(m[2] for m in c_markers)
                max_y = max(m[2] for m in c_markers)
                print(f"  {color} bounding box: x=[{min_x}, {max_x}], y=[{min_y}, {max_y}]")
