import json

with open("/tmp/master_searchable_data.json", "r", encoding="utf-8") as f:
    master_data = json.load(f)

# verify fields in person records
sample_orphan = [p for p in master_data if p.get("badge") == "ایتام"][0]
sample_needy = [p for p in master_data if p.get("badge") == "مددجو"][0]

print("Sample orphan fields:", list(sample_orphan.keys()))
print("Sample needy fields:", list(sample_needy.keys()))
print("Orphan:", sample_orphan["title"], "| Guardian:", sample_orphan.get("guardian"), "| NID:", sample_orphan.get("nationalId"), "| Phone:", sample_orphan.get("phone"))
print("Needy:", sample_needy["title"], "| NID:", sample_needy.get("nationalId"), "| Phone:", sample_needy.get("phone"))
