import re

with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

start_idx = text.find("const comparisonData = {")
end_idx = text.find("function getVillageData", start_idx)

# Extract comparison part: from start_idx up to offset 3558 (before darband-gharbi)
block = text[start_idx:end_idx]

# Let's find maslavi in comparisonData
maslavi_idx = block.find("'maslavi': {")
maslavi_end = block.find("}", maslavi_idx) + 1
# And include projects line
projects_idx = block.find("projects: 'پوشش تحصیلی، توزیع بسته‌های معیشتی'", maslavi_idx)
maslavi_end = block.find("}", projects_idx) + 1

comp_part = block[:maslavi_end]

darband_comp_entry = """
                'darband-gharbi': {
                    name: 'دربند غربی',
                    dehestan: 'حومه غربی',
                    pop: '۲,۷۵۵ نفر',
                    families: '۶۸۱ خانوار',
                    avgFamily: '۴.۰۴ نفر',
                    schools: 'دبستان مرزداران (۱۷۷ دانش‌آموز)',
                    students: '۱۷۷ دانش‌آموز',
                    water: 'شبکه غدیر و آبرسانی روستایی',
                    health: 'خانه بهداشت فعال (۲۰۰ متر مربع)',
                    orphans: '۱۱ پرونده',
                    projects: 'حمایت از ۵۰ خانوار کم‌برخوردار و اشتغال پلاک ۱'
                }
            };"""

render_compare_code = """

            let selectedCompareVillages = ['soureh', 'pol-now', 'ariz', 'darband-gharbi'];
            function renderCompareTable() {
                if (!compareTableHead || !compareTableBody || !compareSelectorBar) return;
                // Render selector chips
                let selectorHtml = '<span style="font-size:12px; font-weight:800; color:var(--ink); margin-left:8px;">انتخاب جهت مقایسه:</span>';
                Object.keys(comparisonData).forEach(vId => {
                    const isChecked = selectedCompareVillages.includes(vId);
                    selectorHtml += `
                        <div class="compare-check-pill ${isChecked ? 'checked' : ''}" data-vid="${vId}">
                            <span>${isChecked ? '✓' : '+'}</span>
                            <span>${comparisonData[vId].name}</span>
                        </div>
                    `;
                });
                compareSelectorBar.innerHTML = selectorHtml;
                compareSelectorBar.querySelectorAll('.compare-check-pill').forEach(pill => {
                    pill.addEventListener('click', () => {
                        const vid = pill.getAttribute('data-vid');
                        if (selectedCompareVillages.includes(vid)) {
                            if (selectedCompareVillages.length > 1) {
                                selectedCompareVillages = selectedCompareVillages.filter(id => id !== vid);
                            } else {
                                showToast('حداقل یک روستا باید در مقایسه فعال باشد');
                            }
                        } else {
                            if (selectedCompareVillages.length < 4) {
                                selectedCompareVillages.push(vid);
                            } else {
                                showToast('حداکثر ۴ روستا به صورت همزمان قابل مقایسه هستند');
                            }
                        }
                        renderCompareTable();
                    });
                });

                // Build Table Head
                let headHtml = '<tr><th style="width:160px; min-width:160px;">شاخص / مشخصه</th>';
                selectedCompareVillages.forEach(vId => {
                    const c = comparisonData[vId];
                    if (c) {
                        headHtml += `<th style="text-align:center; min-width:150px;">${c.name}</th>`;
                    }
                });
                headHtml += '</tr>';
                compareTableHead.innerHTML = headHtml;

                // Build Table Body
                const rows = [
                    { label: 'دهستان', key: 'dehestan' },
                    { label: 'جمعیت کل', key: 'pop' },
                    { label: 'تعداد خانوار', key: 'families' },
                    { label: 'میانگین بعد خانوار', key: 'avgFamily' },
                    { label: 'واحدهای آموزشی', key: 'schools' },
                    { label: 'جمعیت دانش‌آموزی', key: 'students' },
                    { label: 'شبکه آب شرب', key: 'water' },
                    { label: 'خدمات بهداشتی', key: 'health' },
                    { label: 'ایتام و کم‌برخوردار', key: 'orphans' },
                    { label: 'پروژه‌های اولویت‌دار', key: 'projects' }
                ];

                let bodyHtml = '';
                rows.forEach(r => {
                    bodyHtml += `<tr><td style="font-weight:800; color:var(--ink);">${r.label}</td>`;
                    selectedCompareVillages.forEach(vId => {
                        const c = comparisonData[vId];
                        bodyHtml += `<td style="text-align:center;">${c ? (c[r.key] || '-') : '-'}</td>`;
                    });
                    bodyHtml += '</tr>';
                });
                compareTableBody.innerHTML = bodyHtml;
            }

            // Complete Village Analytical Database for Executive Dossier
            const villageDatabase = {
"""

# Now find the village objects in block from darband-gharbi onwards
darband_vdb_idx = block.find("'darband-gharbi': {", maslavi_end)
# We have darband-gharbi, soureh, pol-now, ariz, maslavi
# Then old duplicate darband-gharbi
# Then jadideh, sad-dastgah

# Let's find old darband-gharbi duplicate
old_dg_idx = block.find("'darband-gharbi': {", darband_vdb_idx + 20)
print("First darband-gharbi at:", darband_vdb_idx)
print("Old duplicate darband-gharbi at:", old_dg_idx)

# Find where old_dg ends (before jadideh)
jadideh_vdb_idx = block.find("'jadideh': {", old_dg_idx)

vdb_part1 = block[darband_vdb_idx:old_dg_idx]
# Trim trailing comma and whitespace
vdb_part1 = vdb_part1.rstrip().rstrip(',')

vdb_part2 = block[jadideh_vdb_idx:].rstrip()
# If vdb_part2 does not end with };, ensure it does
if vdb_part2.endswith("};"):
    pass
elif vdb_part2.endswith("}"):
    vdb_part2 += ";"
else:
    # Find last } in vdb_part2
    last_brace = vdb_part2.rfind("}")
    vdb_part2 = vdb_part2[:last_brace+1] + ";"

new_block = comp_part + "," + darband_comp_entry + render_compare_code + "                " + vdb_part1 + ",\n                " + vdb_part2 + "\n\n            "

new_text = text[:start_idx] + new_block + text[end_idx:]

with open("index.html", "w", encoding="utf-8") as f:
    f.write(new_text)

print("Successfully replaced block and restored villageDatabase!")
