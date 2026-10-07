with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# -------------------------------------------------------------
# 1. Inject CSS
# -------------------------------------------------------------
css_code = """
        /* ==================== KINETIC SPLIT-PANE DRAWER ARCHITECTURE (SENIOR UX) ==================== */
        #statsDialog.split-drawer-mode {
            position: fixed !important;
            top: 0 !important;
            right: 0 !important;
            left: auto !important;
            bottom: 0 !important;
            width: min(740px, 49vw) !important;
            height: 100vh !important;
            max-height: 100vh !important;
            margin: 0 !important;
            border-radius: 0 !important;
            border-top: none !important;
            border-bottom: none !important;
            border-right: none !important;
            border-left: 1.5px solid rgba(198, 161, 91, 0.45) !important;
            box-shadow: -25px 0 60px rgba(0, 0, 0, 0.6) !important;
            transform: translateX(0);
            transition: width 0.35s cubic-bezier(0.16, 1, 0.3, 1), transform 0.35s cubic-bezier(0.16, 1, 0.3, 1);
            z-index: 1000 !important;
        }

        #statsDialog.split-drawer-mode::backdrop {
            background: transparent !important;
            pointer-events: none !important;
        }

        #statsDialog.fullscreen-modal-mode {
            position: fixed !important;
            top: 50% !important;
            left: 50% !important;
            right: auto !important;
            bottom: auto !important;
            transform: translate(-50%, -50%) !important;
            width: min(95vw, 1280px) !important;
            max-height: 90vh !important;
            border-radius: 22px !important;
            box-shadow: 0 40px 100px rgba(0, 0, 0, 0.65) !important;
            border: 1px solid rgba(198, 161, 91, 0.45) !important;
            transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
            z-index: 1000 !important;
        }

        #statsDialog.fullscreen-modal-mode::backdrop {
            background: rgba(0, 0, 0, 0.6) !important;
            backdrop-filter: blur(10px) !important;
        }

        #mapScene.drawer-open {
            padding-right: min(740px, 49vw);
            transition: padding 0.35s cubic-bezier(0.16, 1, 0.3, 1);
        }

        @media (max-width: 1024px) {
            #statsDialog.split-drawer-mode {
                width: 100vw !important;
                border-left: none !important;
            }
            #mapScene.drawer-open {
                padding-right: 0 !important;
            }
        }

        .drawer-control-btn {
            background: rgba(255, 255, 255, 0.12) !important;
            color: #edd395 !important;
            border: 1px solid rgba(237, 211, 149, 0.35) !important;
            border-radius: 8px !important;
            padding: 6px 12px !important;
            font-size: 11.5px !important;
            font-weight: 700 !important;
            cursor: pointer !important;
            display: inline-flex !important;
            align-items: center !important;
            gap: 6px !important;
            transition: all 0.2s ease !important;
        }
        .drawer-control-btn:hover {
            background: rgba(237, 211, 149, 0.25) !important;
            color: #ffffff !important;
            border-color: #edd395 !important;
        }

        /* ==================== SPATIAL RETICLE (TWO-WAY CONNECTION) ==================== */
        .spatial-reticle {
            position: absolute;
            transform: translate(-50%, -50%);
            pointer-events: none;
            z-index: 90;
            transition: opacity 0.25s ease;
        }
        .reticle-ring {
            width: 70px;
            height: 70px;
            border: 2px dashed #38bdf8;
            border-radius: 50%;
            animation: reticlePulseAnim 1.6s infinite ease-out;
            box-shadow: 0 0 20px rgba(56, 189, 248, 0.5);
        }
        .reticle-core {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 14px;
            height: 14px;
            background: #f59e0b;
            border: 2px solid #ffffff;
            border-radius: 50%;
            box-shadow: 0 0 14px #f59e0b;
        }
        .reticle-label {
            position: absolute;
            top: -38px;
            left: 50%;
            transform: translateX(-50%);
            background: rgba(15, 23, 42, 0.95);
            color: #f8fafc;
            border: 1px solid rgba(56, 189, 248, 0.6);
            border-radius: 7px;
            padding: 4px 12px;
            font-size: 11.5px;
            font-weight: 800;
            white-space: nowrap;
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.6);
            pointer-events: none;
        }
        @keyframes reticlePulseAnim {
            0% { transform: scale(0.65); opacity: 1; }
            100% { transform: scale(1.65); opacity: 0; }
        }

        /* ==================== SPATIAL CATCHMENT & SERVICE DESERTS ==================== */
        .btn-catchment-toggle {
            background: rgba(30, 58, 138, 0.6) !important;
            border-color: rgba(96, 165, 250, 0.45) !important;
            color: #93c5fd !important;
            font-weight: 700 !important;
            cursor: pointer !important;
            transition: all 0.25s ease !important;
        }
        .btn-catchment-toggle:hover {
            background: rgba(37, 99, 235, 0.8) !important;
            color: #ffffff !important;
            border-color: #93c5fd !important;
        }
        .btn-catchment-toggle.active {
            background: #1e40af !important;
            border-color: #60a5fa !important;
            color: #ffffff !important;
            box-shadow: 0 0 16px rgba(59, 130, 246, 0.6) !important;
        }

        .catchment-layer {
            position: absolute;
            inset: 0;
            pointer-events: none;
            z-index: 2;
        }

        .catchment-item {
            position: absolute;
            transform: translate(-50%, -50%);
            pointer-events: auto;
            cursor: pointer;
        }

        .catchment-ring-school-walk {
            width: 130px;
            height: 130px;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(56, 189, 248, 0.22) 0%, rgba(56, 189, 248, 0.05) 75%, transparent 100%);
            border: 1.5px dashed rgba(56, 189, 248, 0.75);
            transition: all 0.25s ease;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .catchment-item:hover .catchment-ring-school-walk {
            border-color: #38bdf8;
            border-style: solid;
            background: radial-gradient(circle, rgba(56, 189, 248, 0.35) 0%, rgba(56, 189, 248, 0.1) 75%, transparent 100%);
            box-shadow: 0 0 25px rgba(56, 189, 248, 0.4);
        }

        .catchment-ring-health {
            width: 160px;
            height: 160px;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(16, 185, 129, 0.20) 0%, rgba(16, 185, 129, 0.04) 75%, transparent 100%);
            border: 1.5px dashed rgba(16, 185, 129, 0.8);
            transition: all 0.25s ease;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .catchment-item:hover .catchment-ring-health {
            border-color: #10b981;
            border-style: solid;
            background: radial-gradient(circle, rgba(16, 185, 129, 0.32) 0%, rgba(16, 185, 129, 0.08) 75%, transparent 100%);
            box-shadow: 0 0 25px rgba(16, 185, 129, 0.4);
        }

        .catchment-badge-icon {
            font-size: 13px;
            background: rgba(15, 23, 42, 0.85);
            padding: 3px 6px;
            border-radius: 12px;
            border: 1px solid rgba(255, 255, 255, 0.3);
            color: #fff;
            box-shadow: 0 2px 8px rgba(0,0,0,0.4);
        }

        .service-desert-beacon {
            position: absolute;
            transform: translate(-50%, -50%);
            pointer-events: auto;
            cursor: pointer;
            z-index: 5;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .desert-pulse-ring {
            width: 80px;
            height: 80px;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(239, 68, 68, 0.22) 0%, transparent 75%);
            border: 1.5px dashed rgba(244, 63, 94, 0.85);
            animation: desertPulseAnim 2.2s infinite ease-out;
        }
        .desert-badge {
            position: absolute;
            background: #991b1b;
            color: #fff;
            border: 1px solid #f87171;
            border-radius: 12px;
            padding: 2px 7px;
            font-size: 10px;
            font-weight: 800;
            white-space: nowrap;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.6);
        }
        @keyframes desertPulseAnim {
            0% { transform: scale(0.7); opacity: 1; }
            100% { transform: scale(1.4); opacity: 0; }
        }

        .catchment-legend {
            position: absolute;
            bottom: 24px;
            left: 24px;
            background: rgba(15, 23, 42, 0.94);
            backdrop-filter: blur(14px);
            border: 1px solid rgba(255, 255, 255, 0.18);
            border-radius: 12px;
            padding: 12px 16px;
            color: #f1f5f9;
            font-size: 11.5px;
            z-index: 20;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.55);
            max-width: 330px;
        }
        .catchment-legend .legend-header {
            display: flex;
            align-items: center;
            gap: 8px;
            font-weight: 800;
            color: #60a5fa;
            margin-bottom: 8px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
            padding-bottom: 6px;
        }
        .catchment-legend .legend-dot-live {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: #38bdf8;
            box-shadow: 0 0 8px #38bdf8;
        }
        .catchment-legend .legend-item {
            display: flex;
            align-items: center;
            gap: 8px;
            margin-bottom: 5px;
            font-size: 11px;
            color: #cbd5e1;
        }
        .catchment-legend .legend-color {
            width: 14px;
            height: 14px;
            border-radius: 3px;
            flex-shrink: 0;
        }
        .catchment-legend .school-walk { background: rgba(56, 189, 248, 0.5); border: 1px dashed #38bdf8; }
        .catchment-legend .health-ring { background: rgba(16, 185, 129, 0.5); border: 1px dashed #10b981; }
        .catchment-legend .desert-alert { background: rgba(239, 68, 68, 0.6); border: 1px dashed #f87171; }
"""

