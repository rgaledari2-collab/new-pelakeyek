with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# --------------------------------------------------------------------------
# 1. REPLACE #village MARKUP WITH DEDICATED SPLIT CONSOLE (MAP 70% + SIDEBAR 30%)
# --------------------------------------------------------------------------
idx_v_start = html.find('<section class="village" id="village"')
assert idx_v_start != -1, "village section not found"
idx_v_end = html.find("</section>", idx_v_start) + len("</section>")

new_village_markup = """<section class="village" id="village" inert aria-label="نمای تفصیلی و نقشه ماهواره‌ای روستا">
        <!-- Top Executive Bar -->
        <div class="village-top-bar" id="villageTopBar">
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
        </div>

        <!-- Main Workspace (Zero Occlusion: Map on Left 70%, Dossier on Right 30%) -->
        <div class="village-workspace" id="villageWorkspace">
            <!-- 1. Dedicated Village Map Stage (Unobstructed 100% View) -->
            <div class="village-map-stage" id="villageMapStage">
                <div class="village-map-viewport" id="villageMapViewport">
                    <div class="village-map-canvas" id="villageMapCanvas">
                        <div class="village-img-wrapper" id="villageImgWrapper">
                            <!-- User Uploaded Map of Pol-e Now -->
                            <img id="villageSatelliteImg" src="/image_0.webp" onerror="this.onerror=null;this.src='/pol_now_map.webp';" alt="نقشه اختصاصی روستای پل نو" class="village-satellite-img" />
                            
                            <!-- Interactive POIs directly positioned on the user map -->
                            <div class="village-aerial-overlay" id="villageAerialOverlay">
                                <div class="aerial-poi poi-school" style="top: 48%; left: 50%;" data-poi="school" title="دبستان معراج پل نو (۴۲۰ دانش‌آموز)">
                                    <span class="aerial-poi-dot">🏫</span>
                                    <span class="aerial-poi-label">دبستان معراج (۴۲۰ دانش‌آموز)</span>
                                    <span class="aerial-poi-pulse"></span>
                                </div>
                                <div class="aerial-poi poi-health" style="top: 40%; left: 34%;" data-poi="health" title="خانه بهداشت و مرکز سلامت پل نو">
                                    <span class="aerial-poi-dot">🏥</span>
                                    <span class="aerial-poi-label">خانه بهداشت روستایی</span>
                                    <span class="aerial-poi-pulse"></span>
                                </div>
                                <div class="aerial-poi poi-marker" style="top: 58%; left: 84%;" data-poi="marker" title="موقعیت شاخص نشانه‌گذاری‌شده در نقشه پل نو">
                                    <span class="aerial-poi-dot">📍</span>
                                    <span class="aerial-poi-label">موقعیت شاخص روستا</span>
                                    <span class="aerial-poi-pulse"></span>
                                </div>
                                <div class="aerial-poi poi-road" style="bottom: 12%; left: 45%;" data-poi="road" title="محور مواصلاتی شلمچه - خرمشهر">
                                    <span class="aerial-poi-dot">🛣️</span>
                                    <span class="aerial-poi-label">محور مواصلاتی شلمچه</span>
                                    <span class="aerial-poi-pulse"></span>
                                </div>
                                <div class="aerial-poi poi-canal" style="top: 18%; left: 24%;" data-poi="canal" title="کانال آبرسانی و اراضی کشاورزی">
                                    <span class="aerial-poi-dot">🌊</span>
                                    <span class="aerial-poi-label">کانال آبرسانی</span>
                                    <span class="aerial-poi-pulse"></span>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Map Floating Controls -->
                    <div class="village-map-controls" id="villageMapControls">
                        <button type="button" class="v-map-btn" id="vZoomIn" title="بزرگ‌نمایی نقشه (Zoom In)">＋</button>
                        <button type="button" class="v-map-btn" id="vZoomOut" title="کوچک‌نمایی نقشه (Zoom Out)">－</button>
                        <button type="button" class="v-map-btn" id="vResetZoom" title="بازنشانی اندازه نقشه (Reset View)">↺</button>
                        <button type="button" class="v-map-btn" id="vToggleFit" title="تغییر کادربندی (تناسب کامل / پرکردن صفحه)">⛶</button>
                    </div>

                    <div class="village-map-badge" id="villageMapBadge">
                        <span class="badge-dot"></span>
                        <span>پایش هوایی شلمچه · نقشه تفصیلی پل نو</span>
                    </div>
                </div>
            </div>

            <!-- 2. Dedicated Command Dossier Sidebar (Incorporated Side-by-Side with Map) -->
            <aside class="village-sidebar" id="villageSidebar">
                <!-- Card 1: آمار (Stats) -->
                <button type="button" class="choice v-side-card card-stats" id="statsButton" aria-haspopup="dialog">
                    <div class="v-card-glow"></div>
                    <div class="v-card-header">
                        <div class="v-card-badge">۰۱</div>
                        <div class="v-card-titles">
                            <span class="v-card-kicker">کارپوشه تخصصی</span>
                            <h2 class="v-card-name">آمار و شناسنامه جمعیتی</h2>
                        </div>
                        <div class="v-card-icon">
                            <svg viewBox="0 0 32 32" fill="none" stroke="currentColor">
                                <path d="M5 26V17h5v9m4 0V6h5v20m4 0V12h5v14M3 27h27" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
                            </svg>
                        </div>
                    </div>
                    
                    <p class="v-card-desc" id="statsChoiceDesc">جمعیت، هرم تحصیلی، دانش‌آموزان و پرونده‌های نیازمندان</p>
                    
                    <div class="v-metrics-list" id="statsMetricsPreview">
                        <div class="v-metric-row">
                            <span class="m-label">👥 جمعیت کل روستا:</span>
                            <span class="m-val highlight">۳,۸۵۰ نفر (۹۵۰ خانوار)</span>
                        </div>
                        <div class="v-metric-row">
                            <span class="m-label">🎒 دبستان معراج:</span>
                            <span class="m-val">۴۲۰ دانش‌آموز</span>
                        </div>
                        <div class="v-metric-row">
                            <span class="m-label">📋 پرونده‌های مستند:</span>
                            <span class="m-val">۲۹ مورد (ایتام و نیازمند)</span>
                        </div>
                    </div>

                    <div class="v-card-cta">
                        <span>ورود به سامانه آمار و شناسنامه</span>
                        <span class="v-cta-arrow">←</span>
                    </div>
                </button>

                <!-- Card 2: خدمات (Services) -->
                <button type="button" class="choice v-side-card card-services" id="servicesButton" aria-haspopup="dialog">
                    <div class="v-card-glow"></div>
                    <div class="v-card-header">
                        <div class="v-card-badge">۰۲</div>
                        <div class="v-card-titles">
                            <span class="v-card-kicker">کارپوشه تخصصی</span>
                            <h2 class="v-card-name">خدمات، زیرساخت و پروژه‌ها</h2>
                        </div>
                        <div class="v-card-icon">
                            <svg viewBox="0 0 32 32" fill="none" stroke="currentColor">
                                <path d="M12 5h8v7h7v8h-7v7h-8v-7H5v-8h7z" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
                            </svg>
                        </div>
                    </div>

                    <p class="v-card-desc" id="servicesChoiceDesc">خانه بهداشت، دبستان معراج، شبکه آب و طرح‌های توانمندسازی</p>

                    <div class="v-metrics-list" id="servicesMetricsPreview">
                        <div class="v-metric-row">
                            <span class="m-label">🏥 مرکز سلامت:</span>
                            <span class="m-val highlight">خانه بهداشت فعال و بهورزی</span>
                        </div>
                        <div class="v-metric-row">
                            <span class="m-label">💧 زیرساخت معابر و آب:</span>
                            <span class="m-val">شبکه آب شرب و آسفالت</span>
                        </div>
                        <div class="v-metric-row">
                            <span class="m-label">🤝 اقدامات حمایتی:</span>
                            <span class="m-val">بسته‌های معیشتی و اشتغال</span>
                        </div>
                    </div>

                    <div class="v-card-cta">
                        <span>ورود به سامانه خدمات و پروژه‌ها</span>
                        <span class="v-cta-arrow">←</span>
                    </div>
                </button>
            </aside>
        </div>
    </section>"""

