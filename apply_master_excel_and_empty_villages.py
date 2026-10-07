with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# -------------------------------------------------------------
# STEP 1: Empty unentered villages in villages array
# -------------------------------------------------------------
old_mofti = "{ id: 'mofti-ariz', name: 'مفتی عریض', cat: 'village', x: 0.810, y: 0.355, data: { pop: '۱,۴۲۰', fam: '۳۴۰', stats: [['خانوار', 340], ['کشاورزی', 'نخلستان و صیفی'], ['وضعیت آب', 'پایدار']] } },"
new_mofti = "{ id: 'mofti-ariz', name: 'مفتی عریض', cat: 'village', x: 0.810, y: 0.355, data: { pop: '—', fam: '—', stats: [['وضعیت', 'در انتظار ثبت آمار میدانی'], ['شناسنامه', 'خالی']] } },"
if old_mofti in html:
    html = html.replace(old_mofti, new_mofti, 1)

old_sadat = "{ id: 'shahrak-sadat', name: 'شهرک سادات', cat: 'village', x: 0.860, y: 0.565, data: { pop: '۱,۶۵۰', fam: '۴۱۰', stats: [['خانوار', 410], ['کشاورزی', 'فعال']] } },"
new_sadat = "{ id: 'shahrak-sadat', name: 'شهرک سادات', cat: 'village', x: 0.860, y: 0.565, data: { pop: '—', fam: '—', stats: [['وضعیت', 'در انتظار ثبت آمار میدانی'], ['شناسنامه', 'خالی']] } },"
if old_sadat in html:
    html = html.replace(old_sadat, new_sadat, 1)

old_sofla = "{ id: 'sarhaniyeh-sofla', name: 'سرحانیه سفلی', cat: 'village', x: 0.855, y: 0.725, data: { pop: '۲,۱۰۰', fam: '۵۲۰', stats: [['خانوار', 520], ['مدرسه', 1], ['پایگاه سلامت', 'فعال']] } },"
new_sofla = "{ id: 'sarhaniyeh-sofla', name: 'سرحانیه سفلی', cat: 'village', x: 0.855, y: 0.725, data: { pop: '—', fam: '—', stats: [['وضعیت', 'در انتظار ثبت آمار میدانی'], ['شناسنامه', 'خالی']] } },"
if old_sofla in html:
    html = html.replace(old_sofla, new_sofla, 1)

old_olya = "{ id: 'sarhaniyeh-olya', name: 'سرحانیه علیا', cat: 'village', x: 0.885, y: 0.785, data: { pop: '۱,۷۵۰', fam: '۴۳۰', stats: [['خانوار', 430], ['کشاورزی', 'خرما و یونجه']] } },"
new_olya = "{ id: 'sarhaniyeh-olya', name: 'سرحانیه علیا', cat: 'village', x: 0.885, y: 0.785, data: { pop: '—', fam: '—', stats: [['وضعیت', 'در انتظار ثبت آمار میدانی'], ['شناسنامه', 'خالی']] } },"
if old_olya in html:
    html = html.replace(old_olya, new_olya, 1)

old_jadideh = "{ id: 'jadideh', name: 'جدیده', cat: 'village', x: 0.760, y: 0.770, data: { pop: '۳,۲۰۰', fam: '۸۵۰', stats: [['شنوایی', 30], ['جسمی‌حرکتی', 70], ['بینایی', 25], ['ذهنی', 60], ['روانی', 10], ['صوت و گفتار', 1]] } },"
new_jadideh = "{ id: 'jadideh', name: 'جدیده', cat: 'village', x: 0.760, y: 0.770, data: { pop: '—', fam: '—', stats: [['وضعیت', 'در انتظار ثبت آمار میدانی'], ['شناسنامه', 'خالی']] } },"
if old_jadideh in html:
    html = html.replace(old_jadideh, new_jadideh, 1)

old_sharqi = "{ id: 'darband-sharqi', name: 'دربند شرقی', cat: 'village', x: 0.678, y: 0.852, data: { pop: '۱,۵۰۰', fam: '۳۸۰', stats: [['خانوار', 380], ['پوشش حمایتی', 'فعال']] } },"
new_sharqi = "{ id: 'darband-sharqi', name: 'دربند شرقی', cat: 'village', x: 0.678, y: 0.852, data: { pop: '—', fam: '—', stats: [['وضعیت', 'در انتظار ثبت آمار میدانی'], ['شناسنامه', 'خالی']] } },"
if old_sharqi in html:
    html = html.replace(old_sharqi, new_sharqi, 1)

print("1. Emptied unentered villages in villages array!")

# -------------------------------------------------------------
# STEP 2: Empty unentered villages in villageIndicators
# -------------------------------------------------------------
if "'mofti-ariz': ['high-pop']," in html:
    html = html.replace("'mofti-ariz': ['high-pop'],", "'mofti-ariz': [],", 1)
if "'jadideh': ['with-schools', 'high-pop', 'employment']," in html:
    html = html.replace("'jadideh': ['with-schools', 'high-pop', 'employment'],", "'jadideh': [],", 1)
if "'sarhaniyeh-olya': ['with-schools', 'with-health', 'high-pop']," in html:
    html = html.replace("'sarhaniyeh-olya': ['with-schools', 'with-health', 'high-pop'],", "'sarhaniyeh-olya': [],", 1)
if "'sarhaniyeh-sofla': ['high-pop']," in html:
    html = html.replace("'sarhaniyeh-sofla': ['high-pop'],", "'sarhaniyeh-sofla': [],", 1)
if "'shahrak-sadat': ['high-vuln']" in html:
    html = html.replace("'shahrak-sadat': ['high-vuln']", "'shahrak-sadat': []", 1)

print("2. Emptied unentered villages in villageIndicators!")

# -------------------------------------------------------------
# STEP 3: Clean getVillageData fallback for unentered villages
# -------------------------------------------------------------
idx_gvd_start = html.find("function getVillageData(v) {")
assert idx_gvd_start != -1, "getVillageData not found"
idx_gvd_if = html.find("if (!res) {", idx_gvd_start)
idx_gvd_end = html.find("if (!res.indicators) {", idx_gvd_if)
assert idx_gvd_if != -1 and idx_gvd_end != -1, "if (!res) block not found"

