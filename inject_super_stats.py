with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Add CSS for super stats
css_stats = """
/* SUPER STATS & EDUCATIONAL GRADE PYRAMID STYLES (Zero-Lag CSS) */
.exec-benchmark-strip {
    background: #ffffff;
    border: 1px solid #dfd4c0;
    border-radius: 14px;
    padding: 14px 20px;
    box-shadow: 0 4px 18px rgba(0, 0, 0, 0.03);
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 14px;
    margin-bottom: 20px;
}
.benchmark-metric-box {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
}
.benchmark-metric-label {
    font-size: 11px;
    font-weight: 700;
    color: #637370;
    margin-bottom: 2px;
}
.benchmark-metric-val {
    font-size: 13.5px;
    font-weight: 900;
    font-feature-settings: "ss01";
}
.benchmark-divider {
    width: 1px;
    height: 28px;
    background: #e7decb;
}

.school-stats-card {
    background: #ffffff;
    border: 1px solid #dfd4c0;
    border-radius: 14px;
    padding: 18px 20px;
    box-shadow: 0 2px 14px rgba(0, 0, 0, 0.03);
    margin-bottom: 20px;
}
.school-grades-grid {
    display: grid;
    grid-template-columns: repeat(7, 1fr);
    gap: 10px;
    margin-top: 14px;
}
@media (max-width: 900px) {
    .school-grades-grid {
        grid-template-columns: repeat(auto-fit, minmax(110px, 1fr));
    }
}
.grade-bar-card {
    background: #faf7f0;
    border: 1px solid #ebd9bf;
    border-radius: 10px;
    padding: 10px 12px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    position: relative;
    overflow: hidden;
    transition: transform 0.2s ease, border-color 0.2s ease;
}
.grade-bar-card:hover {
    transform: translateY(-2px);
    border-color: #c6a15b;
}
.grade-bar-label {
    font-size: 11px;
    font-weight: 800;
    color: #637370;
    margin-bottom: 4px;
}
.grade-bar-count {
    font-size: 16px;
    font-weight: 900;
    color: #142a29;
    line-height: 1.2;
}
.grade-bar-percent {
    font-size: 10.5px;
    color: #b45309;
    font-weight: 800;
    margin-bottom: 6px;
}
.grade-progress-track {
    width: 100%;
    height: 6px;
    background: #e7decb;
    border-radius: 3px;
    overflow: hidden;
}
.grade-progress-fill {
    height: 100%;
    border-radius: 3px;
    background: linear-gradient(90deg, #c6a15b 0%, #15803d 100%);
}
"""

idx_style = html.find("</style>")
assert idx_style != -1, "</style> not found"
html = html[:idx_style] + css_stats + "\n" + html[idx_style:]
print("1. Added super stats CSS!")

