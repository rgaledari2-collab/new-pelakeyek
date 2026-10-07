with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# -------------------------------------------------------------
# 1. Update #village markup to support the Aerial Satellite View
# -------------------------------------------------------------
old_village_section = """<section class="village" id="village" inert aria-label="روستای سوره"><div class="village-bg"></div><div class="village-content"><div class="village-heading"><h1 id="villageName">سوره</h1></div><div class="choices"><button class="choice" id="statsButton" aria-haspopup="dialog"><span class="index">۰۱</span><svg viewBox="0 0 32 32" fill="none" stroke="currentColor" aria-hidden="true"><path d="M5 26V17h5v9m4 0V6h5v20m4 0V12h5v14M3 27h27"/></svg><h2>آمار</h2><p>جمعیت و شاخص‌های روستا</p><span class="arrow">←</span></button><button class="choice" id="servicesButton" aria-haspopup="dialog"><span class="index">۰۲</span><svg viewBox="0 0 32 32" fill="none" stroke="currentColor" aria-hidden="true"><path d="M12 5h8v7h7v8h-7v7h-8v-7H5v-8h7z"/></svg><h2>خدمات</h2><p>خدمات ارائه‌شده و دسترسی‌ها</p><span class="arrow">←</span></button></div></div></section>"""

new_village_section = """<section class="village" id="village" inert aria-label="نمای تفصیلی روستا">
    <div class="village-bg" id="villageBg"></div>
    
    <!-- Interactive Overlay for Aerial POIs on Pol-e Now Satellite Map -->
    <div class="village-aerial-overlay" id="villageAerialOverlay" style="display:none;">
        <div class="aerial-poi poi-school" style="top: 42%; left: 45%;" title="دبستان معراج پل نو (۴۲۰ دانش‌آموز)">
            <span class="aerial-poi-dot">🏫</span>
            <span class="aerial-poi-label">دبستان معراج پل نو (۴۲۰ دانش‌آموز)</span>
        </div>
        <div class="aerial-poi poi-health" style="top: 56%; left: 38%;" title="خانه بهداشت روستایی پل نو">
            <span class="aerial-poi-dot">🏥</span>
            <span class="aerial-poi-label">خانه بهداشت پل نو</span>
        </div>
        <div class="aerial-poi poi-road" style="bottom: 8%; left: 32%;" title="محور مواصلاتی شلمچه - خرمشهر">
            <span class="aerial-poi-dot">🛣️</span>
            <span class="aerial-poi-label">محور مواصلاتی شلمچه</span>
        </div>
        <div class="aerial-poi poi-canal" style="top: 14%; right: 18%;" title="کانال آبرسانی و اراضی کشاورزی">
            <span class="aerial-poi-dot">🌊</span>
            <span class="aerial-poi-label">کانال آبرسانی حاشیه روستا</span>
        </div>
    </div>

    <div class="village-content" id="villageContent">
        <!-- Floating HUD Header -->
        <div class="village-heading" id="villageHeading">
            <span class="village-aerial-kicker" id="villageAerialKicker">نقشه هوایی ماهواره‌ای روستا · اتود تفصیلی</span>
            <h1 id="villageName">پل نو</h1>
            <p id="villageSubheading">محور مواصلاتی شلمچه · حومه غربی خرمشهر</p>
        </div>

        <!-- Floating Command Dock for Stats and Services -->
        <div class="choices" id="villageChoices">
            <button class="choice" id="statsButton" aria-haspopup="dialog">
                <span class="index">۰۱</span>
                <svg viewBox="0 0 32 32" fill="none" stroke="currentColor" aria-hidden="true">
                    <path d="M5 26V17h5v9m4 0V6h5v20m4 0V12h5v14M3 27h27"/>
                </svg>
                <div class="choice-text">
                    <h2>آمار و شناسنامه</h2>
                    <p id="statsChoiceDesc">جمعیت، هرم تحصیلی و ۲۹ پرونده مستند</p>
                </div>
                <span class="arrow">←</span>
            </button>
            <button class="choice" id="servicesButton" aria-haspopup="dialog">
                <span class="index">۰۲</span>
                <svg viewBox="0 0 32 32" fill="none" stroke="currentColor" aria-hidden="true">
                    <path d="M12 5h8v7h7v8h-7v7h-8v-7H5v-8h7z"/>
                </svg>
                <div class="choice-text">
                    <h2>خدمات و دسترسی‌ها</h2>
                    <p id="servicesChoiceDesc">خانه بهداشت، دبستان و پروژه‌های توانمندسازی</p>
                </div>
                <span class="arrow">←</span>
            </button>
        </div>
    </div>
</section>"""

