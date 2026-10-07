with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# --------------------------------------------------------------------------
# 1. INJECT HIGH-FIDELITY CSS FOR SATELLITE MAP & FLOATING HUD
# --------------------------------------------------------------------------
satellite_css = """
/* =========================================================================
   POL-E NOW DETAILED SATELLITE MAP & HUD COMMAND DOCK (SENIOR GIS UX)
   ========================================================================= */

.in-village .village {
    opacity: 1 !important;
    visibility: visible !important;
    background: #0b1a18 !important;
    z-index: 10 !important;
}

/* Remove dark overlay when in village so satellite map is crystal clear */
.in-village .village:after {
    opacity: 0.15 !important;
    pointer-events: none !important;
}

.village-map-viewport {
    position: absolute;
    inset: 0;
    overflow: hidden;
    background: #091716;
    cursor: grab;
    user-select: none;
    z-index: 1;
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

.village-satellite-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    pointer-events: none;
    user-select: none;
    filter: contrast(1.04) saturate(1.08);
}

.village-map-badge {
    position: absolute;
    bottom: 18px;
    right: 24px;
    background: rgba(11, 26, 24, 0.85);
    border: 1px solid rgba(237, 211, 149, 0.35);
    backdrop-filter: blur(12px);
    border-radius: 20px;
    padding: 6px 14px;
    font-size: 11px;
    font-weight: 800;
    color: #e2e8f0;
    display: inline-flex;
    align-items: center;
    gap: 8px;
    z-index: 15;
    pointer-events: none;
}

.village-map-badge .badge-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: #10b981;
    box-shadow: 0 0 8px #10b981;
}

/* Aerial Interactive POIs */
.village-aerial-overlay {
    position: absolute;
    inset: 0;
    pointer-events: none;
}

.aerial-poi {
    position: absolute;
    pointer-events: auto;
    transform: translate(-50%, -50%);
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(11, 26, 24, 0.92);
    border: 1.5px solid #edd395;
    border-radius: 30px;
    padding: 6px 14px 6px 10px;
    cursor: pointer;
    box-shadow: 0 8px 24px rgba(0,0,0,0.7), 0 0 16px rgba(237, 211, 149, 0.35);
    transition: all 0.22s cubic-bezier(0.2, 0.8, 0.2, 1);
    z-index: 20;
    backdrop-filter: blur(8px);
}

.aerial-poi:hover {
    transform: translate(-50%, -50%) scale(1.1);
    background: rgba(20, 48, 44, 0.98);
    border-color: #facc15;
    box-shadow: 0 12px 32px rgba(0,0,0,0.85), 0 0 24px rgba(250, 204, 21, 0.6);
}

.aerial-poi-dot {
    font-size: 16px;
    line-height: 1;
}

.aerial-poi-label {
    font-size: 11.5px;
    font-weight: 800;
    color: #f8fafc;
    white-space: nowrap;
    font-family: YekanBakh, sans-serif;
}

.aerial-poi-pulse {
    position: absolute;
    inset: -4px;
    border-radius: 34px;
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
    top: 96px;
    left: 20px;
    z-index: 25;
    display: flex;
    flex-direction: column;
    gap: 8px;
    pointer-events: auto;
}

.v-map-btn {
    width: 42px;
    height: 42px;
    border-radius: 12px;
    background: rgba(11, 26, 24, 0.88);
    backdrop-filter: blur(12px);
    border: 1.2px solid rgba(237, 211, 149, 0.45);
    color: #edd395;
    font-size: 18px;
    font-weight: 800;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: all 0.2s ease;
    box-shadow: 0 6px 18px rgba(0,0,0,0.5);
}

.v-map-btn:hover {
    background: #edd395;
    color: #0b1a18;
    transform: translateY(-2px);
    box-shadow: 0 8px 22px rgba(237, 211, 149, 0.5);
}

.v-map-btn.active {
    background: #c6a15b;
    color: #0b1a18;
}

/* Top Floating HUD */
.village-top-hud {
    position: absolute;
    top: 16px;
    left: 20px;
    right: 20px;
    z-index: 25;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
    pointer-events: none;
}

.v-hud-start, .v-hud-center, .v-hud-end {
    pointer-events: auto;
}

.v-hud-back-btn {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: linear-gradient(135deg, #c6a15b 0%, #9e7836 100%);
    color: #0b1a18;
    font-family: YekanBakh, sans-serif;
    font-weight: 800;
    font-size: 13px;
    padding: 9px 20px;
    border: 1px solid #edd395;
    border-radius: 28px;
    cursor: pointer;
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.5);
    transition: all 0.2s ease;
}

.v-hud-back-btn:hover {
    background: linear-gradient(135deg, #edd395 0%, #c6a15b 100%);
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(198, 161, 91, 0.65);
}

.v-hud-center {
    text-align: center;
    background: rgba(11, 26, 24, 0.88);
    backdrop-filter: blur(16px);
    padding: 8px 24px 10px;
    border-radius: 20px;
    border: 1px solid rgba(237, 211, 149, 0.35);
    box-shadow: 0 10px 30px rgba(0,0,0,0.55);
}

.v-hud-badge {
    display: inline-block;
    font-size: 11px;
    font-weight: 800;
    color: #edd395;
    margin-bottom: 2px;
}

.v-hud-title {
    margin: 0;
    font-size: clamp(22px, 2.5vw, 30px);
    font-weight: 900;
    color: #ffffff;
    text-shadow: 0 2px 10px rgba(0,0,0,0.8);
    line-height: 1.2;
}

.v-hud-sub {
    margin: 0;
    font-size: 11.5px;
    color: #cbd5e1;
}

.v-hud-chips {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
}

.v-chip {
    background: rgba(11, 26, 24, 0.88);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(237, 211, 149, 0.35);
    border-radius: 20px;
    padding: 6px 14px;
    font-size: 12px;
    font-weight: 800;
    color: #f8fafc;
    box-shadow: 0 4px 12px rgba(0,0,0,0.4);
}

/* Etude Notice for other villages */
.village-etude-notice {
    position: absolute;
    top: 96px;
    right: 20px;
    z-index: 25;
    background: rgba(11, 26, 24, 0.92);
    backdrop-filter: blur(16px);
    border: 1px solid rgba(237, 211, 149, 0.45);
    border-radius: 14px;
    padding: 10px 16px;
    font-size: 12px;
    color: #e2e8f0;
    display: flex;
    align-items: center;
    gap: 12px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.6);
}

.etude-switch-btn {
    background: #edd395;
    color: #0b1a18;
    border: none;
    border-radius: 8px;
    padding: 4px 10px;
    font-size: 11.5px;
    font-weight: 800;
    font-family: YekanBakh, sans-serif;
    cursor: pointer;
    transition: transform 0.2s ease;
}

.etude-switch-btn:hover {
    transform: scale(1.05);
}

/* Bottom Floating Command HUD Dock */
.village-hud-dock {
    position: absolute;
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%);
    width: min(1040px, 94vw);
    z-index: 25;
    pointer-events: auto;
    transition: transform 0.4s cubic-bezier(0.2, 0.8, 0.2, 1), opacity 0.35s ease;
}

.village-hud-dock.dock-hidden {
    transform: translateX(-50%) translateY(130%);
    opacity: 0;
    pointer-events: none;
}

.dock-inner {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 18px;
}

@media (max-width: 768px) {
    .dock-inner {
        grid-template-columns: 1fr;
        gap: 10px;
    }
    .village-top-hud {
        flex-direction: column;
        align-items: stretch;
        gap: 8px;
    }
}

.hud-dock-card {
    position: relative;
    text-align: right;
    border-radius: 20px;
    background: linear-gradient(135deg, rgba(16, 38, 35, 0.94) 0%, rgba(9, 23, 21, 0.97) 100%) !important;
    backdrop-filter: blur(20px);
    border: 1.5px solid rgba(237, 211, 149, 0.4) !important;
    padding: 18px 22px !important;
    cursor: pointer;
    color: #f8fafc !important;
    box-shadow: 0 16px 40px rgba(0,0,0,0.7), inset 0 1px 1px rgba(255,255,255,0.12) !important;
    transition: all 0.25s cubic-bezier(0.2, 0.8, 0.2, 1) !important;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    gap: 10px;
    font-family: YekanBakh, sans-serif !important;
    min-height: auto !important;
    opacity: 1 !important;
    transform: none !important;
}

.hud-dock-card:hover {
    transform: translateY(-4px) !important;
    border-color: #edd395 !important;
    box-shadow: 0 20px 48px rgba(0,0,0,0.85), 0 0 24px rgba(237, 211, 149, 0.35) !important;
}

.card-top-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
}

.card-num-badge {
    font-family: YekanBakh, sans-serif;
    font-size: 13px;
    font-weight: 900;
    color: #edd395;
    background: rgba(237, 211, 149, 0.14);
    border: 1px solid rgba(237, 211, 149, 0.35);
    border-radius: 8px;
    padding: 2px 8px;
}

.card-headings {
    flex: 1;
}

.card-category {
    font-size: 11px;
    font-weight: 700;
    color: #edd395;
    letter-spacing: 0.5px;
    display: block;
}

.card-main-title {
    font-size: 17.5px;
    font-weight: 800;
    color: #ffffff !important;
    margin: 0 !important;
    line-height: 1.25;
}

.card-icon-bubble {
    width: 38px;
    height: 38px;
    border-radius: 10px;
    background: rgba(237, 211, 149, 0.12);
    display: flex;
    align-items: center;
    justify-content: center;
    color: #edd395;
    flex-shrink: 0;
}

.card-icon-bubble svg {
    width: 22px;
    height: 22px;
}

.card-lead {
    font-size: 12.5px;
    color: #cbd5e1;
    margin: 0;
    line-height: 1.45;
}

.card-stats-preview-chips {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
}

.m-chip {
    font-size: 11px;
    font-weight: 700;
    background: rgba(255, 255, 255, 0.08);
    border: 1px solid rgba(255, 255, 255, 0.14);
    border-radius: 6px;
    padding: 3px 9px;
    color: #f1f5f9;
}

.card-footer-action {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding-top: 8px;
    border-top: 1px solid rgba(255, 255, 255, 0.08);
    font-size: 12px;
    font-weight: 800;
    color: #edd395;
}

.card-arrow-icon {
    font-size: 14px;
    transition: transform 0.2s ease;
}

.hud-dock-card:hover .card-arrow-icon {
    transform: translateX(-4px);
}
"""