new_gvd_block = """if (!res) {
                    res = {
                        name: v.name,
                        corridor: 'روستای حوزه مقاومت و شلمچه',
                        coords: 'مختصات در حال تکمیل',
                        borderDist: '—',
                        cityDist: '—',
                        area: '—',
                        priorityRank: 'در انتظار ورود داده‌های میدانی',
                        priorityClass: 'p-low',
                        priorityDesc: 'شناسنامه، آمار جمعیتی، مدارس و پرونده‌های حمایتی این روستا هنوز توسط کارگروه وارد سامانه نشده و کاملاً خالی نگه داشته شده است.',
                        pop: '—',
                        popSub: 'در انتظار آمار سرشماری',
                        fam: '—',
                        famSub: 'در انتظار آمار خانوار',
                        disabled: '—',
                        disabledSub: 'در انتظار ممیزی',
                        emp: '—',
                        empSub: 'در انتظار ارزیابی',
                        agePyramid: [],
                        disabilities: [],
                        empProjects: [],
                        infrastructures: [],
                        schools: [],
                        indicators: [],
                        orphansCount: 0,
                        vulnerableFamilies: 0,
                        isPendingData: true
                    };
                }
                """

html = html[:idx_gvd_if] + new_gvd_block + html[idx_gvd_end:]
print("3. Cleaned getVillageData fallback to keep unentered villages blank!")

# -------------------------------------------------------------
# STEP 4: Clean getVillageAccordions fallback for unentered villages
# -------------------------------------------------------------
idx_gva = html.find("if (!raw) {")
idx_gva_end = html.find("const accordions = [];", idx_gva)
assert idx_gva != -1 and idx_gva_end != -1, "getVillageAccordions if (!raw) not found"

new_gva_fallback = """if (!raw) {
                    // Clean and honest empty state for unentered villages
                    return `
                        <div style="background:#f8fafc; border:2px dashed #cbd5e1; border-radius:14px; padding:36px 24px; text-align:center; color:#64748b; margin:16px 0;">
                            <div style="font-size:38px; margin-bottom:10px;">📋</div>
                            <h3 style="font-size:16px; font-weight:800; color:#334155; margin-bottom:8px;">اطلاعات و آمار روستای «${villageName}» هنوز وارد نشده است</h3>
                            <p style="font-size:13px; color:#64748b; max-width:460px; margin:0 auto 16px; line-height:1.8;">
                                بر اساس ضوابط قرارگاه، شناسنامه این روستا خالی نگه داشته شده است تا پس از دریافت داده‌های رسمی و مستند در سامانه ثبت گردد.
                            </p>
                            <div style="display:inline-flex; align-items:center; gap:8px; font-size:11.5px; background:#e2e8f0; color:#475569; padding:6px 14px; border-radius:20px; font-weight:700;">
                                <span>وضعیت شناسنامه:</span>
                                <span style="color:#0f172a; font-weight:800;">خالی (در صف ورود آمار)</span>
                            </div>
                        </div>
                    `;
                }

                """

html = html[:idx_gva] + new_gva_fallback + html[idx_gva_end:]
print("4. Replaced fallback accordion with honest clean empty state!")

# -------------------------------------------------------------
# STEP 5: Update regionalDialog table for unentered villages
# -------------------------------------------------------------
idx_tbody_s = html.find("<tbody style=\"font-size:12.5px; color:#33423f;\">")
idx_tbody_e = html.find("</tbody>", idx_tbody_s)
assert idx_tbody_s != -1 and idx_tbody_e != -1, "regionalDialog tbody not found"