assert old_village_section in html, "old_village_section not found"
html = html.replace(old_village_section, new_village_section, 1)
print("1. Updated #village section markup!")

# -------------------------------------------------------------
# 2. Inject CSS for the Aerial Satellite View (Pol-e Now)
# -------------------------------------------------------------
aerial_css = """
        /* ==================== AERIAL SATELLITE MAP ETUDE (POL-E NOW) ==================== */
        .village.is-pol-now-aerial .village-bg {
            background-size: cover !important;
            background-position: center center !important;
            background-repeat: no-repeat !important;
            filter: none !important; /* CRITICAL: 100% sharp and crystal clear! */
            opacity: 1 !important;
            transform: none !important;
            transition: transform 0.6s ease;
        }

        .village.is-pol-now-aerial:after {
            background: radial-gradient(circle at center, transparent 60%, rgba(10, 25, 24, 0.45) 100%) !important;
        }

        .village.is-pol-now-aerial .village-content {
            justify-content: space-between !important;
            padding: 85px 24px 30px !important;
            pointer-events: none;
        }

        .village.is-pol-now-aerial .village-heading {
            pointer-events: auto;
            background: rgba(15, 28, 27, 0.88);
            backdrop-filter: blur(16px);
            border: 1px solid rgba(237, 211, 149, 0.45);
            border-radius: 16px;
            padding: 14px 28px;
            box-shadow: 0 14px 35px rgba(0, 0, 0, 0.6);
            max-width: 520px;
            text-align: center;
        }

        .village.is-pol-now-aerial .village-aerial-kicker {
            display: inline-block;
            font-size: 11px;
            font-weight: 800;
            color: #38bdf8;
            background: rgba(56, 189, 248, 0.15);
            border: 1px solid rgba(56, 189, 248, 0.4);
            padding: 2px 10px;
            border-radius: 12px;
            margin-bottom: 6px;
        }

        .village.is-pol-now-aerial .village-heading h1 {
            font-size: 34px !important;
            line-height: 1.2 !important;
            margin: 4px 0 6px !important;
            color: #f7f2e7 !important;
        }

        .village.is-pol-now-aerial .village-heading p {
            font-size: 12.5px !important;
            color: #edd395 !important;
            margin: 0 !important;
            opacity: 1 !important;
            transform: none !important;
        }

        .village.is-pol-now-aerial .choices {
            pointer-events: auto;
            margin-top: 0 !important;
            margin-bottom: 6px;
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 16px;
            width: min(720px, 94vw);
        }

        .village.is-pol-now-aerial .choice {
            background: rgba(18, 36, 34, 0.90) !important;
            backdrop-filter: blur(16px) !important;
            border: 1.5px solid rgba(237, 211, 149, 0.45) !important;
            box-shadow: 0 14px 35px rgba(0, 0, 0, 0.65) !important;
            border-radius: 16px !important;
            padding: 16px 20px !important;
            transition: all 0.25s ease !important;
        }

        .village.is-pol-now-aerial .choice:hover {
            background: rgba(28, 54, 51, 0.98) !important;
            border-color: #edd395 !important;
            transform: translateY(-4px) !important;
            box-shadow: 0 20px 45px rgba(0, 0, 0, 0.8) !important;
        }

        /* Aerial POI Markers */
        .village-aerial-overlay {
            position: absolute;
            inset: 0;
            z-index: 2;
            pointer-events: auto;
        }

        .aerial-poi {
            position: absolute;
            transform: translate(-50%, -50%);
            display: flex;
            align-items: center;
            gap: 6px;
            background: rgba(15, 28, 27, 0.9);
            backdrop-filter: blur(8px);
            border: 1px solid rgba(237, 211, 149, 0.6);
            border-radius: 20px;
            padding: 4px 10px;
            box-shadow: 0 6px 18px rgba(0, 0, 0, 0.55);
            cursor: pointer;
            transition: all 0.25s ease;
            animation: poiFloatAnim 3s infinite ease-in-out;
        }
        .aerial-poi:hover {
            transform: translate(-50%, -50%) scale(1.1);
            border-color: #facc15;
            background: rgba(18, 48, 44, 0.98);
        }
        .aerial-poi-dot {
            font-size: 15px;
        }
        .aerial-poi-label {
            font-size: 11px;
            font-weight: 800;
            color: #f8fafc;
            white-space: nowrap;
        }
        @keyframes poiFloatAnim {
            0%, 100% { transform: translate(-50%, -50%) translateY(0); }
            50% { transform: translate(-50%, -50%) translateY(-4px); }
        }
"""

