with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

print("Original HTML length:", len(html))

# Check 1: Old village section
old_village_marker = '<section class="village" id="village" inert aria-label="روستای سوره">'
idx_v = html.find(old_village_marker)
print("Found old village marker at:", idx_v)

# Check 2: Catchment legend
idx_c = html.find('<!-- Spatial Catchment Legend (Senior UX) -->')
print("Found catchment legend at:", idx_c)

# Check 3: Catchment JS
idx_cjs = html.find('// SPATIAL CATCHMENT & SERVICE DESERTS ENGINE')
print("Found catchment JS at:", idx_cjs)

# Check 4: enter(v) function
idx_enter = html.find('function enter(v) {')
print("Found enter(v) at:", idx_enter)

print("All markers found:", all(x != -1 for x in [idx_v, idx_c, idx_cjs, idx_enter]))
