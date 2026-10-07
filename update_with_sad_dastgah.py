import json

with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

with open("sad_dastgah_code.txt", "r", encoding="utf-8") as f:
    sad_code = f.read().strip()

# 1. Insert sadDastgahStatsHtml right before darbandGharbiStatsHtml
marker = "const darbandGharbiStatsHtml = `"
idx_m = text.find(marker)
assert idx_m != -1, "darbandGharbiStatsHtml marker not found"
text = text[:idx_m] + sad_code + "\n\n            " + text[idx_m:]
print("1. Injected sadDastgahStatsHtml!")

# 2. Update getVillageAccordions to route 'sad-dastgah'
old_router = "else if (villageId === 'darband-gharbi') raw = darbandGharbiStatsHtml;"
new_router = """else if (villageId === 'darband-gharbi') raw = darbandGharbiStatsHtml;
                else if (villageId === 'sad-dastgah') raw = sadDastgahStatsHtml;"""
assert old_router in text, "old_router not found"
text = text.replace(old_router, new_router, 1)
print("2. Updated getVillageAccordions router for sad-dastgah!")

# 3. Update villageSchoolDatasets to include 'sad-dastgah'
old_vsd = "const villageSchoolDatasets = {"
new_vsd = """const villageSchoolDatasets = {
                'sad-dastgah': {
                    schoolName: 'دبستان علویه (۲۶۵) و متوسطه راهیان نور (۴۳۰)',
                    total: 695,
                    peak: 'پایه‌های چهارم و پنجم (۵۳ نفر)',
                    avg: '۴۴.۲ نفر در هر پایه دبستان',
                    grades: [
                        { label: 'پیش‌دبستانی', count: 0, pct: '۰٪', w: 2 },
                        { label: 'پایه اول', count: 49, pct: '۱۸.۵٪', w: 48 },
                        { label: 'پایه دوم', count: 38, pct: '۱۴.۳٪', w: 37 },
                        { label: 'پایه سوم', count: 40, pct: '۱۵.۱٪', w: 39 },
                        { label: 'پایه چهارم', count: 53, pct: '۲۰.۰٪', w: 52 },
                        { label: 'پایه پنجم', count: 53, pct: '۲۰.۰٪', w: 52 },
                        { label: 'پایه ششم', count: 32, pct: '۱۲.۱٪', w: 31 }
                    ]
                },"""
assert old_vsd in text, "old_vsd not found"
text = text.replace(old_vsd, new_vsd, 1)
print("3. Injected sad-dastgah into villageSchoolDatasets!")

# 4. Update villageDatabase['sad-dastgah'] with full rich profile
idx_vd_s = text.find("'sad-dastgah': {")
idx_vd_e = text.find("},\n                'darband-gharbi': {", idx_vd_s)
assert idx_vd_s != -1 and idx_vd_e != -1, "sad-dastgah in villageDatabase not found"

new_sad_vd = """'sad-dastgah': {
                    name: 'صد دستگاه',
                    corridor: 'بخش مرکزی · شهرستان خرمشهر · استان خوزستان',
                    coords: '30°27\\'05" N, 48°10\\'30" E',
                    borderDist: '۱۲.۰ کیلومتر',
                    cityDist: '۴.۰ کیلومتر',
                    area: '۲۸ هکتار',
                    priorityRank: 'اولویت ۴ از ۱۲ (کانون آموزشی)',
                    priorityClass: 'p-med',
                    priorityDesc: 'پوشش گسترده آموزشی با ۶۹۵ دانش‌آموز (دبستان علویه و متوسطه راهیان نور)، مسجد صاحب‌الزمان، ۲۱ خانوار کم‌برخوردار و ۳ یتیم تحت پوشش.',
                    pop: '۸۸۲',
                    popSub: '۲۱۱ خانوار · بعد خانوار: ۴.۱۸ نفر',
                    fam: '۲۱۱',
                    famSub: '۲۱ خانوار کم‌برخوردار تحت پوشش',
                    disabled: '۲۴',
                    disabledSub: '۳ یتیم و ۲۱ خانوار کم‌برخوردار',
                    emp: 'طرح فعال',
                    empSub: 'کارآفرینی و مشاغل خرد',
                    agePyramid: [
                        { label: 'دانش‌آموزان و کودکان', percent: '۳۸٪', count: '۳۳۵ نفر' },
                        { label: 'سنین فعالیت و اشتغال', percent: '۴۸٪', count: '۴۲۳ نفر' },
                        { label: 'سالمندان و بازنشستگان', percent: '۱۴٪', count: '۱۲۴ نفر' }
                    ],
                    disabilities: [
                        { label: 'ایتام و دانشجویان نیازمند', count: '۳ نفر', percent: '۱۲٪' },
                        { label: 'سرپرستان کم‌برخوردار', count: '۲۱ نفر', percent: '۸۸٪' }
                    ],
                    indicators: [
                        { title: 'پوشش آموزشی و فضاهای تحصیلی', percent: 96, percentFa: '۹۶٪', status: '۶۹۵ دانش‌آموز فعال', statusCls: 'status-excellent', fillCls: 'fill-emerald', desc: 'دبستان علویه (۲۶۵ دانش‌آموز) و متوسطه راهیان نور (۴۳۰ دانش‌آموز) با پوشش آموزشی گسترده منطقه' },
                        { title: 'اماکن مذهبی و فرهنگی', percent: 85, percentFa: '۸۵٪', status: 'مسجد صاحب‌الزمان', statusCls: 'status-excellent', fillCls: 'fill-emerald', desc: 'مسجد صاحب‌الزمان کانون فعالیت‌های فرهنگی، مذهبی و توزیع بسته‌های معیشتی محله' },
                        { title: 'حمایت از ایتام و محصلین نیازمند', percent: 80, percentFa: '۸۰٪', status: '۳ پرونده دانشجویی/دانش‌آموزی', statusCls: 'status-good', fillCls: 'fill-gold', desc: '۳ یتیم شامل ۱ دانشجو و ۲ دانش‌آموز دبیرستانی با شناسنامه کامل معیشتی و تحصیلی' },
                        { title: 'رسیدگی به خانوارهای کم‌برخوردار', percent: 76, percentFa: '۷۶٪', status: '۲۱ خانوار شناسایی‌شده', statusCls: 'status-warning', fillCls: 'fill-amber', desc: '۲۱ خانوار کم‌برخوردار ممیزی‌شده با ثبت دقیق کدملی، کروکی نشانی و شماره تماس' },
                        { title: 'پایداری شبکه آب و خدمات شهری', percent: 75, percentFa: '۷۵٪', status: 'شبکه شهری خرمشهر', statusCls: 'status-good', fillCls: 'fill-emerald', desc: 'اتصال به شبکه شهری و منازل اداره بندر؛ نیازمند بازسازی شبکه داخلی' }
                    ]
                """

