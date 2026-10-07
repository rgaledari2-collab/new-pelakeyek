with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

assert 'id="statsDialog"' in text
assert 'id="mapPlane"' in text
assert 'id="mapFilterBar"' in text
print("All anchor tags confirmed in index.html!")
