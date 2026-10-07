with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# --------------------------------------------------------------------------
# 1. HIDE GLOBAL <header> COMPLETELY IN .in-village
# --------------------------------------------------------------------------

# Replace .in-village #backMap:not([hidden]) rules with strict hiding
old_backmap_css_start = ".in-village #backMap:not([hidden]) {"
idx_bm_s = html.find(old_backmap_css_start)
if idx_bm_s != -1:
    idx_bm_e = html.find(".in-village .map-filter-bar", idx_bm_s)
    if idx_bm_e != -1:
        new_header_hide_css = """/* Village Mode: Completely hide global header and old backMap */
.in-village header,
.in-village #backMap,
.in-village header > * {
    display: none !important;
    visibility: hidden !important;
    pointer-events: none !important;
    opacity: 0 !important;
    height: 0 !important;
    width: 0 !important;
    overflow: hidden !important;
}

"""
        html = html[:idx_bm_s] + new_header_hide_css + html[idx_bm_e:]
        print("1. Replaced old .in-village #backMap CSS with complete header hiding!")

# --------------------------------------------------------------------------
# 2. UPDATE #villageTopBar: REMOVE "بازگشت به نقشه..." TEXT BUTTON AND ADD CLEAN LOGO + CLOSE (✕)
# --------------------------------------------------------------------------
old_top_bar = """        <div class="village-top-bar" id="villageTopBar">
            <div class="v-bar-right">
                <button type="button" class="v-back-btn" id="villageBackBtn" onclick="back()">
                    <span class="v-back-arrow">→</span>
                    <span>بازگشت به نقشه منطقه</span>
                </button>
                <div class="v-title-wrap">
                    <div class="v-badge-pill">
                        <span class="v-live-dot"></span>
                        <span id="villageKicker">نقشه اختصاصی تفصیلی · اتود پایش میدانی</span>
                    </div>
                    <h1 class="v-main-name" id="villageName">پل نو</h1>
                    <span class="v-main-sub" id="villageSubheading">محور مواصلاتی شلمچه - خرمشهر · حومه غربی</span>
                </div>
            </div>
            <div class="v-bar-left">
                <div class="v-layout-controls">
                    <button type="button" class="v-layout-btn" id="vToggleSidebar" title="تغییر کادربندی (ستون داده‌ها / تمام‌صفحه)">
                        <span class="v-layout-icon">◫</span>
                        <span id="vToggleSidebarText">نمای تمام‌صفحه نقشه</span>
                    </button>
                </div>
                <div class="v-top-chips" id="villageQuickChips">
                    <span class="v-top-chip" id="vChipPop">👥 ۳,۸۵۰ نفر</span>
                    <span class="v-top-chip" id="vChipFam">🏡 ۹۵۰ خانوار</span>
                    <span class="v-top-chip" id="vChipSchool">🎒 دبستان معراج</span>
                </div>
            </div>
        </div>"""

new_top_bar = """        <div class="village-top-bar" id="villageTopBar">
            <div class="v-bar-right">
                <!-- Clean integrated logo -->
                <div class="v-brand-icon">
                    <img src="/logo_clean.png" onerror="this.onerror=null;this.src='/new_logo.png';" alt="جمعیت امام رضایی‌ها" class="v-brand-img" />
                </div>
                <div class="v-title-wrap">
                    <div class="v-badge-pill">
                        <span class="v-live-dot"></span>
                        <span id="villageKicker">نقشه اختصاصی تفصیلی · اتود پایش میدانی</span>
                    </div>
                    <h1 class="v-main-name" id="villageName">پل نو</h1>
                    <span class="v-main-sub" id="villageSubheading">محور مواصلاتی شلمچه - خرمشهر · حومه غربی</span>
                </div>
            </div>
            <div class="v-bar-left">
                <div class="v-layout-controls">
                    <button type="button" class="v-layout-btn" id="vToggleSidebar" title="تغییر کادربندی (ستون داده‌ها / تمام‌صفحه)">
                        <span class="v-layout-icon">◫</span>
                        <span id="vToggleSidebarText">نمای تمام‌صفحه نقشه</span>
                    </button>
                </div>
                <div class="v-top-chips" id="villageQuickChips">
                    <span class="v-top-chip" id="vChipPop">👥 ۳,۸۵۰ نفر</span>
                    <span class="v-top-chip" id="vChipFam">🏡 ۹۵۰ خانوار</span>
                    <span class="v-top-chip" id="vChipSchool">🎒 دبستان معراج</span>
                </div>
                <!-- Discreet, clean close button without verbose text -->
                <button type="button" class="v-close-btn" id="villageCloseBtn" onclick="back()" title="بستن و بازگشت به نقشه منطقه">✕</button>
            </div>
        </div>"""

assert old_top_bar in html, "old_top_bar not found"
html = html.replace(old_top_bar, new_top_bar, 1)
print("2. Updated #villageTopBar: removed 'بازگشت به نقشه...' text button and added integrated logo + discrete ✕ close button!")

# --------------------------------------------------------------------------
# 3. UPDATE CSS FOR .v-brand-icon AND .v-close-btn
# --------------------------------------------------------------------------
old_css_vbar = ".v-back-btn {"
idx_vbar_s = html.find(old_css_vbar)
if idx_vbar_s != -1:
    idx_vbar_e = html.find(".v-title-wrap {", idx_vbar_s)
    if idx_vbar_e != -1:
        new_vbar_css = """.v-brand-icon {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 38px;
    width: auto;
}

.v-brand-img {
    height: 34px;
    width: auto;
    object-fit: contain;
    filter: drop-shadow(0 2px 8px rgba(0,0,0,0.5));
}

.v-close-btn {
    width: 38px;
    height: 38px;
    border-radius: 50%;
    background: rgba(237, 211, 149, 0.12);
    border: 1.2px solid rgba(237, 211, 149, 0.38);
    color: #edd395;
    font-size: 16px;
    font-weight: 800;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: all 0.2s ease;
    margin-right: 6px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.35);
}

.v-close-btn:hover {
    background: #edd395;
    color: #0b1a18;
    transform: scale(1.08);
    box-shadow: 0 6px 16px rgba(237, 211, 149, 0.45);
}

"""
        html = html[:idx_vbar_s] + new_vbar_css + html[idx_vbar_e:]
        print("3. Injected .v-brand-icon and .v-close-btn CSS!")

# --------------------------------------------------------------------------
# 4. REMOVE SHOWING backMap IN enter(v)
# --------------------------------------------------------------------------
html = html.replace("if (backMapBtn) backMapBtn.hidden = false;", "// backMap hidden in village view\n                    if (backMapBtn) backMapBtn.hidden = true;")
print("4. Kept backMap hidden inside enter(v)!")

# --------------------------------------------------------------------------
# 5. SUPPORT ESCAPE KEY IN VILLAGE VIEW
# --------------------------------------------------------------------------
esc_hook = """window.addEventListener('keydown', (e) => {
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

idx_setup = html.find("function setupVillageInteractions()")
if idx_setup != -1:
    html = html[:idx_setup] + esc_hook + "\n\n        " + html[idx_setup:]
    print("5. Added Escape key support to exit village view!")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("SUCCESS: Header collision fixed and 'بازگشت به نقشه عمومی' removed!")
