with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Remove from map-filter-bar
old_chips = """    <button class="filter-chip" data-filter="with-schools">دارای مدرسه</button>
    <button class="filter-chip" data-filter="with-health">خانه بهداشت</button>
    <button class="filter-chip" data-filter="with-dossier">دارای پرونده جامع</button>
    <button class="filter-chip" data-filter="employment" onclick="window.open('https://rgaledari2-collab.github.io/pelak1-iran-employment/', '_blank')">💼 پروژه اشتغال ↗</button>
    <button class="filter-chip" id="corridorToggleBtn" data-corridor="false">🛣️ محور مواصلاتی شلمچه</button>"""

new_chips = """    <button class="filter-chip" data-filter="with-schools">دارای مدرسه</button>
    <button class="filter-chip" data-filter="with-dossier">دارای پرونده جامع</button>
    <button class="filter-chip" data-filter="employment" onclick="window.open('https://rgaledari2-collab.github.io/pelak1-iran-employment/', '_blank')">💼 پروژه اشتغال ↗</button>"""

assert old_chips in html, "old_chips not found"
html = html.replace(old_chips, new_chips, 1)
print("1. Removed 'خانه بهداشت' and 'محور مواصلاتی' filter chips from map-filter-bar!")

# 2. Remove mapCorridorOverlay SVG
svg_start = '<svg class="map-corridor-overlay" id="mapCorridorOverlay"'
svg_end = '</svg>'
idx_svg_s = html.find(svg_start)
idx_svg_e = html.find(svg_end, idx_svg_s) + len(svg_end)
assert idx_svg_s != -1 and idx_svg_e != -1, "mapCorridorOverlay SVG not found"
html = html[:idx_svg_s] + html[idx_svg_e:]
print("2. Removed mapCorridorOverlay SVG from mapPlane!")

# 3. Remove corridorToggleBtn JavaScript listener
js_corridor_marker = "// Transport corridor toggle"
idx_js_c = html.find(js_corridor_marker)
if idx_js_c != -1:
    end_js_c = html.find("}", html.find("corridorBtn.addEventListener", idx_js_c) + 20)
    end_js_c = html.find("}", end_js_c + 1)
    end_js_c = html.find("}", end_js_c + 1) + 1
    html = html[:idx_js_c] + html[end_js_c:]
    print("3. Removed corridorToggleBtn JavaScript listener!")

# 4. Remove 'with-health' from villageIndicators
html = html.replace(", 'with-health'", "").replace("'with-health', ", "").replace("'with-health'", "")
print("4. Removed 'with-health' tag from villageIndicators!")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("SUCCESS: Corridor and health house map layers cleanly removed!")
