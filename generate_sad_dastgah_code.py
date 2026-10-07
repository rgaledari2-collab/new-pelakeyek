import json

orphans_data = [
    {
        "row": 1,
        "guardian": "صدیقه زباری",
        "guardian_nid": "181621234",
        "name": "دنیا",
        "family": "عریضاوی",
        "father": "هاشم",
        "nid": "1820612635",
        "age": "۱۹",
        "edu": "دانشجو",
        "school": "دانشگاه",
        "health": "سالم",
        "address": "صد دستگاه – منازل بندر - ردیف ۴ – پلاک ۱۰",
        "phone": "09356466599"
    },
    {
        "row": 2,
        "guardian": "سمیه سلیمانی",
        "guardian_nid": "1090318480",
        "name": "مرام",
        "family": "طیبی",
        "father": "احمد",
        "nid": "1820699374",
        "age": "۱۷",
        "edu": "یازدهم",
        "school": "شهدای شمخانی",
        "health": "سالم",
        "address": "صد دستگاه – پشت مدرسه راهیان نور – پلاک ۱",
        "phone": "09307879842"
    },
    {
        "row": 3,
        "guardian": "ملکه عنبی (عمه)",
        "guardian_nid": "1820514536",
        "name": "رسول",
        "family": "عنبی",
        "father": "جاسم",
        "nid": "1811448712",
        "age": "۱۷",
        "edu": "دهم",
        "school": "شهر",
        "health": "سالم",
        "address": "صد دستگاه – منازل اداره بندر – پلاک ۹",
        "phone": "09165764199 - 09168107791"
    }
]

needy_data = [
    {"row": 1, "name": "مریم غزلاوی", "nid": "1829485121", "phone": "0904467549", "address": "صد دستگاه"},
    {"row": 2, "name": "علی محمدی هلالیان", "nid": "1820064433", "phone": "09386590917", "address": "صد دستگاه"},
    {"row": 3, "name": "نرگس سلمانیان اصل", "nid": "1829411081", "phone": "09045133785", "address": "صد دستگاه"},
    {"row": 4, "name": "سید هاشم مفتی عریض", "nid": "1829654187", "phone": "09375385289", "address": "صد دستگاه"},
    {"row": 5, "name": "حلیمه سلیمانی", "nid": "1820089150", "phone": "09026844921", "address": "صد دستگاه"},
    {"row": 6, "name": "زهرا عسکری", "nid": "1820264580", "phone": "09166339881", "address": "صد دستگاه"},
    {"row": 7, "name": "فروغ عباسیان پور", "nid": "1820688755", "phone": "09034148587", "address": "صد دستگاه"},
    {"row": 8, "name": "سیده کوثر موسوی", "nid": "1940720079", "phone": "09051806711", "address": "صد دستگاه"},
    {"row": 9, "name": "سکینه محمودپور عریض", "nid": "6629861752", "phone": "09036802641", "address": "صد دستگاه"},
    {"row": 10, "name": "علی عباسی کیان", "nid": "1820412326", "phone": "09335463899", "address": "صد دستگاه"},
    {"row": 11, "name": "مرضیه کاشفی سمن", "nid": "3979851109", "phone": "09166331644", "address": "صد دستگاه"},
    {"row": 12, "name": "حسین محمدی اطهر", "nid": "7060016643", "phone": "09169538116", "address": "صد دستگاه"},
    {"row": 13, "name": "محمد مجیل", "nid": "1755060106", "phone": "09368915693", "address": "صد دستگاه"},
    {"row": 14, "name": "ایمان خواجه", "nid": "1820140075", "phone": "0905876667", "address": "صد دستگاه"},
    {"row": 15, "name": "رقیه فیسلی", "nid": "1829962981", "phone": "09023558943", "address": "صد دستگاه"},
    {"row": 16, "name": "عماد فتیلی", "nid": "1820728528", "phone": "09398034496", "address": "صد دستگاه"},
    {"row": 17, "name": "زینب عبادی نژاد", "nid": "1820833054", "phone": "09371679793", "address": "صد دستگاه"},
    {"row": 18, "name": "قدیمه سلیمانی", "nid": "1751976548", "phone": "09388673788", "address": "صد دستگاه"},
    {"row": 19, "name": "حیات جاسم پور بغلانی", "nid": "1818621029", "phone": "09024190333", "address": "صد دستگاه"},
    {"row": 20, "name": "مریم علقمی زاده", "nid": "1829632145", "phone": "09361394346", "address": "صد دستگاه"},
    {"row": 21, "name": "راضیه دریس", "nid": "1828064785", "phone": "09308743894", "address": "صد دستگاه"}
]

