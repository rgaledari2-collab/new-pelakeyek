import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# --------------------------------------------------------------------------
# 1. ADD 'darband-sharqi' TO villageDatabase IF NOT PRESENT
# --------------------------------------------------------------------------
darband_sharqi_db_entry = """                'darband-sharqi': {
                    name: 'دربند شرقی',
                    corridor: 'محور مواصلاتی شلمچه - خرمشهر (حومه غربی)',
                    coords: '30.44920000° N, 48.14850000° E',
                    borderDist: '۵.۸ کیلومتر',
                    cityDist: '۷.۲ کیلومتر',
                    area: '۲۸ هکتار',
                    priorityRank: 'اولویت ۲ از ۱۲ (محور شلمچه)',
                    priorityClass: 'p-mid',
                    priorityDesc: 'روستای همجوار دربند غربی، دارای ۴۵۰ خانوار و ۱,۸۵۰ نفر جمعیت، پوشش خدمات سلامت و آموزشی منطقه‌ای، نیازمند بهسازی انشعابات و آسفالت معابر.',
                    pop: '۱,۸۵۰',
                    popSub: '۴۵۰ خانوار · بعد خانوار: ۴.۱۱ نفر',
                    fam: '۴۵۰',
                    famSub: '۳۲ خانوار تحت پوشش حمایتی',
                    disabled: '۷',
                    disabledSub: 'ایتام و بیماران خاص تحت پوشش',
                    emp: 'طرح فعال',
                    empSub: 'حمایت معیشتی و خوداشتغالی',
                    agePyramid: [
                        { label: 'کودکان و نوجوانان', percent: '۳۲٪', count: '۵۹۲ نفر' },
                        { label: 'سنین فعالیت و کار', percent: '۵۴٪', count: '۹۹۹ نفر' },
                        { label: 'سالمندان', percent: '۱۴٪', count: '۲۵۹ نفر' }
                    ],
                    disabilities: [
                        { label: 'بیماری خاص و معلولیت', count: '۷ نفر', percent: '۱۰۰٪' }
                    ],
                    empProjects: [
                        { title: 'طرح تسهیلات خوداشتغالی روستایی', status: 'در حال ارزیابی', budget: '۱۲۰ میلیون تومان' },
                        { title: 'بسته‌های معیشتی و سبد غذایی', status: 'دوره‌ای فعال', budget: 'مستمر' }
                    ],
                    infrastructures: [
                        { title: 'شبکه آبرسانی شرب', status: 'پایدار با نیاز به نوسازی لوله‌ها' },
                        { title: 'شبکه برق و روشنایی معابر', status: 'فعال' },
                        { title: 'آسفالت معابر اصلی', status: 'بخشی نیازمند بهسازی' }
                    ],
                    schools: [
                        { name: 'پوشش آموزشی منطقه دربند', type: 'دبستان مشترک', shift: 'صبح', students: '۳۱۰ نفر' }
                    ],
                    indicators: [
                        { label: 'ضریب دسترسی فضایی', val: '۷.۲ / ۱۰' },
                        { label: 'امنیت غذایی خانوار', val: 'مطلوب با نظارت' },
                        { label: 'پوشش بهداشت فردی', val: '۸۵٪' }
                    ],
                    orphansCount: 4,
                    vulnerableFamilies: 32,
                    isPendingData: false
                },
"""

if "'darband-sharqi':" not in html:
    idx_db = html.find("const villageDatabase = {")
    assert idx_db != -1, "villageDatabase not found"
    # insert right after opening brace
    insert_pos = idx_db + len("const villageDatabase = {")
    html = html[:insert_pos] + "\n" + darband_sharqi_db_entry + html[insert_pos:]
    print("1. Injected darband-sharqi into villageDatabase!")
else:
    print("1. darband-sharqi already in villageDatabase!")

# --------------------------------------------------------------------------
# 2. ADD vUploadPhoto BUTTON AND FILE INPUT TO #villageMapControls
# --------------------------------------------------------------------------
old_controls = """                    <div class="village-map-controls" id="villageMapControls">
                        <button type="button" class="v-map-btn" id="vZoomIn" title="بزرگ‌نمایی نقشه (Zoom In)">＋</button>
                        <button type="button" class="v-map-btn" id="vZoomOut" title="کوچک‌نمایی نقشه (Zoom Out)">－</button>
                        <button type="button" class="v-map-btn" id="vResetZoom" title="بازنشانی اندازه نقشه (Reset View)">↺</button>
                        <button type="button" class="v-map-btn" id="vToggleFit" title="تغییر کادربندی (تناسب کامل / پرکردن صفحه)">⛶</button>
                    </div>"""