html = html[:idx_v_start] + new_village_markup + html[idx_v_end:]
print("1. Replaced #village markup with Split Console layout!")

# --------------------------------------------------------------------------
# 2. UPDATE CSS FOR SPLIT COMMAND CONSOLE
# --------------------------------------------------------------------------
css_marker_start = "/* =========================================================================\n   POL-E NOW DETAILED SATELLITE MAP"
idx_css_s = html.find(css_marker_start)
assert idx_css_s != -1, "css_marker_start not found"
idx_css_e = html.find("</style>", idx_css_s)
assert idx_css_e != -1, "</style> not found"

split_console_css = """/* =========================================================================
   POL-E NOW EXECUTIVE COMMAND CONSOLE (SPLIT VIEW: MAP 70% + DOSSIER 30%)
   ========================================================================= */

.in-village .village {
    opacity: 1 !important;
    visibility: visible !important;
    background: #091715 !important;
    z-index: 10 !important;
    display: flex !important;
    flex-direction: column !important;
    overflow: hidden !important;
}

.in-village .village:after {
    display: none !important;
}

/* 1. Sleek Top Bar */
.village-top-bar {
    position: relative;
    z-index: 20;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
    padding: 12px 24px;
    background: linear-gradient(180deg, rgba(9, 23, 21, 0.98) 0%, rgba(13, 33, 30, 0.92) 100%);
    border-bottom: 1px solid rgba(237, 211, 149, 0.28);
    backdrop-filter: blur(20px);
    flex-shrink: 0;
}

.v-bar-right {
    display: flex;
    align-items: center;
    gap: 18px;
}

.v-back-btn {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: linear-gradient(135deg, #c6a15b 0%, #9e7836 100%);
    color: #0b1a18;
    font-family: YekanBakh, sans-serif;
    font-weight: 800;
    font-size: 13px;
    padding: 8px 18px;
    border: 1px solid #edd395;
    border-radius: 24px;
    cursor: pointer;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.45);
    transition: all 0.2s ease;
}

.v-back-btn:hover {
    background: linear-gradient(135deg, #edd395 0%, #c6a15b 100%);
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(198, 161, 91, 0.55);
}

.v-back-arrow {
    font-size: 15px;
    font-weight: 900;
}

.v-title-wrap {
    display: flex;
    flex-direction: column;
    gap: 2px;
}

.v-badge-pill {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-size: 10.5px;
    font-weight: 800;
    color: #edd395;
    letter-spacing: 0.3px;
}

.v-live-dot {
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: #10b981;
    box-shadow: 0 0 6px #10b981;
}

.v-main-name {
    margin: 0;
    font-size: 22px;
    font-weight: 900;
    color: #ffffff;
    line-height: 1.15;
}

.v-main-sub {
    font-size: 11.5px;
    color: #94a3b8;
}

.v-bar-left {
    display: flex;
    align-items: center;
    gap: 14px;
}

.v-layout-btn {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(237, 211, 149, 0.12);
    border: 1px solid rgba(237, 211, 149, 0.4);
    color: #edd395;
    font-family: YekanBakh, sans-serif;
    font-size: 12px;
    font-weight: 800;
    padding: 7px 15px;
    border-radius: 20px;
    cursor: pointer;
    transition: all 0.2s ease;
}

.v-layout-btn:hover, .v-layout-btn.active {
    background: #edd395;
    color: #0b1a18;
}

.v-top-chips {
    display: flex;
    align-items: center;
    gap: 8px;
}

.v-top-chip {
    background: rgba(18, 45, 41, 0.85);
    border: 1px solid rgba(237, 211, 149, 0.22);
    border-radius: 16px;
    padding: 5px 12px;
    font-size: 11.5px;
    font-weight: 800;
    color: #f1f5f9;
}

/* 2. Main Workspace Layout */
.village-workspace {
    position: relative;
    flex: 1;
    display: flex;
    width: 100%;
    height: calc(100% - 64px);
    overflow: hidden;
}

/* Map Stage: 70% width, flexible, zero occlusion */
.village-map-stage {
    position: relative;
    flex: 1;
    height: 100%;
    overflow: hidden;
    background: #061110;
    transition: all 0.35s cubic-bezier(0.2, 0.8, 0.2, 1);
}

.village-map-viewport {
    position: absolute;
    inset: 0;
    overflow: hidden;
    cursor: grab;
    user-select: none;
    display: flex;
    align-items: center;
    justify-content: center;
}

.village-map-viewport:active {
    cursor: grabbing;
}

.village-map-canvas {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    transform-origin: center center;
    will-change: transform;
    transition: transform 0.08s ease-out;
}

.village-img-wrapper {
    position: relative;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    max-width: 96%;
    max-height: 94%;
    border-radius: 12px;
    box-shadow: 0 16px 50px rgba(0, 0, 0, 0.85), 0 0 24px rgba(237, 211, 149, 0.2);
    border: 1px solid rgba(237, 211, 149, 0.35);
    overflow: visible;
    transition: all 0.25s ease;
}

.village-img-wrapper.fill-mode {
    max-width: 100%;
    max-height: 100%;
    width: 100%;
    height: 100%;
    border-radius: 0;
    border: none;
    box-shadow: none;
}

.village-satellite-img {
    max-width: 100%;
    max-height: 100%;
    width: auto;
    height: auto;
    object-fit: contain;
    border-radius: 12px;
    display: block;
    user-select: none;
    pointer-events: none;
    filter: contrast(1.05) saturate(1.1);
}

.village-img-wrapper.fill-mode .village-satellite-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 0;
}

/* POIs */
.village-aerial-overlay {
    position: absolute;
    inset: 0;
    pointer-events: none;
    border-radius: 12px;
}

.aerial-poi {
    position: absolute;
    pointer-events: auto;
    transform: translate(-50%, -50%);
    display: inline-flex;
    align-items: center;
    gap: 7px;
    background: rgba(11, 26, 24, 0.94);
    border: 1.5px solid #edd395;
    border-radius: 24px;
    padding: 5px 12px 5px 9px;
    cursor: pointer;
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.7), 0 0 14px rgba(237, 211, 149, 0.35);
    transition: all 0.2s cubic-bezier(0.2, 0.8, 0.2, 1);
    z-index: 10;
    backdrop-filter: blur(8px);
}

.aerial-poi:hover {
    transform: translate(-50%, -50%) scale(1.1);
    background: rgba(20, 48, 44, 0.98);
    border-color: #facc15;
    box-shadow: 0 10px 28px rgba(0, 0, 0, 0.85), 0 0 20px rgba(250, 204, 21, 0.6);
}

.aerial-poi-dot {
    font-size: 15px;
    line-height: 1;
}

.aerial-poi-label {
    font-size: 11px;
    font-weight: 800;
    color: #f8fafc;
    white-space: nowrap;
    font-family: YekanBakh, sans-serif;
}

.aerial-poi-pulse {
    position: absolute;
    inset: -3px;
    border-radius: 28px;
    border: 1.5px solid #edd395;
    animation: aerialPulse 2.4s infinite;
    pointer-events: none;
    opacity: 0;
}

@keyframes aerialPulse {
    0% { transform: scale(0.96); opacity: 0.8; }
    50% { opacity: 0.25; }
    100% { transform: scale(1.35); opacity: 0; }
}

/* Map Controls */
.village-map-controls {
    position: absolute;
    top: 20px;
    left: 20px;
    z-index: 15;
    display: flex;
    flex-direction: column;
    gap: 8px;
    pointer-events: auto;
}

.v-map-btn {
    width: 38px;
    height: 38px;
    border-radius: 10px;
    background: rgba(11, 26, 24, 0.88);
    backdrop-filter: blur(12px);
    border: 1.2px solid rgba(237, 211, 149, 0.4);
    color: #edd395;
    font-size: 17px;
    font-weight: 800;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: all 0.2s ease;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.5);
}

.v-map-btn:hover {
    background: #edd395;
    color: #0b1a18;
    transform: translateY(-2px);
}

.v-map-btn.active {
    background: #c6a15b;
    color: #0b1a18;
}

.village-map-badge {
    position: absolute;
    bottom: 16px;
    right: 20px;
    background: rgba(11, 26, 24, 0.85);
    border: 1px solid rgba(237, 211, 149, 0.3);
    backdrop-filter: blur(12px);
    border-radius: 16px;
    padding: 5px 12px;
    font-size: 10.5px;
    font-weight: 800;
    color: #e2e8f0;
    display: inline-flex;
    align-items: center;
    gap: 7px;
    z-index: 10;
    pointer-events: none;
}

.village-map-badge .badge-dot {
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: #10b981;
    box-shadow: 0 0 6px #10b981;
}

/* 3. Dedicated Executive Dossier Sidebar (30% width) */
.village-sidebar {
    width: 360px;
    max-width: 38vw;
    height: 100%;
    background: linear-gradient(180deg, rgba(11, 26, 24, 0.96) 0%, rgba(7, 18, 17, 0.98) 100%);
    border-right: 1px solid rgba(237, 211, 149, 0.25);
    backdrop-filter: blur(24px);
    padding: 16px;
    display: flex;
    flex-direction: column;
    gap: 14px;
    overflow-y: auto;
    z-index: 15;
    transition: transform 0.35s cubic-bezier(0.2, 0.8, 0.2, 1), margin-right 0.35s cubic-bezier(0.2, 0.8, 0.2, 1);
    flex-shrink: 0;
}

.village-sidebar.collapsed {
    margin-right: -360px;
    transform: translateX(360px);
    pointer-events: none;
}

/* The Two Incorporated Cards inside Sidebar */
.v-side-card {
    position: relative;
    text-align: right;
    border-radius: 16px;
    background: linear-gradient(135deg, rgba(16, 38, 35, 0.94) 0%, rgba(10, 24, 22, 0.96) 100%) !important;
    backdrop-filter: blur(16px);
    border: 1.5px solid rgba(237, 211, 149, 0.35) !important;
    padding: 16px 18px !important;
    cursor: pointer;
    color: #f8fafc !important;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6), inset 0 1px 1px rgba(255, 255, 255, 0.1) !important;
    transition: all 0.22s cubic-bezier(0.2, 0.8, 0.2, 1) !important;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    gap: 10px;
    font-family: YekanBakh, sans-serif !important;
    min-height: auto !important;
    opacity: 1 !important;
    transform: none !important;
}

.v-side-card:hover {
    transform: translateY(-3px) !important;
    border-color: #edd395 !important;
    box-shadow: 0 16px 40px rgba(0, 0, 0, 0.75), 0 0 20px rgba(237, 211, 149, 0.3) !important;
}

.v-card-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 10px;
}

.v-card-badge {
    font-family: YekanBakh, sans-serif;
    font-size: 12px;
    font-weight: 900;
    color: #edd395;
    background: rgba(237, 211, 149, 0.12);
    border: 1px solid rgba(237, 211, 149, 0.35);
    border-radius: 6px;
    padding: 2px 7px;
}

.v-card-titles {
    flex: 1;
}

.v-card-kicker {
    font-size: 10.5px;
    font-weight: 700;
    color: #edd395;
    display: block;
}

.v-card-name {
    font-size: 16px;
    font-weight: 800;
    color: #ffffff !important;
    margin: 0 !important;
    line-height: 1.25;
}

.v-card-icon {
    width: 34px;
    height: 34px;
    border-radius: 9px;
    background: rgba(237, 211, 149, 0.12);
    display: flex;
    align-items: center;
    justify-content: center;
    color: #edd395;
    flex-shrink: 0;
}

.v-card-icon svg {
    width: 20px;
    height: 20px;
}

.v-card-desc {
    font-size: 11.5px;
    color: #cbd5e1;
    margin: 0;
    line-height: 1.45;
}

.v-metrics-list {
    display: flex;
    flex-direction: column;
    gap: 6px;
    background: rgba(0, 0, 0, 0.22);
    padding: 10px 12px;
    border-radius: 10px;
    border: 1px solid rgba(255, 255, 255, 0.05);
}

.v-metric-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 8px;
    font-size: 11.5px;
}

.v-metric-row .m-label {
    color: #94a3b8;
    font-weight: 600;
}

.v-metric-row .m-val {
    color: #f1f5f9;
    font-weight: 800;
}

.v-metric-row .m-val.highlight {
    color: #facc15;
}

.v-card-cta {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding-top: 6px;
    border-top: 1px solid rgba(255, 255, 255, 0.07);
    font-size: 11.5px;
    font-weight: 800;
    color: #edd395;
}

.v-cta-arrow {
    font-size: 14px;
    transition: transform 0.2s ease;
}

.v-side-card:hover .v-cta-arrow {
    transform: translateX(-4px);
}

@media (max-width: 900px) {
    .village-workspace {
        flex-direction: column;
    }
    .village-sidebar {
        width: 100%;
        max-width: 100%;
        height: auto;
        max-height: 240px;
        border-right: none;
        border-top: 1px solid rgba(237, 211, 149, 0.25);
    }
    .village-top-bar {
        flex-direction: column;
        align-items: stretch;
    }
}
"""