css_marker = "</style>"
assert css_marker in html, "</style> not found"
html = html.replace(css_marker, aerial_css + "\n    " + css_marker, 1)
print("2. Injected CSS for Pol-e Now Aerial Satellite View!")

# -------------------------------------------------------------
# 3. Update enter(v) to switch to Pol-e Now map when pol-now is selected
# -------------------------------------------------------------
idx_timer = html.find("timer = setTimeout(() => {")
assert idx_timer != -1, "timer in enter(v) not found"
idx_choices_comment = html.find("// User is now on the Village Hub with choices", idx_timer)
assert idx_choices_comment != -1, "comment in enter(v) not found"

new_enter_village_setup = """// Check if selected village is Pol-e Now for the aerial satellite etude
                    const villageSection = document.getElementById('village');
                    const villageBg = document.getElementById('villageBg');
                    const aerialOverlay = document.getElementById('villageAerialOverlay');
                    const kicker = document.getElementById('villageAerialKicker');
                    const statsDesc = document.getElementById('statsChoiceDesc');
                    const servDesc = document.getElementById('servicesChoiceDesc');

                    if (v.id === 'pol-now') {
                        if (villageSection) villageSection.classList.add('is-pol-now-aerial');
                        if (villageBg) {
                            villageBg.style.backgroundImage = "url('/pol_now_map.webp'), url('/pol_now_map.jpg')";
                        }
                        if (aerialOverlay) aerialOverlay.style.display = 'block';
                        if (kicker) kicker.textContent = 'نقشه هوایی ماهواره‌ای تفصیلی · اتود میدانی';
                        if (statsDesc) statsDesc.textContent = '۳,۸۵۰ نفر جمعیت · دبستان معراج · ۲۹ پرونده مستند';
                        if (servDesc) servDesc.textContent = 'خانه بهداشت پل نو · شبکه آب و خدمات';
                    } else {
                        if (villageSection) villageSection.classList.remove('is-pol-now-aerial');
                        if (villageBg) {
                            villageBg.style.backgroundImage = 'var(--map-main-image)';
                        }
                        if (aerialOverlay) aerialOverlay.style.display = 'none';
                        if (kicker) kicker.textContent = 'شناسنامه و پایش میدانی روستا';
                        if (statsDesc) statsDesc.textContent = 'جمعیت و شاخص‌های آماری روستا';
                        if (servDesc) servDesc.textContent = 'خدمات ارائه‌شده و دسترسی‌ها';
                    }

                    // POI clicks inside Pol-e Now
                    document.querySelectorAll('.aerial-poi').forEach(poi => {
                        poi.onclick = (e) => {
                            e.stopPropagation();
                            const stBtn = document.getElementById('statsButton');
                            if (stBtn) stBtn.click();
                        };
                    });

                    // User is now on the Village Hub with choices: [01 آمار] and [02 خدمات]"""

html = html.replace("// User is now on the Village Hub with choices: [01 آمار] and [02 خدمات]", new_enter_village_setup, 1)
print("3. Updated enter(v) to dynamically load the Pol-e Now satellite map and POIs!")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("SUCCESS: Pol-e Now Aerial Satellite View implemented!")
