import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# --------------------------------------------------------------------------
# 1. ADD CSS FOR VILLAGE SWITCHER PILLS & TOAST GLOW
# --------------------------------------------------------------------------
switcher_css = """
.v-village-switcher {
    display: inline-flex;
    align-items: center;
    gap: 5px;
    background: rgba(11, 26, 24, 0.85);
    border: 1px solid rgba(237, 211, 149, 0.35);
    border-radius: 20px;
    padding: 3px 8px;
    margin-top: 4px;
    flex-wrap: wrap;
}

.v-switcher-label {
    font-size: 11px;
    font-weight: 700;
    color: #94a3b8;
    margin-left: 4px;
}

.v-switch-pill {
    background: rgba(237, 211, 149, 0.1);
    border: 1px solid rgba(237, 211, 149, 0.25);
    color: #e2e8f0;
    font-family: inherit;
    font-size: 11px;
    font-weight: 800;
    padding: 3px 9px;
    border-radius: 12px;
    cursor: pointer;
    transition: all 0.2s ease;
}

.v-switch-pill:hover {
    background: rgba(237, 211, 149, 0.25);
    color: #facc15;
}

.v-switch-pill.active {
    background: #edd395;
    color: #0b1a18;
    border-color: #edd395;
    font-weight: 900;
    box-shadow: 0 0 10px rgba(237, 211, 149, 0.45);
}
"""

if ".v-village-switcher" not in html:
    idx_style = html.find("</style>")
    assert idx_style != -1, "</style> not found"
    html = html[:idx_style] + switcher_css + "\n" + html[idx_style:]
    print("1. Injected switcher CSS!")
else:
    print("1. Switcher CSS already present!")

# --------------------------------------------------------------------------
# 2. INJECT SWITCHER MARKUP INTO #villageTopBar
# --------------------------------------------------------------------------
old_topbar_title = '<span class="v-main-sub" id="villageSubheading">محور مواصلاتی شلمچه - خرمشهر · حومه غربی</span>\n                </div>'
new_topbar_title = """<span class="v-main-sub" id="villageSubheading">محور مواصلاتی شلمچه - خرمشهر · حومه غربی</span>
                    <div class="v-village-switcher" id="vVillageSwitcher">
                        <span class="v-switcher-label">روستاهای دارای نقشه هوایی:</span>
                        <button type="button" class="v-switch-pill active" data-vid="pol-now" onclick="switchToVillage('pol-now')">پل نو</button>
                        <button type="button" class="v-switch-pill" data-vid="ariz" onclick="switchToVillage('ariz')">عریض</button>
                        <button type="button" class="v-switch-pill" data-vid="jadideh" onclick="switchToVillage('jadideh')">جدیده</button>
                        <button type="button" class="v-switch-pill" data-vid="darband-gharbi" onclick="switchToVillage('darband-gharbi')">دربند غربی</button>
                        <button type="button" class="v-switch-pill" data-vid="darband-sharqi" onclick="switchToVillage('darband-sharqi')">دربند شرقی</button>
                    </div>
                </div>"""

if "vVillageSwitcher" not in html and old_topbar_title in html:
    html = html.replace(old_topbar_title, new_topbar_title, 1)
    print("2. Injected vVillageSwitcher into #villageTopBar!")
else:
    print("2. vVillageSwitcher already present or topbar title mismatch")

# --------------------------------------------------------------------------
# 3. UPDATE updateVillageSatelliteView TO USE MEMORY CACHE FIRST & SWITCHER PILLS
# --------------------------------------------------------------------------
old_sat_photo_lookup = "const customUserPhoto = localStorage.getItem('village_custom_photo_' + v.id);"
new_sat_photo_lookup = """const customUserPhoto = (window._villagePhotosCache && window._villagePhotosCache[v.id]) || localStorage.getItem('village_custom_photo_' + v.id);
            // Highlight active switcher pill
            document.querySelectorAll('.v-switch-pill').forEach(btn => {
                btn.classList.toggle('active', btn.getAttribute('data-vid') === v.id);
            });"""

