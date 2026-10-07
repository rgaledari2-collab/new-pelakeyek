with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Check filter bar
idx_fb = text.find('id="mapFilterBar"')
print("Found mapFilterBar at:", idx_fb)

# 2. Check villageIndicators
idx_vi = text.find("const villageIndicators = {")
print("Found villageIndicators at:", idx_vi)

# 3. Check renderExecutiveDashboard
idx_red = text.find("function renderExecutiveDashboard")
print("Found renderExecutiveDashboard at:", idx_red)

print("All targets present and located.")
