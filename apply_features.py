with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update mapFilterBar
idx_start = html.find('<div class="map-filter-bar" id="mapFilterBar">')
assert idx_start != -1, "mapFilterBar not found"
idx_end = html.find('</div>', idx_start) + len('</div>')

new_fb = """<div class="map-filter-bar" id="mapFilterBar">
    <span class="filter-bar-title">فیلتر شاخص‌ها:</span>
    <button class="filter-chip active" data-filter="all">همه روستاها</button>
    <button class="filter-chip" data-filter="with-health">🏥 خانه بهداشت</button>
    <button class="filter-chip" data-filter="with-schools">🏫 دارای مدرسه</button>
    <button class="filter-chip" data-filter="with-dossier">📋 دارای پرونده جامع</button>
    <button class="filter-chip" data-filter="high-pop">👥 جمعیت بالای ۲,۰۰۰ نفر</button>
    <button class="filter-chip" data-filter="high-vuln">⚠️ اولویت فوری مداخله</button>
    <button class="filter-chip" data-filter="employment" onclick="window.open('https://rgaledari2-collab.github.io/pelak1-iran-employment/', '_blank')">💼 پروژه اشتغال ↗</button>
</div>"""

html = html[:idx_start] + new_fb + html[idx_end:]
print("1. Updated mapFilterBar with restored health house and new strategic filters!")

# 2. Update villageIndicators
idx_vi_s = html.find("const villageIndicators = {")
assert idx_vi_s != -1, "villageIndicators start not found"
idx_vi_e = html.find("};", idx_vi_s) + 2

new_vi = """const villageIndicators = {
                'soureh': ['with-schools', 'with-health', 'with-dossier', 'high-pop', 'employment'],
                'pol-now': ['with-schools', 'with-health', 'with-dossier', 'high-pop', 'high-vuln', 'employment'],
                'darband-gharbi': ['with-schools', 'with-health', 'with-dossier', 'high-pop', 'high-vuln', 'employment'],
                'maslavi-1': ['with-schools', 'with-health', 'with-dossier', 'high-pop', 'high-vuln'],
                'maslavi-2': ['with-schools', 'with-health', 'with-dossier', 'high-pop'],
                'shahrak-sevvom': ['with-schools', 'with-dossier', 'high-vuln'],
                'ariz': ['with-schools', 'with-health', 'with-dossier'],
                'mofti-ariz': ['high-pop'],
                'jadideh': ['with-schools', 'high-pop'],
                'sad-dastgah': ['with-schools', 'high-pop', 'high-vuln'],
                'sarhaniyeh-olya': ['with-schools', 'with-health', 'high-pop'],
                'sarhaniyeh-sofla': ['high-pop'],
                'darband-sharqi': [],
                'shahrak-sadat': ['high-vuln']
            };"""

html = html[:idx_vi_s] + new_vi + html[idx_vi_e:]
print("2. Updated villageIndicators!")

# 3. Update filter click listener with smart toast
idx_fl_s = html.find("filterChips.forEach(chip => {")
assert idx_fl_s != -1, "filterChips listener not found"
idx_fl_e = html.find("});\n            });", idx_fl_s) + len("});\n            });")

new_filter_listener = """filterChips.forEach(chip => {
                chip.addEventListener('click', () => {
                    const filter = chip.dataset.filter;
                    if (filter === 'employment') return;
                    filterChips.forEach(c => c.classList.remove('active'));
                    chip.classList.add('active');
                    activeMapFilter = filter;
                    villages.forEach(v => applyFilterToPin(v));

                    if (typeof showSearchToast === 'function') {
                        if (filter === 'with-health') {
                            const c = villages.filter(v => (villageIndicators[v.id] || []).includes('with-health')).length;
                            showSearchToast(`✓ ${c} روستای دارای خانه بهداشت روی نقشه مشخص شدند.`);
                        } else if (filter === 'with-schools') {
                            const c = villages.filter(v => (villageIndicators[v.id] || []).includes('with-schools')).length;
                            showSearchToast(`✓ ${c} روستای دارای مدرسه فعال هایلایت شدند.`);
                        } else if (filter === 'with-dossier') {
                            const c = villages.filter(v => (villageIndicators[v.id] || []).includes('with-dossier')).length;
                            showSearchToast(`✓ ${c} روستای دارای پرونده جامع میدانی تفکیک شدند.`);
                        } else if (filter === 'high-pop') {
                            const c = villages.filter(v => (villageIndicators[v.id] || []).includes('high-pop')).length;
                            showSearchToast(`✓ ${c} کانون روستایی با جمعیت بالای ۲,۰۰۰ نفر فیلتر شدند.`);
                        } else if (filter === 'high-vuln') {
                            const c = villages.filter(v => (villageIndicators[v.id] || []).includes('high-vuln')).length;
                            showSearchToast(`✓ ${c} روستای با ضریب آسیب‌پذیری بالا و نیاز فوری مداخله مشخص شدند.`);
                        } else if (filter === 'all') {
                            showSearchToast('نمایش کلیه روستاهای منطقه شلمچه و خرمشهر.');
                        }
                    }
                });
            });"""

html = html[:idx_fl_s] + new_filter_listener + html[idx_fl_e:]
print("3. Updated filter click listener!")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("SUCCESS: Stage 1 complete!")