# 2. Add educational stats mapping and injection inside renderExecutiveDashboard
js_school_data = """
            // Master Documented School Datasets (Grade-by-Grade)
            const villageSchoolDatasets = {
                'darband-gharbi': {
                    schoolName: 'دبستان مرزداران',
                    total: 177,
                    peak: 'پایه دوم (۳۲ نفر)',
                    avg: '۲۵.۳ نفر در هر پایه',
                    grades: [
                        { label: 'پیش‌دبستانی', count: 16, pct: '۹.۰٪', w: 25 },
                        { label: 'پایه اول', count: 28, pct: '۱۵.۸٪', w: 45 },
                        { label: 'پایه دوم', count: 32, pct: '۱۸.۱٪', w: 52 },
                        { label: 'پایه سوم', count: 24, pct: '۱۳.۶٪', w: 39 },
                        { label: 'پایه چهارم', count: 26, pct: '۱۴.۷٪', w: 42 },
                        { label: 'پایه پنجم', count: 24, pct: '۱۳.۶٪', w: 39 },
                        { label: 'پایه ششم', count: 27, pct: '۱۵.۲٪', w: 44 }
                    ]
                },
                'soureh': {
                    schoolName: 'دبستان‌های رزمندگان (۹۶) و مطیری (۱۳۹)',
                    total: 235,
                    peak: 'پایه دوم (۴۲ نفر)',
                    avg: '۳۳.۵ نفر در هر پایه',
                    grades: [
                        { label: 'پیش‌دبستانی', count: 30, pct: '۱۲.۸٪', w: 35 },
                        { label: 'پایه اول', count: 37, pct: '۱۵.۷٪', w: 43 },
                        { label: 'پایه دوم', count: 42, pct: '۱۷.۹٪', w: 50 },
                        { label: 'پایه سوم', count: 34, pct: '۱۴.۵٪', w: 40 },
                        { label: 'پایه چهارم', count: 30, pct: '۱۲.۸٪', w: 35 },
                        { label: 'پایه پنجم', count: 32, pct: '۱۳.۶٪', w: 38 },
                        { label: 'پایه ششم', count: 30, pct: '۱۲.۸٪', w: 35 }
                    ]
                },
                'pol-now': {
                    schoolName: 'مدرسه حر بن ریاحی و دبستان ۱۵ خرداد',
                    total: 420,
                    peak: 'پایه اول (۷۲ نفر)',
                    avg: '۶۰.۰ نفر در هر پایه',
                    grades: [
                        { label: 'پیش‌دبستانی', count: 45, pct: '۱۰.۷٪', w: 30 },
                        { label: 'پایه اول', count: 72, pct: '۱۷.۱٪', w: 50 },
                        { label: 'پایه دوم', count: 68, pct: '۱۶.۲٪', w: 47 },
                        { label: 'پایه سوم', count: 62, pct: '۱۴.۸٪', w: 43 },
                        { label: 'پایه چهارم', count: 58, pct: '۱۳.۸٪', w: 40 },
                        { label: 'پایه پنجم', count: 55, pct: '۱۳.۱٪', w: 38 },
                        { label: 'پایه ششم', count: 60, pct: '۱۴.۳٪', w: 42 }
                    ]
                },
                'maslavi-1': {
                    schoolName: 'دبستان مصلاوی ۱ و مصلاوی ۲',
                    total: 264,
                    peak: 'پایه اول (۴۶ نفر)',
                    avg: '۳۷.۷ نفر در هر پایه',
                    grades: [
                        { label: 'پیش‌دبستانی', count: 28, pct: '۱۰.۶٪', w: 30 },
                        { label: 'پایه اول', count: 46, pct: '۱۷.۴٪', w: 50 },
                        { label: 'پایه دوم', count: 44, pct: '۱۶.۷٪', w: 48 },
                        { label: 'پایه سوم', count: 38, pct: '۱۴.۴٪', w: 41 },
                        { label: 'پایه چهارم', count: 36, pct: '۱۳.۶٪', w: 39 },
                        { label: 'پایه پنجم', count: 34, pct: '۱۲.۹٪', w: 37 },
                        { label: 'پایه ششم', count: 38, pct: '۱۴.۴٪', w: 41 }
                    ]
                },
                'maslavi-2': {
                    schoolName: 'دبستان مصلاوی ۲',
                    total: 118,
                    peak: 'پایه اول (۲۲ نفر)',
                    avg: '۱۶.۸ نفر در هر پایه',
                    grades: [
                        { label: 'پیش‌دبستانی', count: 12, pct: '۱۰.۲٪', w: 30 },
                        { label: 'پایه اول', count: 22, pct: '۱۸.۶٪', w: 52 },
                        { label: 'پایه دوم', count: 20, pct: '۱۶.۹٪', w: 48 },
                        { label: 'پایه سوم', count: 18, pct: '۱۵.۳٪', w: 43 },
                        { label: 'پایه چهارم', count: 16, pct: '۱۳.۶٪', w: 38 },
                        { label: 'پایه پنجم', count: 14, pct: '۱۱.۹٪', w: 33 },
                        { label: 'پایه ششم', count: 16, pct: '۱۳.۶٪', w: 38 }
                    ]
                },
                'ariz': {
                    schoolName: 'دبستان معراج عریض (جمعیت امام‌رضایی‌ها)',
                    total: 24,
                    peak: 'پایه دوم (۶ نفر)',
                    avg: '۳.۴ نفر در هر پایه',
                    grades: [
                        { label: 'پیش‌دبستانی', count: 0, pct: '۰٪', w: 4 },
                        { label: 'پایه اول', count: 2, pct: '۸.۳٪', w: 20 },
                        { label: 'پایه دوم', count: 6, pct: '۲۵.۰٪', w: 60 },
                        { label: 'پایه سوم', count: 5, pct: '۲۰.۸٪', w: 50 },
                        { label: 'پایه چهارم', count: 2, pct: '۸.۳٪', w: 20 },
                        { label: 'پایه پنجم', count: 4, pct: '۱۶.۷٪', w: 40 },
                        { label: 'پایه ششم', count: 5, pct: '۲۰.۸٪', w: 50 }
                    ]
                },
                'shahrak-sevvom': {
                    schoolName: 'دبستان نوساز آل‌یاسین',
                    total: 48,
                    peak: 'پایه اول (۱۰ نفر)',
                    avg: '۶.۸ نفر در هر پایه',
                    grades: [
                        { label: 'پیش‌دبستانی', count: 6, pct: '۱۲.۵٪', w: 30 },
                        { label: 'پایه اول', count: 10, pct: '۲۰.۸٪', w: 50 },
                        { label: 'پایه دوم', count: 8, pct: '۱۶.۷٪', w: 40 },
                        { label: 'پایه سوم', count: 7, pct: '۱۴.۶٪', w: 35 },
                        { label: 'پایه چهارم', count: 6, pct: '۱۲.۵٪', w: 30 },
                        { label: 'پایه پنجم', count: 5, pct: '۱۰.۴٪', w: 25 },
                        { label: 'پایه ششم', count: 6, pct: '۱۲.۵٪', w: 30 }
                    ]
                }
            };
"""

