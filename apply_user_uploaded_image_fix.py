with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update the img and wrapper in #villageMapCanvas
old_canvas_content = """            <div class="village-map-canvas" id="villageMapCanvas">
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
            </div>"""

new_canvas_content = """            <div class="village-map-canvas" id="villageMapCanvas">
                <div class="village-img-wrapper" id="villageImgWrapper">
                    <!-- User Uploaded Map of Pol-e Now Village -->
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
                            <span class="aerial-poi-label">خانه بهداشت روستایی پل نو</span>
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
            </div>"""

assert old_canvas_content in html, "old_canvas_content not found"
html = html.replace(old_canvas_content, new_canvas_content, 1)
print("1. Replaced canvas content with village-img-wrapper and user map image!")

# 2. Update CSS for village-img-wrapper and satellite-img
old_img_css = """.village-satellite-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    pointer-events: none;
    user-select: none;
    filter: contrast(1.04) saturate(1.08);
}"""

new_img_css = """.village-img-wrapper {
    position: relative;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    max-width: 95vw;
    max-height: 86vh;
    border-radius: 14px;
    box-shadow: 0 16px 60px rgba(0, 0, 0, 0.85), 0 0 30px rgba(237, 211, 149, 0.25);
    border: 1.5px solid rgba(237, 211, 149, 0.45);
    overflow: visible;
    transition: max-width 0.25s ease, max-height 0.25s ease;
}

.village-img-wrapper.fill-mode {
    max-width: 100vw;
    max-height: 100vh;
    border-radius: 0;
    border: none;
    box-shadow: none;
}

.village-satellite-img {
    max-width: 95vw;
    max-height: 86vh;
    width: auto;
    height: auto;
    object-fit: contain;
    border-radius: 14px;
    display: block;
    user-select: none;
    pointer-events: none;
    filter: contrast(1.05) saturate(1.1);
}

.village-img-wrapper.fill-mode .village-satellite-img {
    max-width: 100vw;
    max-height: 100vh;
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 0;
}"""

assert old_img_css in html, "old_img_css not found"
html = html.replace(old_img_css, new_img_css, 1)
print("2. Updated CSS with village-img-wrapper framing and fit modes!")

# 3. Update updateVillageSatelliteView JS logic for image source
old_js_sat_src = "satImg.src = '/pol_now_map.webp';"
new_js_sat_src = "satImg.src = '/image_0.webp';\n                    satImg.onerror = () => { satImg.src = '/pol_now_map.webp'; };"
assert old_js_sat_src in html, "old_js_sat_src not found"
html = html.replace(old_js_sat_src, new_js_sat_src, 1)
print("3. Updated updateVillageSatelliteView JS to load user uploaded image /image_0.webp!")

# 4. Add fit toggle button to controls in HTML
old_controls = """            <div class="village-map-controls" id="villageMapControls">
                <button type="button" class="v-map-btn" id="vZoomIn" title="بزرگ‌نمایی نقشه (Zoom In)">＋</button>
                <button type="button" class="v-map-btn" id="vZoomOut" title="کوچک‌نمایی نقشه (Zoom Out)">－</button>
                <button type="button" class="v-map-btn" id="vResetZoom" title="بازنشانی اندازه نقشه (Reset View)">↺</button>
                <button type="button" class="v-map-btn" id="vToggleHUD" title="نمایش/پنهان‌سازی کادرهای داده">👁️</button>
            </div>"""

new_controls = """            <div class="village-map-controls" id="villageMapControls">
                <button type="button" class="v-map-btn" id="vZoomIn" title="بزرگ‌نمایی نقشه (Zoom In)">＋</button>
                <button type="button" class="v-map-btn" id="vZoomOut" title="کوچک‌نمایی نقشه (Zoom Out)">－</button>
                <button type="button" class="v-map-btn" id="vResetZoom" title="بازنشانی اندازه نقشه (Reset View)">↺</button>
                <button type="button" class="v-map-btn" id="vToggleFit" title="تغییر کادربندی (تناسب / پرکردن صفحه)">⛶</button>
                <button type="button" class="v-map-btn" id="vToggleHUD" title="نمایش/پنهان‌سازی کادرهای داده">👁️</button>
            </div>"""

assert old_controls in html, "old_controls not found"
html = html.replace(old_controls, new_controls, 1)
print("4. Added vToggleFit button to controls!")

# 5. Hook vToggleFit in setupVillageInteractions
old_js_hook = "const tHud = document.getElementById('vToggleHUD');"
new_js_hook = """const tHud = document.getElementById('vToggleHUD');
            const tFit = document.getElementById('vToggleFit');
            const imgWrapper = document.getElementById('villageImgWrapper');

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
            }"""

assert old_js_hook in html, "old_js_hook not found"
html = html.replace(old_js_hook, new_js_hook, 1)
print("5. Hooked vToggleFit in setupVillageInteractions!")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("SUCCESS: User uploaded photo for Pol-e Now applied perfectly!")
