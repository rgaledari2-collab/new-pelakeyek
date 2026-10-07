with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

# Check topNavActions
idx_top = text.find('<div class="nav-actions" id="topNavActions">')
assert idx_top != -1, "topNavActions not found"

# Check mapTools
idx_tools = text.find('<nav class="map-tools" id="mapTools"')
assert idx_tools != -1, "mapTools not found"

print("Both insertion points found!")
