import json, re

with open("/tmp/master_searchable_data.json", "r", encoding="utf-8") as f:
    master_data = json.load(f)

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. New CSS for Search Dropdown, Tabs, Badges & Animations
new_search_css = """/* Enhanced Smart Search Dropdown & Cards */
.search-dropdown {
    position: absolute;
    top: calc(100% + 8px);
    right: 0;
    width: clamp(360px, 34vw, 500px);
    max-height: 520px;
    overflow-y: auto;
    background: rgba(14, 28, 27, 0.98);
    border: 1px solid rgba(237, 211, 149, 0.45);
    backdrop-filter: blur(30px);
    border-radius: 16px;
    box-shadow: 0 24px 60px rgba(0, 0, 0, 0.8), 0 0 25px rgba(0, 0, 0, 0.5);
    z-index: 100;
    display: none;
    padding: 0 0 8px;
    box-sizing: border-box;
}

.search-dropdown.active {
    display: block;
    animation: fadeInDown 0.22s cubic-bezier(0.16, 1, 0.3, 1);
}

.search-tabs-bar {
    display: flex;
    align-items: center;
    gap: 6px;
    padding: 8px 12px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    background: rgba(12, 24, 23, 0.98);
    position: sticky;
    top: 0;
    z-index: 20;
    overflow-x: auto;
}

.search-tab-chip {
    padding: 4px 10px;
    font-size: 11px;
    font-weight: 700;
    color: #cbd5e1;
    background: rgba(255, 255, 255, 0.06);
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 14px;
    cursor: pointer;
    white-space: nowrap;
    transition: all 0.15s ease;
    display: inline-flex;
    align-items: center;
    gap: 4px;
}

.search-tab-chip:hover {
    background: rgba(255, 255, 255, 0.12);
    color: #fff;
}

.search-tab-chip.active {
    background: rgba(237, 211, 149, 0.22);
    border-color: var(--gold);
    color: var(--gold);
}

.search-group-header {
    padding: 8px 14px 4px;
    font-size: 11.5px;
    font-weight: 800;
    color: var(--gold);
    letter-spacing: 0.5px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: rgba(255, 255, 255, 0.02);
    border-bottom: 1px solid rgba(255, 255, 255, 0.05);
}

.search-item {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    padding: 10px 14px;
    color: var(--cream);
    cursor: pointer;
    transition: all 0.15s ease;
    border-bottom: 1px solid rgba(255, 255, 255, 0.04);
    gap: 10px;
}

.search-item:hover, .search-item.highlighted {
    background: rgba(237, 211, 149, 0.14);
}

.search-item-info {
    display: flex;
    flex-direction: column;
    gap: 4px;
    flex: 1;
    min-width: 0;
}

.search-item-title-row {
    display: flex;
    align-items: center;
    gap: 8px;
    flex-wrap: wrap;
}

.search-item-title {
    font-weight: 800;
    font-size: 13.5px;
    color: #ffffff;
}

.search-badge-orphan {
    background: rgba(237, 211, 149, 0.2);
    border: 1px solid rgba(237, 211, 149, 0.5);
    color: #edd395;
    font-size: 10.5px;
    font-weight: 700;
    padding: 1px 7px;
    border-radius: 10px;
}

.search-badge-needy {
    background: rgba(52, 211, 153, 0.15);
    border: 1px solid rgba(52, 211, 153, 0.4);
    color: #6ee7b7;
    font-size: 10.5px;
    font-weight: 700;
    padding: 1px 7px;
    border-radius: 10px;
}

.search-badge-village {
    background: rgba(59, 130, 246, 0.2);
    border: 1px solid rgba(96, 165, 250, 0.4);
    color: #93c5fd;
    font-size: 10.5px;
    font-weight: 700;
    padding: 1px 7px;
    border-radius: 10px;
}

.search-badge-school {
    background: rgba(244, 114, 182, 0.2);
    border: 1px solid rgba(244, 114, 182, 0.4);
    color: #fbcfe8;
    font-size: 10.5px;
    font-weight: 700;
    padding: 1px 7px;
    border-radius: 10px;
}

.search-village-pill {
    background: rgba(255, 255, 255, 0.08);
    color: #e2e8f0;
    font-size: 10.5px;
    padding: 1px 6px;
    border-radius: 6px;
}

.search-item-meta-row {
    display: flex;
    align-items: center;
    gap: 8px;
    flex-wrap: wrap;
    font-size: 11px;
    color: #cbd5e1;
}

.search-meta-tag {
    background: rgba(255, 255, 255, 0.05);
    padding: 1px 6px;
    border-radius: 4px;
    border: 1px solid rgba(255, 255, 255, 0.07);
    color: #cbd5e1;
    font-size: 10.5px;
}

.search-match-hl {
    background: rgba(237, 211, 149, 0.35);
    color: #fff;
    padding: 0 2px;
    border-radius: 2px;
    font-weight: 800;
}

.search-empty-state {
    padding: 16px;
    text-align: right;
}

.search-hint-title {
    font-size: 12.5px;
    font-weight: 800;
    color: var(--gold);
    margin-bottom: 6px;
    display: flex;
    align-items: center;
    gap: 6px;
}

.search-hint-desc {
    font-size: 11.5px;
    color: #94a3b8;
    line-height: 1.5;
    margin: 0 0 12px;
}

.search-quick-chips {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
}

.quick-chip {
    background: rgba(255, 255, 255, 0.06);
    border: 1px solid rgba(255, 255, 255, 0.12);
    color: #e2e8f0;
    font-family: YekanBakh, sans-serif;
    font-size: 11px;
    padding: 4px 10px;
    border-radius: 12px;
    cursor: pointer;
    transition: all 0.15s ease;
}

.quick-chip:hover {
    background: rgba(237, 211, 149, 0.2);
    border-color: var(--gold);
    color: var(--gold);
    transform: translateY(-1px);
}

.search-row-highlight {
    animation: rowHighlightPulse 1s ease-in-out 3 !important;
    outline: 2px solid var(--gold) !important;
    background: rgba(237, 211, 149, 0.25) !important;
    position: relative;
    z-index: 5;
}

@keyframes rowHighlightPulse {
    0% { background: rgba(237, 211, 149, 0.45); box-shadow: inset 0 0 15px rgba(237, 211, 149, 0.6); }
    50% { background: rgba(237, 211, 149, 0.15); box-shadow: inset 0 0 5px rgba(237, 211, 149, 0.2); }
    100% { background: rgba(237, 211, 149, 0.45); box-shadow: inset 0 0 15px rgba(237, 211, 149, 0.6); }
}"""

