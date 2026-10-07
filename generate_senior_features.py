with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# --------------------------------------------------------------------------
# 1. CSS INJECTION
# --------------------------------------------------------------------------
css_injection = """
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
            pointer-events: auto;
            z-index: 1;
        }

        .catchment-ring-school-walk {
            position: absolute;
            transform: translate(-50%, -50%);
            width: 140px;
            height: 140px;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(56, 189, 248, 0.22) 0%, rgba(56, 189, 248, 0.05) 75%, transparent 100%);
            border: 1.5px dashed rgba(56, 189, 248, 0.75);
            pointer-events: auto;
            cursor: pointer;
            transition: all 0.25s ease;
        }
        .catchment-ring-school-walk:hover {
            border-color: #38bdf8;
            border-style: solid;
            background: radial-gradient(circle, rgba(56, 189, 248, 0.35) 0%, rgba(56, 189, 248, 0.1) 75%, transparent 100%);
            box-shadow: 0 0 25px rgba(56, 189, 248, 0.4);
            z-index: 10;
        }

        .catchment-ring-school-transit {
            position: absolute;
            transform: translate(-50%, -50%);
            width: 250px;
            height: 250px;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(14, 165, 233, 0.08) 0%, transparent 80%);
            border: 1px dotted rgba(56, 189, 248, 0.35);
            pointer-events: none;
        }

        .catchment-ring-health {
            position: absolute;
            transform: translate(-50%, -50%);
            width: 180px;
            height: 180px;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(16, 185, 129, 0.20) 0%, rgba(16, 185, 129, 0.04) 75%, transparent 100%);
            border: 1.5px dashed rgba(16, 185, 129, 0.8);
            pointer-events: auto;
            cursor: pointer;
            transition: all 0.25s ease;
        }
        .catchment-ring-health:hover {
            border-color: #10b981;
            border-style: solid;
            background: radial-gradient(circle, rgba(16, 185, 129, 0.32) 0%, rgba(16, 185, 129, 0.08) 75%, transparent 100%);
            box-shadow: 0 0 25px rgba(16, 185, 129, 0.4);
            z-index: 10;
        }

        .service-desert-beacon {
            position: absolute;
            transform: translate(-50%, -50%);
            pointer-events: auto;
            cursor: pointer;
            z-index: 5;
        }
        .desert-pulse-ring {
            width: 90px;
            height: 90px;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(239, 68, 68, 0.18) 0%, transparent 75%);
            border: 1.5px dashed rgba(244, 63, 94, 0.8);
            animation: desertPulseAnim 2.2s infinite ease-out;
        }
        .desert-badge {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
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
            background: rgba(15, 23, 42, 0.92);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.15);
            border-radius: 12px;
            padding: 12px 16px;
            color: #f1f5f9;
            font-size: 11.5px;
            z-index: 20;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
            max-width: 320px;
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

# Find place to inject CSS
css_anchor = "</style>"
assert css_anchor in html, "style end tag not found"
html = html.replace(css_anchor, css_injection + "\n    " + css_anchor, 1)
print("1. Injected CSS for Kinetic Drawer & Spatial Catchment!")

# --------------------------------------------------------------------------
# 2. MARKUP INJECTION: Catchment Toggle in filter bar
# --------------------------------------------------------------------------
filter_bar_end = '</button></div><div class="map-blur-bg"'
catchment_btn_html = """</button>
    <span style="display:inline-block; width:1px; height:18px; background:rgba(255,255,255,0.2); margin:0 4px; vertical-align:middle;"></span>
    <button class="filter-chip btn-catchment-toggle" id="toggleCatchmentBtn" title="تحلیل فضایی شعاع دسترسی مدارس و بهداشت و شناسایی نقاط کور خدماتی">
        🌐 شعاع دسترسی و نقاط کور خدمات
    </button>
</div><div class="map-blur-bg" """

assert filter_bar_end in html, "filter_bar_end not found"
html = html.replace(filter_bar_end, catchment_btn_html, 1)
print("2. Injected toggleCatchmentBtn in mapFilterBar!")

# --------------------------------------------------------------------------
# 3. MARKUP INJECTION: Catchment Layer and Spatial Reticle in mapPlane
# --------------------------------------------------------------------------
plane_anchor = '<img class="map-image" id="mapImage"'
catchment_layer_markup = """<!-- Spatial Catchment & Reticle Overlays (Senior UX) -->
    <div id="catchmentLayer" class="catchment-layer" style="display:none;"></div>
    <div id="spatialReticle" class="spatial-reticle" style="display:none;">
        <div class="reticle-ring"></div>
        <div class="reticle-core"></div>
        <div class="reticle-label" id="reticleLabel"></div>
    </div>
    <img class="map-image" id="mapImage" """

assert plane_anchor in html, "mapImage anchor not found"
html = html.replace(plane_anchor, catchment_layer_markup, 1)
print("3. Injected catchmentLayer & spatialReticle in mapPlane!")

# --------------------------------------------------------------------------
# 4. MARKUP INJECTION: Catchment Legend inside mapScene
# --------------------------------------------------------------------------
scene_end_anchor = '</section>'
catchment_legend_markup = """    <!-- Spatial Catchment Legend (Senior UX) -->
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

assert scene_end_anchor in html, "scene_end_anchor not found"
html = html.replace(scene_end_anchor, catchment_legend_markup, 1)
print("4. Injected catchmentLegend in mapScene!")

# --------------------------------------------------------------------------
# 5. MARKUP INJECTION: Drawer Mode Toggle in statsDialog header
# --------------------------------------------------------------------------
stats_head_anchor = '<dialog id="statsDialog" aria-labelledby="statsTitle">\n        <div class="dialog-head">\n            <div>\n                <h2 id="statsTitle">📊 آمار و شناسنامه تحلیلی روستا</h2>'
if stats_head_anchor not in html:
    # search more flexibly
    idx_sd = html.find('id="statsDialog"')
    idx_close = html.find('<button class="close"', idx_sd)
    btn_drawer_toggle = """<button id="toggleDrawerModeBtn" class="drawer-control-btn" title="تغییر وضعیت نمایش (کشویی کنار نقشه یا تمام‌صفحه)">
                    <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2">
                        <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
                        <line x1="9" y1="3" x2="9" y2="21"></line>
                    </svg>
                    <span id="drawerToggleText">تمام‌صفحه</span>
                </button>
                """
    html = html[:idx_close] + btn_drawer_toggle + html[idx_close:]
else:
    # replace right at close button
    idx_sd = html.find(stats_head_anchor)
    idx_close = html.find('<button class="close"', idx_sd)
    btn_drawer_toggle = """<button id="toggleDrawerModeBtn" class="drawer-control-btn" title="تغییر وضعیت نمایش (کشویی کنار نقشه یا تمام‌صفحه)">
                    <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2">
                        <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
                        <line x1="9" y1="3" x2="9" y2="21"></line>
                    </svg>
                    <span id="drawerToggleText">تمام‌صفحه</span>
                </button>
                """
    html = html[:idx_close] + btn_drawer_toggle + html[idx_close:]

print("5. Injected toggleDrawerModeBtn into statsDialog header!")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("SUCCESS Part 1 (Markup and CSS applied)!")
