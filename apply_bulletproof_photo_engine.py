with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# --------------------------------------------------------------------------
# 1. CLEAN UP #villageSatelliteImg MARKUP (REMOVE INLINE onerror)
# --------------------------------------------------------------------------
old_sat_img = '<img id="villageSatelliteImg" src="/image_0.webp" onerror="this.onerror=null;this.src=\'/pol_now_map.webp\';" alt="نقشه اختصاصی روستای پل نو" class="village-satellite-img" />'
new_sat_img = '<img id="villageSatelliteImg" src="/image_0.webp" alt="نقشه ماهواره‌ای اختصاصی روستا" class="village-satellite-img" />'

if old_sat_img in html:
    html = html.replace(old_sat_img, new_sat_img, 1)
    print("1. Cleaned up villageSatelliteImg markup!")
else:
    print("1. old_sat_img pattern not found, checking alternatives...")
    # remove inline onerror if present
    html = html.replace('onerror="this.onerror=null;this.src=\'/pol_now_map.webp\';"', '')
    print("1. Stripped any inline onerror to /pol_now_map.webp")

# --------------------------------------------------------------------------
# 2. ENSURE PERMANENT GLOBAL FILE INPUT IS PRESENT
# --------------------------------------------------------------------------
if 'id="globalVillagePhotoInput"' not in html:
    idx_body_end = html.rfind("</body>")
    global_input_html = '<input type="file" id="globalVillagePhotoInput" accept="image/*" style="display:none;" />\n'
    if idx_body_end != -1:
        html = html[:idx_body_end] + global_input_html + html[idx_body_end:]
        print("2. Added permanent globalVillagePhotoInput before </body>!")
    else:
        # insert before </script>
        idx_s_end = html.rfind("</script>")
        html = html[:idx_s_end] + global_input_html + html[idx_s_end:]
        print("2. Added globalVillagePhotoInput before </script>!")
else:
    print("2. globalVillagePhotoInput already in HTML!")

# --------------------------------------------------------------------------
# 3. REWRITE THE SATELLITE & PHOTO MANAGEMENT ENGINE
# --------------------------------------------------------------------------
idx_start = html.find("function updateVillageSatelliteView(v)")
assert idx_start != -1, "function updateVillageSatelliteView not found"
idx_end = html.rfind("</script>")
assert idx_end != -1, "</script> not found"