new_controls = """                    <div class="village-map-controls" id="villageMapControls">
                        <button type="button" class="v-map-btn" id="vZoomIn" title="بزرگ‌نمایی نقشه (Zoom In)">＋</button>
                        <button type="button" class="v-map-btn" id="vZoomOut" title="کوچک‌نمایی نقشه (Zoom Out)">－</button>
                        <button type="button" class="v-map-btn" id="vResetZoom" title="بازنشانی اندازه نقشه (Reset View)">↺</button>
                        <button type="button" class="v-map-btn" id="vToggleFit" title="تغییر کادربندی (تناسب کامل / پرکردن صفحه)">⛶</button>
                        <button type="button" class="v-map-btn" id="vUploadPhoto" title="بارگذاری عکس ماهواره‌ای اختصاصی دلخواه برای این روستا">📷</button>
                        <input type="file" id="vPhotoFileInput" accept="image/*" style="display:none;" />
                    </div>"""

if old_controls in html:
    html = html.replace(old_controls, new_controls, 1)
    print("2. Added vUploadPhoto and hidden file input to controls!")
else:
    print("2. Controls already modified or pattern not found")

# --------------------------------------------------------------------------
# 3. REWRITE updateVillageSatelliteView AND setupVillageInteractions
# --------------------------------------------------------------------------
start_engine_marker = "function updateVillageSatelliteView(v) {"
idx_start = html.find(start_engine_marker)
assert idx_start != -1, "updateVillageSatelliteView not found"

idx_end = html.find("document.addEventListener('DOMContentLoaded', setupVillageInteractions);", idx_start)
assert idx_end != -1, "DOMContentLoaded setupVillageInteractions not found"

# Find end of that setTimeout block
idx_timeout = html.find("setTimeout(setupVillageInteractions, 150);", idx_end)
assert idx_timeout != -1, "setTimeout not found"
idx_block_end = idx_timeout + len("setTimeout(setupVillageInteractions, 150);")

