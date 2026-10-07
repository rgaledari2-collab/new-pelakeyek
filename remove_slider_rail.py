with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Remove CSS
css_start = "/* ==================== VILLAGE HORIZONTAL SLIDER RAIL (SENIOR UX) ==================== */"
idx_cs = html.find(css_start)
if idx_cs != -1:
    idx_ce = html.find(".rail-village-card:hover .rail-card-action {\n            color: #facc15;\n        }", idx_cs)
    if idx_ce != -1:
        idx_ce += len(".rail-village-card:hover .rail-card-action {\n            color: #facc15;\n        }")
        html = html[:idx_cs] + html[idx_ce:]
        print("1. Removed slider rail CSS!")

# 2. Remove Markup
markup_start = "<!-- Village Horizontal Slider Rail (Senior UX) -->"
idx_ms = html.find(markup_start)
if idx_ms != -1:
    idx_me = html.find('<div id="catchmentLegend"', idx_ms)
    if idx_me != -1:
        html = html[:idx_ms] + html[idx_me:]
        print("2. Removed slider rail markup!")

# 3. Remove JS
js_start = "// =========================================================================\n        // VILLAGE HORIZONTAL SLIDER RAIL ENGINE (SENIOR UX)"
idx_js = html.find(js_start)
if idx_js != -1:
    idx_je = html.find("setTimeout(() => {\n            buildVillageSliderRail();\n        }, 150);", idx_js)
    if idx_je != -1:
        idx_je += len("setTimeout(() => {\n            buildVillageSliderRail();\n        }, 150);")
        html = html[:idx_js] + html[idx_je:]
        print("3. Removed slider rail JS!")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("SUCCESS: Village Slider Rail completely deleted!")
