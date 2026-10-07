with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# --------------------------------------------------------------------------
# 1. Remove the two buttons from statsDialog header
# --------------------------------------------------------------------------
old_header_controls = """            <div style="display:flex; align-items:center; gap:12px;">
                <button type="button" class="nav-action-btn" id="statsBackToMapBtn" title="بستن شناسنامه و بازگشت به نقشه منطقه" style="font-size:12px; height:34px; padding:0 14px; background:rgba(237,211,149,0.2); border:1px solid rgba(237,211,149,0.6); color:#edd395; border-radius:8px; font-weight:700; cursor:pointer;">
                    🗺️ بازگشت به نقشه
                </button>
                <button id="toggleDrawerModeBtn" class="drawer-control-btn" title="تغییر وضعیت نمایش (کشویی کنار نقشه یا تمام‌صفحه)">
                    <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2">
                        <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
                        <line x1="9" y1="3" x2="9" y2="21"></line>
                    </svg>
                    <span id="drawerToggleText">تمام‌صفحه</span>
                </button>
                <button class="close" id="closeStatsBtn" aria-label="بستن آمار">×</button>
            </div>"""

new_header_controls = """            <div style="display:flex; align-items:center; gap:12px;">
                <button class="close" id="closeStatsBtn" aria-label="بستن آمار">×</button>
            </div>"""

assert old_header_controls in html, "old_header_controls not found"
html = html.replace(old_header_controls, new_header_controls, 1)
print("1. Removed toggleDrawerModeBtn and statsBackToMapBtn from HTML!")

# --------------------------------------------------------------------------
# 2. Clean up split-drawer-mode CSS overrides
# --------------------------------------------------------------------------
# Remove split-drawer-mode rules so statsDialog always displays as clean centered dialog
idx_drawer_css = html.find("/* ==================== KINETIC SPLIT-PANE DRAWER ARCHITECTURE (SENIOR UX) ==================== */")
if idx_drawer_css != -1:
    idx_drawer_css_end = html.find("/* ==================== SPATIAL RETICLE", idx_drawer_css)
    if idx_drawer_css_end != -1:
        html = html[:idx_drawer_css] + html[idx_drawer_css_end:]
        print("2. Removed drawer mode CSS rules!")

# --------------------------------------------------------------------------
# 3. Clean up JS functions/event listeners for drawer mode and statsBackToMapBtn
# --------------------------------------------------------------------------
# Clean JS references
old_js_drawer = """        // =========================================================================
        // KINETIC SPLIT-PANE DRAWER & TWO-WAY SPATIAL CONNECTION (SENIOR UX)
        // =========================================================================
        let isDrawerMode = (window.innerWidth >= 1024);

        function updateDrawerClasses() {
            const statsDlg = document.getElementById('statsDialog');
            const mapSceneEl = document.getElementById('mapScene');
            const toggleText = document.getElementById('drawerToggleText');
            if (!statsDlg) return;

            if (isDrawerMode && window.innerWidth >= 1024) {
                statsDlg.classList.add('split-drawer-mode');
                statsDlg.classList.remove('fullscreen-modal-mode');
                if (statsDlg.open && mapSceneEl) {
                    mapSceneEl.classList.add('drawer-open');
                }
                if (toggleText) toggleText.textContent = 'تمام‌صفحه';
            } else {
                statsDlg.classList.remove('split-drawer-mode');
                statsDlg.classList.add('fullscreen-modal-mode');
                if (mapSceneEl) {
                    mapSceneEl.classList.remove('drawer-open');
                }
                if (toggleText) toggleText.textContent = 'حالت کشویی (کنار نقشه)';
            }
        }

        window.toggleDrawerMode = function() {
            isDrawerMode = !isDrawerMode;
            updateDrawerClasses();
        };"""

new_js_drawer = """        // Window drawer helpers (no-op after removing drawer mode)
        function updateDrawerClasses() {}
        window.toggleDrawerMode = function() {};"""

if old_js_drawer in html:
    html = html.replace(old_js_drawer, new_js_drawer, 1)
    print("3. Replaced JS drawer mode logic with clean no-op!")

# Clean event listener for statsBackToMapBtn if present
old_back_listener = """                const statsBackToMapBtn = document.getElementById('statsBackToMapBtn');
                if (statsBackToMapBtn) {
                    statsBackToMapBtn.addEventListener('click', () => {
                        statsDialog.close();
                        if (typeof back === 'function') back();
                    });
                }"""
if old_back_listener in html:
    html = html.replace(old_back_listener, "", 1)
    print("4. Removed statsBackToMapBtn event listener!")

# Remove toggleDrawerBtn binding
old_toggle_bind = """            const toggleDrawerBtn = document.getElementById('toggleDrawerModeBtn');
            if (toggleDrawerBtn) {
                toggleDrawerBtn.addEventListener('click', window.toggleDrawerMode);
            }"""
if old_toggle_bind in html:
    html = html.replace(old_toggle_bind, "", 1)

old_tDBtn = """            const tDBtn = document.getElementById('toggleDrawerModeBtn');
            if (tDBtn && !tDBtn._bound) {
                tDBtn._bound = true;
                tDBtn.addEventListener('click', window.toggleDrawerMode);
            }"""
if old_tDBtn in html:
    html = html.replace(old_tDBtn, "", 1)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("SUCCESS: Screenshot buttons removed completely!")