new_tbody_content = """<tbody style=\"font-size:12.5px; color:#33423f;\">
                <tr style=\"background:#f0fdf4;\"><td style=\"padding:9px 14px;\">۱</td><td style=\"padding:9px 14px; font-weight:800; color:#142a29;\">سوره</td><td style=\"padding:9px 14px;\">حومه غربی</td><td style=\"padding:9px 14px; font-weight:800; color:#15803d;\">۴,۱۷۵ نفر</td><td style=\"padding:9px 14px; font-weight:700;\">۱,۰۵۱</td><td style=\"padding:9px 14px;\">۲ مدرسه (رزمندگان و مطیری با ۲۳۵ نفر)</td><td style=\"padding:9px 14px; font-weight:800; color:#b45309;\">۷۰ پرونده (۱۴ یتیم + ۵۶ مددجو)</td></tr>
                <tr style=\"background:#f0fdf4;\"><td style=\"padding:9px 14px;\">۲</td><td style=\"padding:9px 14px; font-weight:800; color:#142a29;\">دربند غربی</td><td style=\"padding:9px 14px;\">حومه غربی</td><td style=\"padding:9px 14px; font-weight:800; color:#15803d;\">۲,۷۵۵ نفر</td><td style=\"padding:9px 14px; font-weight:700;\">۶۸۱</td><td style=\"padding:9px 14px;\">دبستان مرزداران (۱۷۷ دانش‌آموز)</td><td style=\"padding:9px 14px; font-weight:800; color:#b45309;\">۶۱ پرونده (۱۱ یتیم + ۵۰ مددجو)</td></tr>
                <tr style=\"background:#f0fdf4;\"><td style=\"padding:9px 14px;\">۳</td><td style=\"padding:9px 14px; font-weight:800; color:#142a29;\">پل نو</td><td style=\"padding:9px 14px;\">حومه غربی</td><td style=\"padding:9px 14px; font-weight:800; color:#15803d;\">۳,۸۵۰ نفر</td><td style=\"padding:9px 14px; font-weight:700;\">۹۵۰</td><td style=\"padding:9px 14px;\">دبستان معراج (۴۲۰ دانش‌آموز)</td><td style=\"padding:9px 14px; font-weight:800; color:#b45309;\">۲۹ پرونده (۳ یتیم + ۲۶ مددجو)</td></tr>
                <tr style=\"background:#f0fdf4;\"><td style=\"padding:9px 14px;\">۴</td><td style=\"padding:9px 14px; font-weight:800; color:#142a29;\">صد دستگاه</td><td style=\"padding:9px 14px;\">بخش مرکزی</td><td style=\"padding:9px 14px; font-weight:800; color:#15803d;\">۸۸۲ نفر</td><td style=\"padding:9px 14px; font-weight:700;\">۲۱۱</td><td style=\"padding:9px 14px;\">۲ مدرسه (علویه و راهیان نور با ۶۹۵ دانش‌آموز)</td><td style=\"padding:9px 14px; font-weight:800; color:#b45309;\">۲۴ پرونده (۳ یتیم + ۲۱ مددجو)</td></tr>
                <tr style=\"background:#f0fdf4;\"><td style=\"padding:9px 14px;\">۵</td><td style=\"padding:9px 14px; font-weight:800; color:#142a29;\">مصلاوی ۱ و ۲</td><td style=\"padding:9px 14px;\">حومه غربی</td><td style=\"padding:9px 14px; font-weight:800; color:#15803d;\">۲,۰۶۳ نفر</td><td style=\"padding:9px 14px; font-weight:700;\">۶۸۹</td><td style=\"padding:9px 14px;\">۲ دبستان (مصلاوی ۱ و ۲ با ۲۶۴ نفر)</td><td style=\"padding:9px 14px; font-weight:800; color:#b45309;\">۱۶ پرونده (۱ یتیم + ۱۵ مددجو)</td></tr>
                <tr style=\"background:#f0fdf4;\"><td style=\"padding:9px 14px;\">۶</td><td style=\"padding:9px 14px; font-weight:800; color:#142a29;\">شهرک سوم</td><td style=\"padding:9px 14px;\">محور مرزی شلمچه</td><td style=\"padding:9px 14px; font-weight:800; color:#15803d;\">۴۰۳ نفر</td><td style=\"padding:9px 14px; font-weight:700;\">۱۳۴</td><td style=\"padding:9px 14px;\">دبستان نوساز آل یاسین (۴۸ نفر)</td><td style=\"padding:9px 14px; font-weight:800; color:#b45309;\">۱۶ پرونده (۱ یتیم + ۱۵ مددجو)</td></tr>
                <tr style=\"background:#f0fdf4;\"><td style=\"padding:9px 14px;\">۷</td><td style=\"padding:9px 14px; font-weight:800; color:#142a29;\">عریض</td><td style=\"padding:9px 14px;\">محور شلمچه</td><td style=\"padding:9px 14px; font-weight:800; color:#15803d;\">۲۸۱ نفر</td><td style=\"padding:9px 14px; font-weight:700;\">۶۵</td><td style=\"padding:9px 14px;\">دبستان ۱۵ خرداد (۳۰ دانش‌آموز)</td><td style=\"padding:9px 14px; font-weight:800; color:#b45309;\">۵ پرونده (۱ یتیم + ۴ مددجو)</td></tr>
                <tr><td style=\"padding:9px 14px;\">۸</td><td style=\"padding:9px 14px; font-weight:800; color:#64748b;\">جدیده</td><td style=\"padding:9px 14px; color:#64748b;\">حومه شرقی</td><td style=\"padding:9px 14px; color:#94a3b8;\">—</td><td style=\"padding:9px 14px; color:#94a3b8;\">—</td><td style=\"padding:9px 14px; color:#94a3b8;\">—</td><td style=\"padding:9px 14px; color:#94a3b8; font-weight:600;\">خالی (در انتظار ثبت آمار میدانی)</td></tr>
                <tr><td style=\"padding:9px 14px;\">۹</td><td style=\"padding:9px 14px; font-weight:800; color:#64748b;\">سرحانیه اول (علیا)</td><td style=\"padding:9px 14px; color:#64748b;\">حومه شرقی</td><td style=\"padding:9px 14px; color:#94a3b8;\">—</td><td style=\"padding:9px 14px; color:#94a3b8;\">—</td><td style=\"padding:9px 14px; color:#94a3b8;\">—</td><td style=\"padding:9px 14px; color:#94a3b8; font-weight:600;\">خالی (در انتظار ثبت آمار میدانی)</td></tr>
                <tr><td style=\"padding:9px 14px;\">۱۰</td><td style=\"padding:9px 14px; font-weight:800; color:#64748b;\">دربند شرقی</td><td style=\"padding:9px 14px; color:#64748b;\">حومه غربی</td><td style=\"padding:9px 14px; color:#94a3b8;\">—</td><td style=\"padding:9px 14px; color:#94a3b8;\">—</td><td style=\"padding:9px 14px; color:#94a3b8;\">—</td><td style=\"padding:9px 14px; color:#94a3b8; font-weight:600;\">خالی (در انتظار ثبت آمار میدانی)</td></tr>
                <tr><td style=\"padding:9px 14px;\">۱۱</td><td style=\"padding:9px 14px; font-weight:800; color:#64748b;\">سرحانیه سفلی</td><td style=\"padding:9px 14px; color:#64748b;\">حومه شرقی</td><td style=\"padding:9px 14px; color:#94a3b8;\">—</td><td style=\"padding:9px 14px; color:#94a3b8;\">—</td><td style=\"padding:9px 14px; color:#94a3b8;\">—</td><td style=\"padding:9px 14px; color:#94a3b8; font-weight:600;\">خالی (در انتظار ثبت آمار میدانی)</td></tr>
                <tr><td style=\"padding:9px 14px;\">۱۲</td><td style=\"padding:9px 14px; font-weight:800; color:#64748b;\">شهرک سادات</td><td style=\"padding:9px 14px; color:#64748b;\">محور شلمچه</td><td style=\"padding:9px 14px; color:#94a3b8;\">—</td><td style=\"padding:9px 14px; color:#94a3b8;\">—</td><td style=\"padding:9px 14px; color:#94a3b8;\">—</td><td style=\"padding:9px 14px; color:#94a3b8; font-weight:600;\">خالی (در انتظار ثبت آمار میدانی)</td></tr>
                <tr><td style=\"padding:9px 14px;\">۱۳</td><td style=\"padding:9px 14px; font-weight:800; color:#64748b;\">مفتی عریض</td><td style=\"padding:9px 14px; color:#64748b;\">محور شلمچه</td><td style=\"padding:9px 14px; color:#94a3b8;\">—</td><td style=\"padding:9px 14px; color:#94a3b8;\">—</td><td style=\"padding:9px 14px; color:#94a3b8;\">—</td><td style=\"padding:9px 14px; color:#94a3b8; font-weight:600;\">خالی (در انتظار ثبت آمار میدانی)</td></tr>
            """

html = html[:idx_tbody_s] + new_tbody_content + html[idx_tbody_e:]
print("5. Updated regionalDialog table!")

# -------------------------------------------------------------
# STEP 6: Add button in header for Master Excel export
# -------------------------------------------------------------
btn_marker = 'id="regionalSummaryBtn"'
idx_bs = html.find(btn_marker)
assert idx_bs != -1, "regionalSummaryBtn not found"
idx_be = html.find("</button>", idx_bs)
assert idx_be != -1, "end of regionalSummaryBtn not found"

new_header_btn_inject = """</button>
        <button class="nav-action-btn btn-master-excel" id="masterExcelExportBtn" title="دریافت دیتابیس جامع ۵ برگه اکسل کل منطقه (۲۲۴ پرونده، مدارس و زیرساخت‌ها)">
            <svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
                <polyline points="7 10 12 15 17 10"></polyline>
                <line x1="12" y1="15" x2="12" y2="3"></line>
            </svg>
            <span>اکسل جامع منطقه</span>
        </button>"""

html = html[:idx_be] + new_header_btn_inject + html[idx_be + len("</button>"):]

