with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

# Let's inspect from 'const comparisonData' to 'function getVillageData'
start_idx = text.find("const comparisonData = {")
end_idx = text.find("function getVillageData", start_idx)

print("start_idx:", start_idx, "end_idx:", end_idx)
block = text[start_idx:end_idx]

# Check what was in that block
print("Block length:", len(block))
