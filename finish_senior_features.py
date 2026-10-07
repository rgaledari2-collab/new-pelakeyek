with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# -------------------------------------------------------------
# 4. Inject catchmentLegend before </section>
# -------------------------------------------------------------
idx_ms = html.find('id="mapScene"')
idx_end = html.find('</section>', idx_ms)
assert idx_ms != -1 and idx_end != -1, "mapScene closing tag not found"

catchment_legend_markup = """
    <!-- Spatial Catchment Legend (Senior UX) -->
    <div id="catchmentLegend" class="catchment-legend" style="display:none;">
        <div class="legend-header">
            <span class="legend-dot-live"></span>
            <strong>تحلیل هوش فضایی و شعاع دسترسی</strong>
        </div>
        <div class="legend-items">
            <div class="legend-item"><span class="legend-color school-walk"></span> شعاع پیاده‌روی مدارس (۸۰۰ متر)</div>
            <div class="legend-item"><span class="legend-color health-ring"></span> حوزه پوشش خانه بهداشت (بهورزی)</div>
            <div class="legend-item"><span class="legend-color desert-alert"></span> نقطه کور دسترسی (Service Desert)</div>
        </div>
    </div>
"""

html = html[:idx_end] + catchment_legend_markup + html[idx_end:]
print("4. Injected catchmentLegend in mapScene!")

# -------------------------------------------------------------
# 5. Inject drawer mode toggle button in statsDialog head
# -------------------------------------------------------------
close_btn_marker = '<button class="close" id="closeStatsBtn" aria-label="بستن آمار">×</button>'
new_drawer_toggle = """<button id="toggleDrawerModeBtn" class="drawer-control-btn" title="تغییر وضعیت نمایش (کشویی کنار نقشه یا تمام‌صفحه)">
                    <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2">
                        <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
                        <line x1="9" y1="3" x2="9" y2="21"></line>
                    </svg>
                    <span id="drawerToggleText">تمام‌صفحه</span>
                </button>
                <button class="close" id="closeStatsBtn" aria-label="بستن آمار">×</button>"""

assert close_btn_marker in html, "close_btn_marker not found"
html = html.replace(close_btn_marker, new_drawer_toggle, 1)
print("5. Injected toggleDrawerModeBtn into statsDialog!")

