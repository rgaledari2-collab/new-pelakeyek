with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

assert 'id="maslavi-1"' or "'maslavi-1'" in text
assert 'id="maslavi-2"' or "'maslavi-2'" in text
assert 'id="mapScene"' in text

print("Found anchors for Maslavi and mapScene!")