new_engine_code = """// =========================================================================
        // ROBUST CLIENT-SIDE IMAGE PERSISTENCE & CANVAS COMPRESSION ENGINE
        // =========================================================================

        window._villageCustomPhotos = {};
        window._currentVillageViewing = null;
        window._targetVillageForUpload = null;

        const DB_NAME = 'VillageMapsDB';
        const DB_STORE = 'photos';

        function initPhotosDB() {
            return new Promise((resolve) => {
                if (!window.indexedDB) return resolve(null);
                try {
                    const req = indexedDB.open(DB_NAME, 1);
                    req.onupgradeneeded = (e) => {
                        const db = e.target.result;
                        if (!db.objectStoreNames.contains(DB_STORE)) {
                            db.createObjectStore(DB_STORE);
                        }
                    };
                    req.onsuccess = (e) => resolve(e.target.result);
                    req.onerror = () => resolve(null);
                } catch (e) {
                    resolve(null);
                }
            });
        }

        async function savePhotoToStorage(vid, dataUrl) {
            window._villageCustomPhotos[vid] = dataUrl;
            try {
                localStorage.setItem('village_custom_photo_' + vid, dataUrl);
            } catch (err) {
                console.warn('localStorage full, falling back to IndexedDB', err);
            }
            try {
                const db = await initPhotosDB();
                if (db) {
                    const tx = db.transaction(DB_STORE, 'readwrite');
                    tx.objectStore(DB_STORE).put(dataUrl, vid);
                }
            } catch (err) {
                console.warn('IndexedDB write error', err);
            }
        }

        async function removePhotoFromStorage(vid) {
            delete window._villageCustomPhotos[vid];
            try {
                localStorage.removeItem('village_custom_photo_' + vid);
            } catch (err) {}
            try {
                const db = await initPhotosDB();
                if (db) {
                    const tx = db.transaction(DB_STORE, 'readwrite');
                    tx.objectStore(DB_STORE).delete(vid);
                }
            } catch (err) {}
        }

        function getCachedCustomPhoto(vid) {
            if (window._villageCustomPhotos && window._villageCustomPhotos[vid]) {
                return window._villageCustomPhotos[vid];
            }
            try {
                const local = localStorage.getItem('village_custom_photo_' + vid);
                if (local) {
                    window._villageCustomPhotos[vid] = local;
                    return local;
                }
            } catch (e) {}
            return null;
        }

        async function preloadAllVillagePhotos() {
            try {
                const db = await initPhotosDB();
                if (!db) return;
                const tx = db.transaction(DB_STORE, 'readonly');
                const store = tx.objectStore(DB_STORE);
                const req = store.openCursor();
                req.onsuccess = (e) => {
                    const cursor = e.target.result;
                    if (cursor) {
                        window._villageCustomPhotos[cursor.key] = cursor.value;
                        cursor.continue();
                    }
                };
            } catch (err) {}
        }

        function compressAndProcessImage(file, maxWidth = 1920, quality = 0.85) {
            return new Promise((resolve, reject) => {
                const reader = new FileReader();
                reader.onload = (e) => {
                    const img = new Image();
                    img.onload = () => {
                        let { width, height } = img;
                        if (width > maxWidth || height > maxWidth) {
                            if (width > height) {
                                height = Math.round((height * maxWidth) / width);
                                width = maxWidth;
                            } else {
                                width = Math.round((width * maxWidth) / height);
                                height = maxWidth;
                            }
                        }
                        const canvas = document.createElement('canvas');
                        canvas.width = width;
                        canvas.height = height;
                        const ctx = canvas.getContext('2d');
                        ctx.drawImage(img, 0, 0, width, height);
                        const compressedDataUrl = canvas.toDataURL('image/jpeg', quality);
                        resolve(compressedDataUrl);
                    };
                    img.onerror = () => reject(new Error('Failed to load image for compression'));
                    img.src = e.target.result;
                };
                reader.onerror = () => reject(new Error('Failed to read file'));
                reader.readAsDataURL(file);
            });
        }

        // =========================================================================
        // VILLAGE REGISTRY & POIS
        // =========================================================================

        const targetPhotoVillages = [
            { id: 'pol-now', name: 'پل نو', defaultImg: '/image_0.webp', fallback: '/pol_now_map.webp', desc: 'محور شلمچه · حومه غربی' },
            { id: 'ariz', name: 'عریض', defaultImg: '/ariz_map.webp', fallback: '/ariz_map.jpg', desc: 'جاده شلمچه · بخش مرکزی' },
            { id: 'jadideh', name: 'جدیده', defaultImg: '/jadideh_map.webp', fallback: '/jadideh_map.jpg', desc: 'حومه شرقی · نخلستان‌ها' },
            { id: 'darband-gharbi', name: 'دربند غربی', defaultImg: '/darband-gharbi_map.webp', fallback: '/darband-gharbi_map.jpg', desc: 'حومه غربی · کانون سکونتگاهی' },
            { id: 'darband-sharqi', name: 'دربند شرقی', defaultImg: '/darband-sharqi_map.webp', fallback: '/darband-sharqi_map.jpg', desc: 'حومه غربی · همجوار دربند غربی' }
        ];

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

        function getActiveVillagePhoto(vid) {
            const custom = getCachedCustomPhoto(vid);
            if (custom) return { src: custom, isCustom: true };
            const item = targetPhotoVillages.find(x => x.id === vid);
            if (item) return { src: item.defaultImg, fallback: item.fallback, isCustom: false };
            return { src: '/main_map_final.jpg', isCustom: false };
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
            const mapBadge = document.getElementById('villageMapBadge');

            resetVillageMapView();
            window._currentVillageViewing = v;

            const reg = villageMapRegistry[v.id];
            const customUserPhoto = getCachedCustomPhoto(v.id);

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
                // Fallback for other villages
                if (satImg) {
                    satImg.src = customUserPhoto || '/main_map_final.jpg';
                    satImg.onerror = null;
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

        // =========================================================================
        // UNIFIED ROBUST PHOTO UPLOAD & CHANGE ENGINE
        // =========================================================================

        function getVillageRecord(vid) {
            const list = window.villages || [];
            return list.find(x => x.id === vid) || targetPhotoVillages.find(x => x.id === vid) || null;
        }

        async function handleVillagePhotoUpload(vid, file) {
            if (!file || !file.type.startsWith('image/')) {
                if (typeof showSearchToast === 'function') {
                    showSearchToast('لطفاً یک فایل تصویری معتبر (JPG, PNG, WebP) انتخاب فرمایید.');
                }
                return;
            }

            const vObj = getVillageRecord(vid);
            const vTitle = vObj ? vObj.name : vid;

            if (typeof showSearchToast === 'function') {
                showSearchToast(`در حال پردازش و بهینه‌سازی عکس ${vTitle}... ⏳`);
            }

            try {
                // Compress image down to web-optimized dataURL (< 300KB)
                const compressedDataUrl = await compressAndProcessImage(file, 1920, 0.85);

                // Save to memory cache, localStorage, and IndexedDB
                await savePhotoToStorage(vid, compressedDataUrl);

                // Immediately update live map if this village is active on screen
                if (window._currentVillageViewing && window._currentVillageViewing.id === vid) {
                    const satImg = document.getElementById('villageSatelliteImg');
                    if (satImg) {
                        satImg.src = compressedDataUrl;
                        satImg.onerror = null;
                    }
                }

                // Update thumbnail in modal if visible
                const thumbEl = document.getElementById('thumb_' + vid);
                if (thumbEl) {
                    thumbEl.src = compressedDataUrl;
                }

                // Re-render modal cards to update badges and action buttons
                renderVillagePhotosGrid();

                if (typeof showSearchToast === 'function') {
                    showSearchToast(`عکس جدید روستای ${vTitle} با موفقیت جایگزین و ذخیره شد! 📸✨`);
                }
            } catch (err) {
                console.error('Error handling photo upload', err);
                if (typeof showSearchToast === 'function') {
                    showSearchToast('خطا در پردازش تصویر. لطفاً مجدداً امتحان کنید.');
                }
            }
        }

        function triggerPhotoUpload(vid) {
            window._targetVillageForUpload = vid;
            let input = document.getElementById('globalVillagePhotoInput');
            if (!input) {
                input = document.createElement('input');
                input.type = 'file';
                input.id = 'globalVillagePhotoInput';
                input.accept = 'image/*';
                input.style.display = 'none';
                document.body.appendChild(input);
            }
            input.value = '';
            input.onchange = (e) => {
                const file = e.target.files && e.target.files[0];
                if (file) {
                    const targetVid = window._targetVillageForUpload || vid;
                    handleVillagePhotoUpload(targetVid, file);
                }
            };
            input.click();
        }

        async function resetVillagePhoto(vid) {
            await removePhotoFromStorage(vid);
            const vObj = getVillageRecord(vid);
            const vTitle = vObj ? vObj.name : vid;

            // Revert live image if currently viewing this village
            if (window._currentVillageViewing && window._currentVillageViewing.id === vid) {
                updateVillageSatelliteView(window._currentVillageViewing);
            }

            if (typeof showSearchToast === 'function') {
                showSearchToast(`عکس روستای ${vTitle} به حالت اولیه بازنشانی شد ↺`);
            }

            renderVillagePhotosGrid();
        }

        function goToVillageFromModal(vid) {
            const modal = document.getElementById('villagePhotosDialog');
            if (modal) modal.close();

            const vObj = getVillageRecord(vid);
            const enterFn = window.enter;
            if (vObj && typeof enterFn === 'function') {
                const isVillageView = document.getElementById('experience')?.classList.contains('in-village');
                if (typeof window.back === 'function' && isVillageView) {
                    window.back();
                    setTimeout(() => enterFn(vObj), 150);
                } else {
                    enterFn(vObj);
                }
            }
        }

        function renderVillagePhotosGrid() {
            const grid = document.getElementById('villagePhotosGrid');
            if (!grid) return;

            grid.innerHTML = targetPhotoVillages.map(v => {
                const photoInfo = getActiveVillagePhoto(v.id);
                const badgeLabel = photoInfo.isCustom ? 'عکس اختصاصی کاربر ✅' : 'عکس پیش‌فرض ⚙️';
                const badgeClass = photoInfo.isCustom ? 'custom' : 'default';

                return `
                    <div class="v-photo-card" id="photoCard_${v.id}" data-vid="${v.id}">
                        <div class="v-photo-card-top">
                            <span class="v-photo-card-title">${v.name}</span>
                            <span class="v-photo-card-badge ${badgeClass}">${badgeLabel}</span>
                        </div>
                        <div class="v-photo-preview-box" onclick="triggerPhotoUpload('${v.id}')" title="برای تغییر عکس کلیک کنید یا فایل را اینجا رها کنید">
                            <img src="${photoInfo.src}" onerror="this.onerror=null;this.src='${photoInfo.fallback || '/main_map_final.jpg'}';" alt="${v.name}" class="v-photo-thumb" id="thumb_${v.id}" />
                            <div class="v-photo-drop-hint">
                                <span>📁 کلیک برای انتخاب عکس</span>
                                <span>یا Drag & Drop فایل عکس</span>
                            </div>
                        </div>
                        <div class="v-photo-card-actions">
                            <button type="button" class="v-photo-btn" onclick="triggerPhotoUpload('${v.id}')">
                                <span>📁</span>
                                <span>تعویض عکس</span>
                            </button>
                            ${photoInfo.isCustom ? `
                                <button type="button" class="v-photo-reset-btn" onclick="resetVillagePhoto('${v.id}')" title="بازنشانی به حالت اولیه">
                                    ↺
                                </button>
                            ` : ''}
                            <button type="button" class="v-photo-btn" style="flex:0 0 auto;" onclick="goToVillageFromModal('${v.id}')" title="ورود و مشاهده نقشه این روستا">
                                <span>👁️ ورود به نقشه</span>
                            </button>
                        </div>
                    </div>
                `;
            }).join('');

            // Bind drag & drop for each individual card in the modal
            targetPhotoVillages.forEach(v => {
                const card = document.getElementById('photoCard_' + v.id);
                if (card) {
                    card.addEventListener('dragover', (e) => {
                        e.preventDefault();
                        e.stopPropagation();
                        card.classList.add('card-dragover');
                    });
                    card.addEventListener('dragleave', (e) => {
                        e.preventDefault();
                        e.stopPropagation();
                        card.classList.remove('card-dragover');
                    });
                    card.addEventListener('drop', (e) => {
                        e.preventDefault();
                        e.stopPropagation();
                        card.classList.remove('card-dragover');
                        const file = e.dataTransfer && e.dataTransfer.files && e.dataTransfer.files[0];
                        if (file && file.type.startsWith('image/')) {
                            handleVillagePhotoUpload(v.id, file);
                        }
                    });
                }
            });
        }

        function openVillagePhotosModal() {
            const modal = document.getElementById('villagePhotosDialog');
            if (modal) {
                renderVillagePhotosGrid();
                try {
                    if (!modal.open) modal.showModal();
                } catch (e) {
                    modal.style.display = 'block';
                }
            }
        }

        // =========================================================================
        // VILLAGE VIEW INTERACTIONS & DRAG-AND-DROP ON MAP
        // =========================================================================

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
            const floatingBtn = document.getElementById('vChangePhotoFloatingBtn');
            const dropOverlay = document.getElementById('villageMapDropOverlay');
            const aerialOverlay = document.getElementById('villageAerialOverlay');

            // Close button (✕)
            if (cBtn && !cBtn._bound) {
                cBtn._bound = true;
                cBtn.onclick = (e) => {
                    e.stopPropagation();
                    if (typeof window.back === 'function') window.back();
                };
            }

            // Top Bar & Camera upload triggers
            if (uBtn && !uBtn._bound) {
                uBtn._bound = true;
                uBtn.onclick = (e) => {
                    e.stopPropagation();
                    const cur = window._currentVillageViewing;
                    triggerPhotoUpload(cur ? cur.id : 'pol-now');
                };
            }

            if (floatingBtn && !floatingBtn._bound) {
                floatingBtn._bound = true;
                floatingBtn.onclick = (e) => {
                    e.stopPropagation();
                    const cur = window._currentVillageViewing;
                    triggerPhotoUpload(cur ? cur.id : 'pol-now');
                };
            }

            // Zoom controls
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

            // Fit / Fill toggle
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

            // Sidebar fullscreen toggle
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

            // Drag and Pan interactions on viewport
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

            // HTML5 Drag and Drop of Image Files DIRECTLY ON THE MAP
            if (viewport && dropOverlay && !viewport._boundDrop) {
                viewport._boundDrop = true;

                viewport.addEventListener('dragover', (e) => {
                    e.preventDefault();
                    e.stopPropagation();
                    dropOverlay.classList.add('active');
                });

                viewport.addEventListener('dragleave', (e) => {
                    e.preventDefault();
                    e.stopPropagation();
                    if (!viewport.contains(e.relatedTarget)) {
                        dropOverlay.classList.remove('active');
                    }
                });

                viewport.addEventListener('drop', (e) => {
                    e.preventDefault();
                    e.stopPropagation();
                    dropOverlay.classList.remove('active');

                    const file = e.dataTransfer && e.dataTransfer.files && e.dataTransfer.files[0];
                    if (file && file.type.startsWith('image/')) {
                        const cur = window._currentVillageViewing;
                        if (cur) {
                            handleVillagePhotoUpload(cur.id, file);
                        } else {
                            openVillagePhotosModal();
                        }
                    }
                });
            }

            // POI delegation click handling
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

        function bindPhotosManagerEvents() {
            const openHeaderBtn = document.getElementById('openVillagePhotosBtn');
            const openTopBarBtn = document.getElementById('vOpenVillagePhotosModalBtn');
            const closeBtn = document.getElementById('closePhotosModalBtn');
            const doneBtn = document.getElementById('donePhotosModalBtn');
            const modal = document.getElementById('villagePhotosDialog');

            if (openHeaderBtn && !openHeaderBtn._bound) {
                openHeaderBtn._bound = true;
                openHeaderBtn.onclick = openVillagePhotosModal;
            }

            if (openTopBarBtn && !openTopBarBtn._bound) {
                openTopBarBtn._bound = true;
                openTopBarBtn.onclick = openVillagePhotosModal;
            }

            if (closeBtn && !closeBtn._bound) {
                closeBtn._bound = true;
                closeBtn.onclick = () => { if (modal) modal.close(); };
            }

            if (doneBtn && !doneBtn._bound) {
                doneBtn._bound = true;
                doneBtn.onclick = () => { if (modal) modal.close(); };
            }
        }

        // Global exports
        window.openVillagePhotosModal = openVillagePhotosModal;
        window.triggerPhotoUpload = triggerPhotoUpload;
        window.handleVillagePhotoUpload = handleVillagePhotoUpload;
        window.resetVillagePhoto = resetVillagePhoto;
        window.goToVillageFromModal = goToVillageFromModal;

        preloadAllVillagePhotos();
        document.addEventListener('DOMContentLoaded', () => {
            setupVillageInteractions();
            bindPhotosManagerEvents();
        });
        setTimeout(() => {
            setupVillageInteractions();
            bindPhotosManagerEvents();
        }, 150);
"""

html = html[:idx_start] + new_engine_code + "\n    " + html[idx_end:]
print("3. Replaced satellite & photo engine with bulletproof implementation!")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("SUCCESS: index.html updated successfully!")