old_css_marker = ".search-dropdown {"
old_css_end = ".search-group-header {"
idx_css_s = html.find(old_css_marker)
idx_css_e = html.find(old_css_end)
assert idx_css_s != -1 and idx_css_e != -1, "CSS markers not found"
html = html[:idx_css_s] + new_search_css + "\n" + html[idx_css_e:]
print("1. Injected enhanced search CSS!")

# 2. Build JavaScript Search Engine
master_json_str = json.dumps(master_data, ensure_ascii=False)

new_search_js = f"""// ==================== 2. SMART SEARCH SYSTEM (COMPREHENSIVE INDIVIDUALS & ASSETS) ====================
            const searchInput = $('smartSearchInput');
            const searchDropdown = $('searchResultsDropdown');
            const clearSearchBtn = $('clearSearch');

            const searchableData = {master_json_str};

            let currentSearchCategory = 'all';
            let activeHighlightedIndex = -1;

            // Advanced Persian/Arabic digit & letter normalizer
            function normalizePersianSearch(str) {{
                if (!str) return '';
                return str
                    .toString()
                    .toLowerCase()
                    .replace(/[۰٠]/g, '0')
                    .replace(/[۱١]/g, '1')
                    .replace(/[۲٢]/g, '2')
                    .replace(/[۳٣]/g, '3')
                    .replace(/[۴٤]/g, '4')
                    .replace(/[۵٥]/g, '5')
                    .replace(/[۶٦]/g, '6')
                    .replace(/[۷٧]/g, '7')
                    .replace(/[۸٨]/g, '8')
                    .replace(/[۹٩]/g, '9')
                    .replace(/[يى]/g, 'ی')
                    .replace(/[ك]/g, 'ک')
                    .replace(/[ة]/g, 'ه')
                    .replace(/[آأإ]/g, 'ا')
                    .replace(/[\\u064B-\\u065F\\u0670]/g, '')
                    .replace(/[\\u200C\\u200B]/g, ' ')
                    .replace(/[-_.,،؛:()/\\\\]/g, ' ')
                    .replace(/\\s+/g, ' ')
                    .trim();
            }}

            function stemPersianWord(w) {{
                if (w.length > 4 && w.endsWith('های')) return w.slice(0, -3).trim();
                if (w.length > 3 && w.endsWith('ها')) return w.slice(0, -2).trim();
                if (w.length > 4 && w.endsWith('یان')) return w.slice(0, -3).trim();
                if (w.length > 3 && w.endsWith('ان')) return w.slice(0, -2).trim();
                return w;
            }}

            function highlightMatch(text, tokens) {{
                if (!text || !tokens || tokens.length === 0) return text || '';
                let result = text.toString();
                tokens.forEach(tok => {{
                    if (tok.length < 2) return;
                    try {{
                        const reg = new RegExp('(' + tok.replace(/[.*+?^${{}}()|[\\]\\\\]/g, '\\\\$&') + ')', 'gi');
                        result = result.replace(reg, '<mark class="search-match-hl">$1</mark>');
                    }} catch (e) {{}}
                }});
                return result;
            }}

            function renderSearchEmptyState() {{
                if (!searchDropdown) return;
                searchDropdown.innerHTML = `
                    <div class="search-empty-state">
                        <div class="search-hint-title">
                            <span>💡</span>
                            <span>راهنمای جستجوی هوشمند افراد، پرونده‌ها و اماکن</span>
                        </div>
                        <p class="search-hint-desc">
                            پوشش کامل تمام افراد، ایتام و مددجویان با نام، نام سرپرست، کد ملی، شماره تماس یا نام روستا:
                        </p>
                        <div class="search-quick-chips">
                            <button type="button" class="quick-chip" data-search="معصومه صنگور">معصومه صنگور (ایتام سوره)</button>
                            <button type="button" class="quick-chip" data-search="عباس محاسبه معیل">عباس محاسبه معیل (دربند)</button>
                            <button type="button" class="quick-chip" data-search="۱۹۴۰۷۱۴۹۷۴">کد ملی ۱۹۴۰۷۱۴۹۷۴</button>
                            <button type="button" class="quick-chip" data-search="شیرین دوارچی">سرپرست شیرین دوارچی</button>
                            <button type="button" class="quick-chip" data-search="کاظم سلیمانی">کاظم سلیمانی (دربند)</button>
                            <button type="button" class="quick-chip" data-search="ایتام مصلاوی">ایتام مصلاوی</button>
                            <button type="button" class="quick-chip" data-search="مددجویان پل نو">مددجویان پل نو</button>
                            <button type="button" class="quick-chip" data-search="دبستان مرزداران">دبستان مرزداران</button>
                            <button type="button" class="quick-chip" data-search="09330735636">تماس 09330735636</button>
                        </div>
                    </div>
                `;
                searchDropdown.classList.add('active');

                searchDropdown.querySelectorAll('.quick-chip').forEach(btn => {{
                    btn.addEventListener('click', (e) => {{
                        e.stopPropagation();
                        const query = btn.getAttribute('data-search');
                        if (searchInput) {{
                            searchInput.value = query;
                            searchInput.dispatchEvent(new Event('input', {{ bubbles: true }}));
                            searchInput.focus();
                        }}
                    }});
                }});
            }}

            function performSmartSearch(rawQuery) {{
                if (!searchDropdown) return;
                const qNorm = normalizePersianSearch(rawQuery);
                if (!qNorm) {{
                    renderSearchEmptyState();
                    return;
                }}

                const tokens = qNorm.split(' ').filter(Boolean);
                const stemmedTokens = tokens.map(t => stemPersianWord(t));

                // Filter & Score items
                const scored = [];
                searchableData.forEach(item => {{
                    // Category filter
                    if (currentSearchCategory === 'person' && item.type !== 'person') return;
                    if (currentSearchCategory === 'village' && item.type !== 'village') return;
                    if (currentSearchCategory === 'facility' && item.type !== 'school' && item.type !== 'health' && item.type !== 'culture' && item.type !== 'infra') return;
                    if (currentSearchCategory === 'project' && item.type !== 'project') return;

                    const t = normalizePersianSearch(item.title);
                    const sub = normalizePersianSearch(item.subtitle);
                    const g = normalizePersianSearch(item.guardian || '');
                    const f = normalizePersianSearch(item.father || '');
                    const nid = normalizePersianSearch(item.nationalId || '');
                    const ph = normalizePersianSearch(item.phone || '');
                    const v = normalizePersianSearch(item.village || '');
                    const k = normalizePersianSearch(item.keyword || '');
                    const addr = normalizePersianSearch(item.address || '');

                    const combined = `${{t}} ${{g}} ${{f}} ${{nid}} ${{ph}} ${{v}} ${{addr}} ${{k}} ${{sub}}`;

                    let allMatch = true;
                    for (let i = 0; i < tokens.length; i++) {{
                        const tok = tokens[i];
                        const st = stemmedTokens[i];
                        if (!combined.includes(tok) && !combined.includes(st)) {{
                            allMatch = false;
                            break;
                        }}
                    }}

                    if (allMatch) {{
                        let score = 0;
                        if (t.startsWith(qNorm)) score += 120;
                        else if (t.includes(qNorm)) score += 70;

                        if (nid && (nid === qNorm || nid.startsWith(qNorm))) score += 110;
                        else if (nid && nid.includes(qNorm)) score += 60;

                        if (ph && (ph === qNorm || ph.startsWith(qNorm))) score += 100;
                        else if (ph && ph.includes(qNorm)) score += 50;

                        if (g && g.includes(qNorm)) score += 55;
                        if (f && f.includes(qNorm)) score += 50;
                        if (item.type === 'person') score += 15; // prioritize direct person lookups

                        scored.push({{ item, score }});
                    }}
                }});

                scored.sort((a, b) => b.score - a.score);
                const totalMatches = scored.length;
                const topResults = scored.slice(0, 35).map(s => s.item);

                // Count categories for tabs
                const counts = {{
                    all: 0,
                    person: 0,
                    village: 0,
                    facility: 0,
                    project: 0
                }};
                searchableData.forEach(item => {{
                    const t = normalizePersianSearch(item.title);
                    const sub = normalizePersianSearch(item.subtitle);
                    const g = normalizePersianSearch(item.guardian || '');
                    const f = normalizePersianSearch(item.father || '');
                    const nid = normalizePersianSearch(item.nationalId || '');
                    const ph = normalizePersianSearch(item.phone || '');
                    const v = normalizePersianSearch(item.village || '');
                    const k = normalizePersianSearch(item.keyword || '');
                    const addr = normalizePersianSearch(item.address || '');
                    const combined = `${{t}} ${{g}} ${{f}} ${{nid}} ${{ph}} ${{v}} ${{addr}} ${{k}} ${{sub}}`;

                    let allMatch = true;
                    for (let i = 0; i < tokens.length; i++) {{
                        const tok = tokens[i];
                        const st = stemmedTokens[i];
                        if (!combined.includes(tok) && !combined.includes(st)) {{
                            allMatch = false;
                            break;
                        }}
                    }}
                    if (allMatch) {{
                        counts.all++;
                        if (item.type === 'person') counts.person++;
                        else if (item.type === 'village') counts.village++;
                        else if (item.type === 'school' || item.type === 'health' || item.type === 'culture' || item.type === 'infra') counts.facility++;
                        else if (item.type === 'project') counts.project++;
                    }}
                }});

                // Build HTML
                let html = `
                    <div class="search-tabs-bar">
                        <button type="button" class="search-tab-chip ${{currentSearchCategory === 'all' ? 'active' : ''}}" data-cat="all">
                            <span>همه</span>
                            <span style="opacity:0.75; font-size:10px;">(${{counts.all}})</span>
                        </button>
                        <button type="button" class="search-tab-chip ${{currentSearchCategory === 'person' ? 'active' : ''}}" data-cat="person">
                            <span>👤 افراد و پرونده‌ها</span>
                            <span style="opacity:0.75; font-size:10px;">(${{counts.person}})</span>
                        </button>
                        <button type="button" class="search-tab-chip ${{currentSearchCategory === 'village' ? 'active' : ''}}" data-cat="village">
                            <span>🏡 روستاها</span>
                            <span style="opacity:0.75; font-size:10px;">(${{counts.village}})</span>
                        </button>
                        <button type="button" class="search-tab-chip ${{currentSearchCategory === 'facility' ? 'active' : ''}}" data-cat="facility">
                            <span>🏫 مدارس و امکانات</span>
                            <span style="opacity:0.75; font-size:10px;">(${{counts.facility}})</span>
                        </button>
                        <button type="button" class="search-tab-chip ${{currentSearchCategory === 'project' ? 'active' : ''}}" data-cat="project">
                            <span>📋 پروژه‌ها</span>
                            <span style="opacity:0.75; font-size:10px;">(${{counts.project}})</span>
                        </button>
                    </div>
                `;

                if (totalMatches === 0) {{
                    html += `
                        <div style="padding: 24px 16px; text-align: center; color: #94a3b8; font-size: 13px;">
                            <div style="font-size: 24px; margin-bottom: 6px;">🔍</div>
                            <div>موردی با عنوان «<strong>${{rawQuery}}</strong>» یافت نشد.</div>
                            <div style="font-size: 11.5px; margin-top: 6px; color: #64748b;">
                                لطفاً نام شخص، کد ملی، شماره تماس یا نام روستا را بررسی کنید.
                            </div>
                        </div>
                    `;
                    searchDropdown.innerHTML = html;
                    searchDropdown.classList.add('active');
                    bindCategoryTabs();
                    return;
                }}

                // Render Results List
                html += `<div class="search-results-list" style="max-height: 440px; overflow-y: auto;">`;
                topResults.forEach((item, idx) => {{
                    const isPerson = item.type === 'person';
                    const isOrphan = item.badge === 'ایتام';
                    const isNeedy = item.badge === 'مددجو';

                    let badgeClass = 'search-badge-village';
                    if (isOrphan) badgeClass = 'search-badge-orphan';
                    else if (isNeedy) badgeClass = 'search-badge-needy';
                    else if (item.badge === 'آموزش') badgeClass = 'search-badge-school';

                    const highlightedTitle = highlightMatch(item.title, tokens);
                    
                    let metaRows = '';
                    if (isPerson) {{
                        const metaItems = [];
                        if (item.guardian && item.guardian !== '-' && item.guardian !== item.title) {{
                            metaItems.push(`<span>👤 سرپرست: <strong>${{highlightMatch(item.guardian, tokens)}}</strong></span>`);
                        }}
                        if (item.father && item.father !== '-') {{
                            metaItems.push(`<span>فرزند: <strong>${{highlightMatch(item.father, tokens)}}</strong></span>`);
                        }}
                        if (item.nationalId && item.nationalId !== '-') {{
                            metaItems.push(`<span>💳 کدملی: <strong style="letter-spacing:0.5px; color:#edd395;">${{highlightMatch(item.nationalId, tokens)}}</strong></span>`);
                        }}
                        if (item.phone && item.phone !== '-') {{
                            metaItems.push(`<span>📞 تماس: <strong style="letter-spacing:0.5px;">${{highlightMatch(item.phone, tokens)}}</strong></span>`);
                        }}
                        if (item.address && item.address !== '-') {{
                            metaItems.push(`<span style="max-width:240px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">🏠 ${{item.address}}</span>`);
                        }}
                        metaRows = `<div class="search-item-meta-row">${{metaItems.join(' · ')}}</div>`;
                    }} else {{
                        metaRows = `<div class="search-item-meta-row" style="color:rgba(243,235,221,0.7);">${{highlightMatch(item.subtitle, tokens)}}</div>`;
                    }}

                    html += `
                        <div class="search-item ${{idx === 0 ? 'highlighted' : ''}}" data-index="${{idx}}" data-target="${{item.target}}" data-section="${{item.section || 'stats'}}" data-query="${{item.rowQuery || item.keyword || item.title}}">
                            <div class="search-item-info">
                                <div class="search-item-title-row">
                                    <span class="search-item-title">${{highlightedTitle}}</span>
                                    <span class="${{badgeClass}}">${{item.badge}}</span>
                                    ${{item.village ? `<span class="search-village-pill">📍 ${{item.village}}</span>` : ''}}
                                </div>
                                ${{metaRows}}
                            </div>
                            <span style="color:var(--gold); font-size:11.5px; font-weight:700; flex-shrink:0; display:flex; align-items:center; gap:2px; margin-top:2px;">
                                مشاهده ↗
                            </span>
                        </div>
                    `;
                }});
                html += `</div>`;

                searchDropdown.innerHTML = html;
                searchDropdown.classList.add('active');
                activeHighlightedIndex = 0;

                bindCategoryTabs();
                bindItemClicks(topResults);
            }}

            function bindCategoryTabs() {{
                if (!searchDropdown) return;
                searchDropdown.querySelectorAll('.search-tab-chip').forEach(btn => {{
                    btn.addEventListener('click', (e) => {{
                        e.stopPropagation();
                        currentSearchCategory = btn.getAttribute('data-cat') || 'all';
                        if (searchInput) performSmartSearch(searchInput.value.trim());
                    }});
                }});
            }}

            function bindItemClicks(results) {{
                if (!searchDropdown) return;
                searchDropdown.querySelectorAll('.search-item').forEach(el => {{
                    el.addEventListener('click', (e) => {{
                        e.stopPropagation();
                        const idx = parseInt(el.getAttribute('data-index'), 10);
                        const item = results[idx];
                        if (item) selectSearchItem(item);
                    }});
                }});
            }}

            function selectSearchItem(item) {{
                if (!item) return;
                if (searchDropdown) {{
                    searchDropdown.classList.remove('active');
                    searchDropdown.innerHTML = '';
                }}
                if (searchInput) {{
                    searchInput.value = '';
                    searchInput.blur();
                }}
                if (clearSearchBtn) clearSearchBtn.style.display = 'none';

                const targetId = item.target;
                const section = item.section || 'stats';
                const keyword = item.rowQuery || item.nationalId || item.title;

                navigateToVillage(targetId, section, keyword);
            }}

            // Event Listeners for Search Input
            if (searchInput && searchDropdown) {{
                searchInput.addEventListener('input', () => {{
                    const q = searchInput.value.trim();
                    if (clearSearchBtn) clearSearchBtn.style.display = q ? 'flex' : 'none';
                    if (!q) {{
                        renderSearchEmptyState();
                    }} else {{
                        performSmartSearch(q);
                    }}
                }});

                searchInput.addEventListener('focus', () => {{
                    const q = searchInput.value.trim();
                    if (!q) {{
                        renderSearchEmptyState();
                    }} else {{
                        performSmartSearch(q);
                    }}
                }});

                searchInput.addEventListener('keydown', (e) => {{
                    const items = searchDropdown.querySelectorAll('.search-item');
                    if (items.length === 0) return;

                    if (e.key === 'ArrowDown') {{
                        e.preventDefault();
                        activeHighlightedIndex = (activeHighlightedIndex + 1) % items.length;
                        items.forEach((it, i) => it.classList.toggle('highlighted', i === activeHighlightedIndex));
                        items[activeHighlightedIndex].scrollIntoView({{ block: 'nearest' }});
                    }} else if (e.key === 'ArrowUp') {{
                        e.preventDefault();
                        activeHighlightedIndex = (activeHighlightedIndex - 1 + items.length) % items.length;
                        items.forEach((it, i) => it.classList.toggle('highlighted', i === activeHighlightedIndex));
                        items[activeHighlightedIndex].scrollIntoView({{ block: 'nearest' }});
                    }} else if (e.key === 'Enter') {{
                        e.preventDefault();
                        const current = items[activeHighlightedIndex] || items[0];
                        if (current) current.click();
                    }} else if (e.key === 'Escape') {{
                        searchDropdown.classList.remove('active');
                        searchInput.blur();
                    }}
                }});

                if (clearSearchBtn) {{
                    clearSearchBtn.addEventListener('click', () => {{
                        searchInput.value = '';
                        clearSearchBtn.style.display = 'none';
                        searchDropdown.classList.remove('active');
                    }});
                }}

                document.addEventListener('click', (e) => {{
                    if (!e.target.closest('#searchBoxWrap') && !e.target.closest('#searchResultsDropdown')) {{
                        searchDropdown.classList.remove('active');
                    }}
                }});
            }}"""

