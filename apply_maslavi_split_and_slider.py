with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# =========================================================================
# STEP 1: Separate Maslavi 1 and Maslavi 2 in villages array
# =========================================================================
idx_m1 = html.find("{ id: 'maslavi-1'")
idx_m2_end = html.find("{ id: 'shahrak-sadat'", idx_m1)
assert idx_m1 != -1 and idx_m2_end != -1, "maslavi slice not found"

new_m1_m2 = """{ id: 'maslavi-1', name: 'مصلاوی ۱', cat: 'village', x: 0.795, y: 0.645, data: { pop: '۱,۱۰۰', fam: '۳۶۰', stats: [['دانش‌آموزان', 146], ['مدرسه', 'دبستان مصلاوی ۱'], ['ایتام', 1], ['کم‌برخوردار', 15], ['خانه بهداشت', 1]] } },
                { id: 'maslavi-2', name: 'مصلاوی ۲', cat: 'village', x: 0.835, y: 0.620, data: { pop: '—', fam: '—', stats: [['وضعیت', 'در انتظار ثبت آمار میدانی'], ['شناسنامه', 'خالی']] } },
                """

html = html[:idx_m1] + new_m1_m2 + html[idx_m2_end:]
print("1. Updated villages array: Maslavi 1 is authentic, Maslavi 2 is empty/pending!")

# =========================================================================
# STEP 2: Update getVillageAccordions so Maslavi 2 does not share Maslavi 1 data
# =========================================================================
old_gva_maslavi = "else if (villageId === 'maslavi' || villageId === 'maslavi-1' || villageId === 'maslavi-2') raw = maslaviStatsHtml;"
new_gva_maslavi = "else if (villageId === 'maslavi' || villageId === 'maslavi-1') raw = maslaviStatsHtml;"

if old_gva_maslavi in html:
    html = html.replace(old_gva_maslavi, new_gva_maslavi, 1)
    print("2. Updated getVillageAccordions: Maslavi 2 now shows pending empty card!")

# =========================================================================
# STEP 3: Update regionalDialog table rows for Maslavi 1 and Maslavi 2
# =========================================================================
old_reg_m12 = '<tr style="background:#f0fdf4;"><td style="padding:9px 14px;">۵</td><td style="padding:9px 14px; font-weight:800; color:#142a29;">مصلاوی ۱ و ۲</td><td style="padding:9px 14px;">حومه غربی</td><td style="padding:9px 14px; font-weight:800; color:#15803d;">۲,۰۶۳ نفر</td><td style="padding:9px 14px; font-weight:700;">۶۸۹</td><td style="padding:9px 14px;">۲ دبستان (مصلاوی ۱ و ۲ با ۲۶۴ نفر)</td><td style="padding:9px 14px; font-weight:800; color:#b45309;">۱۶ پرونده (۱ یتیم + ۱۵ مددجو)</td></tr>'

new_reg_m12 = """<tr style="background:#f0fdf4;"><td style="padding:9px 14px;">۵</td><td style="padding:9px 14px; font-weight:800; color:#142a29;">مصلاوی ۱</td><td style="padding:9px 14px;">حومه غربی</td><td style="padding:9px 14px; font-weight:800; color:#15803d;">۱,۱۰۰ نفر</td><td style="padding:9px 14px; font-weight:700;">۳۶۰</td><td style="padding:9px 14px;">دبستان مصلاوی ۱ (۱۴۶ دانش‌آموز)</td><td style="padding:9px 14px; font-weight:800; color:#b45309;">۱۶ پرونده (۱ یتیم + ۱۵ مددجو)</td></tr>
                <tr><td style="padding:9px 14px;">۶</td><td style="padding:9px 14px; font-weight:800; color:#64748b;">مصلاوی ۲</td><td style="padding:9px 14px; color:#64748b;">حومه غربی</td><td style="padding:9px 14px; color:#94a3b8;">—</td><td style="padding:9px 14px; color:#94a3b8;">—</td><td style="padding:9px 14px; color:#94a3b8;">—</td><td style="padding:9px 14px; color:#94a3b8; font-weight:600;">خالی (در انتظار ثبت آمار میدانی)</td></tr>"""

if old_reg_m12 in html:
    html = html.replace(old_reg_m12, new_reg_m12, 1)
    print("3. Updated regionalDialog table: Maslavi 1 separated from Maslavi 2!")

# =========================================================================
# STEP 4: Update Master Excel regionalList
# =========================================================================
old_excel_maslavi = "{ name: 'مصلاوی ۱ و ۲', dehestan: 'حومه غربی', status: 'ثبت جامع و مستند', pop: '۲,۰۶۳', fam: '۶۸۹', school: '۲ دبستان (۲۶۴ دانش‌آموز)', dossiers: '۱۶ پرونده (۱ یتیم + ۱۵ مددجو)' },"

