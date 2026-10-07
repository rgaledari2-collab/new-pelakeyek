with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Add Excel/CSV Export and Print Buttons in statsDialog header
old_acc_btns = """<div style="display:flex; gap:8px;">
                                <button id="btnOpenAllAccs" style="background:#fdfcf9; border:1px solid #c6a15b; color:#142a29; font-weight:800; font-size:11px; padding:5px 12px; border-radius:8px; cursor:pointer; transition:all 0.15s ease;">⤢ باز کردن همه</button>
                                <button id="btnCloseAllAccs" style="background:#fff; border:1px solid #d9ccb4; color:#5c6e6a; font-weight:700; font-size:11px; padding:5px 12px; border-radius:8px; cursor:pointer; transition:all 0.15s ease;">⤡ بستن همه</button>
                            </div>"""

new_acc_btns = """<div style="display:flex; align-items:center; gap:8px; flex-wrap:wrap;">
                                <button id="btnExportTablesCsv" type="button" style="background:#f0fdf4; border:1px solid #86efac; color:#166534; font-weight:800; font-size:11px; padding:5px 12px; border-radius:8px; cursor:pointer; display:inline-flex; align-items:center; gap:5px; transition:all 0.15s ease;" title="دریافت فایل اکسل / CSV جداول آماری و پرونده‌ها">
                                    <span>📊</span>
                                    <span>خروجی اکسل (CSV)</span>
                                </button>
                                <button id="btnPrintDossierA4" type="button" style="background:#fefce8; border:1px solid #fde047; color:#854d0e; font-weight:800; font-size:11px; padding:5px 12px; border-radius:8px; cursor:pointer; display:inline-flex; align-items:center; gap:5px; transition:all 0.15s ease;" title="چاپ کارنامه آماری رسمی روستا">
                                    <span>🖨️</span>
                                    <span>چاپ کارنامه A4</span>
                                </button>
                                <button id="btnOpenAllAccs" type="button" style="background:#fdfcf9; border:1px solid #c6a15b; color:#142a29; font-weight:800; font-size:11px; padding:5px 12px; border-radius:8px; cursor:pointer; transition:all 0.15s ease;">⤢ باز کردن همه</button>
                                <button id="btnCloseAllAccs" type="button" style="background:#fff; border:1px solid #d9ccb4; color:#5c6e6a; font-weight:700; font-size:11px; padding:5px 12px; border-radius:8px; cursor:pointer; transition:all 0.15s ease;">⤡ بستن همه</button>
                            </div>"""

assert old_acc_btns in html, "old_acc_btns not found"
html = html.replace(old_acc_btns, new_acc_btns, 1)
print("1. Added Export CSV and Print buttons to village tables header!")

# 2. Add JavaScript handlers for Export CSV and Print A4 in statsDialog
export_csv_js = """
            // ========================================================
            // STATISTICAL DATA EXPORT (خروجی اکسل / CSV جداول آماری روستا)
            // ========================================================
            function exportVillageTablesToCsv() {
                const wrap = document.getElementById('villageAccordionsWrap');
                if (!wrap) return;
                const villageTitleEl = document.getElementById('sideVillageName');
                const vName = villageTitleEl ? villageTitleEl.textContent.trim() : 'روستا';

                const tables = wrap.querySelectorAll('table');
                if (tables.length === 0) {
                    if (typeof showSearchToast === 'function') {
                        showSearchToast('جدول اطلاعاتی جهت دریافت خروجی یافت نشد.');
                    }
                    return;
                }

                let csvContent = '\\uFEFF'; // UTF-8 BOM for Persian in Excel
                csvContent += `شناسنامه آماری و پرونده‌های میدانی - روستای ${vName}\\r\\n`;
                csvContent += `تاریخ گزارش: ${new Intl.DateTimeFormat('fa-IR').format(new Date())}\\r\\n\\r\\n`;

                tables.forEach((tbl, idx) => {
                    // Find table title from closest details summary or h3
                    const details = tbl.closest('details.dos-accordion');
                    let tableTitle = `جدول آماری ${idx + 1}`;
                    if (details) {
                        const sum = details.querySelector('summary h2, summary h3, summary');
                        if (sum) tableTitle = sum.textContent.replace(/\\s+/g, ' ').trim();
                    }
                    csvContent += `[${tableTitle}]\\r\\n`;

                    const rows = tbl.querySelectorAll('tr');
                    rows.forEach(r => {
                        const cols = r.querySelectorAll('th, td');
                        const rowData = [];
                        cols.forEach(c => {
                            let text = c.textContent.replace(/"/g, '""').replace(/\\s+/g, ' ').trim();
                            rowData.push(`"${text}"`);
                        });
                        if (rowData.length > 0) {
                            csvContent += rowData.join(',') + '\\r\\n';
                        }
                    });
                    csvContent += '\\r\\n';
                });

                const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
                const url = URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.href = url;
                a.download = `شناسنامه_آماری_${vName}_${new Date().toISOString().slice(0,10)}.csv`;
                document.body.appendChild(a);
                a.click();
                document.body.removeChild(a);
                URL.revokeObjectURL(url);

                if (typeof showSearchToast === 'function') {
                    showSearchToast(`✓ خروجی اکسل (CSV) روستای ${vName} با موفقیت دانلود شد.`);
                }
            }

            // Bind click listener to dynamically rendered export button
            document.addEventListener('click', (e) => {
                if (e.target && e.target.closest('#btnExportTablesCsv')) {
                    exportVillageTablesToCsv();
                } else if (e.target && e.target.closest('#btnPrintDossierA4')) {
                    window.print();
                }
            });
"""

# Insert export_csv_js right before togglePureMapMode
pure_map_marker = "function togglePureMapMode(enable)"
idx_pm = html.find(pure_map_marker)
assert idx_pm != -1, "togglePureMapMode not found"
html = html[:idx_pm] + export_csv_js + "\n\n            " + html[idx_pm:]
print("2. Added exportVillageTablesToCsv JavaScript logic!")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("SUCCESS: Statistical export features integrated into index.html!")
