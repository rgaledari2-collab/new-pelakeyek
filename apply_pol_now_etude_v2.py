import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# --------------------------------------------------------------------------
# 1. REMOVE ITEM 2 (SPATIAL CATCHMENT & SERVICE DESERTS) AS REQUESTED
# --------------------------------------------------------------------------

# Remove catchment markup
c_legend_start = "<!-- Spatial Catchment Legend (Senior UX) -->"
if c_legend_start in html:
    idx_start = html.find(c_legend_start)
    idx_end = html.find("</div>\n    </div>", idx_start)
    if idx_end != -1:
        idx_end += len("</div>\n    </div>")
        html = html[:idx_start] + html[idx_end:]
        print("1. Catchment Legend HTML removed successfully!")
    else:
        # alternative end
        idx_end = html.find("</div>", html.find('id="catchmentLegend"', idx_start))
        idx_end = html.find("</div>", idx_end + 6) + 6
        html = html[:idx_start] + html[idx_end:]
        print("1. Catchment Legend HTML removed (fallback)!")

# Remove catchment JS block
c_js_start = "// SPATIAL CATCHMENT & SERVICE DESERTS ENGINE"
if c_js_start in html:
    idx_js1 = html.find(c_js_start)
    # go back to comment banner
    idx_banner = html.rfind("// =====================", 0, idx_js1)
    if idx_banner != -1:
        idx_js1 = idx_banner
    
    idx_js2 = html.find("// Explicit binding for Village Hub choice cards", idx_js1)
    if idx_js2 != -1:
        # Keep dialog close listeners and remove catchment
        clean_cleanup_code = """// Clean close handlers for modals
        document.addEventListener('DOMContentLoaded', () => {
            const statsDlg = document.getElementById('statsDialog');
            if (statsDlg) {
                statsDlg.addEventListener('close', () => {
                    const mapSceneEl = document.getElementById('mapScene');
                    if (mapSceneEl) mapSceneEl.classList.remove('drawer-open');
                    if (typeof window.hideSpatialReticle === 'function') window.hideSpatialReticle();
                });
            }
        });
        
        """
        html = html[:idx_js1] + clean_cleanup_code + html[idx_js2:]
        print("2. Catchment JS engine removed successfully!")

# --------------------------------------------------------------------------
# 2. UPDATE #village MARKUP WITH SATELLITE MAP VIEWPORT & FLOATING HUD DOCK
# --------------------------------------------------------------------------
old_village_marker = '<section class="village" id="village" inert aria-label="روستای سوره">'
idx_v_start = html.find(old_village_marker)
assert idx_v_start != -1, "Old village section start not found"
idx_v_end = html.find("</section>", idx_v_start)
assert idx_v_end != -1, "Old village section end not found"
idx_v_end += len("</section>")

