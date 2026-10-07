import json, re

with open("/tmp/master_searchable_data.json", "r", encoding="utf-8") as f:
    master_data = json.load(f)

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

master_json_str = json.dumps(master_data, ensure_ascii=False)

new_js = f"""// ==================== 2. SMART SEARCH SYSTEM (PHONETIC FUZZY + DEDICATED BENEFICIARY DOSSIER) ====================
            const searchInput = $('smartSearchInput');
            const searchDropdown = $('searchResultsDropdown');
            const clearSearchBtn = $('clearSearch');

            const searchableData = {master_json_str};

            let currentSearchCategory = 'all';
            let activeHighlightedIndex = -1;
            let currentSelectedPerson = null;

            // Toast helper
            function showSearchToast(message) {{
                let toast = document.getElementById('searchGlobalToast');
                if (!toast) {{
                    toast = document.createElement('div');
                    toast.id = 'searchGlobalToast';
                    toast.className = 'search-toast';
                    document.body.appendChild(toast);
                }}
                toast.textContent = message;
                toast.classList.add('show');
                setTimeout(() => toast.classList.remove('show'), 2800);
            }}

            // Advanced Persian/Arabic normalizer
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

            // Phonetic phonetic/typo-tolerant representation
            function phoneticPersian(str) {{
                if (!str) return '';
                let s = normalizePersianSearch(str);
                const pMap = {{
                    'ص': 'س', 'ث': 'س',
                    'ط': 'ت',
                    'ض': 'ز', 'ظ': 'ز', 'ذ': 'ز',
                    'ح': 'ه',
                    'ق': 'غ',
                    'ع': 'ا'
                }};
                let res = '';
                for (let ch of s) {{
                    res += pMap[ch] || ch;
                }}
                return res.replace(/\\s+/g, ' ').trim();
            }}

            function stemPersianWord(w) {{
                if (w.length > 4 && w.endsWith('های')) return w.slice(0, -3).trim();
                if (w.length > 3 && w.endsWith('ها')) return w.slice(0, -2).trim();
                if (w.length > 4 && w.endsWith('یان')) return w.slice(0, -3).trim();
                if (w.length > 3 && w.endsWith('ان')) return w.slice(0, -2).trim();
                return w;
            }}

            // Recent Searches in LocalStorage
            function getRecentSearches() {{
                try {{
                    const s = localStorage.getItem('shalamcheh_recent_searches');
                    return s ? JSON.parse(s) : [];
                }} catch (e) {{
                    return [];
                }}
            }}

            function saveRecentSearch(term) {{
                if (!term || term.length < 2) return;
                try {{
                    let recents = getRecentSearches().filter(t => t !== term);
                    recents.unshift(term);
                    if (recents.length > 6) recents = recents.slice(0, 6);
                    localStorage.setItem('shalamcheh_recent_searches', JSON.stringify(recents));
                }} catch (e) {{}}
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

            // Render Empty State & Suggestions
            function renderSearchEmptyState() {{
                if (!searchDropdown) return;
                const recents = getRecentSearches();

                let recentHtml = '';
                if (recents.length > 0) {{
                    recentHtml = `
                        <div style="margin-bottom: 14px;">
                            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
                                <span style="font-size:11.5px; font-weight:800; color:var(--gold);">🕒 جستجوهای اخیر شما:</span>
                                <button type="button" id="clearRecentSearchesBtn" style="background:none; border:none; color:#94a3b8; font-size:10.5px; cursor:pointer; text-decoration:underline;">پاک کردن</button>
                            </div>
                            <div class="search-quick-chips">
                                ${{recents.map(r => `<button type="button" class="quick-chip recent-chip" data-search="${{r}}">${{r}} ✕</button>`).join('')}}
                            </div>
                        </div>
                    `;
                }}

                searchDropdown.innerHTML = `
                    <div class="search-empty-state">
                        ${{recentHtml}}
                        <div class="search-hint-title">
                            <span>💡</span>
                            <span>پیشنهادات هوشمند جستجوی پرونده‌ها و اماکن:</span>
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
                            <button type="button" class="quick-chip" data-search="فاطمه ناصری">فاطمه ناصری (مصلاوی)</button>
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

                const clearBtn = searchDropdown.querySelector('#clearRecentSearchesBtn');
                if (clearBtn) {{
                    clearBtn.addEventListener('click', (e) => {{
                        e.stopPropagation();
                        localStorage.removeItem('shalamcheh_recent_searches');
                        renderSearchEmptyState();
                    }});
                }}
            }}

            // Perform Smart Multi-Token & Phonetic Search
            function performSmartSearch(rawQuery) {{
                if (!searchDropdown) return;
                const qNorm = normalizePersianSearch(rawQuery);
                if (!qNorm) {{
                    renderSearchEmptyState();
                    return;
                }}

                const tokens = qNorm.split(' ').filter(Boolean);
                const stemmedTokens = tokens.map(t => stemPersianWord(t));
                const phoneticTokens = tokens.map(t => phoneticPersian(t));
                const qPhone = phoneticPersian(rawQuery);

                // Digit-only query for phone or national ID
                const rawDigits = rawQuery.replace(/[^0-9۰-۹]/g, '');
                const normDigits = normalizePersianSearch(rawDigits);

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
                    const combinedPhone = phoneticPersian(combined);

                    // Check token matching (Exact, Stemmed, or Phonetic)
                    let allMatch = true;
                    let isPhoneticMatch = false;

                    for (let i = 0; i < tokens.length; i++) {{
                        const tok = tokens[i];
                        const st = stemmedTokens[i];
                        const phTok = phoneticTokens[i];

                        if (combined.includes(tok) || combined.includes(st)) {{
                            // exact or stemmed hit
                        }} else if (combinedPhone.includes(phTok)) {{
                            isPhoneticMatch = true;
                        }} else {{
                            allMatch = false;
                            break;
                        }}
                    }}

                    // Partial Phone match (e.g. 933073 matching 09330735636)
                    let isDigitMatch = false;
                    if (normDigits.length >= 4) {{
                        const rawNid = nid.replace(/\\D/g, '');
                        const rawPh = ph.replace(/\\D/g, '');
                        if (rawNid.includes(normDigits) || rawPh.includes(normDigits)) {{
                            allMatch = true;
                            isDigitMatch = true;
                        }}
                    }}

                    if (allMatch) {{
                        let score = 0;
                        if (t.startsWith(qNorm)) score += 140;
                        else if (t.includes(qNorm)) score += 80;

                        if (nid && (nid === qNorm || nid.startsWith(qNorm))) score += 150;
                        else if (nid && nid.includes(qNorm)) score += 85;

                        if (ph && (ph === qNorm || ph.startsWith(qNorm) || ph.includes(qNorm))) score += 110;

                        if (isDigitMatch) score += 95;
                        if (g && g.includes(qNorm)) score += 65;
                        if (f && f.includes(qNorm)) score += 55;
                        if (item.type === 'person') score += 25; // boost direct person lookup
                        if (isPhoneticMatch) score -= 15; // slightly lower than exact hit

                        scored.push({{ item, score }});
                    }}
                }});

                scored.sort((a, b) => b.score - a.score);
                const totalMatches = scored.length;
                const topResults = scored.slice(0, 40).map(s => s.item);

                // Category counts
                const counts = {{ all: 0, person: 0, village: 0, facility: 0, project: 0 }};
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
                    const combinedPhone = phoneticPersian(combined);

                    let m = true;
                    for (let i = 0; i < tokens.length; i++) {{
                        if (!combined.includes(tokens[i]) && !combined.includes(stemmedTokens[i]) && !combinedPhone.includes(phoneticTokens[i])) {{
                            m = false; break;
                        }}
                    }}
                    if (normDigits.length >= 4 && (nid.replace(/\\D/g, '').includes(normDigits) || ph.replace(/\\D/g, '').includes(normDigits))) {{
                        m = true;
                    }}
                    if (m) {{
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
                            <div>موردی با عبارت «<strong>${{rawQuery}}</strong>» یافت نشد.</div>
                            <div style="font-size: 11.5px; margin-top: 6px; color: #64748b;">
                                می‌توانید با نام، نام سرپرست، کد ملی، شماره تماس یا نام روستا جستجو کنید.
                            </div>
                        </div>
                    `;
                    searchDropdown.innerHTML = html;
                    searchDropdown.classList.add('active');
                    bindCategoryTabs();
                    return;
                }}

                // Render Results
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
                        <div class="search-item ${{idx === 0 ? 'highlighted' : ''}}" data-index="${{idx}}">
                            <div class="search-item-info">
                                <div class="search-item-title-row">
                                    <span class="search-item-title">${{highlightedTitle}}</span>
                                    <span class="${{badgeClass}}">${{item.badge}}</span>
                                    ${{item.village ? `<span class="search-village-pill">📍 ${{item.village}}</span>` : ''}}
                                </div>
                                ${{metaRows}}
                            </div>
                            <div style="display:flex; align-items:center; gap:6px; flex-shrink:0;">
                                ${{isPerson ? `
                                    <button type="button" class="search-action-btn view-dossier-btn" data-index="${{idx}}" title="مشاهده شناسنامه اختصاصی پرونده" style="padding:4px 8px; background:rgba(237,211,149,0.18); border:1px solid rgba(237,211,149,0.4); color:#edd395; border-radius:6px; font-size:11px; font-weight:800; cursor:pointer;">
                                        پرونده 👤
                                    </button>
                                    <button type="button" class="search-action-btn view-table-btn" data-index="${{idx}}" title="مشاهده در جدول روستا" style="padding:4px 7px; background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.15); color:#cbd5e1; border-radius:6px; font-size:11px; cursor:pointer;">
                                        جدول ↗
                                    </button>
                                ` : `
                                    <span style="color:var(--gold); font-size:11.5px; font-weight:700; display:flex; align-items:center; gap:2px;">
                                        مشاهده ↗
                                    </span>
                                `}}
                            </div>
                        </div>
                    `;
                }});
                html += `</div>`;

                searchDropdown.innerHTML = html;
                searchDropdown.classList.add('active');
                activeHighlightedIndex = 0;

                bindCategoryTabs();
                bindItemClicks(topResults, rawQuery);
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

            function bindItemClicks(results, rawQuery) {{
                if (!searchDropdown) return;
                searchDropdown.querySelectorAll('.search-item').forEach(el => {{
                    el.addEventListener('click', (e) => {{
                        e.stopPropagation();
                        const idx = parseInt(el.getAttribute('data-index'), 10);
                        const item = results[idx];
                        if (!item) return;

                        // Check if direct table button clicked
                        if (e.target.closest('.view-table-btn')) {{
                            directNavigateToTable(item, rawQuery);
                        }} else if (item.type === 'person') {{
                            // Open Dedicated Person Dossier Modal!
                            saveRecentSearch(rawQuery || item.title);
                            openPersonDossier(item);
                        }} else {{
                            // Village or Facility
                            saveRecentSearch(rawQuery || item.title);
                            selectSearchItem(item);
                        }}
                    }});
                }});
            }}

            function directNavigateToTable(item, rawQuery) {{
                saveRecentSearch(rawQuery || item.title);
                if (searchDropdown) searchDropdown.classList.remove('active');
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

            // OPEN DEDICATED BENEFICIARY DOSSIER MODAL
            function openPersonDossier(p) {{
                currentSelectedPerson = p;
                const dlg = document.getElementById('personDossierDialog');
                if (!dlg) {{
                    // Fallback to village table
                    selectSearchItem(p);
                    return;
                }}

                // Close search dropdown
                if (searchDropdown) searchDropdown.classList.remove('active');

                // Populate Fields
                const nameEl = document.getElementById('pdFullName');
                if (nameEl) nameEl.textContent = p.title || 'مددجوی گرامی';

                const roleBadge = document.getElementById('pdRoleBadge');
                if (roleBadge) {{
                    roleBadge.textContent = p.badge || (p.personType === 'orphan' ? 'ایتام' : 'مددجو');
                    roleBadge.className = (p.badge === 'ایتام' || p.personType === 'orphan') ? 'search-badge-orphan' : 'search-badge-needy';
                }}

                const vPill = document.getElementById('pdVillagePill');
                if (vPill) vPill.textContent = '📍 ' + (p.village || 'روستای حوزه شلمچه');

                const nidEl = document.getElementById('pdNationalId');
                if (nidEl) nidEl.textContent = p.nationalId && p.nationalId !== '-' ? p.nationalId : 'ثبت نشده';

                const fatherEl = document.getElementById('pdFatherName');
                if (fatherEl) fatherEl.textContent = p.father && p.father !== '-' ? p.father : '—';

                const guardianEl = document.getElementById('pdGuardianName');
                if (guardianEl) guardianEl.textContent = p.guardian && p.guardian !== '-' ? p.guardian : (p.title || 'سرپرست خانوار');

                const phoneEl = document.getElementById('pdPhone');
                const callBtn = document.getElementById('callPdPhoneBtn');
                if (phoneEl) {{
                    const phoneVal = p.phone && p.phone !== '-' ? p.phone : 'ثبت نشده';
                    phoneEl.textContent = phoneVal;
                    if (callBtn) {{
                        if (phoneVal !== 'ثبت نشده') {{
                            callBtn.href = 'tel:' + phoneVal.split(/[_\\-\\s]/)[0];
                            callBtn.style.display = 'inline-block';
                        }} else {{
                            callBtn.style.display = 'none';
                        }}
                    }}
                }}

                // Health status extracted from keyword / subtitle
                const healthEl = document.getElementById('pdHealthStatus');
                if (healthEl) {{
                    let hText = 'تحت پایش و ارزیابی';
                    if (p.keyword && p.keyword.includes('معلول حرکتی')) hText = 'معلولیت جسمی‌حرکتی';
                    else if (p.keyword && p.keyword.includes('پیوند قلب')) hText = 'پیوند قلب / بیمار خاص';
                    else if (p.keyword && p.keyword.includes('کلیوی')) hText = 'بیماری مزمن کلیوی';
                    else if (p.subtitle && p.subtitle.includes('سلامت:')) {{
                        const m = p.subtitle.match(/سلامت:\\s*([^·]+)/);
                        if (m) hText = m[1].trim();
                    }}
                    healthEl.textContent = hText;
                }}

                const eduEl = document.getElementById('pdEducation');
                if (eduEl) {{
                    let eText = '—';
                    if (p.subtitle && p.subtitle.includes('مدرسه:')) {{
                        const m = p.subtitle.match(/مدرسه:\\s*([^·]+)/);
                        if (m) eText = m[1].trim();
                    }} else if (p.keyword && p.keyword.includes('دانشگاه')) {{
                        eText = 'دانشجوی مقطع کارشناسی';
                    }} else if (p.personType === 'orphan') {{
                        eText = 'دانش‌آموز تحت پوشش';
                    }}
                    eduEl.textContent = eText;
                }}

                const addrEl = document.getElementById('pdAddress');
                if (addrEl) {{
                    addrEl.textContent = p.address && p.address !== '-' 
                        ? p.address 
                        : (p.village ? `روستای ${{p.village}} - اطلاعات تکمیلی در دهیاری و پرونده میدانی موجود است.` : 'محدوده جغرافیایی منطقه شلمچه و خرمشهر');
                }}

                const viewLabel = document.getElementById('pdViewVillageLabel');
                if (viewLabel) {{
                    viewLabel.textContent = `مشاهده در جدول و نقشه روستای ${{p.village || ''}} ↗`;
                }}

                // Show Modal
                if (typeof dlg.showModal === 'function') {{
                    try {{
                        if (!dlg.open) dlg.showModal();
                    }} catch (e) {{
                        dlg.setAttribute('open', '');
                    }}
                }} else {{
                    dlg.setAttribute('open', '');
                }}
            }}

            // Copy National ID
            const copyNidBtn = document.getElementById('copyPdNidBtn');
            if (copyNidBtn) {{
                copyNidBtn.addEventListener('click', () => {{
                    if (currentSelectedPerson && currentSelectedPerson.nationalId && currentSelectedPerson.nationalId !== '-') {{
                        navigator.clipboard.writeText(currentSelectedPerson.nationalId).then(() => {{
                            showSearchToast('✓ کد ملی با موفقیت کپی شد: ' + currentSelectedPerson.nationalId);
                        }}).catch(() => {{
                            showSearchToast('کد ملی: ' + currentSelectedPerson.nationalId);
                        }});
                    }} else {{
                        showSearchToast('کد ملی در سامانه موجود نیست.');
                    }}
                }});
            }}

            // Copy Summary
            const copySummaryBtn = document.getElementById('pdCopySummaryBtn');
            if (copySummaryBtn) {{
                copySummaryBtn.addEventListener('click', () => {{
                    if (!currentSelectedPerson) return;
                    const p = currentSelectedPerson;
                    const summary = `📋 خلاصه پرونده مددجو:\nنام: ${{p.title}}\nروستا: ${{p.village}}\nکد ملی: ${{p.nationalId || '-'}}\nسرپرست: ${{p.guardian || '-'}}\nتماس: ${{p.phone || '-'}}\nنشانی: ${{p.address || '-'}}`;
                    navigator.clipboard.writeText(summary).then(() => {{
                        showSearchToast('✓ خلاصه پرونده در کلیپ‌بورد کپی شد.');
                    }}).catch(() => {{
                        showSearchToast('خلاصه کپی شد.');
                    }});
                }});
            }}

            // View In Village Table Button
            const pdViewInVillageBtn = document.getElementById('pdViewInVillageBtn');
            if (pdViewInVillageBtn) {{
                pdViewInVillageBtn.addEventListener('click', () => {{
                    const dlg = document.getElementById('personDossierDialog');
                    if (dlg) dlg.close();

                    if (currentSelectedPerson) {{
                        const p = currentSelectedPerson;
                        navigateToVillage(p.target, 'stats', p.rowQuery || p.nationalId || p.title);
                    }}
                }});
            }}

            // Print Beneficiary Card
            const pdPrintCardBtn = document.getElementById('pdPrintCardBtn');
            if (pdPrintCardBtn) {{
                pdPrintCardBtn.addEventListener('click', () => {{
                    document.body.classList.add('printing-person-dossier');
                    window.print();
                    setTimeout(() => {{
                        document.body.classList.remove('printing-person-dossier');
                    }}, 1000);
                }});
            }}

            // Close Person Dossier Button
            const closePdBtn = document.getElementById('closePersonDossierBtn');
            if (closePdBtn) {{
                closePdBtn.addEventListener('click', () => {{
                    const dlg = document.getElementById('personDossierDialog');
                    if (dlg) dlg.close();
                }});
            }}

            // Search input listeners
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
                    if (!e.target.closest('#searchBoxWrap') && !e.target.closest('#searchResultsDropdown') && !e.target.closest('#personDossierDialog')) {{
                        searchDropdown.classList.remove('active');
                    }}
                }});
            }}"""

# Find search block in html
s_start = html.find("// ==================== 2. SMART SEARCH SYSTEM")
s_end = html.find("const comparisonData = {", s_start)
assert s_start != -1 and s_end != -1, "Search block not found"

html = html[:s_start] + new_js + "\n\n            " + html[s_end:]
print("Updated Search JS block successfully!")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Saved updated index.html with Phonetic Matcher and Person Dossier Modal!")