# Build HTML accordions
html = """const sadDastgahStatsHtml = `<div class="dos-content-grid" id="stats-content">
    <!-- جدول ۱: تقسیمات و مشخصات عمومی صد دستگاه -->
    <div style="margin-bottom: 12px;">
        <details class="dos-accordion">
            <summary class="dos-accordion-header">
                <div style="display:flex; align-items:center; gap:10px; flex-wrap:wrap;">
                    <h2 class="dos-section-title" style="margin:0; font-size:13.5px; font-weight:800;">
                        <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:middle; color:var(--brand-clay);"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
                        تقسیمات، موقعیت جغرافیایی و جمعیت صد دستگاه
                    </h2>
                    <span style="font-size:11px; background:#eff6ff; color:#1d4ed8; padding:2px 8px; border-radius:12px; font-weight:700;">۸۸۲ نفر · ۲۱۱ خانوار</span>
                </div>
                <div style="display:flex; align-items:center; gap:10px;">
                    <span class="dos-accordion-hint">کلیک جهت مشاهده جزئیات</span>
                    <span class="dos-accordion-chevron">▾</span>
                </div>
            </summary>
            <div class="dos-accordion-body" style="padding-top:14px;">
                <table class="dos-table" style="width:100%; border-collapse:collapse; margin-bottom:12px;">
                    <thead>
                        <tr style="background:#f1eee7; color:var(--ink);">
                            <th>شاخص</th>
                            <th>مقدار مستند</th>
                            <th>شاخص</th>
                            <th>مقدار مستند</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td style="font-weight:800;">بخش</td>
                            <td>مرکزی</td>
                            <td style="font-weight:800;">طول جغرافیایی</td>
                            <td style="direction:ltr; text-align:right;">48°10'30" E</td>
                        </tr>
                        <tr>
                            <td style="font-weight:800;">شهرستان</td>
                            <td>خرمشهر</td>
                            <td style="font-weight:800;">عرض جغرافیایی</td>
                            <td style="direction:ltr; text-align:right;">30°27'05" N</td>
                        </tr>
                        <tr>
                            <td style="font-weight:800;">استان</td>
                            <td>خوزستان</td>
                            <td style="font-weight:800;">بُعد خانوار</td>
                            <td>۴.۱۸ نفر</td>
                        </tr>
                        <tr>
                            <td style="font-weight:800;">جمعیت کل</td>
                            <td style="font-weight:900; color:#15803d;">۸۸۲ نفر</td>
                            <td style="font-weight:800;">تعداد خانوار</td>
                            <td style="font-weight:900; color:#b45309;">۲۱۱ خانوار</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </details>
    </div>

    <!-- جدول ۲: زیرساخت‌های صد دستگاه -->
    <div style="margin-bottom: 12px;">
        <details class="dos-accordion">
            <summary class="dos-accordion-header">
                <div style="display:flex; align-items:center; gap:10px; flex-wrap:wrap;">
                    <h2 class="dos-section-title" style="margin:0; font-size:13.5px; font-weight:800;">
                        <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:middle; color:var(--brand-clay);"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
                        زیرساخت‌ها و اماکن مهم صد دستگاه
                    </h2>
                    <span style="font-size:11px; background:#f0fdf4; color:#15803d; padding:2px 8px; border-radius:12px; font-weight:700;">۲ کانون فعال</span>
                </div>
                <div style="display:flex; align-items:center; gap:10px;">
                    <span class="dos-accordion-hint">کلیک جهت مشاهده</span>
                    <span class="dos-accordion-chevron">▾</span>
                </div>
            </summary>
            <div class="dos-accordion-body" style="padding-top:14px;">
                <table class="dos-table" style="width:100%; border-collapse:collapse;">
                    <thead>
                        <tr style="background:#f1eee7; color:var(--ink);">
                            <th style="width:60px;">ردیف</th>
                            <th>عنوان زیرساخت</th>
                            <th>متراژ / مشخصات</th>
                            <th>آمار و وضعیت</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>۱</td>
                            <td style="font-weight:800;">مسجد صاحب‌الزمان</td>
                            <td>کانون فرهنگی، مذهبی و محرومیت‌زدایی محله</td>
                            <td><span style="color:#15803d; font-weight:800;">فعال</span></td>
                        </tr>
                        <tr>
                            <td>۲</td>
                            <td style="font-weight:800;">مدرسه علویه - راهیان نور</td>
                            <td>مجتمع آموزشی ۲ مقطعی (ابتدایی و متوسطه اول)</td>
                            <td style="font-weight:800; color:#b45309;">۶۹۵ دانش‌آموز</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </details>
    </div>

    <!-- جدول ۳: مدارس و دانش‌آموزان صد دستگاه -->
    <div style="margin-bottom: 12px;">
        <details class="dos-accordion">
            <summary class="dos-accordion-header">
                <div style="display:flex; align-items:center; gap:10px; flex-wrap:wrap;">
                    <h2 class="dos-section-title" style="margin:0; font-size:13.5px; font-weight:800;">
                        <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:middle; color:var(--brand-clay);"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>
                        دانش‌آموزان مدارس صد دستگاه (۶۹۵ نفر)
                    </h2>
                    <span style="font-size:11px; background:#fef3c7; color:#b45309; padding:2px 8px; border-radius:12px; font-weight:700;">۲ مرکز آموزشی</span>
                </div>
                <div style="display:flex; align-items:center; gap:10px;">
                    <span class="dos-accordion-hint">کلیک جهت مشاهده تفکیک مقاطع</span>
                    <span class="dos-accordion-chevron">▾</span>
                </div>
            </summary>
            <div class="dos-accordion-body" style="padding-top:14px;">
                <table class="dos-table" style="width:100%; border-collapse:collapse;">
                    <thead>
                        <tr style="background:#f1eee7; color:var(--ink);">
                            <th>نام مدرسه</th>
                            <th>پیش‌دبستانی</th>
                            <th>پایه اول</th>
                            <th>پایه دوم</th>
                            <th>پایه سوم</th>
                            <th>پایه چهارم</th>
                            <th>پایه پنجم</th>
                            <th>پایه ششم</th>
                            <th>جمع</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td style="font-weight:800;">دبستان علویه</td>
                            <td>—</td>
                            <td>۴۹</td>
                            <td>۳۸</td>
                            <td>۴۰</td>
                            <td>۵۳</td>
                            <td>۵۳</td>
                            <td>۳۲</td>
                            <td style="font-weight:900; color:#15803d;">۲۶۵</td>
                        </tr>
                        <tr>
                            <td style="font-weight:800;">متوسطه اول - راهیان نور</td>
                            <td colspan="7" style="text-align:center; color:#64748b;">مقطع متوسطه اول فعال</td>
                            <td style="font-weight:900; color:#b45309;">۴۳۰</td>
                        </tr>
                        <tr style="background:#faf5eb; font-weight:900;">
                            <td colspan="8" style="text-align:right;">مجموع کل دانش‌آموزان صد دستگاه</td>
                            <td style="color:#b91c1c; font-size:14px;">۶۹۵</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </details>
    </div>

    <!-- جدول ۴: لیست ایتام صد دستگاه -->
    <div style="margin-bottom: 12px;">
        <details class="dos-accordion">
            <summary class="dos-accordion-header">
                <div style="display:flex; align-items:center; gap:10px; flex-wrap:wrap;">
                    <h2 class="dos-section-title" style="margin:0; font-size:13.5px; font-weight:800;">
                        <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:middle; color:var(--brand-clay);"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>
                        لیست ایتام صد دستگاه (۳ پرونده مستند)
                    </h2>
                    <span style="font-size:11px; background:#fee2e2; color:#b91c1c; padding:2px 8px; border-radius:12px; font-weight:700;">۳ نفر تحت حمایت</span>
                </div>
                <div style="display:flex; align-items:center; gap:10px;">
                    <span class="dos-accordion-hint">کلیک جهت مشاهده سطرها</span>
                    <span class="dos-accordion-chevron">▾</span>
                </div>
            </summary>
            <div class="dos-accordion-body" style="padding-top:14px;">
                <table class="dos-table" style="width:100%; border-collapse:collapse;">
                    <thead>
                        <tr style="background:#f1eee7; color:var(--ink);">
                            <th style="width:40px;">ردیف</th>
                            <th>نام سرپرست</th>
                            <th>کد ملی سرپرست</th>
                            <th>نام و خانوادگی یتیم</th>
                            <th>نام پدر</th>
                            <th>کد ملی یتیم</th>
                            <th>سن</th>
                            <th>تحصیلات</th>
                            <th>مدرسه</th>
                            <th>آدرس</th>
                            <th>شماره تماس</th>
                        </tr>
                    </thead>
                    <tbody>
"""