idx_style = html.rfind("</style>")
assert idx_style != -1, "</style> not found"
html = html[:idx_style] + satellite_css + "\n" + html[idx_style:]
print("1. Injected Satellite & HUD CSS!")

# --------------------------------------------------------------------------
# 2. INJECT JS ENGINE & UPDATE enter(v) AND back()
# --------------------------------------------------------------------------

village_engine_js = """
        // =========================================================================
        // SATELLITE VILLAGE MAP INTERACTION & HUD ENGINE (SENIOR GIS UX)
        // =========================================================================
        let vZoom = 1.0;
        let vPanX = 0;
        let vPanY = 0;
        let vIsDragging = false;
        let vStartX = 0;
        let vStartY = 0;
        let vHudVisible = true;

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
            const etudeNotice = document.getElementById('villageEtudeNotice');

            resetVillageMapView();

            if (v.id === 'pol-now') {
                if (satImg) {
                    satImg.src = '/pol_now_map.webp';
                    satImg.alt = 'نقشه هوایی ماهواره‌ای تفصیلی روستای پل نو';
                }
                if (aerialOverlay) aerialOverlay.style.display = 'block';
                if (kicker) kicker.textContent = '🛰️ نقشه هوایی ماهواره‌ای تفصیلی · اتود میدانی';
                if (vName) vName.textContent = 'پل نو';
                if (vSub) vSub.textContent = 'محور مواصلاتی شلمچه · حومه غربی خرمشهر';
                if (chipPop) chipPop.textContent = '👥 ۳,۸۵۰ نفر';
                if (chipFam) chipFam.textContent = '🏡 ۹۵۰ خانوار';
                if (chipSchool) chipSchool.textContent = '🏫 دبستان معراج (۴۲۰ دانش‌آموز)';
                if (statsDesc) statsDesc.textContent = 'جمعیت، هرم تحصیلی و ۲۹ پرونده مستند';
                if (statsPreview) {
                    statsPreview.innerHTML = `
                        <span class="m-chip">👥 جمعیت: ۳,۸۵۰</span>
                        <span class="m-chip">🎒 دانش‌آموز: ۴۲۰</span>
                        <span class="m-chip">📋 پرونده‌ها: ۲۹</span>
                    `;
                }
                if (servDesc) servDesc.textContent = 'خانه بهداشت پل نو، دبستان معراج و طرح‌های توانمندسازی';
                if (servPreview) {
                    servPreview.innerHTML = `
                        <span class="m-chip">🏥 خانه بهداشت فعال</span>
                        <span class="m-chip">💧 شبکه آب و آسفالت</span>
                        <span class="m-chip">🤝 بسته‌های حمایتی</span>
                    `;
                }
                if (etudeNotice) etudeNotice.style.display = 'none';
            } else {
                if (aerialOverlay) aerialOverlay.style.display = 'none';
                if (kicker) kicker.textContent = 'شناسنامه و آمار تفصیلی روستا';
                if (vName) vName.textContent = v.name;
                if (vSub) vSub.textContent = 'بخش مرکزی شهرستان خرمشهر · کریدور شلمچه';
                
                const popVal = v.data?.pop ? `👥 ${v.data.pop} نفر` : '👥 —';
                const famVal = v.data?.fam ? `🏡 ${v.data.fam} خانوار` : '🏡 —';
                if (chipPop) chipPop.textContent = popVal;
                if (chipFam) chipFam.textContent = famVal;
                if (chipSchool) chipSchool.textContent = '🏫 پرونده آموزشی و مدارس';

                if (statsDesc) statsDesc.textContent = `جمعیت و شاخص‌های آماری ${v.name}`;
                if (statsPreview) {
                    statsPreview.innerHTML = `
                        <span class="m-chip">${popVal}</span>
                        <span class="m-chip">${famVal}</span>
                        <span class="m-chip">📊 پرونده آماری</span>
                    `;
                }
                if (servDesc) servDesc.textContent = `خدمات، دسترسی‌ها و زیرساخت‌های ${v.name}`;
                if (servPreview) {
                    servPreview.innerHTML = `
                        <span class="m-chip">🏥 وضعیت بهداشت</span>
                        <span class="m-chip">💧 زیرساخت و انشعابات</span>
                        <span class="m-chip">🤝 پروژه‌ها</span>
                    `;
                }
                if (etudeNotice) etudeNotice.style.display = 'flex';
            }
        }

        function setupVillageInteractions() {
            const viewport = document.getElementById('villageMapViewport');
            const zIn = document.getElementById('vZoomIn');
            const zOut = document.getElementById('vZoomOut');
            const zReset = document.getElementById('vResetZoom');
            const tHud = document.getElementById('vToggleHUD');
            const hudDock = document.getElementById('villageHudDock');
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
            if (tHud && hudDock && !tHud._bound) {
                tHud._bound = true;
                tHud.onclick = () => {
                    vHudVisible = !vHudVisible;
                    hudDock.classList.toggle('dock-hidden', !vHudVisible);
                    tHud.classList.toggle('active', !vHudVisible);
                    if (typeof showSearchToast === 'function') {
                        showSearchToast(vHudVisible ? 'نمایش کادرهای آمار و خدمات' : 'پنهان‌سازی کادرها · نمای ۱۰۰٪ نقشه ماهواره‌ای');
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
                    if (e.target.closest('button') || e.target.closest('.aerial-poi') || e.target.closest('.village-hud-dock')) return;
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
                        if (e.target.closest('button') || e.target.closest('.aerial-poi') || e.target.closest('.village-hud-dock')) return;
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

            const switchBtn = document.getElementById('switchToPolNowBtn');
            if (switchBtn && !switchBtn._bound) {
                switchBtn._bound = true;
                switchBtn.onclick = () => {
                    const polNowObj = villages.find(x => x.id === 'pol-now');
                    if (polNowObj && typeof enter === 'function') {
                        enter(polNowObj);
                    }
                };
            }
        }

        document.addEventListener('DOMContentLoaded', setupVillageInteractions);
        setTimeout(setupVillageInteractions, 150);
"""

# Now insert village_engine_js right before closing script tag
idx_script_end = html.rfind("</script>")
assert idx_script_end != -1, "</script> not found"
html = html[:idx_script_end] + village_engine_js + "\n    " + html[idx_script_end:]
print("2. Injected Village Satellite JS Engine!")

# --------------------------------------------------------------------------
# 3. HOOK updateVillageSatelliteView INTO enter(v)
# --------------------------------------------------------------------------
idx_timer_enter = html.find("timer = setTimeout(() => {")
assert idx_timer_enter != -1, "timer in enter(v) not found"
idx_hook = html.find("// User is now on the Village Hub with choices", idx_timer_enter)
assert idx_hook != -1, "hook comment in enter(v) not found"

hook_replacement = """// Update Village Satellite Map Viewport and HUD Dock
                    updateVillageSatelliteView(v);
                    // User is now on the Village Hub with choices: [01 آمار] and [02 خدمات]"""

html = html.replace("// User is now on the Village Hub with choices: [01 آمار] and [02 خدمات]", hook_replacement, 1)
print("3. Hooked updateVillageSatelliteView into enter(v)!")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("SUCCESS: Stage 2 complete.")
