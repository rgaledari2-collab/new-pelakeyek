with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Check where maslavi-2 is in villages
idx_m2 = html.find("{ id: 'maslavi-2'")
print("Found maslavi-2 in villages at:", idx_m2)
assert idx_m2 != -1

# Check where getVillageAccordions has maslavi-2
idx_gva = html.find("villageId === 'maslavi-2'")
print("Found maslavi-2 in getVillageAccordions at:", idx_gva)
assert idx_gva != -1

print("Ready to apply updates!")