new_excel_maslavi = """{ name: 'مصلاوی ۱', dehestan: 'حومه غربی', status: 'ثبت جامع و مستند', pop: '۱,۱۰۰', fam: '۳۶۰', school: 'دبستان مصلاوی ۱ (۱۴۶ نفر)', dossiers: '۱۶ پرونده (۱ یتیم + ۱۵ مددجو)' },
                    { name: 'مصلاوی ۲', dehestan: 'حومه غربی', status: 'خالی (در انتظار ثبت آمار)', pop: '—', fam: '—', school: '—', dossiers: 'خالی (در انتظار آمار)' },"""

if old_excel_maslavi in html:
    html = html.replace(old_excel_maslavi, new_excel_maslavi, 1)
    print("4. Updated Master Excel regionalList for Maslavi 1 and Maslavi 2!")

# =========================================================================
# STEP 5: Add CSS for the Village Slider Rail
# =========================================================================
slider_css = """
        /* ==================== VILLAGE HORIZONTAL SLIDER RAIL (SENIOR UX) ==================== */
        .village-slider-rail {
            position: absolute;
            bottom: 22px;
            left: 50%;
            transform: translateX(-50%);
            width: min(1200px, calc(100% - 40px));
            background: rgba(15, 23, 42, 0.90);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.16);
            border-radius: 18px;
            box-shadow: 0 16px 40px rgba(0, 0, 0, 0.65), 0 0 0 1px rgba(198, 161, 91, 0.2);
            z-index: 25;
            padding: 12px 16px;
            transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
            direction: rtl;
        }

        .village-slider-rail.is-collapsed {
            width: auto;
            min-width: 340px;
            padding: 8px 16px;
        }
        .village-slider-rail.is-collapsed .slider-track-wrapper {
            display: none !important;
        }

        .slider-rail-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 12px;
            padding-bottom: 8px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
            margin-bottom: 10px;
        }
        .village-slider-rail.is-collapsed .slider-rail-header {
            margin-bottom: 0;
            padding-bottom: 0;
            border-bottom: none;
        }

        .slider-rail-title {
            display: flex;
            align-items: center;
            gap: 8px;
            color: #f1f5f9;
            font-size: 12.5px;
            font-weight: 800;
        }
        .rail-indicator-dot {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: #eab308;
            box-shadow: 0 0 8px #eab308;
        }
        .rail-stats-pill {
            font-size: 11px;
            font-weight: 700;
            color: #94a3b8;
            background: rgba(255, 255, 255, 0.08);
            padding: 2px 8px;
            border-radius: 12px;
        }

        .slider-rail-controls {
            display: flex;
            align-items: center;
            gap: 6px;
        }
        .rail-nav-btn {
            background: rgba(255, 255, 255, 0.1);
            border: 1px solid rgba(255, 255, 255, 0.2);
            color: #f8fafc;
            width: 28px;
            height: 28px;
            border-radius: 6px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 12px;
            transition: all 0.2s ease;
        }
        .rail-nav-btn:hover {
            background: rgba(234, 179, 8, 0.3);
            border-color: #eab308;
            color: #ffffff;
        }
        .rail-toggle-btn {
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid rgba(255, 255, 255, 0.2);
            color: #edd395;
            padding: 4px 10px;
            border-radius: 6px;
            font-size: 11px;
            font-weight: 700;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 4px;
            transition: all 0.2s ease;
        }
        .rail-toggle-btn:hover {
            background: rgba(237, 211, 149, 0.25);
            color: #ffffff;
        }

        .slider-track-wrapper {
            position: relative;
            overflow: hidden;
            width: 100%;
        }
        .slider-track {
            display: flex;
            align-items: stretch;
            gap: 10px;
            overflow-x: auto;
            scroll-behavior: smooth;
            padding: 4px 2px 6px;
            scrollbar-width: thin;
            scrollbar-color: rgba(234, 179, 8, 0.3) transparent;
        }
        .slider-track::-webkit-scrollbar {
            height: 5px;
        }
        .slider-track::-webkit-scrollbar-thumb {
            background: rgba(234, 179, 8, 0.35);
            border-radius: 4px;
        }

        .rail-village-card {
            flex: 0 0 175px;
            background: rgba(30, 41, 59, 0.7);
            border: 1px solid rgba(255, 255, 255, 0.12);
            border-radius: 12px;
            padding: 10px 12px;
            cursor: pointer;
            text-align: right;
            transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
            position: relative;
            color: #f8fafc;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }
        .rail-village-card:hover {
            background: rgba(30, 41, 59, 0.95);
            border-color: #eab308;
            transform: translateY(-3px);
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.45);
        }
        .rail-village-card.is-active-card {
            border-color: #38bdf8;
            background: rgba(14, 116, 144, 0.4);
            box-shadow: 0 0 16px rgba(56, 189, 248, 0.5);
        }

        .rail-card-top {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 6px;
        }
        .rail-card-name {
            font-size: 13.5px;
            font-weight: 800;
            color: #f8fafc;
        }
        .rail-card-badge {
            font-size: 9.5px;
            font-weight: 800;
            padding: 2px 6px;
            border-radius: 10px;
            white-space: nowrap;
        }
        .rail-card-badge.completed {
            background: rgba(16, 185, 129, 0.25);
            border: 1px solid rgba(16, 185, 129, 0.6);
            color: #6ee7b7;
        }
        .rail-card-badge.pending {
            background: rgba(148, 163, 184, 0.15);
            border: 1px solid rgba(148, 163, 184, 0.3);
            color: #94a3b8;
        }

        .rail-card-meta {
            font-size: 11px;
            color: #cbd5e1;
            margin-bottom: 6px;
            line-height: 1.4;
        }
        .rail-card-action {
            font-size: 10px;
            font-weight: 700;
            color: #edd395;
            display: flex;
            align-items: center;
            gap: 4px;
        }
        .rail-village-card:hover .rail-card-action {
            color: #facc15;
        }
"""

