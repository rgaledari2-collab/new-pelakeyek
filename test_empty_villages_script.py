with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

# Check villages array
idx_v = text.find("const villages = [")
idx_ve = text.find("];", idx_v)
villages_block = text[idx_v:idx_ve]

print("Villages block length:", len(villages_block))
assert "'ariz'" in villages_block
assert "'darband-gharbi'" in villages_block
assert "'sad-dastgah'" in villages_block
print("Villages block check passed!")