text = text[:idx_vd_s] + new_sad_vd + text[idx_vd_e:]
print("4. Updated villageDatabase for sad-dastgah!")

# 5. Update villages pin data for sad-dastgah
old_pin = "{ id: 'sad-dastgah', name: 'صد دستگاه', cat: 'village', x: 0.822, y: 0.888, data: { pop: '۱,۱۲۰', fam: '۲۶۰', stats: [['خانوار', 260], ['جمعیت', '۱,۱۲۰ نفر'], ['دانش‌آموزان', 115], ['ایتام', 3], ['کم‌برخوردار', 14], ['پوشش حمایتی', 'فعال']] } }"
new_pin = "{ id: 'sad-dastgah', name: 'صد دستگاه', cat: 'village', x: 0.822, y: 0.888, data: { pop: '۸۸۲', fam: '۲۱۱', stats: [['خانوار', 211], ['جمعیت', '۸۸۲ نفر'], ['دانش‌آموزان', 695], ['ایتام', 3], ['کم‌برخوردار', 21], ['مدرسه', '۲ مرکز']] } }"
assert old_pin in text, "old_pin not found"
text = text.replace(old_pin, new_pin, 1)
print("5. Updated sad-dastgah pin stats in villages!")

# 6. Update regionalDialog summary table for sad-dastgah
old_reg_row = '<tr><td style="padding:9px 14px;">۸</td><td style="padding:9px 14px; font-weight:800; color:#142a29;">صد دستگاه</td><td style="padding:9px 14px;">حومه شرقی</td><td style="padding:9px 14px; font-weight:700;">۲,۵۰۰ نفر</td><td style="padding:9px 14px;">۶۱۰</td><td style="padding:9px 14px;">۱ دبستان</td><td style="padding:9px 14px; color:#64748b;">تحت ارزیابی اولیه</td></tr>'
new_reg_row = '<tr><td style="padding:9px 14px;">۸</td><td style="padding:9px 14px; font-weight:800; color:#142a29;">صد دستگاه</td><td style="padding:9px 14px;">بخش مرکزی</td><td style="padding:9px 14px; font-weight:700;">۸۸۲ نفر</td><td style="padding:9px 14px;">۲۱۱</td><td style="padding:9px 14px;">۲ مدرسه (علویه و راهیان نور با ۶۹۵ دانش‌آموز)</td><td style="padding:9px 14px; font-weight:800; color:#b45309;">۲۴ پرونده (۳ یتیم + ۲۱ مددجو)</td></tr>'
assert old_reg_row in text, "old_reg_row not found"
text = text.replace(old_reg_row, new_reg_row, 1)
print("6. Updated regionalDialog table row for sad-dastgah!")

# 7. Update villageIndicators
old_vi_sad = "'sad-dastgah': ['with-schools', 'high-pop', 'high-vuln', 'employment'],"
new_vi_sad = "'sad-dastgah': ['with-schools', 'with-dossier', 'high-vuln', 'employment'],"
assert old_vi_sad in text, "old_vi_sad not found"
text = text.replace(old_vi_sad, new_vi_sad, 1)
print("7. Updated villageIndicators for sad-dastgah (added with-dossier)!")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(text)

print("SUCCESS: Stage 1 of sad-dastgah integration complete!")