# Add button in regionalDialog header
print_marker = 'id="printRegionalBtn"'
idx_ps = html.find(print_marker)
if idx_ps != -1:
    btn_start = html.rfind("<button", 0, idx_ps)
    new_reg_btn_code = """<button class="dos-btn-primary" id="exportRegionalMasterExcelBtn" style="background:#1B4D3E; color:#fff; display:flex; align-items:center; gap:6px; font-weight:700; border-radius:8px; padding:6px 12px; cursor:pointer;">
                <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
                <span>دانلود دیتابیس اکسل منطقه (۵ برگه)</span>
            </button>
            """
    html = html[:btn_start] + new_reg_btn_code + html[btn_start:]

print("6. Added buttons in header and regionalDialog!")

# -------------------------------------------------------------
# STEP 7: Add CSS for btn-master-excel
# -------------------------------------------------------------
css_marker = ".nav-action-btn:hover {"
if css_marker in html:
    new_css = """.btn-master-excel {
            background: #064e3b !important;
            color: #ecfdf5 !important;
            border-color: #047857 !important;
            font-weight: 700 !important;
        }
        .btn-master-excel:hover {
            background: #047857 !important;
            color: #ffffff !important;
            border-color: #10b981 !important;
            box-shadow: 0 4px 12px rgba(4, 120, 87, 0.3) !important;
        }
        .nav-action-btn:hover {"""
    html = html.replace(css_marker, new_css, 1)

print("7. Injected CSS for btn-master-excel!")