if old_sat_photo_lookup in html:
    html = html.replace(old_sat_photo_lookup, new_sat_photo_lookup, 1)
    print("3. Updated updateVillageSatelliteView photo lookup with cache and switcher active state!")

# --------------------------------------------------------------------------
# 4. REPLACE PHOTOS MANAGER SCRIPT BLOCK WITH ROBUST INDEXEDDB + CANVAS ENGINE
# --------------------------------------------------------------------------
marker_start = "// VILLAGE PHOTOS & SATELLITE MAP MANAGER ENGINE"
idx_start = html.find(marker_start)
assert idx_start != -1, "marker_start not found"

idx_end = html.rfind("</script>")
assert idx_end != -1, "</script> not found"

new_engine_code = """// VILLAGE PHOTOS & SATELLITE MAP MANAGER ENGINE
        // =========================================================================

        const targetPhotoVillages = [
            { id: 'pol-now', name: 'پل نو', defaultImg: '/image_0.webp', fallback: '/pol_now_map.webp', desc: 'محور شلمچه · حومه غربی' },
            { id: 'ariz', name: 'عریض', defaultImg: '/ariz_map.webp', fallback: '/ariz_map.jpg', desc: 'جاده شلمچه · بخش مرکزی' },
            { id: 'jadideh', name: 'جدیده', defaultImg: '/jadideh_map.webp', fallback: '/jadideh_map.jpg', desc: 'حومه شرقی · نخلستان‌ها' },
            { id: 'darband-gharbi', name: 'دربند غربی', defaultImg: '/darband-gharbi_map.webp', fallback: '/darband-gharbi_map.jpg', desc: 'حومه غربی · کانون سکونتگاهی' },
            { id: 'darband-sharqi', name: 'دربند شرقی', defaultImg: '/darband-sharqi_map.webp', fallback: '/darband-sharqi_map.jpg', desc: 'حومه غربی · همجوار دربند غربی' }
        ];

        // Global memory cache for immediate synchronous rendering
        window._villagePhotosCache = window._villagePhotosCache || {};

        // IndexedDB store for zero-quota failure
        const DB_NAME = 'VillagePhotosDB';
        const STORE_NAME = 'photos';

        function openPhotosDB() {
            return new Promise((resolve) => {
                try {
                    const req = indexedDB.open(DB_NAME, 1);
                    req.onupgradeneeded = (e) => {
                        const db = e.target.result;
                        if (!db.objectStoreNames.contains(STORE_NAME)) {
                            db.createObjectStore(STORE_NAME, { keyPath: 'id' });
                        }
                    };
                    req.onsuccess = () => resolve(req.result);
                    req.onerror = () => resolve(null);
                } catch(err) {
                    resolve(null);
                }
            });
        }

        async function savePhotoToIDB(id, dataUrl) {
            try {
                const db = await openPhotosDB();
                if (!db) return false;
                return new Promise((resolve) => {
                    const tx = db.transaction(STORE_NAME, 'readwrite');
                    const store = tx.objectStore(STORE_NAME);
                    store.put({ id, dataUrl, updated: Date.now() });
                    tx.oncomplete = () => resolve(true);
                    tx.onerror = () => resolve(false);
                });
            } catch(e) {
                return false;
            }
        }

        async function getPhotoFromIDB(id) {
            try {
                const db = await openPhotosDB();
                if (!db) return null;
                return new Promise((resolve) => {
                    const tx = db.transaction(STORE_NAME, 'readonly');
                    const store = tx.objectStore(STORE_NAME);
                    const req = store.get(id);
                    req.onsuccess = () => resolve(req.result ? req.result.dataUrl : null);
                    req.onerror = () => resolve(null);
                });
            } catch(e) {
                return null;
            }
        }

        async function removePhotoFromIDB(id) {
            try {
                const db = await openPhotosDB();
                if (!db) return false;
                return new Promise((resolve) => {
                    const tx = db.transaction(STORE_NAME, 'readwrite');
                    const store = tx.objectStore(STORE_NAME);
                    store.delete(id);
                    tx.oncomplete = () => resolve(true);
                    tx.onerror = () => resolve(false);
                });
            } catch(e) {
                return false;
            }
        }

        // Automatic image compression via HTML5 canvas (scales down to max 2048px, reduces 10MB -> 300KB)
        function compressImage(file, maxDim = 2048, quality = 0.86) {
            return new Promise((resolve, reject) => {
                const reader = new FileReader();
                reader.onload = (e) => {
                    const img = new Image();
                    img.onload = () => {
                        let w = img.width;
                        let h = img.height;
                        if (w > maxDim || h > maxDim) {
                            if (w > h) {
                                h = Math.round((h * maxDim) / w);
                                w = maxDim;
                            } else {
                                w = Math.round((w * maxDim) / h);
                                h = maxDim;
                            }
                        }
                        const canvas = document.createElement('canvas');
                        canvas.width = w;
                        canvas.height = h;
                        const ctx = canvas.getContext('2d');
                        ctx.drawImage(img, 0, 0, w, h);
                        const compressedDataUrl = canvas.toDataURL('image/jpeg', quality);
                        resolve(compressedDataUrl);
                    };
                    img.onerror = () => resolve(e.target.result); // fallback to raw
                    img.src = e.target.result;
                };
                reader.onerror = () => reject(new Error('File read error'));
                reader.readAsDataURL(file);
            });
        }

        function getActiveVillagePhoto(vid) {
            if (window._villagePhotosCache && window._villagePhotosCache[vid]) {
                return { src: window._villagePhotosCache[vid], isCustom: true };
            }
            const custom = localStorage.getItem('village_custom_photo_' + vid);
            if (custom) return { src: custom, isCustom: true };
            const item = targetPhotoVillages.find(x => x.id === vid);
            if (item) return { src: item.defaultImg, fallback: item.fallback, isCustom: false };
            return { src: '/main_map_final.jpg', isCustom: false };
        }

        function getVillageRecord(vid) {
            const list = window.villages || [];
            return list.find(x => x.id === vid) || targetPhotoVillages.find(x => x.id === vid) || null;
        }

        function getVillageName(vid) {
            const item = targetPhotoVillages.find(x => x.id === vid);
            if (item) return item.name;
            const rec = getVillageRecord(vid);
            return rec ? rec.name : vid;
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
                        <div class="v-photo-preview-box" onclick="triggerPhotoUpload('${v.id}')" title="برای بارگذاری یا تعویض عکس کلیک کنید یا عکس را اینجا رها کنید">
                            <img src="${photoInfo.src}" onerror="this.onerror=null;this.src='${photoInfo.fallback || '/main_map_final.jpg'}';" alt="${v.name}" class="v-photo-thumb" id="thumb_${v.id}" />
                            <div class="v-photo-drop-hint">
                                <span>📁 کلیک برای انتخاب عکس</span>
                                <span>یا Drag & Drop فایل</span>
                            </div>
                        </div>
                        <input type="file" id="fileInput_${v.id}" accept="image/*" style="display:none;" onchange="handleVillageCardUpload('${v.id}', this)" />
                        <div class="v-photo-card-actions">
                            <button type="button" class="v-photo-btn" onclick="triggerPhotoUpload('${v.id}')">
                                <span>📁</span>
                                <span>انتخاب / تعویض عکس</span>
                            </button>
                            ${photoInfo.isCustom ? `
                                <button type="button" class="v-photo-reset-btn" onclick="resetVillagePhoto('${v.id}')" title="بازنشانی به تصویر اولیه">
                                    ↺
                                </button>
                            ` : ''}
                            <button type="button" class="v-photo-btn" style="flex:0 0 auto;" onclick="goToVillageFromModal('${v.id}')" title="مشاهده نقشه ماهواره‌ای این روستا">
                                <span>👁️ مشاهده</span>
                            </button>
                        </div>
                    </div>
                `;
            }).join('');

            // Bind drag & drop for each card
            targetPhotoVillages.forEach(v => {
                const card = document.getElementById('photoCard_' + v.id);
                if (card && !card._boundDrag) {
                    card._boundDrag = true;
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
                            saveCustomVillagePhotoFile(v.id, file);
                        }
                    });
                }
            });
        }

        function triggerPhotoUpload(vid) {
            const input = document.getElementById('fileInput_' + vid);
            if (input) {
                input.value = ''; // Reset so change fires even for same file
                input.click();
            }
        }

        function handleVillageCardUpload(vid, inputEl) {
            const file = inputEl.files && inputEl.files[0];
            if (!file) return;
            saveCustomVillagePhotoFile(vid, file);
            inputEl.value = '';
        }

        async function saveCustomVillagePhotoFile(vid, file) {
            if (!file) return;
            const vName = getVillageName(vid);

            if (typeof showSearchToast === 'function') {
                showSearchToast(`در حال پردازش و اعمال عکس برای روستای ${vName}... ⏳`);
            }

            try {
                // 1. Compress image to guaranteed fit (approx 200KB - 400KB)
                const optimizedDataUrl = await compressImage(file, 2048, 0.88);

                // 2. Synchronous in-memory cache update
                window._villagePhotosCache[vid] = optimizedDataUrl;

                // 3. Save to IndexedDB (unlimited)
                await savePhotoToIDB(vid, optimizedDataUrl);

                // 4. Save to localStorage
                try {
                    localStorage.setItem('village_custom_photo_' + vid, optimizedDataUrl);
                } catch(e) {
                    console.warn('LocalStorage limit reached, saved in IndexedDB and memory cache', e);
                }

                // 5. Update live DOM elements immediately
                const satImg = document.getElementById('villageSatelliteImg');
                if (satImg && window._currentVillageViewing && window._currentVillageViewing.id === vid) {
                    satImg.src = optimizedDataUrl;
                }

                const thumb = document.getElementById('thumb_' + vid);
                if (thumb) thumb.src = optimizedDataUrl;

                if (typeof showSearchToast === 'function') {
                    showSearchToast(`✓ عکس روستای ${vName} با موفقیت جایگزین و ذخیره شد! 📸`);
                }

                renderVillagePhotosGrid();
            } catch(err) {
                console.error('Error compressing/saving photo', err);
                // Fallback to raw FileReader
                const reader = new FileReader();
                reader.onload = (e) => {
                    const rawUrl = e.target.result;
                    window._villagePhotosCache[vid] = rawUrl;
                    savePhotoToIDB(vid, rawUrl);
                    try { localStorage.setItem('village_custom_photo_' + vid, rawUrl); } catch(ex){}
                    const satImg = document.getElementById('villageSatelliteImg');
                    if (satImg && window._currentVillageViewing && window._currentVillageViewing.id === vid) {
                        satImg.src = rawUrl;
                    }
                    renderVillagePhotosGrid();
                };
                reader.readAsDataURL(file);
            }
        }

        async function resetVillagePhoto(vid) {
            delete window._villagePhotosCache[vid];
            localStorage.removeItem('village_custom_photo_' + vid);
            await removePhotoFromIDB(vid);

            const vName = getVillageName(vid);
            if (typeof showSearchToast === 'function') {
                showSearchToast(`عکس روستای ${vName} به تصویر پیش‌فرض بازنشانی شد ↺`);
            }

            if (window._currentVillageViewing && window._currentVillageViewing.id === vid) {
                updateVillageSatelliteView(window._currentVillageViewing);
            }

            renderVillagePhotosGrid();
        }

        // Direct instant village switcher (0ms transition without flight delay if already inside village)
        function switchToVillage(vid) {
            const vObj = getVillageRecord(vid);
            if (!vObj) return;

            const isVillageView = document.getElementById('experience')?.classList.contains('in-village');
            if (isVillageView) {
                window.activeLocation = vObj;
                if (typeof renderExecutiveDashboard === 'function') {
                    renderExecutiveDashboard(vObj);
                }
                const vName = document.getElementById('villageName');
                if (vName) vName.textContent = vObj.name;
                updateVillageSatelliteView(vObj);

                // Highlight active pill
                document.querySelectorAll('.v-switch-pill').forEach(btn => {
                    btn.classList.toggle('active', btn.getAttribute('data-vid') === vid);
                });
            } else {
                const enterFn = window.enter;
                if (typeof enterFn === 'function') {
                    enterFn(vObj);
                }
            }
        }

        function goToVillageFromModal(vid) {
            const modal = document.getElementById('villagePhotosDialog');
            if (modal) modal.close();
            switchToVillage(vid);
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

        async function preloadPhotosFromStorage() {
            for (const v of targetPhotoVillages) {
                let photo = localStorage.getItem('village_custom_photo_' + v.id);
                if (!photo) {
                    photo = await getPhotoFromIDB(v.id);
                    if (photo) {
                        try { localStorage.setItem('village_custom_photo_' + v.id, photo); } catch(e){}
                    }
                }
                if (photo) {
                    window._villagePhotosCache[v.id] = photo;
                }
            }
            if (window._currentVillageViewing) {
                updateVillageSatelliteView(window._currentVillageViewing);
            }
            renderVillagePhotosGrid();
        }

        function bindPhotosManagerEvents() {
            const openHeaderBtn = document.getElementById('openVillagePhotosBtn');
            const openTopBarBtn = document.getElementById('vOpenVillagePhotosModalBtn');
            const floatingBtn = document.getElementById('vChangePhotoFloatingBtn');
            const closeBtn = document.getElementById('closePhotosModalBtn');
            const doneBtn = document.getElementById('donePhotosModalBtn');
            const modal = document.getElementById('villagePhotosDialog');
            const viewport = document.getElementById('villageMapViewport');
            const dropOverlay = document.getElementById('villageMapDropOverlay');
            const fileInput = document.getElementById('vPhotoFileInput');
            const uBtn = document.getElementById('vUploadPhoto');

            if (openHeaderBtn && !openHeaderBtn._bound) {
                openHeaderBtn._bound = true;
                openHeaderBtn.onclick = openVillagePhotosModal;
            }

            if (openTopBarBtn && !openTopBarBtn._bound) {
                openTopBarBtn._bound = true;
                openTopBarBtn.onclick = openVillagePhotosModal;
            }

            if (floatingBtn && !floatingBtn._bound) {
                floatingBtn._bound = true;
                floatingBtn.onclick = () => {
                    const cur = window._currentVillageViewing;
                    if (cur) {
                        triggerPhotoUpload(cur.id);
                    } else {
                        openVillagePhotosModal();
                    }
                };
            }

            if (uBtn && fileInput && !uBtn._bound) {
                uBtn._bound = true;
                uBtn.onclick = (e) => {
                    e.stopPropagation();
                    const cur = window._currentVillageViewing;
                    if (cur) {
                        triggerPhotoUpload(cur.id);
                    } else {
                        openVillagePhotosModal();
                    }
                };
            }

            if (closeBtn && !closeBtn._bound) {
                closeBtn._bound = true;
                closeBtn.onclick = () => { if (modal) modal.close(); };
            }

            if (doneBtn && !doneBtn._bound) {
                doneBtn._bound = true;
                doneBtn.onclick = () => { if (modal) modal.close(); };
            }

            // Viewport HTML5 Drag and Drop for Current Village
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
                            saveCustomVillagePhotoFile(cur.id, file);
                        } else {
                            openVillagePhotosModal();
                        }
                    }
                });
            }
        }

        window.openVillagePhotosModal = openVillagePhotosModal;
        window.triggerPhotoUpload = triggerPhotoUpload;
        window.handleVillageCardUpload = handleVillageCardUpload;
        window.resetVillagePhoto = resetVillagePhoto;
        window.goToVillageFromModal = goToVillageFromModal;
        window.switchToVillage = switchToVillage;

        document.addEventListener('DOMContentLoaded', () => {
            bindPhotosManagerEvents();
            preloadPhotosFromStorage();
        });
        setTimeout(() => {
            bindPhotosManagerEvents();
            preloadPhotosFromStorage();
        }, 150);
"""

html = html[:idx_start] + new_engine_code + "\n    " + html[idx_end:]
print("4. Injected upgraded Photos Engine!")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("SUCCESS: index.html fully updated!")