css_marker = "</style>"
assert css_marker in html, "</style> not found"
html = html.replace(css_marker, slider_css + "\n    " + css_marker, 1)
print("5. Injected CSS for Village Slider Rail!")

# =========================================================================
# STEP 6: Add Slider Rail Markup in mapScene
# =========================================================================
scene_marker = '<div id="catchmentLegend"'
slider_markup = """<!-- Village Horizontal Slider Rail (Senior UX) -->
    <div id="villageSliderRail" class="village-slider-rail">
        <div class="slider-rail-header">
            <div class="slider-rail-title">
                <span class="rail-indicator-dot"></span>
                <strong>نوار پیمایش و دسترسی سریع به روستاها (لکه‌گذاری و کشو)</strong>
                <span class="rail-stats-pill">۷ روستای مستند · ۱۲ روستا در انتظار آمار</span>
            </div>
            <div class="slider-rail-controls">
                <button type="button" class="rail-nav-btn" id="railScrollRightBtn" title="حرکت به راست">◀</button>
                <button type="button" class="rail-nav-btn" id="railScrollLeftBtn" title="حرکت به چپ">▶</button>
                <button type="button" class="rail-toggle-btn" id="toggleRailCollapseBtn" title="کوچک‌سازی / باز کردن نوار">
                    <span id="railToggleIcon">▾</span>
                    <span id="railToggleText">بستن نوار</span>
                </button>
            </div>
        </div>
        <div class="slider-track-wrapper" id="sliderTrackWrapper">
            <div class="slider-track" id="sliderTrack"></div>
        </div>
    </div>

    <div id="catchmentLegend" """

assert scene_marker in html, "catchmentLegend marker not found"
html = html.replace(scene_marker, slider_markup, 1)
print("6. Injected Village Slider Rail Markup!")