html = html[:idx_css_s] + split_console_css + html[idx_css_e:]
print("2. Replaced CSS with Split Console CSS!")

# --------------------------------------------------------------------------
# 3. UPDATE JS ENGINE FOR SPLIT CONSOLE & SIDEBAR TOGGLE
# --------------------------------------------------------------------------
idx_js_engine_s = html.find("// SATELLITE VILLAGE MAP INTERACTION & HUD ENGINE")
assert idx_js_engine_s != -1, "js_engine not found"
idx_js_engine_e = html.rfind("</script>")
assert idx_js_engine_e != -1, "</script> not found"

split_js_engine = """// SATELLITE VILLAGE MAP INTERACTION & SPLIT CONSOLE ENGINE (SENIOR GIS UX)
        // =========================================================================
        let vZoom = 1.0;
        let vPanX = 0;
        let vPanY = 0;
        let vIsDragging = false;
        let vStartX = 0;
        let vStartY = 0;
        let vSidebarCollapsed = false;

        function applyVTransform() {
            const canvas = document.getElementById('villageMapCanvas');
            if (canvas) {
                canvas.style.transform = `translate(${vPanX}px, ${vPanY}px) scale(${vZoom})`;
            }
        }

        function resetVillageMapView() {
            vZoom = 1.0;
            vPanX = 0;
            vPanY = 0;
            applyVTransform();
        }

        function updateVillageSatelliteView(v) {
            const satImg = document.getElementById('villageSatelliteImg');
            const aerialOverlay = document.getElementById('villageAerialOverlay');
            const kicker = document.getElementById('villageKicker');
            const vName = document.getElementById('villageName');
            const vSub = document.getElementById('villageSubheading');
            const chipPop = document.getElementById('vChipPop');
            const chipFam = document.getElementById('vChipFam');
            const chipSchool = document.getElementById('vChipSchool');
            const statsDesc = document.getElementById('statsChoiceDesc');
            const statsPreview = document.getElementById('statsMetricsPreview');
            const servDesc = document.getElementById('servicesChoiceDesc');
            const servPreview = document.getElementById('servicesMetricsPreview');

            resetVillageMapView();

            if (v.id === 'pol-now') {
                if (satImg) {
                    satImg.src = '/image_0.webp';
                    satImg.onerror = () => { satImg.src = '/pol_now_map.webp'; };
                    satImg.alt = 'نقشه اختصاصی تفصیلی روستای پل نو';
                }
                if (aerialOverlay) aerialOverlay.style.display = 'block';
                if (kicker) kicker.textContent = 'نقشه اختصاصی تفصیلی · اتود پایش میدانی';
                if (vName) vName.textContent = 'پل نو';
                if (vSub) vSub.textContent = 'محور مواصلاتی شلمچه - خرمشهر · حومه غربی';
                if (chipPop) chipPop.textContent = '👥 ۳,۸۵۰ نفر';
                if (chipFam) chipFam.textContent = '🏡 ۹۵۰ خانوار';
                if (chipSchool) chipSchool.textContent = '🎒 دبستان معراج (۴۲۰ دانش‌آموز)';
                
                if (statsDesc) statsDesc.textContent = 'جمعیت، هرم تحصیلی و ۲۹ پرونده مستند';
                if (statsPreview) {
                    statsPreview.innerHTML = `
                        <div class="v-metric-row">
                            <span class="m-label">👥 جمعیت کل روستا:</span>
                            <span class="m-val highlight">۳,۸۵۰ نفر (۹۵۰ خانوار)</span>
                        </div>
                        <div class="v-metric-row">
                            <span class="m-label">🎒 دبستان معراج:</span>
                            <span class="m-val">۴۲۰ دانش‌آموز</span>
                        </div>
                        <div class="v-metric-row">
                            <span class="m-label">📋 پرونده‌های مستند:</span>
                            <span class="m-val">۲۹ مورد (ایتام و نیازمند)</span>
                        </div>
                    `;
                }
                if (servDesc) servDesc.textContent = 'خانه بهداشت پل نو، دبستان معراج و طرح‌های توانمندسازی';
                if (servPreview) {
                    servPreview.innerHTML = `
                        <div class="v-metric-row">
                            <span class="m-label">🏥 مرکز سلامت:</span>
                            <span class="m-val highlight">خانه بهداشت فعال و بهورزی</span>
                        </div>
                        <div class="v-metric-row">
                            <span class="m-label">💧 زیرساخت معابر و آب:</span>
                            <span class="m-val">شبکه آب شرب و آسفالت</span>
                        </div>
                        <div class="v-metric-row">
                            <span class="m-label">🤝 اقدامات حمایتی:</span>
                            <span class="m-val">بسته‌های معیشتی و اشتغال</span>
                        </div>
                    `;
                }
            } else {
                if (satImg) {
                    satImg.src = 'var(--map-main-image)';
                }
                if (aerialOverlay) aerialOverlay.style.display = 'none';
                if (kicker) kicker.textContent = 'شناسنامه و آمار تفصیلی روستا';
                if (vName) vName.textContent = v.name;
                if (vSub) vSub.textContent = 'بخش مرکزی شهرستان خرمشهر · کریدور شلمچه';
                
                const popVal = v.data?.pop ? `👥 ${v.data.pop} نفر` : '👥 —';
                const famVal = v.data?.fam ? `🏡 ${v.data.fam} خانوار` : '🏡 —';
                if (chipPop) chipPop.textContent = popVal;
                if (chipFam) chipFam.textContent = famVal;
                if (chipSchool) chipSchool.textContent = '🎒 پرونده آموزشی و مدارس';

                if (statsDesc) statsDesc.textContent = `جمعیت و شاخص‌های آماری ${v.name}`;
                if (statsPreview) {
                    statsPreview.innerHTML = `
                        <div class="v-metric-row">
                            <span class="m-label">👥 جمعیت:</span>
                            <span class="m-val highlight">${popVal}</span>
                        </div>
                        <div class="v-metric-row">
                            <span class="m-label">🏡 خانوارها:</span>
                            <span class="m-val">${famVal}</span>
                        </div>
                        <div class="v-metric-row">
                            <span class="m-label">📊 وضعیت پرونده:</span>
                            <span class="m-val">ثبت آماری تفصیلی</span>
                        </div>
                    `;
                }
                if (servDesc) servDesc.textContent = `خدمات، دسترسی‌ها و زیرساخت‌های ${v.name}`;
                if (servPreview) {
                    servPreview.innerHTML = `
                        <div class="v-metric-row">
                            <span class="m-label">🏥 بهداشت و درمان:</span>
                            <span class="m-val">پایش میدانی</span>
                        </div>
                        <div class="v-metric-row">
                            <span class="m-label">💧 زیرساخت و انشعابات:</span>
                            <span class="m-val">پرونده دهیاری</span>
                        </div>
                        <div class="v-metric-row">
                            <span class="m-label">🤝 پروژه‌ها:</span>
                            <span class="m-val">طرح‌های توانمندسازی</span>
                        </div>
                    `;
                }
            }
        }

        function setupVillageInteractions() {
            const viewport = document.getElementById('villageMapViewport');
            const zIn = document.getElementById('vZoomIn');
            const zOut = document.getElementById('vZoomOut');
            const zReset = document.getElementById('vResetZoom');
            const tFit = document.getElementById('vToggleFit');
            const imgWrapper = document.getElementById('villageImgWrapper');
            const tSidebar = document.getElementById('vToggleSidebar');
            const sidebar = document.getElementById('villageSidebar');
            const tSidebarText = document.getElementById('vToggleSidebarText');
            const bBtn = document.getElementById('villageBackBtn');

            if (zIn && !zIn._bound) {
                zIn._bound = true;
                zIn.onclick = () => {
                    vZoom = Math.min(3.5, vZoom + 0.35);
                    applyVTransform();
                };
            }
            if (zOut && !zOut._bound) {
                zOut._bound = true;
                zOut.onclick = () => {
                    vZoom = Math.max(0.7, vZoom - 0.35);
                    applyVTransform();
                };
            }
            if (zReset && !zReset._bound) {
                zReset._bound = true;
                zReset.onclick = () => {
                    resetVillageMapView();
                };
            }
            if (tFit && imgWrapper && !tFit._bound) {
                tFit._bound = true;
                let isFill = false;
                tFit.onclick = () => {
                    isFill = !isFill;
                    imgWrapper.classList.toggle('fill-mode', isFill);
                    tFit.classList.toggle('active', isFill);
                    if (typeof showSearchToast === 'function') {
                        showSearchToast(isFill ? 'حالت پر کردن صفحه (Fill Mode)' : 'حالت تناسب کامل نقشه (Fit Mode)');
                    }
                };
            }
            if (tSidebar && sidebar && !tSidebar._bound) {
                tSidebar._bound = true;
                tSidebar.onclick = () => {
                    vSidebarCollapsed = !vSidebarCollapsed;
                    sidebar.classList.toggle('collapsed', vSidebarCollapsed);
                    tSidebar.classList.toggle('active', vSidebarCollapsed);
                    if (tSidebarText) {
                        tSidebarText.textContent = vSidebarCollapsed ? 'نمایش ستون آمار و خدمات' : 'نمای تمام‌صفحه نقشه';
                    }
                    if (typeof showSearchToast === 'function') {
                        showSearchToast(vSidebarCollapsed ? 'حالت تمام‌صفحه نقشه فعال شد' : 'ستون کادرهای آمار و خدمات بازگردانی شد');
                    }
                };
            }
            if (bBtn && !bBtn._bound) {
                bBtn._bound = true;
                bBtn.onclick = () => {
                    if (typeof back === 'function') back();
                };
            }

            if (viewport && !viewport._boundDrag) {
                viewport._boundDrag = true;
                viewport.addEventListener('mousedown', (e) => {
                    if (e.target.closest('button') || e.target.closest('.aerial-poi')) return;
                    vIsDragging = true;
                    vStartX = e.clientX - vPanX;
                    vStartY = e.clientY - vPanY;
                    viewport.style.cursor = 'grabbing';
                });
                window.addEventListener('mousemove', (e) => {
                    if (!vIsDragging) return;
                    vPanX = e.clientX - vStartX;
                    vPanY = e.clientY - vStartY;
                    applyVTransform();
                });
                window.addEventListener('mouseup', () => {
                    if (vIsDragging) {
                        vIsDragging = false;
                        if (viewport) viewport.style.cursor = 'grab';
                    }
                });

                viewport.addEventListener('wheel', (e) => {
                    e.preventDefault();
                    const delta = e.deltaY < 0 ? 0.2 : -0.2;
                    vZoom = Math.max(0.7, Math.min(3.5, vZoom + delta));
                    applyVTransform();
                }, { passive: false });

                viewport.addEventListener('touchstart', (e) => {
                    if (e.touches.length === 1) {
                        if (e.target.closest('button') || e.target.closest('.aerial-poi')) return;
                        vIsDragging = true;
                        vStartX = e.touches[0].clientX - vPanX;
                        vStartY = e.touches[0].clientY - vPanY;
                    }
                });
                viewport.addEventListener('touchmove', (e) => {
                    if (vIsDragging && e.touches.length === 1) {
                        e.preventDefault();
                        vPanX = e.touches[0].clientX - vStartX;
                        vPanY = e.touches[0].clientY - vStartY;
                        applyVTransform();
                    }
                }, { passive: false });
                viewport.addEventListener('touchend', () => {
                    vIsDragging = false;
                });
            }

            // POI markers
            document.querySelectorAll('.aerial-poi').forEach(poi => {
                if (!poi._bound) {
                    poi._bound = true;
                    poi.onclick = (e) => {
                        e.stopPropagation();
                        const pType = poi.getAttribute('data-poi');
                        if (pType === 'school') {
                            const stBtn = document.getElementById('statsButton');
                            if (stBtn) stBtn.click();
                        } else if (pType === 'health') {
                            const svBtn = document.getElementById('servicesButton');
                            if (svBtn) svBtn.click();
                        } else {
                            const lbl = poi.querySelector('.aerial-poi-label')?.textContent || '';
                            if (typeof showSearchToast === 'function') {
                                showSearchToast(`📍 ${lbl}`);
                            }
                        }
                    };
                }
            });
        }

        document.addEventListener('DOMContentLoaded', setupVillageInteractions);
        setTimeout(setupVillageInteractions, 150);
"""

html = html[:idx_js_engine_s] + split_js_engine + "\n    " + html[idx_js_engine_e:]
print("3. Replaced JS engine with Split Console engine!")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("SUCCESS: Split Command Console implemented!")