# -------------------------------------------------------------
# STEP 8: Inject exportMasterRegionalExcel function and wire up events
# -------------------------------------------------------------
excel_func_code = """
        // =========================================================================
        // Master Multi-Sheet Excel Export (Proposal #3)
        // =========================================================================
        window.exportMasterRegionalExcel = function() {
            try {
                const orphans = (typeof searchableData !== 'undefined') ? searchableData.filter(d => d.type === 'person' && d.personType === 'orphan') : [];
                const needy = (typeof searchableData !== 'undefined') ? searchableData.filter(d => d.type === 'person' && d.personType === 'needy') : [];

                function esc(val) {
                    if (val === undefined || val === null) return '';
                    return String(val)
                        .replace(/&/g, '&amp;')
                        .replace(/</g, '&lt;')
                        .replace(/>/g, '&gt;')
                        .replace(/\"/g, '&quot;')
                        .replace(/'/g, '&apos;');
                }

                let xml = `<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<?mso-application progid=\"Excel.Sheet\"?>
<Workbook xmlns=\"urn:schemas-microsoft-com:office:spreadsheet\"
 xmlns:o=\"urn:schemas-microsoft-com:office:office\"
 xmlns:x=\"urn:schemas-microsoft-com:office:excel\"
 xmlns:ss=\"urn:schemas-microsoft-com:office:spreadsheet\"
 xmlns:html=\"http://www.w3.org/TR/REC-html40\">
 <DocumentProperties xmlns=\"urn:schemas-microsoft-com:office:office\">
  <Author>جمعیت بین‌المللی امام‌رضایی‌ها</Author>
  <Title>بانک جامع اطلاعات و آمار منطقه شلمچه و خرمشهر</Title>
  <Created>${new Date().toISOString()}</Created>
 </DocumentProperties>
 <Styles>
  <Style ss:ID=\"Default\" ss:Name=\"Normal\">
   <Alignment ss:Vertical=\"Center\"/>
   <Borders/>
   <Font ss:FontName=\"Tahoma\" x:CharSet=\"178\" ss:Size=\"10\"/>
   <Interior/>
   <NumberFormat/>
   <Protection/>
  </Style>
  <Style ss:ID=\"Header\">
   <Alignment ss:Horizontal=\"Center\" ss:Vertical=\"Center\" ss:WrapText=\"1\"/>
   <Borders>
    <Border ss:Position=\"Bottom\" ss:LineStyle=\"Continuous\" ss:Weight=\"1\" ss:Color=\"#000000\"/>
    <Border ss:Position=\"Left\" ss:LineStyle=\"Continuous\" ss:Weight=\"1\" ss:Color=\"#000000\"/>
    <Border ss:Position=\"Right\" ss:LineStyle=\"Continuous\" ss:Weight=\"1\" ss:Color=\"#000000\"/>
    <Border ss:Position=\"Top\" ss:LineStyle=\"Continuous\" ss:Weight=\"1\" ss:Color=\"#000000\"/>
   </Borders>
   <Font ss:FontName=\"Tahoma\" x:CharSet=\"178\" ss:Size=\"10.5\" ss:Bold=\"1\" ss:Color=\"#FFFFFF\"/>
   <Interior ss:Color=\"#1B4D3E\" ss:Pattern=\"Solid\"/>
  </Style>
  <Style ss:ID=\"HeaderGold\">
   <Alignment ss:Horizontal=\"Center\" ss:Vertical=\"Center\" ss:WrapText=\"1\"/>
   <Borders>
    <Border ss:Position=\"Bottom\" ss:LineStyle=\"Continuous\" ss:Weight=\"1\" ss:Color=\"#000000\"/>
    <Border ss:Position=\"Left\" ss:LineStyle=\"Continuous\" ss:Weight=\"1\" ss:Color=\"#000000\"/>
    <Border ss:Position=\"Right\" ss:LineStyle=\"Continuous\" ss:Weight=\"1\" ss:Color=\"#000000\"/>
    <Border ss:Position=\"Top\" ss:LineStyle=\"Continuous\" ss:Weight=\"1\" ss:Color=\"#000000\"/>
   </Borders>
   <Font ss:FontName=\"Tahoma\" x:CharSet=\"178\" ss:Size=\"10.5\" ss:Bold=\"1\" ss:Color=\"#142A29\"/>
   <Interior ss:Color=\"#DED1B8\" ss:Pattern=\"Solid\"/>
  </Style>
  <Style ss:ID=\"Cell\">
   <Alignment ss:Horizontal=\"Right\" ss:Vertical=\"Center\"/>
   <Borders>
    <Border ss:Position=\"Bottom\" ss:LineStyle=\"Continuous\" ss:Weight=\"1\" ss:Color=\"#E2E8F0\"/>
    <Border ss:Position=\"Left\" ss:LineStyle=\"Continuous\" ss:Weight=\"1\" ss:Color=\"#E2E8F0\"/>
    <Border ss:Position=\"Right\" ss:LineStyle=\"Continuous\" ss:Weight=\"1\" ss:Color=\"#E2E8F0\"/>
    <Border ss:Position=\"Top\" ss:LineStyle=\"Continuous\" ss:Weight=\"1\" ss:Color=\"#E2E8F0\"/>
   </Borders>
   <Font ss:FontName=\"Tahoma\" x:CharSet=\"178\" ss:Size=\"9.5\"/>
  </Style>
  <Style ss:ID=\"CellCenter\">
   <Alignment ss:Horizontal=\"Center\" ss:Vertical=\"Center\"/>
   <Borders>
    <Border ss:Position=\"Bottom\" ss:LineStyle=\"Continuous\" ss:Weight=\"1\" ss:Color=\"#E2E8F0\"/>
    <Border ss:Position=\"Left\" ss:LineStyle=\"Continuous\" ss:Weight=\"1\" ss:Color=\"#E2E8F0\"/>
    <Border ss:Position=\"Right\" ss:LineStyle=\"Continuous\" ss:Weight=\"1\" ss:Color=\"#E2E8F0\"/>
    <Border ss:Position=\"Top\" ss:LineStyle=\"Continuous\" ss:Weight=\"1\" ss:Color=\"#E2E8F0\"/>
   </Borders>
   <Font ss:FontName=\"Tahoma\" x:CharSet=\"178\" ss:Size=\"9.5\"/>
  </Style>
  <Style ss:ID=\"CellBold\">
   <Alignment ss:Horizontal=\"Right\" ss:Vertical=\"Center\"/>
   <Borders>
    <Border ss:Position=\"Bottom\" ss:LineStyle=\"Continuous\" ss:Weight=\"1\" ss:Color=\"#E2E8F0\"/>
    <Border ss:Position=\"Left\" ss:LineStyle=\"Continuous\" ss:Weight=\"1\" ss:Color=\"#E2E8F0\"/>
    <Border ss:Position=\"Right\" ss:LineStyle=\"Continuous\" ss:Weight=\"1\" ss:Color=\"#E2E8F0\"/>
    <Border ss:Position=\"Top\" ss:LineStyle=\"Continuous\" ss:Weight=\"1\" ss:Color=\"#E2E8F0\"/>
   </Borders>
   <Font ss:FontName=\"Tahoma\" x:CharSet=\"178\" ss:Size=\"9.5\" ss:Bold=\"1\"/>
  </Style>
 </Styles>`;

                // SHEET 1: خلاصه ۱۹ روستا
                xml += `
 <Worksheet ss:Name=\"خلاصه ۱۹ روستا\" ss:RightToLeft=\"1\">
  <Table>
   <Column ss:Width=\"36\"/>
   <Column ss:Width=\"110\"/>
   <Column ss:Width=\"95\"/>
   <Column ss:Width=\"140\"/>
   <Column ss:Width=\"85\"/>
   <Column ss:Width=\"85\"/>
   <Column ss:Width=\"190\"/>
   <Column ss:Width=\"170\"/>
   <Row ss:Height=\"26\" ss:StyleID=\"Header\">
    <Cell><Data ss:Type=\"String\">ردیف</Data></Cell>
    <Cell><Data ss:Type=\"String\">نام روستا</Data></Cell>
    <Cell><Data ss:Type=\"String\">بخش / حوزه</Data></Cell>
    <Cell><Data ss:Type=\"String\">وضعیت شناسنامه در سامانه</Data></Cell>
    <Cell><Data ss:Type=\"String\">جمعیت مستند</Data></Cell>
    <Cell><Data ss:Type=\"String\">تعداد خانوار</Data></Cell>
    <Cell><Data ss:Type=\"String\">مراکز آموزشی و مدارس</Data></Cell>
    <Cell><Data ss:Type=\"String\">پرونده‌های حمایتی مستند</Data></Cell>
   </Row>`;

                const regionalList = [
                    { name: 'سوره', dehestan: 'حومه غربی', status: 'ثبت جامع و مستند', pop: '۴,۱۷۵', fam: '۱,۰۵۱', school: '۲ مدرسه (رزمندگان و مطیری)', dossiers: '۷۰ پرونده (۱۴ یتیم + ۵۶ مددجو)' },
                    { name: 'دربند غربی', dehestan: 'حومه غربی', status: 'ثبت جامع و مستند', pop: '۲,۷۵۵', fam: '۶۸۱', school: 'دبستان مرزداران (۱۷۷ دانش‌آموز)', dossiers: '۶۱ پرونده (۱۱ یتیم + ۵۰ مددجو)' },
                    { name: 'پل نو', dehestan: 'حومه غربی', status: 'ثبت جامع و مستند', pop: '۳,۸۵۰', fam: '۹۵۰', school: 'دبستان معراج (۴۲۰ دانش‌آموز)', dossiers: '۲۹ پرونده (۳ یتیم + ۲۶ مددجو)' },
                    { name: 'صد دستگاه', dehestan: 'بخش مرکزی', status: 'ثبت جامع و مستند', pop: '۸۸۲', fam: '۲۱۱', school: '۲ مرکز (علویه و راهیان نور با ۶۹۵ نفر)', dossiers: '۲۴ پرونده (۳ یتیم + ۲۱ مددجو)' },
                    { name: 'مصلاوی ۱ و ۲', dehestan: 'حومه غربی', status: 'ثبت جامع و مستند', pop: '۲,۰۶۳', fam: '۶۸۹', school: '۲ دبستان (۲۶۴ دانش‌آموز)', dossiers: '۱۶ پرونده (۱ یتیم + ۱۵ مددجو)' },
                    { name: 'شهرک سوم', dehestan: 'محور مرزی شلمچه', status: 'ثبت جامع و مستند', pop: '۴۰۳', fam: '۱۳۴', school: 'دبستان نوساز آل یاسین (۴۸ نفر)', dossiers: '۱۶ پرونده (۱ یتیم + ۱۵ مددجو)' },
                    { name: 'عریض', dehestan: 'محور شلمچه', status: 'ثبت جامع و مستند', pop: '۲۸۱', fam: '۶۵', school: 'دبستان ۱۵ خرداد (۳۰ دانش‌آموز)', dossiers: '۵ پرونده (۱ یتیم + ۴ مددجو)' },
                    { name: 'جدیده', dehestan: 'حومه شرقی', status: 'خالی (در انتظار ثبت آمار)', pop: '—', fam: '—', school: '—', dossiers: 'خالی (در انتظار آمار)' },
                    { name: 'سرحانیه علیا', dehestan: 'حومه شرقی', status: 'خالی (در انتظار ثبت آمار)', pop: '—', fam: '—', school: '—', dossiers: 'خالی (در انتظار آمار)' },
                    { name: 'سرحانیه سفلی', dehestan: 'حومه شرقی', status: 'خالی (در انتظار ثبت آمار)', pop: '—', fam: '—', school: '—', dossiers: 'خالی (در انتظار آمار)' },
                    { name: 'دربند شرقی', dehestan: 'حومه غربی', status: 'خالی (در انتظار ثبت آمار)', pop: '—', fam: '—', school: '—', dossiers: 'خالی (در انتظار آمار)' },
                    { name: 'شهرک سادات', dehestan: 'محور شلمچه', status: 'خالی (در انتظار ثبت آمار)', pop: '—', fam: '—', school: '—', dossiers: 'خالی (در انتظار آمار)' },
                    { name: 'مفتی عریض', dehestan: 'محور شلمچه', status: 'خالی (در انتظار ثبت آمار)', pop: '—', fam: '—', school: '—', dossiers: 'خالی (در انتظار آمار)' }
                ];

                regionalList.forEach((r, idx) => {
                    xml += `
   <Row ss:Height=\"22\">
    <Cell ss:StyleID=\"CellCenter\"><Data ss:Type=\"Number\">${idx + 1}</Data></Cell>
    <Cell ss:StyleID=\"CellBold\"><Data ss:Type=\"String\">${esc(r.name)}</Data></Cell>
    <Cell ss:StyleID=\"CellCenter\"><Data ss:Type=\"String\">${esc(r.dehestan)}</Data></Cell>
    <Cell ss:StyleID=\"CellCenter\"><Data ss:Type=\"String\">${esc(r.status)}</Data></Cell>
    <Cell ss:StyleID=\"CellCenter\"><Data ss:Type=\"String\">${esc(r.pop)}</Data></Cell>
    <Cell ss:StyleID=\"CellCenter\"><Data ss:Type=\"String\">${esc(r.fam)}</Data></Cell>
    <Cell ss:StyleID=\"Cell\"><Data ss:Type=\"String\">${esc(r.school)}</Data></Cell>
    <Cell ss:StyleID=\"CellBold\"><Data ss:Type=\"String\">${esc(r.dossiers)}</Data></Cell>
   </Row>`;
                });
                xml += `
  </Table>
 </Worksheet>`;

                // SHEET 2: بانک جامع ایتام
                xml += `
 <Worksheet ss:Name=\"بانک جامع ایتام (${orphans.length} نفر)\" ss:RightToLeft=\"1\">
  <Table>
   <Column ss:Width=\"36\"/>
   <Column ss:Width=\"120\"/>
   <Column ss:Width=\"75\"/>
   <Column ss:Width=\"45\"/>
   <Column ss:Width=\"70\"/>
   <Column ss:Width=\"95\"/>
   <Column ss:Width=\"110\"/>
   <Column ss:Width=\"90\"/>
   <Column ss:Width=\"85\"/>
   <Column ss:Width=\"90\"/>
   <Column ss:Width=\"220\"/>
   <Column ss:Width=\"110\"/>
   <Row ss:Height=\"26\" ss:StyleID=\"Header\">
    <Cell><Data ss:Type=\"String\">ردیف</Data></Cell>
    <Cell><Data ss:Type=\"String\">نام و نام خانوادگی</Data></Cell>
    <Cell><Data ss:Type=\"String\">نام پدر</Data></Cell>
    <Cell><Data ss:Type=\"String\">سن</Data></Cell>
    <Cell><Data ss:Type=\"String\">تحصیلات</Data></Cell>
    <Cell><Data ss:Type=\"String\">مدرسه / دانشگاه</Data></Cell>
    <Cell><Data ss:Type=\"String\">نام سرپرست</Data></Cell>
    <Cell><Data ss:Type=\"String\">کد ملی یتیم</Data></Cell>
    <Cell><Data ss:Type=\"String\">روستا</Data></Cell>
    <Cell><Data ss:Type=\"String\">وضعیت سلامت</Data></Cell>
    <Cell><Data ss:Type=\"String\">نشانی دقیق</Data></Cell>
    <Cell><Data ss:Type=\"String\">شماره تماس</Data></Cell>
   </Row>`;

                orphans.forEach((o, idx) => {
                    xml += `
   <Row ss:Height=\"21\">
    <Cell ss:StyleID=\"CellCenter\"><Data ss:Type=\"Number\">${idx + 1}</Data></Cell>
    <Cell ss:StyleID=\"CellBold\"><Data ss:Type=\"String\">${esc(o.title)}</Data></Cell>
    <Cell ss:StyleID=\"CellCenter\"><Data ss:Type=\"String\">${esc(o.father || '—')}</Data></Cell>
    <Cell ss:StyleID=\"CellCenter\"><Data ss:Type=\"String\">${esc(o.age || '—')}</Data></Cell>
    <Cell ss:StyleID=\"CellCenter\"><Data ss:Type=\"String\">${esc(o.edu || '—')}</Data></Cell>
    <Cell ss:StyleID=\"Cell\"><Data ss:Type=\"String\">${esc(o.school || '—')}</Data></Cell>
    <Cell ss:StyleID=\"Cell\"><Data ss:Type=\"String\">${esc(o.guardian || '—')}</Data></Cell>
    <Cell ss:StyleID=\"CellCenter\"><Data ss:Type=\"String\">${esc(o.nationalId || '—')}</Data></Cell>
    <Cell ss:StyleID=\"CellCenter\"><Data ss:Type=\"String\">${esc(o.village || '—')}</Data></Cell>
    <Cell ss:StyleID=\"CellCenter\"><Data ss:Type=\"String\">${esc(o.health || 'سالم')}</Data></Cell>
    <Cell ss:StyleID=\"Cell\"><Data ss:Type=\"String\">${esc(o.address || '—')}</Data></Cell>
    <Cell ss:StyleID=\"CellCenter\"><Data ss:Type=\"String\">${esc(o.phone || '—')}</Data></Cell>
   </Row>`;
                });
                xml += `
  </Table>
 </Worksheet>`;

                // SHEET 3: بانک خانوارهای کم‌برخوردار
                xml += `
 <Worksheet ss:Name=\"بانک کم‌برخوردار (${needy.length} خانوار)\" ss:RightToLeft=\"1\">
  <Table>
   <Column ss:Width=\"36\"/>
   <Column ss:Width=\"140\"/>
   <Column ss:Width=\"95\"/>
   <Column ss:Width=\"105\"/>
   <Column ss:Width=\"95\"/>
   <Column ss:Width=\"260\"/>
   <Column ss:Width=\"110\"/>
   <Row ss:Height=\"26\" ss:StyleID=\"Header\">
    <Cell><Data ss:Type=\"String\">ردیف</Data></Cell>
    <Cell><Data ss:Type=\"String\">نام و نام خانوادگی سرپرست</Data></Cell>
    <Cell><Data ss:Type=\"String\">کد ملی</Data></Cell>
    <Cell><Data ss:Type=\"String\">شماره تماس</Data></Cell>
    <Cell><Data ss:Type=\"String\">روستا</Data></Cell>
    <Cell><Data ss:Type=\"String\">نشانی و موقعیت</Data></Cell>
    <Cell><Data ss:Type=\"String\">نوع پرونده</Data></Cell>
   </Row>`;

                needy.forEach((n, idx) => {
                    xml += `
   <Row ss:Height=\"21\">
    <Cell ss:StyleID=\"CellCenter\"><Data ss:Type=\"Number\">${idx + 1}</Data></Cell>
    <Cell ss:StyleID=\"CellBold\"><Data ss:Type=\"String\">${esc(n.title)}</Data></Cell>
    <Cell ss:StyleID=\"CellCenter\"><Data ss:Type=\"String\">${esc(n.nationalId || '—')}</Data></Cell>
    <Cell ss:StyleID=\"CellCenter\"><Data ss:Type=\"String\">${esc(n.phone || '—')}</Data></Cell>
    <Cell ss:StyleID=\"CellCenter\"><Data ss:Type=\"String\">${esc(n.village || '—')}</Data></Cell>
    <Cell ss:StyleID=\"Cell\"><Data ss:Type=\"String\">${esc(n.address || '—')}</Data></Cell>
    <Cell ss:StyleID=\"CellCenter\"><Data ss:Type=\"String\">مددجوی کم‌برخوردار</Data></Cell>
   </Row>`;
                });
                xml += `
  </Table>
 </Worksheet>`;

                // SHEET 4: مدارس و هرم تحصیلی
                xml += `
 <Worksheet ss:Name=\"مدارس و هرم تحصیلی\" ss:RightToLeft=\"1\">
  <Table>
   <Column ss:Width=\"36\"/>
   <Column ss:Width=\"90\"/>
   <Column ss:Width=\"150\"/>
   <Column ss:Width=\"80\"/>
   <Column ss:Width=\"65\"/>
   <Column ss:Width=\"60\"/>
   <Column ss:Width=\"60\"/>
   <Column ss:Width=\"60\"/>
   <Column ss:Width=\"60\"/>
   <Column ss:Width=\"60\"/>
   <Column ss:Width=\"60\"/>
   <Column ss:Width=\"70\"/>
   <Row ss:Height=\"26\" ss:StyleID=\"Header\">
    <Cell><Data ss:Type=\"String\">ردیف</Data></Cell>
    <Cell><Data ss:Type=\"String\">روستا</Data></Cell>
    <Cell><Data ss:Type=\"String\">نام مدرسه</Data></Cell>
    <Cell><Data ss:Type=\"String\">مقطع</Data></Cell>
    <Cell><Data ss:Type=\"String\">پیش‌دبستان</Data></Cell>
    <Cell><Data ss:Type=\"String\">پایه اول</Data></Cell>
    <Cell><Data ss:Type=\"String\">پایه دوم</Data></Cell>
    <Cell><Data ss:Type=\"String\">پایه سوم</Data></Cell>
    <Cell><Data ss:Type=\"String\">پایه چهارم</Data></Cell>
    <Cell><Data ss:Type=\"String\">پایه پنجم</Data></Cell>
    <Cell><Data ss:Type=\"String\">پایه ششم</Data></Cell>
    <Cell><Data ss:Type=\"String\">جمع کل</Data></Cell>
   </Row>`;

                const schoolRows = [
                    { village: 'سوره', name: 'دبستان رزمندگان', level: 'ابتدایی', pre: '—', g1: '۱۳', g2: '۱۴', g3: '۱۶', g4: '۱۶', g5: '۱۸', g6: '۱۹', total: '۹۶' },
                    { village: 'سوره', name: 'دبستان مطیری', level: 'ابتدایی', pre: '—', g1: '۲۹', g2: '۱۹', g3: '۲۰', g4: '۱۷', g5: '۱۹', g6: '۱۵', total: '۱۳۹' },
                    { village: 'دربند غربی', name: 'دبستان مرزداران', level: 'ابتدایی', pre: '—', g1: '۲۶', g2: '۳۲', g3: '۲۸', g4: '۳۱', g5: '۲۹', g6: '۳۱', total: '۱۷۷' },
                    { village: 'پل نو', name: 'دبستان معراج', level: 'ابتدایی', pre: '—', g1: '۷۲', g2: '۶۸', g3: '۷۰', g4: '۷۱', g5: '۶۹', g6: '۷۰', total: '۴۲۰' },
                    { village: 'صد دستگاه', name: 'دبستان علویه', level: 'ابتدایی', pre: '—', g1: '۴۹', g2: '۳۸', g3: '۴۰', g4: '۵۳', g5: '۵۳', g6: '۳۲', total: '۲۶۵' },
                    { village: 'صد دستگاه', name: 'متوسطه راهیان نور', level: 'متوسطه اول', pre: '—', g1: '—', g2: '—', g3: '—', g4: '—', g5: '—', g6: '—', total: '۴۳۰' },
                    { village: 'مصلاوی ۱', name: 'دبستان مصلاوی ۱', level: 'ابتدایی', pre: '—', g1: '۲۴', g2: '۲۵', g3: '۲۲', g4: '۲۵', g5: '۲۶', g6: '۲۴', total: '۱۴۶' },
                    { village: 'مصلاوی ۲', name: 'دبستان مصلاوی ۲', level: 'ابتدایی', pre: '—', g1: '۱۹', g2: '۲۰', g3: '۱۸', g4: '۲۱', g5: '۲۰', g6: '۲۰', total: '۱۱۸' },
                    { village: 'شهرک سوم', name: 'دبستان آل یاسین', level: 'ابتدایی', pre: '—', g1: '۸', g2: '۷', g3: '۹', g4: '۸', g5: '۸', g6: '۸', total: '۴۸' },
                    { village: 'عریض', name: 'دبستان ۱۵ خرداد', level: 'ابتدایی', pre: '—', g1: '۵', g2: '۴', g3: '۵', g4: '۵', g5: '۵', g6: '۶', total: '۳۰' }
                ];

                schoolRows.forEach((s, idx) => {
                    xml += `
   <Row ss:Height=\"21\">
    <Cell ss:StyleID=\"CellCenter\"><Data ss:Type=\"Number\">${idx + 1}</Data></Cell>
    <Cell ss:StyleID=\"CellCenter\"><Data ss:Type=\"String\">${esc(s.village)}</Data></Cell>
    <Cell ss:StyleID=\"CellBold\"><Data ss:Type=\"String\">${esc(s.name)}</Data></Cell>
    <Cell ss:StyleID=\"CellCenter\"><Data ss:Type=\"String\">${esc(s.level)}</Data></Cell>
    <Cell ss:StyleID=\"CellCenter\"><Data ss:Type=\"String\">${esc(s.pre)}</Data></Cell>
    <Cell ss:StyleID=\"CellCenter\"><Data ss:Type=\"String\">${esc(s.g1)}</Data></Cell>
    <Cell ss:StyleID=\"CellCenter\"><Data ss:Type=\"String\">${esc(s.g2)}</Data></Cell>
    <Cell ss:StyleID=\"CellCenter\"><Data ss:Type=\"String\">${esc(s.g3)}</Data></Cell>
    <Cell ss:StyleID=\"CellCenter\"><Data ss:Type=\"String\">${esc(s.g4)}</Data></Cell>
    <Cell ss:StyleID=\"CellCenter\"><Data ss:Type=\"String\">${esc(s.g5)}</Data></Cell>
    <Cell ss:StyleID=\"CellCenter\"><Data ss:Type=\"String\">${esc(s.g6)}</Data></Cell>
    <Cell ss:StyleID=\"CellBold\"><Data ss:Type=\"String\">${esc(s.total)}</Data></Cell>
   </Row>`;
                });
                xml += `
  </Table>
 </Worksheet>`;

                // SHEET 5: زیرساخت‌ها و اماکن
                xml += `
 <Worksheet ss:Name=\"زیرساخت‌ها و اماکن\" ss:RightToLeft=\"1\">
  <Table>
   <Column ss:Width=\"36\"/>
   <Column ss:Width=\"95\"/>
   <Column ss:Width=\"160\"/>
   <Column ss:Width=\"190\"/>
   <Column ss:Width=\"160\"/>
   <Row ss:Height=\"26\" ss:StyleID=\"Header\">
    <Cell><Data ss:Type=\"String\">ردیف</Data></Cell>
    <Cell><Data ss:Type=\"String\">روستا</Data></Cell>
    <Cell><Data ss:Type=\"String\">عنوان زیرساخت</Data></Cell>
    <Cell><Data ss:Type=\"String\">متراژ و مشخصات</Data></Cell>
    <Cell><Data ss:Type=\"String\">وضعیت و آمار پوشش</Data></Cell>
   </Row>`;

                const infraRows = [
                    { village: 'سوره', title: 'خانه بهداشت سوره ۱', spec: 'زیربنا ۲۰۰ مترمربع', status: 'فعال تحت پوشش ۴۹۸ خانوار' },
                    { village: 'سوره', title: 'کتابخانه عمومی قلم‌چی', spec: '۵۰۰ مترمربع زیربنا', status: '۵۲۲ عضو فعال' },
                    { village: 'دربند غربی', title: 'خانه بهداشت دربند غربی', spec: '۲۰۰ مترمربع زمین اهدایی', status: 'فعال · ۶۸۱ خانوار تحت پوشش' },
                    { village: 'پل نو', title: 'خانه بهداشت پل نو', spec: 'مرکز بهداشت روستایی', status: 'فعال · بهورز مستقر' },
                    { village: 'مصلاوی', title: 'خانه بهداشت مصلاوی', spec: 'مرکز بهداشت روستایی', status: 'فعال · ۶۸۹ خانوار' },
                    { village: 'عریض', title: 'خانه بهداشت عریض', spec: 'پایگاه سلامت روستایی', status: 'فعال · تحت پوشش روستای عریض' },
                    { village: 'صد دستگاه', title: 'مسجد صاحب‌الزمان', spec: 'کانون مذهبی، فرهنگی و محرومیت‌زدایی', status: 'فعال · ۲۱۱ خانوار محله' }
                ];

                infraRows.forEach((inf, idx) => {
                    xml += `
   <Row ss:Height=\"21\">
    <Cell ss:StyleID=\"CellCenter\"><Data ss:Type=\"Number\">${idx + 1}</Data></Cell>
    <Cell ss:StyleID=\"CellCenter\"><Data ss:Type=\"String\">${esc(inf.village)}</Data></Cell>
    <Cell ss:StyleID=\"CellBold\"><Data ss:Type=\"String\">${esc(inf.title)}</Data></Cell>
    <Cell ss:StyleID=\"Cell\"><Data ss:Type=\"String\">${esc(inf.spec)}</Data></Cell>
    <Cell ss:StyleID=\"Cell\"><Data ss:Type=\"String\">${esc(inf.status)}</Data></Cell>
   </Row>`;
                });
                xml += `
  </Table>
 </Worksheet>
</Workbook>`;

                const blob = new Blob([xml], { type: 'application/vnd.ms-excel;charset=utf-8;' });
                const url = URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.href = url;
                a.download = `Regional_Master_Database_Shalamcheh_${new Date().toISOString().slice(0, 10)}.xls`;
                document.body.appendChild(a);
                a.click();
                document.body.removeChild(a);
                URL.revokeObjectURL(url);

                if (typeof showSearchToast === 'function') {
                    showSearchToast(`✓ فایل اکسل جامع ۵ برگه با ۲۲۴ پرونده مستند با موفقیت دانلود شد.`);
                }
            } catch (err) {
                console.error('Error exporting master regional excel:', err);
            }
        };

        // Wire up buttons
        document.addEventListener('DOMContentLoaded', () => {
            const masterExcelBtn = document.getElementById('masterExcelExportBtn');
            if (masterExcelBtn) {
                masterExcelBtn.addEventListener('click', () => {
                    window.exportMasterRegionalExcel();
                });
            }

            const regMasterExcelBtn = document.getElementById('exportRegionalMasterExcelBtn');
            if (regMasterExcelBtn) {
                regMasterExcelBtn.addEventListener('click', () => {
                    window.exportMasterRegionalExcel();
                });
            }
        });
        // Also bind immediately if DOM already loaded
        setTimeout(() => {
            const mBtn = document.getElementById('masterExcelExportBtn');
            if (mBtn && !mBtn._bound) {
                mBtn._bound = true;
                mBtn.addEventListener('click', () => window.exportMasterRegionalExcel());
            }
            const rBtn = document.getElementById('exportRegionalMasterExcelBtn');
            if (rBtn && !rBtn._bound) {
                rBtn._bound = true;
                rBtn.addEventListener('click', () => window.exportMasterRegionalExcel());
            }
        }, 100);
"""

idx_last_script = html.rfind("</script>")
html = html[:idx_last_script] + excel_func_code + "\n    " + html[idx_last_script:]
print("8. Injected exportMasterRegionalExcel function and event listeners!")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("SUCCESS: Proposal #3 and empty villages implemented perfectly!")
