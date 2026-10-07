with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# --------------------------------------------------------------------------
# 1. EXPOSE window.back = back IN MAIN MAP SCRIPT
# --------------------------------------------------------------------------
old_back_fn = """            function back() {
                if (phase !== 'village' && phase !== 'flying') return;
                clearTimeout(timer); clearTimeout(finishTimer);
                phase = 'map';
                root.classList.remove('in-village', 'flying');
                village.inert = true;
                map.inert = false;
                updateDOM();
                villages.forEach(x => { if (x.el) x.el.disabled = false; });
                $('backMap').hidden = true;
                if (activeLocation && activeLocation.el) activeLocation.el.focus({ preventScroll: true });
            }"""

new_back_fn = """            function back() {
                if (phase !== 'village' && phase !== 'flying') return;
                clearTimeout(timer); clearTimeout(finishTimer);
                phase = 'map';
                root.classList.remove('in-village', 'flying');
                village.inert = true;
                map.inert = false;
                updateDOM();
                villages.forEach(x => { if (x.el) x.el.disabled = false; });
                $('backMap').hidden = true;
                if (activeLocation && activeLocation.el) activeLocation.el.focus({ preventScroll: true });
            }
            window.back = back;"""

assert old_back_fn in html, "old_back_fn not found"
html = html.replace(old_back_fn, new_back_fn, 1)
print("1. Exposed window.back = back in main map script!")

# --------------------------------------------------------------------------
# 2. REMOVE REDUNDANT KEYDOWN LISTENER WITH UNDEFINED phase
# --------------------------------------------------------------------------
redundant_keydown = """window.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && phase === 'village') {
                const sDlg = document.getElementById('statsDialog');
                const srvDlg = document.getElementById('servicesDialog');
                const pDlg = document.getElementById('personDossierDialog');
                if ((sDlg && sDlg.open) || (srvDlg && srvDlg.open) || (pDlg && pDlg.open)) {
                    return; // let dialog close
                }
                if (typeof back === 'function') back();
            }
        });"""

assert redundant_keydown in html, "redundant_keydown not found"
html = html.replace(redundant_keydown, "// Escape handling handled by main map controller", 1)
print("2. Removed redundant keydown listener that caused ReferenceError: phase is not defined!")

# --------------------------------------------------------------------------
# 3. UPDATE #villageCloseBtn: REMOVE INLINE onclick="back()" & BIND IN JS
# --------------------------------------------------------------------------
old_close_btn = '<button type="button" class="v-close-btn" id="villageCloseBtn" onclick="back()" title="بستن و بازگشت به نقشه منطقه">✕</button>'
new_close_btn = '<button type="button" class="v-close-btn" id="villageCloseBtn" title="بستن و بازگشت به نقشه منطقه">✕</button>'

assert old_close_btn in html, "old_close_btn not found"
html = html.replace(old_close_btn, new_close_btn, 1)
print("3. Removed inline onclick='back()' from #villageCloseBtn!")

# 4. Bind villageCloseBtn in setupVillageInteractions
old_binding = "const bBtn = document.getElementById('villageBackBtn');"
new_binding = """const bBtn = document.getElementById('villageBackBtn');
            const cBtn = document.getElementById('villageCloseBtn');
            if (cBtn && !cBtn._bound) {
                cBtn._bound = true;
                cBtn.onclick = (e) => {
                    e.stopPropagation();
                    if (typeof window.back === 'function') window.back();
                };
            }"""

assert old_binding in html, "old_binding not found"
html = html.replace(old_binding, new_binding, 1)
print("4. Bound #villageCloseBtn click handler cleanly in setupVillageInteractions!")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("SUCCESS: Both ReferenceErrors fixed completely!")