# Inject before </style>
css_marker = "</style>"
assert css_marker in html, "</style> not found"
html = html.replace(css_marker, css_code + "\n    " + css_marker, 1)
print("1. Injected CSS!")

# -------------------------------------------------------------
# 2. Inject toggle button in mapFilterBar
# -------------------------------------------------------------
filter_bar_btn = '<button class="filter-chip" data-filter="employment">💼 دارای طرح اشتغال</button>'
new_filter_btn = filter_bar_btn + """
    <span style="display:inline-block; width:1px; height:18px; background:rgba(255,255,255,0.25); margin:0 6px; vertical-align:middle;"></span>
    <button class="filter-chip btn-catchment-toggle" id="toggleCatchmentBtn" title="تحلیل فضایی شعاع دسترسی مدارس و بهداشت و شناسایی نقاط کور خدماتی">
        🌐 شعاع دسترسی و نقاط کور خدمات
    </button>"""

assert filter_bar_btn in html, "filter_bar_btn not found"
html = html.replace(filter_bar_btn, new_filter_btn, 1)
print("2. Injected toggleCatchmentBtn in mapFilterBar!")

# -------------------------------------------------------------
# 3. Inject catchmentLayer and spatialReticle in mapPlane
# -------------------------------------------------------------
img_marker = '<img class="map-image" id="mapImage"'
new_layers = """<!-- Spatial Catchment & Reticle Overlays (Senior UX) -->
    <div id="catchmentLayer" class="catchment-layer" style="display:none;"></div>
    <div id="spatialReticle" class="spatial-reticle" style="display:none;">
        <div class="reticle-ring"></div>
        <div class="reticle-core"></div>
        <div class="reticle-label" id="reticleLabel"></div>
    </div>
    <img class="map-image" id="mapImage" """

assert img_marker in html, "img_marker not found"
html = html.replace(img_marker, new_layers, 1)
print("3. Injected catchmentLayer and spatialReticle in mapPlane!")

# -------------------------------------------------------------
# 4. Inject catchmentLegend before </section>
# -------------------------------------------------------------
scene_close = '<div class="map-shade"></div></div></section>'
new_scene_close = """<div class="map-shade"></div></div>
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
</section>"""

assert scene_close in html, "scene_close not found"
html = html.replace(scene_close, new_scene_close, 1)
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

assert old_enter_marker in html, "old_enter_marker not found"
html = html.replace(old_enter_marker, new_enter_code, 1)
print("7. Connected enter(v) to updateDrawerClasses()!")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("SUCCESS: Senior Design Features 2 and 3 fully applied!")
