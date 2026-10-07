with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update button in mapFilterBar
old_btn = '<button class="filter-chip" data-filter="employment" onclick="window.open(\'https://rgaledari2-collab.github.io/pelak1-iran-employment/\', \'_blank\')">💼 پروژه اشتغال ↗</button>'
new_btn = '<button class="filter-chip" data-filter="employment">💼 دارای طرح اشتغال</button>'

assert old_btn in html, "old_btn not found"
html = html.replace(old_btn, new_btn, 1)
print("1. Replaced external link button with regular filter chip!")

# 2. Update villageIndicators to include employment tags
old_vi = """const villageIndicators = {
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

new_vi = """const villageIndicators = {
                'soureh': ['with-schools', 'with-health', 'with-dossier', 'high-pop', 'employment'],
                'pol-now': ['with-schools', 'with-health', 'with-dossier', 'high-pop', 'high-vuln', 'employment'],
                'darband-gharbi': ['with-schools', 'with-health', 'with-dossier', 'high-pop', 'high-vuln', 'employment'],
                'maslavi-1': ['with-schools', 'with-health', 'with-dossier', 'high-pop', 'high-vuln', 'employment'],
                'maslavi-2': ['with-schools', 'with-health', 'with-dossier', 'high-pop', 'employment'],
                'shahrak-sevvom': ['with-schools', 'with-dossier', 'high-vuln'],
                'ariz': ['with-schools', 'with-health', 'with-dossier'],
                'mofti-ariz': ['high-pop'],
                'jadideh': ['with-schools', 'high-pop', 'employment'],
                'sad-dastgah': ['with-schools', 'high-pop', 'high-vuln', 'employment'],
                'sarhaniyeh-olya': ['with-schools', 'with-health', 'high-pop'],
                'sarhaniyeh-sofla': ['high-pop'],
                'darband-sharqi': [],
                'shahrak-sadat': ['high-vuln']
            };"""

assert old_vi in html, "old_vi not found"
html = html.replace(old_vi, new_vi, 1)
print("2. Updated villageIndicators with employment tag for active villages!")

# 3. Update filter click handler (remove early return and add employment toast)
old_handler = """filterChips.forEach(chip => {
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

new_handler = """filterChips.forEach(chip => {
                chip.addEventListener('click', () => {
                    const filter = chip.dataset.filter;
                    filterChips.forEach(c => c.classList.remove('active'));
                    chip.classList.add('active');
                    activeMapFilter = filter;
                    villages.forEach(v => applyFilterToPin(v));

                    if (typeof showSearchToast === 'function') {
                        if (filter === 'employment') {
                            const c = villages.filter(v => (villageIndicators[v.id] || []).includes('employment')).length;
                            showSearchToast(`✓ ${c} روستای دارای طرح‌های اشتغال و کارآفرینی فعال روی نقشه هایلایت شدند.`);
                        } else if (filter === 'with-health') {
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

assert old_handler in html, "old_handler not found"
html = html.replace(old_handler, new_handler, 1)
print("3. Updated filter click handler to filter employment in-app!")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("SUCCESS: Employment filter converted to in-app filter!")