new_satellite_engine_js = """function updateVillageSatelliteView(v) {
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
            const mapBadge = document.getElementById('villageMapBadge');

            resetVillageMapView();
            window._currentVillageViewing = v;

            // Database of dedicated high-res satellite photos and POIs for villages
            const villageMapRegistry = {
                'pol-now': {
                    img: '/image_0.webp',
                    fallback: '/pol_now_map.webp',
                    badge: 'پایش هوایی شلمچه · نقشه تفصیلی روستای پل نو',
                    kicker: '🛰️ نقشه هوایی ماهواره‌ای تفصیلی · روستای پل نو',
                    name: 'پل نو',
                    sub: 'محور مواصلاتی شلمچه - خرمشهر · حومه غربی',
                    chipPop: '👥 ۳,۸۵۰ نفر',
                    chipFam: '🏡 ۹۵۰ خانوار',
                    chipSchool: '🎒 دبستان معراج (۴۲۰ دانش‌آموز)',
                    statsDesc: 'جمعیت، هرم تحصیلی و ۲۹ پرونده مستند',
                    statsHtml: `
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
                    `,
                    servDesc: 'خانه بهداشت پل نو، دبستان معراج و طرح‌های توانمندسازی',
                    servHtml: `
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
                    `,
                    pois: [
                        { icon: '🏫', label: 'دبستان معراج (۴۲۰ دانش‌آموز)', type: 'school', top: '48%', left: '50%' },
                        { icon: '🏥', label: 'خانه بهداشت روستایی پل نو', type: 'health', top: '40%', left: '34%' },
                        { icon: '📍', label: 'موقعیت شاخص روستا', type: 'marker', top: '58%', left: '84%' },
                        { icon: '🛣️', label: 'محور مواصلاتی شلمچه', type: 'road', bottom: '12%', left: '45%' },
                        { icon: '🌊', label: 'کانال آبرسانی', type: 'canal', top: '18%', left: '24%' }
                    ]
                },
                'ariz': {
                    img: '/ariz_map.webp',
                    fallback: '/ariz_map.jpg',
                    badge: 'پایش هوایی جاده شلمچه · نقشه تفصیلی روستای عریض',
                    kicker: '🛰️ نقشه هوایی ماهواره‌ای تفصیلی · روستای عریض',
                    name: 'عریض',
                    sub: 'محور جاده شلمچه · بخش مرکزی خرمشهر',
                    chipPop: '👥 ۱,۴۵۰ نفر',
                    chipFam: '🏡 ۳۸۰ خانوار',
                    chipSchool: '🎒 دبستان معراج عریض (۱۹۰ دانش‌آموز)',
                    statsDesc: 'جمعیت، خانوارها و پرونده‌های نیازمندان روستای عریض',
                    statsHtml: `
                        <div class="v-metric-row">
                            <span class="m-label">👥 جمعیت کل روستا:</span>
                            <span class="m-val highlight">۱,۴۵۰ نفر (۳۸۰ خانوار)</span>
                        </div>
                        <div class="v-metric-row">
                            <span class="m-label">🎒 دبستان معراج عریض:</span>
                            <span class="m-val">۱۹۰ دانش‌آموز</span>
                        </div>
                        <div class="v-metric-row">
                            <span class="m-label">📋 پرونده‌های مستند:</span>
                            <span class="m-val">۱۷ خانوار کم‌برخوردار و ۳ یتیم</span>
                        </div>
                    `,
                    servDesc: 'خانه بهداشت عریض، دبستان، شبکه آب پایدار و طرح‌های معیشتی',
                    servHtml: `
                        <div class="v-metric-row">
                            <span class="m-label">🏥 مرکز سلامت:</span>
                            <span class="m-val highlight">خانه بهداشت فعال عریض</span>
                        </div>
                        <div class="v-metric-row">
                            <span class="m-label">💧 زیرساخت معابر و آب:</span>
                            <span class="m-val">شبکه آب شرب و آسفالت</span>
                        </div>
                        <div class="v-metric-row">
                            <span class="m-label">🤝 اقدامات حمایتی:</span>
                            <span class="m-val">بسته‌های معیشتی و اشتغال‌زایی</span>
                        </div>
                    `,
                    pois: [
                        { icon: '🏫', label: 'دبستان معراج عریض (۱۹۰ دانش‌آموز)', type: 'school', top: '45%', left: '50%' },
                        { icon: '🏥', label: 'خانه بهداشت روستایی عریض', type: 'health', top: '36%', left: '34%' },
                        { icon: '🕌', label: 'حسینیه و مسجد اهل‌بیت (ع)', type: 'mosque', top: '55%', left: '65%' },
                        { icon: '🌴', label: 'نخلستان و اراضی کشاورزی', type: 'canal', top: '22%', left: '25%' },
                        { icon: '🛣️', label: 'محور جاده شلمچه - خرمشهر', type: 'road', bottom: '12%', left: '48%' }
                    ]
                },
                'jadideh': {
                    img: '/jadideh_map.webp',
                    fallback: '/jadideh_map.jpg',
                    badge: 'پایش هوایی حومه شرقی · نقشه تفصیلی روستای جدیده',
                    kicker: '🛰️ نقشه هوایی ماهواره‌ای تفصیلی · روستای جدیده',
                    name: 'جدیده',
                    sub: 'بخش مرکزی · حومه شرقی شهرستان خرمشهر',
                    chipPop: '👥 ۳,۲۰۰ نفر',
                    chipFam: '🏡 ۸۵۰ خانوار',
                    chipSchool: '🎒 ۲ واحد دبستان (۴۱۰ دانش‌آموز)',
                    statsDesc: 'جمعیت، هرم تحصیلی و پایش آماری روستای جدیده',
                    statsHtml: `
                        <div class="v-metric-row">
                            <span class="m-label">👥 جمعیت کل روستا:</span>
                            <span class="m-val highlight">۳,۲۰۰ نفر (۸۵۰ خانوار)</span>
                        </div>
                        <div class="v-metric-row">
                            <span class="m-label">🎒 مدارس ابتدایی:</span>
                            <span class="m-val">۴۱۰ دانش‌آموز در ۲ واحد دبستان</span>
                        </div>
                        <div class="v-metric-row">
                            <span class="m-label">📊 پایش میدانی:</span>
                            <span class="m-val">ثبت کامل پرونده‌های حمایتی</span>
                        </div>
                    `,
                    servDesc: 'مرکز سلامت جدیده، زیرساخت آب شرب پایدار و طرح‌های توانمندسازی',
                    servHtml: `
                        <div class="v-metric-row">
                            <span class="m-label">🏥 مرکز سلامت:</span>
                            <span class="m-val highlight">مرکز خدمات جامع سلامت جدیده</span>
                        </div>
                        <div class="v-metric-row">
                            <span class="m-label">💧 زیرساخت آب:</span>
                            <span class="m-val">خط انتقال و شبکه آب شرب پایدار</span>
                        </div>
                        <div class="v-metric-row">
                            <span class="m-label">🤝 حمایت اجتماعی:</span>
                            <span class="m-val">بسته‌های معیشتی و پروژه‌های اشتغال</span>
                        </div>
                    `,
                    pois: [
                        { icon: '🏫', label: 'دبستان‌های جدیده (۴۱۰ دانش‌آموز)', type: 'school', top: '46%', left: '52%' },
                        { icon: '🏥', label: 'مرکز جامع سلامت جدیده', type: 'health', top: '38%', left: '32%' },
                        { icon: '🕌', label: 'مسجد جامع امام حسن مجتبی (ع)', type: 'mosque', top: '58%', left: '66%' },
                        { icon: '🌴', label: 'نخلستان‌ها و باغات خرما', type: 'canal', top: '24%', left: '75%' },
                        { icon: '🛣️', label: 'بلوار دسترسی اصلی روستا', type: 'road', bottom: '14%', left: '44%' }
                    ]
                },
                'darband-gharbi': {
                    img: '/darband-gharbi_map.webp',
                    fallback: '/darband-gharbi_map.jpg',
                    badge: 'پایش هوایی حومه غربی · نقشه تفصیلی روستای دربند غربی',
                    kicker: '🛰️ نقشه هوایی ماهواره‌ای تفصیلی · روستای دربند غربی',
                    name: 'دربند غربی',
                    sub: 'حومه غربی · کانون سکونتگاهی راهبردی شلمچه',
                    chipPop: '👥 ۲,۷۵۵ نفر',
                    chipFam: '🏡 ۶۸۱ خانوار',
                    chipSchool: '🎒 دبستان مرزداران (۱۷۷ دانش‌آموز)',
                    statsDesc: 'جمعیت، توان‌خواهان و پرونده‌های حمایتی دربند غربی',
                    statsHtml: `
                        <div class="v-metric-row">
                            <span class="m-label">👥 جمعیت کل روستا:</span>
                            <span class="m-val highlight">۲,۷۵۵ نفر (۶۸۱ خانوار)</span>
                        </div>
                        <div class="v-metric-row">
                            <span class="m-label">🎒 دبستان مرزداران:</span>
                            <span class="m-val">۱۷۷ دانش‌آموز</span>
                        </div>
                        <div class="v-metric-row">
                            <span class="m-label">📋 پرونده‌های توان‌خواهان:</span>
                            <span class="m-val">۸۳ مورد پایش‌شده (جسمی، ذهنی و ...)</span>
                        </div>
                    `,
                    servDesc: 'خانه بهداشت دربند غربی، بهسازی معابر، آسفالت و توانمندسازی',
                    servHtml: `
                        <div class="v-metric-row">
                            <span class="m-label">🏥 مرکز سلامت:</span>
                            <span class="m-val highlight">خانه بهداشت فعال دربند غربی</span>
                        </div>
                        <div class="v-metric-row">
                            <span class="m-label">💧 زیرساخت معابر:</span>
                            <span class="m-val">آسفالت معابر و شبکه آبرسانی</span>
                        </div>
                        <div class="v-metric-row">
                            <span class="m-label">🤝 حمایت اجتماعی:</span>
                            <span class="m-val">طرح ویژه توان‌خواهان و ایتام</span>
                        </div>
                    `,
                    pois: [
                        { icon: '🏫', label: 'دبستان مرزداران (۱۷۷ دانش‌آموز)', type: 'school', top: '46%', left: '48%' },
                        { icon: '🏥', label: 'خانه بهداشت دربند غربی', type: 'health', top: '36%', left: '35%' },
                        { icon: '🕌', label: 'حسینیه فاطمیه و کانون فرهنگی', type: 'mosque', top: '55%', left: '66%' },
                        { icon: '📍', label: 'کانون جمعیتی و خدمات', type: 'marker', top: '62%', left: '26%' },
                        { icon: '🛣️', label: 'محور مواصلاتی دربند', type: 'road', bottom: '14%', left: '52%' }
                    ]
                },
                'darband-sharqi': {
                    img: '/darband-sharqi_map.webp',
                    fallback: '/darband-sharqi_map.jpg',
                    badge: 'پایش هوایی حومه غربی · نقشه تفصیلی روستای دربند شرقی',
                    kicker: '🛰️ نقشه هوایی ماهواره‌ای تفصیلی · روستای دربند شرقی',
                    name: 'دربند شرقی',
                    sub: 'حومه غربی · همجوار دربند غربی و شلمچه',
                    chipPop: '👥 ۱,۸۵۰ نفر',
                    chipFam: '🏡 ۴۵۰ خانوار',
                    chipSchool: '🎒 پوشش آموزشی مشترک',
                    statsDesc: 'جمعیت، خانوارها و شاخص‌های نیازسنجی دربند شرقی',
                    statsHtml: `
                        <div class="v-metric-row">
                            <span class="m-label">👥 جمعیت کل روستا:</span>
                            <span class="m-val highlight">۱,۸۵۰ نفر (۴۵۰ خانوار)</span>
                        </div>
                        <div class="v-metric-row">
                            <span class="m-label">📊 ضریب دسترسی:</span>
                            <span class="m-val">امتیاز محرومیت ۷.۲ از ۱۰</span>
                        </div>
                        <div class="v-metric-row">
                            <span class="m-label">📋 پرونده‌های حمایتی:</span>
                            <span class="m-val">۳۲ خانوار تحت پوشش و ۴ یتیم</span>
                        </div>
                    `,
                    servDesc: 'خدمات سلامت، خطوط آبرسانی، بهسازی معابر و بسته‌های معیشتی',
                    servHtml: `
                        <div class="v-metric-row">
                            <span class="m-label">🏥 پوشش سلامت:</span>
                            <span class="m-val highlight">پایش سلامت خانواده و بهورزی</span>
                        </div>
                        <div class="v-metric-row">
                            <span class="m-label">💧 زیرساخت معابر:</span>
                            <span class="m-val">نوسازی لوله‌های آب و روشنایی</span>
                        </div>
                        <div class="v-metric-row">
                            <span class="m-label">🤝 حمایت اجتماعی:</span>
                            <span class="m-val">بسته‌های معیشتی و توانمندسازی</span>
                        </div>
                    `,
                    pois: [
                        { icon: '🕌', label: 'حسینیه و کانون مذهبی دربند شرقی', type: 'mosque', top: '48%', left: '52%' },
                        { icon: '🏫', label: 'دسترسی آموزشی و مدارس', type: 'school', top: '38%', left: '40%' },
                        { icon: '🏥', label: 'پایگاه سلامت و بهداشت', type: 'health', top: '58%', left: '34%' },
                        { icon: '🌴', label: 'نخلستان و بافت سنتی', type: 'canal', top: '22%', left: '68%' },
                        { icon: '🛣️', label: 'جاده ارتباطی بین‌روستایی', type: 'road', bottom: '15%', left: '46%' }
                    ]
                }
            };

            const reg = villageMapRegistry[v.id];
            const customUserPhoto = localStorage.getItem('village_custom_photo_' + v.id);

            if (reg) {
                if (satImg) {
                    satImg.src = customUserPhoto || reg.img;
                    satImg.onerror = () => { satImg.src = reg.fallback || '/main_map_final.jpg'; };
                    satImg.alt = `نقشه اختصاصی تفصیلی روستای ${reg.name}`;
                }
                if (kicker) kicker.textContent = reg.kicker;
                if (vName) vName.textContent = reg.name;
                if (vSub) vSub.textContent = reg.sub;
                if (chipPop) chipPop.textContent = reg.chipPop;
                if (chipFam) chipFam.textContent = reg.chipFam;
                if (chipSchool) chipSchool.textContent = reg.chipSchool;
                if (statsDesc) statsDesc.textContent = reg.statsDesc;
                if (statsPreview) statsPreview.innerHTML = reg.statsHtml;
                if (servDesc) servDesc.textContent = reg.servDesc;
                if (servPreview) servPreview.innerHTML = reg.servHtml;
                if (mapBadge) {
                    mapBadge.innerHTML = `<span class="badge-dot"></span><span>${reg.badge}</span>`;
                }

                // Render interactive Aerial POIs
                if (aerialOverlay) {
                    aerialOverlay.style.display = 'block';
                    aerialOverlay.innerHTML = reg.pois.map(p => {
                        const posStyle = [
                            p.top ? `top: ${p.top};` : '',
                            p.bottom ? `bottom: ${p.bottom};` : '',
                            p.left ? `left: ${p.left};` : '',
                            p.right ? `right: ${p.right};` : ''
                        ].filter(Boolean).join(' ');

                        return `
                            <div class="aerial-poi poi-${p.type}" style="${posStyle}" data-poi="${p.type}" title="${p.label}">
                                <span class="aerial-poi-dot">${p.icon}</span>
                                <span class="aerial-poi-label">${p.label}</span>
                                <span class="aerial-poi-pulse"></span>
                            </div>
                        `;
                    }).join('');
                }
            } else {
                // Fallback for any other village: High-res regional satellite map
                if (satImg) {
                    satImg.src = customUserPhoto || '/main_map_final.jpg';
                    satImg.alt = `نقشه روستای ${v.name}`;
                }
                if (aerialOverlay) {
                    aerialOverlay.style.display = 'block';
                    aerialOverlay.innerHTML = `
                        <div class="aerial-poi poi-marker" style="top: 50%; left: 50%;" data-poi="marker" title="موقعیت روستای ${v.name}">
                            <span class="aerial-poi-dot">📍</span>
                            <span class="aerial-poi-label">موقعیت روستای ${v.name}</span>
                            <span class="aerial-poi-pulse"></span>
                        </div>
                    `;
                }
                if (kicker) kicker.textContent = `شناسنامه و نقشه هوایی · روستای ${v.name}`;
                if (vName) vName.textContent = v.name;
                if (vSub) vSub.textContent = 'بخش مرکزی شهرستان خرمشهر · حوزه پایش میدانی';

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
                if (mapBadge) {
                    mapBadge.innerHTML = `<span class="badge-dot"></span><span>پایش هوایی منطقه · روستای ${v.name}</span>`;
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
            const cBtn = document.getElementById('villageCloseBtn');
            const uBtn = document.getElementById('vUploadPhoto');
            const fileInput = document.getElementById('vPhotoFileInput');
            const aerialOverlay = document.getElementById('villageAerialOverlay');

            // Close button (✕)
            if (cBtn && !cBtn._bound) {
                cBtn._bound = true;
                cBtn.onclick = (e) => {
                    e.stopPropagation();
                    if (typeof window.back === 'function') window.back();
                };
            }

            // Custom photo upload listener
            if (uBtn && fileInput && !uBtn._bound) {
                uBtn._bound = true;
                uBtn.onclick = (e) => {
                    e.stopPropagation();
                    fileInput.click();
                };

                fileInput.onchange = (e) => {
                    const file = e.target.files && e.target.files[0];
                    if (!file) return;
                    const v = window._currentVillageViewing;
                    if (!v) return;

                    const reader = new FileReader();
                    reader.onload = (evt) => {
                        const dataUrl = evt.target.result;
                        const satImg = document.getElementById('villageSatelliteImg');
                        if (satImg) satImg.src = dataUrl;
                        try {
                            localStorage.setItem('village_custom_photo_' + v.id, dataUrl);
                        } catch (err) {
                            console.warn('Storage limit for custom image', err);
                        }
                        if (typeof showSearchToast === 'function') {
                            showSearchToast(`عکس ماهواره‌ای اختصاصی روستای ${v.name} با موفقیت بارگذاری و ذخیره شد 📸`);
                        }
                    };
                    reader.readAsDataURL(file);
                };
            }

            // Zoom In / Out / Reset
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

            // Fit Mode / Fill Mode toggle
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

            // Fullscreen Map / Sidebar Toggle
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

            // Drag and Pan interactions
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

            // POI delegation click handling for dynamically generated aerial POIs
            if (aerialOverlay && !aerialOverlay._boundClick) {
                aerialOverlay._boundClick = true;
                aerialOverlay.addEventListener('click', (e) => {
                    const poi = e.target.closest('.aerial-poi');
                    if (!poi) return;
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
                });
            }
        }

        document.addEventListener('DOMContentLoaded', setupVillageInteractions);
        setTimeout(setupVillageInteractions, 150);"""

html = html[:idx_start] + new_satellite_engine_js + html[idx_block_end:]
print("3. Replaced satellite engine JS with multi-village satellite maps support!")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("SUCCESS: index.html updated successfully!")