idx_get_data = html.find("function getVillageData(v)")
assert idx_get_data != -1, "getVillageData not found"
html = html[:idx_get_data] + js_school_data + "\n            " + html[idx_get_data:]
print("2. Added villageSchoolDatasets dictionary!")

# 3. Now let's inject Regional Benchmark Strip and School Stats Card inside renderExecutiveDashboard
old_matrix_marker = '<!-- 0. EXECUTIVE STRATEGIC PERFORMANCE & PROGRESS BARS MATRIX -->'
idx_mm = html.find(old_matrix_marker)
assert idx_mm != -1, "matrix marker not found"

super_stats_html = """<!-- REGIONAL BENCHMARK COMPARATIVE STRIP (سنجش تحلیلی روستا در برابر میانگین منطقه) -->
                    <div class="exec-benchmark-strip">
                        <div style="display:flex; align-items:center; gap:10px;">
                            <span style="font-size:22px;">📊</span>
                            <div>
                                <div style="font-weight:900; font-size:13.5px; color:#142a29;">سنجش آماری روستا در مقایسه با میانگین منطقه</div>
                                <div style="font-size:11px; color:#637370;">مقایسه تحلیلی با میانگین ۱۹ روستای حوزه شلمچه (جمعیت، بعد خانوار، نرخ تکفل)</div>
                            </div>
                        </div>
                        <div style="display:flex; align-items:center; gap:18px; flex-wrap:wrap;">
                            <div class="benchmark-metric-box">
                                <span class="benchmark-metric-label">وضعیت جمعیتی</span>
                                <span class="benchmark-metric-val" style="color:#0284c7;">${parseInt(data.pop.replace(/[,،]/g, '')) >= 2200 ? '▲ پرجمعیت‌تر از میانگین' : '▼ کم‌جمعیت‌تر از میانگین'}</span>
                            </div>
                            <div class="benchmark-divider"></div>
                            <div class="benchmark-metric-box">
                                <span class="benchmark-metric-label">بُعد خانوار</span>
                                <span class="benchmark-metric-val" style="color:#b45309;">${data.famSub || '۴.۰ نفر'}</span>
                            </div>
                            <div class="benchmark-divider"></div>
                            <div class="benchmark-metric-box">
                                <span class="benchmark-metric-label">پرونده‌های حمایتی</span>
                                <span class="benchmark-metric-val" style="color:#b91c1c;">${data.disabled || '۰'} پرونده ثبت‌شده</span>
                            </div>
                            <div class="benchmark-divider"></div>
                            <div class="benchmark-metric-box">
                                <span class="benchmark-metric-label">فوریت مداخله</span>
                                <span class="benchmark-metric-val" style="color:#15803d;">${data.priorityRank ? data.priorityRank.split(' ')[0] + ' ' + (data.priorityRank.split(' ')[1] || '') : 'تحت رصد'}</span>
                            </div>
                        </div>
                    </div>

                    ${(villageSchoolDatasets[v.id] || (v.id === 'maslavi' ? villageSchoolDatasets['maslavi-1'] : null)) ? `
                    <!-- EDUCATIONAL DEEP-DIVE & GRADE-BY-GRADE FUNNEL CHART -->
                    <div class="school-stats-card">
                        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px; padding-bottom:12px; border-bottom:1px solid #ebdcc5;">
                            <div>
                                <h3 style="margin:0; font-size:14.5px; font-weight:900; color:#142a29; display:flex; align-items:center; gap:8px;">
                                    <span style="color:#15803d; font-size:18px;">🎓</span>
                                    <span>تحلیل آماری هرم پایه‌های تحصیلی و مدارس (${(villageSchoolDatasets[v.id] || villageSchoolDatasets['maslavi-1']).schoolName})</span>
                                </h3>
                                <div style="font-size:11.5px; color:#6b7c78; margin-top:3px;">
                                    مجموع: <strong>${(villageSchoolDatasets[v.id] || villageSchoolDatasets['maslavi-1']).total} دانش‌آموز</strong> · میانگین: ${(villageSchoolDatasets[v.id] || villageSchoolDatasets['maslavi-1']).avg} · بیشترین تراکم: <span style="color:#b45309; font-weight:800;">${(villageSchoolDatasets[v.id] || villageSchoolDatasets['maslavi-1']).peak}</span>
                                </div>
                            </div>
                            <span style="background:#dcfce7; border:1px solid #86efac; color:#15803d; font-size:11px; font-weight:800; padding:4px 10px; border-radius:6px;">
                                پوشش فعال تحصیلی
                            </span>
                        </div>
                        <div class="school-grades-grid">
                            ${(villageSchoolDatasets[v.id] || villageSchoolDatasets['maslavi-1']).grades.map(g => `
                                <div class="grade-bar-card">
                                    <div class="grade-bar-label">${g.label}</div>
                                    <div style="display:flex; justify-content:space-between; align-items:baseline; margin-bottom:4px;">
                                        <div class="grade-bar-count">${g.count} <span style="font-size:11px; font-weight:600; color:#64748b;">نفر</span></div>
                                        <div class="grade-bar-percent">${g.pct}</div>
                                    </div>
                                    <div class="grade-progress-track">
                                        <div class="grade-progress-fill" style="width:${g.w}%;"></div>
                                    </div>
                                </div>
                            `).join('')}
                        </div>
                    </div>
                    ` : ''}

                    <!-- 0. EXECUTIVE STRATEGIC PERFORMANCE & PROGRESS BARS MATRIX -->"""

html = html.replace(old_matrix_marker, super_stats_html, 1)
print("3. Injected Regional Benchmark Strip and School Stats Card!")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("SUCCESS: Super Stats Suite injected cleanly into index.html!")