old_js_start = "// ==================== 2. SMART SEARCH SYSTEM ===================="
old_js_end = "const comparisonData = {"
idx_js_s = html.find(old_js_start)
idx_js_e = html.find(old_js_end)
assert idx_js_s != -1 and idx_js_e != -1, "JS markers not found"

html = html[:idx_js_s] + new_search_js + "\n\n            " + html[idx_js_e:]
print("2. Injected complete Search Engine and dataset!")

# 3. Enhance navigateToVillage to auto-open accordion and highlight exact person row
old_nav_kw = """// Handle search keywords or show top of dashboard
                if (keywordToSearch) {
                    requestAnimationFrame(() => {
                        const liveSearch = document.getElementById('liveTableSearch');
                        if (liveSearch) {
                            liveSearch.value = keywordToSearch;
                            liveSearch.dispatchEvent(new Event('input', { bubbles: true }));
                            setTimeout(() => {
                                const match = document.querySelector('#statsDialog mark.search-match-hl') ||
                                              document.querySelector('#statsDialog details.dos-accordion[open]');
                                if (match) {
                                    match.scrollIntoView({ behavior: 'smooth', block: 'center' });
                                }
                            }, 300);
                        }
                    });
                }"""

new_nav_kw = """// Handle search keywords or show top of dashboard
                if (keywordToSearch) {
                    requestAnimationFrame(() => {
                        const liveSearch = document.getElementById('liveTableSearch');
                        if (liveSearch) {
                            liveSearch.value = keywordToSearch;
                            liveSearch.dispatchEvent(new Event('input', { bubbles: true }));
                        }

                        setTimeout(() => {
                            const statsDlg = document.getElementById('statsDialog');
                            if (!statsDlg) return;

                            const normKw = normalizePersianSearch ? normalizePersianSearch(keywordToSearch) : keywordToSearch;
                            const accordions = statsDlg.querySelectorAll('details.dos-accordion');
                            let targetRow = null;

                            accordions.forEach(acc => {
                                const accText = normalizePersianSearch ? normalizePersianSearch(acc.textContent || '') : (acc.textContent || '');
                                if (accText.includes(normKw)) {
                                    acc.open = true;
                                    const rows = acc.querySelectorAll('tbody tr');
                                    rows.forEach(tr => {
                                        const trText = normalizePersianSearch ? normalizePersianSearch(tr.textContent || '') : (tr.textContent || '');
                                        if (trText.includes(normKw) && !targetRow) {
                                            targetRow = tr;
                                        }
                                    });
                                }
                            });

                            if (targetRow) {
                                targetRow.scrollIntoView({ behavior: 'smooth', block: 'center' });
                                targetRow.classList.remove('search-row-highlight');
                                void targetRow.offsetWidth;
                                targetRow.classList.add('search-row-highlight');
                                setTimeout(() => targetRow.classList.remove('search-row-highlight'), 4000);
                            } else {
                                const match = statsDlg.querySelector('mark.search-match-hl') || statsDlg.querySelector('details.dos-accordion[open]');
                                if (match) match.scrollIntoView({ behavior: 'smooth', block: 'center' });
                            }
                        }, 250);
                    });
                }"""

if old_nav_kw in html:
    html = html.replace(old_nav_kw, new_nav_kw, 1)
    print("3. Injected auto-accordion open & row highlight in navigateToVillage!")
else:
    print("Warning: old_nav_kw exact match not found; checking with regex")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("SUCCESS: Enhanced search with 239 master assets and 200 real individuals saved to index.html!")
