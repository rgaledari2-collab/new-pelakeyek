with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# -------------------------------------------------------------
# 1. Fix enter(v) so it does NOT prematurely open statsDialog
# -------------------------------------------------------------
idx_enter = html.find("function enter(v) {")
assert idx_enter != -1, "function enter(v) not found"
idx_timer = html.find("timer = setTimeout(() => {", idx_enter)
idx_timer_end = html.find("}, reduced ? 20 : 350);", idx_timer)
assert idx_timer != -1 and idx_timer_end != -1, "timer in enter(v) not found"

old_timer_body = html[idx_timer:idx_timer_end + len("}, reduced ? 20 : 350);")]

new_timer_body = """timer = setTimeout(() => {
                    phase = 'village';
                    root.classList.add('in-village');
                    root.classList.remove('flying');
                    village.inert = false;
                    const backMapBtn = $('backMap');
                    if (backMapBtn) backMapBtn.hidden = false;

                    // Update titles for selection screen
                    if (portalName) portalName.textContent = v.name;
                    if (villageName) villageName.textContent = v.name;
                    const servTitle = document.getElementById('servicesTitle');
                    if (servTitle) servTitle.textContent = 'خدمات و پروژه‌های ' + v.name;
                    const stTitle = document.getElementById('statsTitle');
                    if (stTitle) stTitle.textContent = 'آمار و شناسنامه ' + v.name;

                    // User is now on the Village Hub with choices: [01 آمار] and [02 خدمات]
                }, reduced ? 20 : 350);"""

html = html.replace(old_timer_body, new_timer_body, 1)
print("1. Fixed enter(v) so it lands on the Village Hub with 01 Stats & 02 Services choices!")

# -------------------------------------------------------------
# 2. Fix navigateToVillage so it only opens a section if sectionToOpen is specified
# -------------------------------------------------------------
idx_nv = html.find("function navigateToVillage(")
assert idx_nv != -1, "function navigateToVillage not found"
idx_open_stats = html.find("// Open Stats Dialog instantly", idx_nv)
assert idx_open_stats != -1, "// Open Stats Dialog instantly not found"
idx_kw = html.find("// Handle search keywords", idx_open_stats)
assert idx_kw != -1, "// Handle search keywords not found"

old_nav_open_block = html[idx_open_stats:idx_kw]

new_nav_open_block = """// Open section only if explicitly requested, otherwise stay on Village Hub choices
                if (sectionToOpen === 'stats') {
                    const statsDlg = $('statsDialog');
                    if (typeof updateDrawerClasses === 'function') updateDrawerClasses();
                    if (statsDlg) {
                        try {
                            if (!statsDlg.open) statsDlg.showModal();
                            statsDlg.scrollTop = 0;
                        } catch (err) {
                            statsDlg.setAttribute('open', '');
                        }
                    }
                } else if (sectionToOpen === 'services') {
                    const servDlg = $('servicesDialog');
                    if (servDlg) {
                        try {
                            if (!servDlg.open) servDlg.showModal();
                            servDlg.scrollTop = 0;
                        } catch (err) {
                            servDlg.setAttribute('open', '');
                        }
                    }
                }
                
                """

html = html.replace(old_nav_open_block, new_nav_open_block, 1)
print("2. Updated navigateToVillage conditional dialog opening!")

# -------------------------------------------------------------
# 3. Ensure statsButton and servicesButton click listeners are bound cleanly
# -------------------------------------------------------------
binding_code = """
        // Explicit binding for Village Hub choice cards
        document.addEventListener('DOMContentLoaded', () => {
            const stBtn = document.getElementById('statsButton');
            if (stBtn) {
                stBtn.addEventListener('click', () => {
                    const statsDlg = document.getElementById('statsDialog');
                    if (typeof updateDrawerClasses === 'function') updateDrawerClasses();
                    if (statsDlg) {
                        try {
                            if (!statsDlg.open) statsDlg.showModal();
                            statsDlg.scrollTop = 0;
                        } catch (e) {
                            statsDlg.setAttribute('open', '');
                        }
                    }
                });
            }

            const servBtn = document.getElementById('servicesButton');
            if (servBtn) {
                servBtn.addEventListener('click', () => {
                    const servDlg = document.getElementById('servicesDialog');
                    if (servDlg) {
                        try {
                            if (!servDlg.open) servDlg.showModal();
                            servDlg.scrollTop = 0;
                        } catch (e) {
                            servDlg.setAttribute('open', '');
                        }
                    }
                });
            }
        });
"""

idx_last_script = html.rfind("</script>")
html = html[:idx_last_script] + binding_code + "\n    " + html[idx_last_script:]
print("3. Injected explicit click listeners for statsButton and servicesButton!")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("SUCCESS: Village Hub entry flow restored perfectly!")