# -------------------------------------------------------------
# 6. Inject Javascript logic for Kinetic Drawer and Spatial Catchment
# -------------------------------------------------------------
js_code = """
        // =========================================================================
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
        };

        // Two-Way Spatial Reticle
        window.showSpatialReticle = function(v, label) {
            const reticle = document.getElementById('spatialReticle');
            const labelEl = document.getElementById('reticleLabel');
            if (!reticle || !v) return;

            reticle.style.left = (v.x * 100) + '%';
            reticle.style.top = (v.y * 100) + '%';
            if (labelEl) labelEl.textContent = label || v.name;
            reticle.style.display = 'block';
        };

        window.hideSpatialReticle = function() {
            const reticle = document.getElementById('spatialReticle');
            if (reticle) reticle.style.display = 'none';
        };

        // =========================================================================
        // SPATIAL CATCHMENT & SERVICE DESERTS ENGINE (SENIOR SPATIAL INTELLIGENCE)
        // =========================================================================
        const catchmentSchools = [
            { id: 'soureh', name: 'سوره', title: 'دبستان رزمندگان و مطیری', x: 0.690, y: 0.755, students: 235 },
            { id: 'darband-gharbi', name: 'دربند غربی', title: 'دبستان مرزداران', x: 0.742, y: 0.872, students: 177 },
            { id: 'pol-now', name: 'پل نو', title: 'دبستان معراج', x: 0.710, y: 0.585, students: 420 },
            { id: 'sad-dastgah', name: 'صد دستگاه', title: 'مجتمع علویه و راهیان نور', x: 0.822, y: 0.888, students: 695 },
            { id: 'maslavi-1', name: 'مصلاوی ۱', title: 'دبستان مصلاوی ۱', x: 0.795, y: 0.645, students: 146 },
            { id: 'maslavi-2', name: 'مصلاوی ۲', title: 'دبستان مصلاوی ۲', x: 0.835, y: 0.620, students: 118 },
            { id: 'shahrak-sevvom', name: 'شهرک سوم', title: 'دبستان آل یاسین', x: 0.510, y: 0.440, students: 48 },
            { id: 'ariz', name: 'عریض', title: 'دبستان ۱۵ خرداد', x: 0.695, y: 0.395, students: 30 }
        ];

        const catchmentHealth = [
            { id: 'soureh', name: 'سوره', title: 'خانه بهداشت سوره ۱', x: 0.690, y: 0.755, coverage: '۴۹۸ خانوار' },
            { id: 'darband-gharbi', name: 'دربند غربی', title: 'خانه بهداشت دربند غربی', x: 0.742, y: 0.872, coverage: '۶۸۱ خانوار' },
            { id: 'pol-now', name: 'پل نو', title: 'خانه بهداشت پل نو', x: 0.710, y: 0.585, coverage: '۸۹۰ خانوار' },
            { id: 'maslavi-1', name: 'مصلاوی', title: 'خانه بهداشت مصلاوی', x: 0.795, y: 0.645, coverage: '۶۸۹ خانوار' },
            { id: 'ariz', name: 'عریض', title: 'خانه بهداشت عریض', x: 0.695, y: 0.395, coverage: '۶۵ خانوار' }
        ];

        const serviceDeserts = [
            { id: 'shahrak-sadat', name: 'شهرک سادات', x: 0.860, y: 0.565, reason: 'فاقد دبستان استاندارد و خانه بهداشت مستقل · فاصله تا پل نو: ۲.۱ ک‌م' },
            { id: 'sarhaniyeh-sofla', name: 'سرحانیه سفلی', x: 0.855, y: 0.725, reason: 'فاقد دبستان مستقل · اتکا به مدارس سرحانیه علیا و خرمشهر' },
            { id: 'darband-sharqi', name: 'دربند شرقی', x: 0.678, y: 0.852, reason: 'کمبود زیرساخت بهداشتی/آموزشی · وابستگی به دربند غربی' },
            { id: 'mofti-ariz', name: 'مفتی عریض', x: 0.810, y: 0.355, reason: 'فاقد مرکز بهداشت و دبستان مستقل · تردد به روستای عریض' }
        ];

        let catchmentLayerActive = false;

        function buildCatchmentOverlays() {
            const container = document.getElementById('catchmentLayer');
            if (!container) return;
            container.innerHTML = '';

            // 1. Health catchment rings
            catchmentHealth.forEach(h => {
                const el = document.createElement('div');
                el.className = 'catchment-item';
                el.style.left = (h.x * 100) + '%';
                el.style.top = (h.y * 100) + '%';
                el.innerHTML = `
                    <div class="catchment-ring-health" title="${h.title} (شعاع بهورزی)">
                        <span class="catchment-badge-icon">🏥 ${h.coverage}</span>
                    </div>
                `;
                el.addEventListener('click', (e) => {
                    e.stopPropagation();
                    if (typeof showSearchToast === 'function') {
                        showSearchToast(`🏥 ${h.title} · حوزه پوشش بهورزی: ${h.coverage}`);
                    }
                });
                container.appendChild(el);
            });

            // 2. School catchment rings
            catchmentSchools.forEach(s => {
                const el = document.createElement('div');
                el.className = 'catchment-item';
                el.style.left = (s.x * 100) + '%';
                el.style.top = (s.y * 100) + '%';
                el.innerHTML = `
                    <div class="catchment-ring-school-walk" title="${s.title} (شعاع پیاده‌روی ۸۰۰م)">
                        <span class="catchment-badge-icon">🏫 ${s.students} دانش‌آموز</span>
                    </div>
                `;
                el.addEventListener('click', (e) => {
                    e.stopPropagation();
                    if (typeof showSearchToast === 'function') {
                        showSearchToast(`🏫 ${s.title} (${s.name}) · ظرفیت: ${s.students} دانش‌آموز`);
                    }
                });
                container.appendChild(el);
            });

            // 3. Service Desert Beacons
            serviceDeserts.forEach(d => {
                const el = document.createElement('div');
                el.className = 'service-desert-beacon';
                el.style.left = (d.x * 100) + '%';
                el.style.top = (d.y * 100) + '%';
                el.innerHTML = `
                    <div class="desert-pulse-ring"></div>
                    <div class="desert-badge">⚠️ نقطه کور</div>
                `;
                el.addEventListener('click', (e) => {
                    e.stopPropagation();
                    if (typeof showSearchToast === 'function') {
                        showSearchToast(`⚠️ روستای ${d.name} · ${d.reason}`);
                    }
                });
                container.appendChild(el);
            });
        }

        window.toggleCatchmentLayer = function() {
            catchmentLayerActive = !catchmentLayerActive;
            const container = document.getElementById('catchmentLayer');
            const legend = document.getElementById('catchmentLegend');
            const btn = document.getElementById('toggleCatchmentBtn');

            if (catchmentLayerActive) {
                buildCatchmentOverlays();
                if (container) container.style.display = 'block';
                if (legend) legend.style.display = 'block';
                if (btn) btn.classList.add('active');
                if (typeof showSearchToast === 'function') {
                    showSearchToast(`🌐 لایه هوش فضایی و نقاط کور خدمات فعال شد.`);
                }
            } else {
                if (container) container.style.display = 'none';
                if (legend) legend.style.display = 'none';
                if (btn) btn.classList.remove('active');
            }
        };

        // Attach listeners when DOM is loaded
        document.addEventListener('DOMContentLoaded', () => {
            const toggleCatchmentBtn = document.getElementById('toggleCatchmentBtn');
            if (toggleCatchmentBtn) {
                toggleCatchmentBtn.addEventListener('click', window.toggleCatchmentLayer);
            }

            const toggleDrawerBtn = document.getElementById('toggleDrawerModeBtn');
            if (toggleDrawerBtn) {
                toggleDrawerBtn.addEventListener('click', window.toggleDrawerMode);
            }

            const statsDlg = document.getElementById('statsDialog');
            if (statsDlg) {
                statsDlg.addEventListener('close', () => {
                    const mapSceneEl = document.getElementById('mapScene');
                    if (mapSceneEl) mapSceneEl.classList.remove('drawer-open');
                    window.hideSpatialReticle();
                });
            }

            updateDrawerClasses();
        });

        // Also run immediately
        setTimeout(() => {
            const tCBtn = document.getElementById('toggleCatchmentBtn');
            if (tCBtn && !tCBtn._bound) {
                tCBtn._bound = true;
                tCBtn.addEventListener('click', window.toggleCatchmentLayer);
            }
            const tDBtn = document.getElementById('toggleDrawerModeBtn');
            if (tDBtn && !tDBtn._bound) {
                tDBtn._bound = true;
                tDBtn.addEventListener('click', window.toggleDrawerMode);
            }
            const sDlg = document.getElementById('statsDialog');
            if (sDlg && !sDlg._boundClose) {
                sDlg._boundClose = true;
                sDlg.addEventListener('close', () => {
                    const mScene = document.getElementById('mapScene');
                    if (mScene) mScene.classList.remove('drawer-open');
                    window.hideSpatialReticle();
                });
            }
            updateDrawerClasses();
        }, 100);
"""

# Inject before closing script tag
idx_script_end = html.rfind("</script>")
assert idx_script_end != -1, "</script> tag not found"
html = html[:idx_script_end] + js_code + "\n    " + html[idx_script_end:]
print("6. Injected JavaScript logic!")

# -------------------------------------------------------------
# 7. Update enter(v) to trigger updateDrawerClasses()
# -------------------------------------------------------------
old_enter_marker = "const statsDlg = $('statsDialog');"
new_enter_code = """const statsDlg = $('statsDialog');
                    if (typeof updateDrawerClasses === 'function') updateDrawerClasses();"""

if old_enter_marker in html:
    html = html.replace(old_enter_marker, new_enter_code, 1)
    print("7. Connected enter(v) to updateDrawerClasses()!")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("SUCCESS: Senior Design Features 2 and 3 fully completed!")
