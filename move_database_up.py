with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

# Locate the database block
db_start = text.find("const comparisonData = {")
db_end = text.find("function getVillageData(v) {")

db_block = text[db_start:db_end].strip()

# Ensure window bindings
if "window.villageDatabase =" not in db_block:
    db_block += "\n            window.villageDatabase = villageDatabase;\n            window.comparisonData = comparisonData;\n"

# Remove db_block from text
text_without_db = text[:db_start] + text[db_end:]

# Find target location: right before '// Universal Village Object Resolver'
target_marker = "// Universal Village Object Resolver (Aliases, IDs, and Fallbacks)"
target_idx = text_without_db.find(target_marker)

if target_idx == -1:
    print("ERROR: target marker not found!")
    exit(1)

new_text = text_without_db[:target_idx] + db_block + "\n\n            " + text_without_db[target_idx:]

with open("index.html", "w", encoding="utf-8") as f:
    f.write(new_text)

print("Successfully moved villageDatabase and comparisonData before resolveVillageObject!")