new_village_section = """<section class="village" id="village" inert aria-label="نمای تفصیلی و نقشه ماهواره‌ای روستا">
        <!-- Village High-Resolution Satellite Map Viewport -->
        <div class="village-map-viewport" id="villageMapViewport">
            <div class="village-map-canvas" id="villageMapCanvas">
                <!-- High-res Satellite Image (Pol-e Now by default) -->
                <img id="villageSatelliteImg" src="/pol_now_map.webp" onerror="this.onerror=null;this.src='/pol_now_map.jpg';" alt="نقشه ماهواره‌ای روستای پل نو" class="village-satellite-img" />
                
                <!-- Interactive Aerial POIs for Pol-e Now -->
                <div class="village-aerial-overlay" id="villageAerialOverlay">
                    <div class="aerial-poi poi-school" style="top: 42%; left: 47%;" data-poi="school" title="دبستان معراج پل نو (۴۲۰ دانش‌آموز)">
                        <span class="aerial-poi-dot">🏫</span>
                        <span class="aerial-poi-label">دبستان معراج (۴۲۰ دانش‌آموز)</span>
                        <span class="aerial-poi-pulse"></span>
                    </div>
                    <div class="aerial-poi poi-health" style="top: 56%; left: 39%;" data-poi="health" title="خانه بهداشت و مرکز سلامت پل نو">
                        <span class="aerial-poi-dot">🏥</span>
                        <span class="aerial-poi-label">خانه بهداشت روستایی پل نو</span>
                        <span class="aerial-poi-pulse"></span>
                    </div>
                    <div class="aerial-poi poi-road" style="bottom: 12%; left: 28%;" data-poi="road" title="محور مواصلاتی شلمچه - خرمشهر">
                        <span class="aerial-poi-dot">🛣️</span>
                        <span class="aerial-poi-label">محور مواصلاتی شلمچه</span>
                        <span class="aerial-poi-pulse"></span>
                    </div>
                    <div class="aerial-poi poi-canal" style="top: 15%; right: 20%;" data-poi="canal" title="کانال آبرسانی و اراضی نخلستان">
                        <span class="aerial-poi-dot">🌊</span>
                        <span class="aerial-poi-label">کانال آبرسانی حاشیه روستا</span>
                        <span class="aerial-poi-pulse"></span>
                    </div>
                    <div class="aerial-poi poi-mosque" style="top: 48%; left: 56%;" data-poi="mosque" title="مسجد و کانون فرهنگی روستا">
                        <span class="aerial-poi-dot">🕌</span>
                        <span class="aerial-poi-label">مسجد جامع روستا</span>
                        <span class="aerial-poi-pulse"></span>
                    </div>
                </div>
            </div>

            <!-- Satellite Map Zoom & View Controls -->
            <div class="village-map-controls" id="villageMapControls">
                <button type="button" class="v-map-btn" id="vZoomIn" title="بزرگ‌نمایی نقشه (Zoom In)">＋</button>
                <button type="button" class="v-map-btn" id="vZoomOut" title="کوچک‌نمایی نقشه (Zoom Out)">－</button>
                <button type="button" class="v-map-btn" id="vResetZoom" title="بازنشانی اندازه نقشه (Reset View)">↺</button>
                <button type="button" class="v-map-btn" id="vToggleHUD" title="نمایش/پنهان‌سازی کادرهای داده">👁️</button>
            </div>

            <!-- Village Compass / Attribution Badge -->
            <div class="village-map-badge" id="villageMapBadge">
                <span class="badge-dot"></span>
                <span>پایش هوایی شلمچه · مقیاس ۱:۲۵۰۰</span>
            </div>
        </div>

        <!-- Top Floating HUD Bar -->
        <div class="village-top-hud" id="villageTopHud">
            <div class="v-hud-start">
                <button type="button" class="v-hud-back-btn" id="villageBackBtn">
                    <span class="back-arrow">←</span>
                    <span>بازگشت به نقشه عمومی منطقه</span>
                </button>
            </div>
            <div class="v-hud-center">
                <span class="v-hud-badge" id="villageKicker">🛰️ نقشه هوایی ماهواره‌ای تفصیلی · اتود میدانی</span>
                <h1 class="v-hud-title" id="villageName">پل نو</h1>
                <p class="v-hud-sub" id="villageSubheading">محور مواصلاتی شلمچه · حومه غربی خرمشهر</p>
            </div>
            <div class="v-hud-end">
                <div class="v-hud-chips" id="villageQuickChips">
                    <span class="v-chip" id="vChipPop">👥 ۳,۸۵۰ نفر</span>
                    <span class="v-chip" id="vChipFam">🏡 ۹۵۰ خانوار</span>
                    <span class="v-chip" id="vChipSchool">🏫 دبستان معراج</span>
                </div>
            </div>
        </div>

        <!-- Notice for other villages if they dont have aerial imagery yet -->
        <div class="village-etude-notice" id="villageEtudeNotice" style="display:none;">
            <span>ℹ️ نقشه هوایی تفصیلی هم‌اکنون برای روستای <strong>پل نو</strong> بارگذاری شده است.</span>
            <button type="button" id="switchToPolNowBtn" class="etude-switch-btn">مشاهده نقشه تفصیلی پل نو ↗</button>
        </div>

        <!-- Bottom Command HUD Dock: The Two Incorporated Cards for Stats & Services -->
        <div class="village-hud-dock" id="villageHudDock">
            <div class="dock-inner">
                <!-- Card 1: آمار (Stats) -->
                <button type="button" class="choice hud-dock-card hud-card-stats" id="statsButton" aria-haspopup="dialog">
                    <div class="card-glow"></div>
                    <div class="card-top-row">
                        <div class="card-num-badge">۰۱</div>
                        <div class="card-headings">
                            <span class="card-category">کارپوشه تخصصی</span>
                            <h2 class="card-main-title">آمار و شناسنامه جمعیتی</h2>
                        </div>
                        <div class="card-icon-bubble">
                            <svg viewBox="0 0 32 32" fill="none" stroke="currentColor" aria-hidden="true">
                                <path d="M5 26V17h5v9m4 0V6h5v20m4 0V12h5v14M3 27h27" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
                            </svg>
                        </div>
                    </div>
                    <p class="card-lead" id="statsChoiceDesc">جمعیت، هرم تحصیلی، دانش‌آموزان و پرونده‌های نیازمندان</p>
                    <div class="card-stats-preview-chips" id="statsMetricsPreview">
                        <span class="m-chip">👥 جمعیت: ۳,۸۵۰</span>
                        <span class="m-chip">🎒 دانش‌آموز: ۴۲۰</span>
                        <span class="m-chip">📋 پرونده‌ها: ۲۹</span>
                    </div>
                    <div class="card-footer-action">
                        <span>ورود به کارپوشه جامع آمار</span>
                        <span class="card-arrow-icon">←</span>
                    </div>
                </button>

                <!-- Card 2: خدمات (Services) -->
                <button type="button" class="choice hud-dock-card hud-card-services" id="servicesButton" aria-haspopup="dialog">
                    <div class="card-glow"></div>
                    <div class="card-top-row">
                        <div class="card-num-badge">۰۲</div>
                        <div class="card-headings">
                            <span class="card-category">کارپوشه تخصصی</span>
                            <h2 class="card-main-title">خدمات، دسترسی‌ها و پروژه‌ها</h2>
                        </div>
                        <div class="card-icon-bubble">
                            <svg viewBox="0 0 32 32" fill="none" stroke="currentColor" aria-hidden="true">
                                <path d="M12 5h8v7h7v8h-7v7h-8v-7H5v-8h7z" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
                            </svg>
                        </div>
                    </div>
                    <p class="card-lead" id="servicesChoiceDesc">خانه بهداشت، دبستان معراج، شبکه آب و طرح‌های توانمندسازی</p>
                    <div class="card-stats-preview-chips" id="servicesMetricsPreview">
                        <span class="m-chip">🏥 خانه بهداشت فعال</span>
                        <span class="m-chip">💧 شبکه آب و آسفالت</span>
                        <span class="m-chip">🤝 بسته‌های حمایتی</span>
                    </div>
                    <div class="card-footer-action">
                        <span>ورود به کارپوشه جامع خدمات</span>
                        <span class="card-arrow-icon">←</span>
                    </div>
                </button>
            </div>
        </div>
    </section>"""

html = html[:idx_v_start] + new_village_section + html[idx_v_end:]
print("3. Replaced #village with Satellite Map Viewport and HUD Dock!")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("SUCCESS: Stage 1 complete.")
