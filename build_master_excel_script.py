import json

# Let's verify how many orphans and needy we have in searchableData
with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

s_idx = text.find("const searchableData = [")
e_idx = text.find("];\n\n            let currentSearchCategory", s_idx)
data_str = text[s_idx + len("const searchableData = "):e_idx + 1]
data = json.loads(data_str)

orphans = [item for item in data if item.get("personType") == "orphan"]
needy = [item for item in data if item.get("personType") == "needy"]

print(f"Total orphans in searchableData: {len(orphans)}")
print(f"Total needy in searchableData: {len(needy)}")
print(f"Total beneficiaries: {len(orphans) + len(needy)}")

# Group by village
from collections import Counter
print("Orphans by village:", Counter(o.get("village") for o in orphans))
print("Needy by village:", Counter(n.get("village") for n in needy))