for o in orphans_data:
    full_name = f"{o['name']} {o['family']}"
    html += f"""                        <tr class="dos-row-orphan" data-guardian="{o['guardian']}" data-national-id="{o['nid']}" data-phone="{o['phone']}" data-address="{o['address']}" data-village="صد دستگاه" style="cursor:pointer;" title="کلیک جهت مشاهده شناسنامه پرونده">
                            <td>{o['row']}</td>
                            <td style="font-weight:700;">{o['guardian']}</td>
                            <td style="font-family:monospace; font-size:11.5px;">{o['guardian_nid']}</td>
                            <td style="font-weight:800; color:#142a29;"><span style="color:#b45309; text-decoration:underline;">{full_name}</span></td>
                            <td>{o['father']}</td>
                            <td style="font-family:monospace; font-size:11.5px; font-weight:700;">{o['nid']}</td>
                            <td>{o['age']}</td>
                            <td>{o['edu']}</td>
                            <td>{o['school']}</td>
                            <td style="font-size:11px; max-width:180px;">{o['address']}</td>
                            <td style="direction:ltr; text-align:right; font-family:monospace; font-size:11.5px;">{o['phone']}</td>
                        </tr>
"""

html += """                    </tbody>
                </table>
            </div>
        </details>
    </div>

    <!-- جدول ۵: خانوارهای کم‌برخوردار صد دستگاه -->
    <div style="margin-bottom: 12px;">
        <details class="dos-accordion">
            <summary class="dos-accordion-header">
                <div style="display:flex; align-items:center; gap:10px; flex-wrap:wrap;">
                    <h2 class="dos-section-title" style="margin:0; font-size:13.5px; font-weight:800;">
                        <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:middle; color:var(--brand-clay);"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
                        خانوارهای کم‌برخوردار صد دستگاه (۲۱ پرونده مستند)
                    </h2>
                    <span style="font-size:11px; background:#fef3c7; color:#b45309; padding:2px 8px; border-radius:12px; font-weight:700;">۲۱ خانوار ممیزی‌شده</span>
                </div>
                <div style="display:flex; align-items:center; gap:10px;">
                    <span class="dos-accordion-hint">کلیک جهت مشاهده سطرها</span>
                    <span class="dos-accordion-chevron">▾</span>
                </div>
            </summary>
            <div class="dos-accordion-body" style="padding-top:14px;">
                <table class="dos-table" style="width:100%; border-collapse:collapse;">
                    <thead>
                        <tr style="background:#f1eee7; color:var(--ink);">
                            <th style="width:40px;">ردیف</th>
                            <th>نام و نام خانوادگی</th>
                            <th>کد ملی</th>
                            <th>شماره تماس</th>
                            <th>آدرس</th>
                        </tr>
                    </thead>
                    <tbody>
"""

for n in needy_data:
    html += f"""                        <tr class="dos-row-needy" data-guardian="سرپرست خانوار" data-national-id="{n['nid']}" data-phone="{n['phone']}" data-address="{n['address']}" data-village="صد دستگاه" style="cursor:pointer;" title="کلیک جهت مشاهده شناسنامه پرونده">
                            <td>{n['row']}</td>
                            <td style="font-weight:800; color:#142a29;"><span style="color:#15803d; text-decoration:underline;">{n['name']}</span></td>
                            <td style="font-family:monospace; font-size:12px; font-weight:700;">{n['nid']}</td>
                            <td style="direction:ltr; text-align:right; font-family:monospace; font-size:12px;">{n['phone']}</td>
                            <td>{n['address']}</td>
                        </tr>
"""

html += """                    </tbody>
                </table>
            </div>
        </details>
    </div>
</div>`;
"""

with open("sad_dastgah_code.txt", "w", encoding="utf-8") as f:
    f.write(html)

print("Generated sadDastgahStatsHtml successfully!")