# =========================================================================
# STEP 7: Inject Slider Rail JS Logic
# =========================================================================
slider_js = """
        // =========================================================================
        // VILLAGE HORIZONTAL SLIDER RAIL ENGINE (SENIOR UX)
        // =========================================================================
        function buildVillageSliderRail() {
            const track = document.getElementById('sliderTrack');
            if (!track || typeof villages === 'undefined') return;
            track.innerHTML = '';

            const villageItems = villages.filter(v => v.cat === 'village');

            villageItems.forEach(v => {
                const card = document.createElement('div');
                card.className = 'rail-village-card';
                card.id = `rail-card-${v.id}`;
                card.setAttribute('data-village-id', v.id);

                const isCompleted = ['soureh', 'darband-gharbi', 'pol-now', 'maslavi-1', 'sad-dastgah', 'shahrak-sevvom', 'ariz'].includes(v.id);
                
                let badgeText = '⏳ در انتظار دیتا';
                let badgeCls = 'pending';
                let metaText = 'در انتظار ورود داده‌های میدانی';

                if (v.id === 'soureh') {
                    badgeText = '📋 ۷۰ پرونده';
                    badgeCls = 'completed';
                    metaText = '۴,۱۷۵ نفر · ۱,۰۵۱ خانوار';
                } else if (v.id === 'darband-gharbi') {
                    badgeText = '📋 ۶۱ پرونده';
                    badgeCls = 'completed';
                    metaText = '۲,۷۵۵ نفر · ۶۸۱ خانوار';
                } else if (v.id === 'pol-now') {
                    badgeText = '📋 ۲۹ پرونده';
                    badgeCls = 'completed';
                    metaText = '۳,۸۵۰ نفر · ۹۵۰ خانوار';
                } else if (v.id === 'sad-dastgah') {
                    badgeText = '📋 ۲۴ پرونده';
                    badgeCls = 'completed';
                    metaText = '۸۸۲ نفر · ۲۱۱ خانوار';
                } else if (v.id === 'maslavi-1') {
                    badgeText = '📋 ۱۶ پرونده';
                    badgeCls = 'completed';
                    metaText = '۱,۱۰۰ نفر · ۳۶۰ خانوار';
                } else if (v.id === 'shahrak-sevvom') {
                    badgeText = '📋 ۱۶ پرونده';
                    badgeCls = 'completed';
                    metaText = '۴۰۳ نفر · ۱۳۴ خانوار';
                } else if (v.id === 'ariz') {
                    badgeText = '📋 ۵ پرونده';
                    badgeCls = 'completed';
                    metaText = '۲۸۱ نفر · ۶۵ خانوار';
                }

                card.innerHTML = `
                    <div>
                        <div class="rail-card-top">
                            <span class="rail-card-name">${v.name}</span>
                            <span class="rail-card-badge ${badgeCls}">${badgeText}</span>
                        </div>
                        <div class="rail-card-meta">${metaText}</div>
                    </div>
                    <div class="rail-card-action">
                        <span>ورود به پرتال</span>
                        <span>←</span>
                    </div>
                `;

                // Hover interaction: highlight on map and show reticle
                card.addEventListener('mouseenter', () => {
                    if (v.el) v.el.classList.add('highlighted-pin');
                    if (typeof showSpatialReticle === 'function') {
                        showSpatialReticle(v, v.name);
                    }
                });
                card.addEventListener('mouseleave', () => {
                    if (v.el) v.el.classList.remove('highlighted-pin');
                    if (typeof hideSpatialReticle === 'function') {
                        hideSpatialReticle();
                    }
                });

                // Click interaction: enter village hub
                card.addEventListener('click', (e) => {
                    e.stopPropagation();
                    if (typeof enter === 'function') {
                        enter(v);
                    }
                });

                track.appendChild(card);
            });
        }

        function highlightVillageCardInRail(villageId) {
            document.querySelectorAll('.rail-village-card').forEach(c => c.classList.remove('is-active-card'));
            const activeCard = document.getElementById(`rail-card-${villageId}`);
            if (activeCard) {
                activeCard.classList.add('is-active-card');
                activeCard.scrollIntoView({ behavior: 'smooth', inline: 'center', block: 'nearest' });
            }
        }

        // Initialize rail buttons and build on load
        document.addEventListener('DOMContentLoaded', () => {
            buildVillageSliderRail();

            const track = document.getElementById('sliderTrack');
            const leftBtn = document.getElementById('railScrollLeftBtn');
            const rightBtn = document.getElementById('railScrollRightBtn');
            const toggleBtn = document.getElementById('toggleRailCollapseBtn');
            const rail = document.getElementById('villageSliderRail');
            const toggleIcon = document.getElementById('railToggleIcon');
            const toggleText = document.getElementById('railToggleText');

            if (leftBtn && track) {
                leftBtn.addEventListener('click', () => {
                    track.scrollBy({ left: -240, behavior: 'smooth' });
                });
            }
            if (rightBtn && track) {
                rightBtn.addEventListener('click', () => {
                    track.scrollBy({ left: 240, behavior: 'smooth' });
                });
            }
            if (toggleBtn && rail) {
                toggleBtn.addEventListener('click', () => {
                    rail.classList.toggle('is-collapsed');
                    if (rail.classList.contains('is-collapsed')) {
                        if (toggleIcon) toggleIcon.textContent = '▴';
                        if (toggleText) toggleText.textContent = 'باز کردن نوار';
                    } else {
                        if (toggleIcon) toggleIcon.textContent = '▾';
                        if (toggleText) toggleText.textContent = 'بستن نوار';
                    }
                });
            }
        });

        // Also run immediately
        setTimeout(() => {
            buildVillageSliderRail();
        }, 150);
"""

script_end = "</script>"
idx_se = html.rfind(script_end)
assert idx_se != -1, "closing script tag not found"
html = html[:idx_se] + slider_js + "\n    " + html[idx_se:]
print("7. Injected Village Slider Rail JS Logic!")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("SUCCESS: Maslavi 1 & 2 separated and Village Slider Rail implemented!")
