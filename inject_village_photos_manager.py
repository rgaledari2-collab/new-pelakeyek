import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# --------------------------------------------------------------------------
# 1. INJECT CSS FOR PHOTOS DIALOG & DRAG-AND-DROP
# --------------------------------------------------------------------------
photos_css = """
/* =========================================================================
   VILLAGE PHOTOS & SATELLITE MAP MANAGER MODAL & DRAG-DROP
   ========================================================================= */

.village-photos-dialog {
    border: none;
    padding: 0;
    background: transparent;
    max-width: 920px;
    width: 95vw;
    border-radius: 20px;
    box-shadow: 0 30px 100px rgba(0, 0, 0, 0.9), 0 0 40px rgba(237, 211, 149, 0.25);
    outline: none;
    margin: auto;
}

.village-photos-dialog::backdrop {
    background: rgba(5, 15, 14, 0.82);
    backdrop-filter: blur(8px);
}

.photos-modal-wrap {
    background: linear-gradient(145deg, #0d2220 0%, #081615 100%);
    border: 1.5px solid rgba(237, 211, 149, 0.45);
    border-radius: 20px;
    padding: 24px 28px;
    color: #e2e8f0;
    font-family: YekanBakh, sans-serif;
    display: flex;
    flex-direction: column;
    max-height: 88vh;
    overflow: hidden;
}

.photos-modal-header {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    gap: 16px;
    padding-bottom: 18px;
    border-bottom: 1px solid rgba(237, 211, 149, 0.25);
}

.photos-modal-title-wrap {
    display: flex;
    flex-direction: column;
    gap: 4px;
}

.photos-modal-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(237, 211, 149, 0.15);
    border: 1px solid rgba(237, 211, 149, 0.35);
    color: #edd395;
    padding: 3px 10px;
    border-radius: 14px;
    font-size: 11px;
    font-weight: 800;
    width: fit-content;
}

.photos-modal-h2 {
    font-size: 20px;
    font-weight: 900;
    color: #f8fafc;
    margin: 0;
}

.photos-modal-sub {
    font-size: 12.5px;
    color: #94a3b8;
    margin: 0;
    line-height: 1.6;
}

.photos-modal-close {
    width: 36px;
    height: 36px;
    border-radius: 50%;
    background: rgba(237, 211, 149, 0.12);
    border: 1px solid rgba(237, 211, 149, 0.35);
    color: #edd395;
    font-size: 16px;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.2s ease;
    flex-shrink: 0;
}

.photos-modal-close:hover {
    background: #edd395;
    color: #0b1a18;
    transform: scale(1.08);
}

.photos-grid-scroll {
    overflow-y: auto;
    padding: 18px 4px;
    flex: 1;
}

.photos-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 16px;
}

.v-photo-card {
    background: rgba(11, 26, 24, 0.7);
    border: 1.5px solid rgba(237, 211, 149, 0.28);
    border-radius: 16px;
    padding: 14px;
    display: flex;
    flex-direction: column;
    gap: 10px;
    transition: all 0.25s cubic-bezier(0.2, 0.8, 0.2, 1);
    position: relative;
}

.v-photo-card:hover {
    border-color: #facc15;
    transform: translateY(-2px);
    box-shadow: 0 10px 24px rgba(0,0,0,0.6), 0 0 16px rgba(237, 211, 149, 0.2);
}

.v-photo-card.card-dragover {
    border: 2px dashed #facc15 !important;
    background: rgba(20, 50, 45, 0.95) !important;
    transform: scale(1.02);
}

.v-photo-card-top {
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.v-photo-card-title {
    font-size: 15px;
    font-weight: 800;
    color: #f8fafc;
}

.v-photo-card-badge {
    font-size: 10px;
    font-weight: 800;
    padding: 2px 8px;
    border-radius: 10px;
}

.v-photo-card-badge.custom {
    background: rgba(16, 185, 129, 0.2);
    color: #34d399;
    border: 1px solid rgba(16, 185, 129, 0.4);
}

.v-photo-card-badge.default {
    background: rgba(237, 211, 149, 0.15);
    color: #edd395;
    border: 1px solid rgba(237, 211, 149, 0.3);
}

.v-photo-preview-box {
    position: relative;
    width: 100%;
    height: 140px;
    border-radius: 10px;
    overflow: hidden;
    background: #061110;
    border: 1px solid rgba(237, 211, 149, 0.2);
    cursor: pointer;
}

.v-photo-thumb {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
    transition: transform 0.3s ease;
}

.v-photo-preview-box:hover .v-photo-thumb {
    transform: scale(1.05);
}

.v-photo-drop-hint {
    position: absolute;
    inset: 0;
    background: rgba(11, 26, 24, 0.7);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 4px;
    color: #edd395;
    font-size: 11px;
    font-weight: 700;
    opacity: 0;
    transition: opacity 0.2s ease;
    text-align: center;
    padding: 8px;
}

.v-photo-preview-box:hover .v-photo-drop-hint {
    opacity: 1;
}

.v-photo-card-actions {
    display: flex;
    align-items: center;
    gap: 8px;
}

.v-photo-btn {
    flex: 1;
    background: rgba(237, 211, 149, 0.12);
    border: 1px solid rgba(237, 211, 149, 0.35);
    color: #edd395;
    font-family: inherit;
    font-size: 11.5px;
    font-weight: 700;
    padding: 6px 10px;
    border-radius: 8px;
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 6px;
    transition: all 0.2s ease;
}

.v-photo-btn:hover {
    background: #edd395;
    color: #0b1a18;
}

.v-photo-reset-btn {
    background: rgba(239, 68, 68, 0.12);
    border: 1px solid rgba(239, 68, 68, 0.35);
    color: #f87171;
    width: 32px;
    height: 32px;
    border-radius: 8px;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.2s ease;
}

.v-photo-reset-btn:hover {
    background: #ef4444;
    color: #fff;
}

.photos-modal-footer {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
    padding-top: 16px;
    border-top: 1px solid rgba(237, 211, 149, 0.25);
}

.photos-footer-hint {
    font-size: 11px;
    color: #94a3b8;
    line-height: 1.6;
    max-width: 70%;
}

.photos-modal-done-btn {
    background: #edd395;
    color: #0b1a18;
    border: none;
    font-family: inherit;
    font-size: 13px;
    font-weight: 800;
    padding: 8px 22px;
    border-radius: 10px;
    cursor: pointer;
    transition: all 0.2s ease;
    white-space: nowrap;
}

.photos-modal-done-btn:hover {
    background: #facc15;
    transform: scale(1.04);
}

/* Map Drag & Drop Overlay */
.village-map-drop-overlay {
    position: absolute;
    inset: 0;
    background: rgba(11, 26, 24, 0.88);
    backdrop-filter: blur(8px);
    border: 3px dashed #facc15;
    z-index: 50;
    display: none;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    gap: 12px;
    color: #fef08a;
    font-size: 16px;
    font-weight: 800;
    pointer-events: none;
    text-shadow: 0 2px 10px rgba(0,0,0,0.8);
}

.village-map-drop-overlay.active {
    display: flex;
}

.v-change-photo-badge {
    position: absolute;
    bottom: 18px;
    left: 24px;
    background: rgba(11, 26, 24, 0.88);
    border: 1px solid rgba(237, 211, 149, 0.45);
    backdrop-filter: blur(12px);
    border-radius: 20px;
    padding: 6px 14px;
    font-size: 11px;
    font-weight: 800;
    color: #edd395;
    display: inline-flex;
    align-items: center;
    gap: 8px;
    z-index: 15;
    cursor: pointer;
    transition: all 0.2s ease;
    box-shadow: 0 4px 16px rgba(0,0,0,0.5);
}

.v-change-photo-badge:hover {
    background: #edd395;
    color: #0b1a18;
    transform: scale(1.05);
}
"""

idx_style = html.find("</style>")
assert idx_style != -1, "</style> not found"
html = html[:idx_style] + photos_css + "\n" + html[idx_style:]
print("1. Injected Photos Manager CSS!")

# --------------------------------------------------------------------------
# 2. INJECT PHOTOS MODAL DIALOG MARKUP BEFORE <script>
# --------------------------------------------------------------------------
photos_modal_html = """
    <!-- Village Photos & Satellite Maps Gallery & Manager Modal -->
    <dialog id="villagePhotosDialog" class="village-photos-dialog" aria-labelledby="photosModalTitle">
        <div class="photos-modal-wrap">
            <div class="photos-modal-header">
                <div class="photos-modal-title-wrap">
                    <span class="photos-modal-badge">📸 سامانه مدیریت و بارگذاری تصاویر اختصاصی</span>
                    <h2 id="photosModalTitle" class="photos-modal-h2">مدیریت و بارگذاری عکس‌های ماهواره‌ای روستاها</h2>
                    <p class="photos-modal-sub">تصاویر اختصاصی هر روستا را از کامپیوتر یا گوشی خود انتخاب کرده یا روی کارت روستا رها (Drag & Drop) کنید تا بلافاصله جایگزین شوند.</p>
                </div>
                <button type="button" class="photos-modal-close" id="closePhotosModalBtn" title="بستن">✕</button>
            </div>
            
            <div class="photos-grid-scroll">
                <div class="photos-grid" id="villagePhotosGrid">
                    <!-- Populated dynamically by renderVillagePhotosGrid() -->
                </div>
            </div>

            <div class="photos-modal-footer">
                <div class="photos-footer-hint">
                    💡 نکته: تصاویر بارگذاری‌شده اختصاصی روی مرورگر ذخیره شده و در نقشه تفصیلی نمایش داده می‌شوند. همچنین می‌توانید در صفحه هر روستا، عکس را مستقیماً روی نقشه رها (Drop) کنید.
                </div>
                <button type="button" class="photos-modal-done-btn" id="donePhotosModalBtn">تایید و بازگشت به نقشه</button>
            </div>
        </div>
    </dialog>
"""

idx_script = html.find("<script>")
assert idx_script != -1, "<script> not found"
html = html[:idx_script] + photos_modal_html + "\n    " + html[idx_script:]
print("2. Injected villagePhotosDialog modal markup!")

# --------------------------------------------------------------------------
# 3. ADD BUTTON IN TOP NAV ACTIONS (<header>)
# --------------------------------------------------------------------------
old_header_actions = '<button class="nav-action-btn" id="projectsTrackBtn"'
new_header_actions = """<button class="nav-action-btn" id="openVillagePhotosBtn" title="مدیریت و بارگذاری عکس‌های ماهواره‌ای اختصاصی روستاها">
            <svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2">
                <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
                <circle cx="8.5" cy="8.5" r="1.5"></circle>
                <polyline points="21 15 16 10 5 21"></polyline>
            </svg>
            <span>عکس‌های ماهواره‌ای روستاها 📷</span>
        </button>
        <button class="nav-action-btn" id="projectsTrackBtn" """

if old_header_actions in html:
    html = html.replace(old_header_actions, new_header_actions, 1)
    print("3. Injected openVillagePhotosBtn into header nav actions!")

# --------------------------------------------------------------------------
# 4. ADD BUTTON IN #villageTopBar (<div class="v-layout-controls">)
# --------------------------------------------------------------------------
old_v_controls = '<div class="v-layout-controls">'
new_v_controls = """<div class="v-layout-controls">
                    <button type="button" class="v-layout-btn" id="vOpenVillagePhotosModalBtn" title="مدیریت و تعویض عکس ماهواره‌ای این روستا و سایر روستاها">
                        <span class="v-layout-icon">📷</span>
                        <span>تعویض / بارگذاری عکس</span>
                    </button>"""

if old_v_controls in html:
    html = html.replace(old_v_controls, new_v_controls, 1)
    print("4. Injected vOpenVillagePhotosModalBtn into village top bar!")

# --------------------------------------------------------------------------
# 5. ADD DROP OVERLAY & FLOATING CHANGE-PHOTO BADGE TO #villageMapViewport
# --------------------------------------------------------------------------
old_badge = '<div class="village-map-badge" id="villageMapBadge">'
new_badge = """<div class="village-map-drop-overlay" id="villageMapDropOverlay">
                        <span style="font-size: 38px;">📥</span>
                        <span>فایل عکس جدید را اینجا رها کنید (Drop)</span>
                        <span style="font-size: 12px; color: #edd395;">عکس بلافاصله جایگزین و ذخیره می‌شود</span>
                    </div>
                    <button type="button" class="v-change-photo-badge" id="vChangePhotoFloatingBtn" title="بارگذاری عکس جدید برای این روستا">
                        <span>📷</span>
                        <span>تعویض عکس این روستا</span>
                    </button>
                    <div class="village-map-badge" id="villageMapBadge">"""

if old_badge in html:
    html = html.replace(old_badge, new_badge, 1)
    print("5. Injected drop overlay and floating change-photo badge into village map viewport!")

# --------------------------------------------------------------------------
# 6. INJECT JAVASCRIPT FUNCTIONS FOR PHOTOS MANAGER IN SCRIPT BLOCK
# --------------------------------------------------------------------------
js_photos_manager = """
        // =========================================================================
        // VILLAGE PHOTOS & SATELLITE MAP MANAGER ENGINE
        // =========================================================================

        const targetPhotoVillages = [
            { id: 'pol-now', name: 'پل نو', defaultImg: '/image_0.webp', fallback: '/pol_now_map.webp', desc: 'محور شلمچه · حومه غربی' },
            { id: 'ariz', name: 'عریض', defaultImg: '/ariz_map.webp', fallback: '/ariz_map.jpg', desc: 'جاده شلمچه · بخش مرکزی' },
            { id: 'jadideh', name: 'جدیده', defaultImg: '/jadideh_map.webp', fallback: '/jadideh_map.jpg', desc: 'حومه شرقی · نخلستان‌ها' },
            { id: 'darband-gharbi', name: 'دربند غربی', defaultImg: '/darband-gharbi_map.webp', fallback: '/darband-gharbi_map.jpg', desc: 'حومه غربی · کانون سکونتگاهی' },
            { id: 'darband-sharqi', name: 'دربند شرقی', defaultImg: '/darband-sharqi_map.webp', fallback: '/darband-sharqi_map.jpg', desc: 'حومه غربی · همجوار دربند غربی' }
        ];

        function getActiveVillagePhoto(vid) {
            const custom = localStorage.getItem('village_custom_photo_' + vid);
            if (custom) return { src: custom, isCustom: true };
            const item = targetPhotoVillages.find(x => x.id === vid);
            if (item) return { src: item.defaultImg, fallback: item.fallback, isCustom: false };
            return { src: '/main_map_final.jpg', isCustom: false };
        }

        function renderVillagePhotosGrid() {
            const grid = document.getElementById('villagePhotosGrid');
            if (!grid) return;

            grid.innerHTML = targetPhotoVillages.map(v => {
                const photoInfo = getActiveVillagePhoto(v.id);
                const badgeLabel = photoInfo.isCustom ? 'عکس اختصاصی کاربر ✅' : 'عکس پیش‌فرض سیستمی ⚙️';
                const badgeClass = photoInfo.isCustom ? 'custom' : 'default';

                return `
                    <div class="v-photo-card" id="photoCard_${v.id}" data-vid="${v.id}">
                        <div class="v-photo-card-top">
                            <span class="v-photo-card-title">${v.name}</span>
                            <span class="v-photo-card-badge ${badgeClass}">${badgeLabel}</span>
                        </div>
                        <div class="v-photo-preview-box" onclick="triggerPhotoUpload('${v.id}')" title="برای بارگذاری عکس کلیک کنید یا عکس را اینجا رها کنید">
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
                                <span>انتخاب عکس</span>
                            </button>
                            ${photoInfo.isCustom ? `
                                <button type="button" class="v-photo-reset-btn" onclick="resetVillagePhoto('${v.id}')" title="بازنشانی به تصویر اولیه">
                                    ↺
                                </button>
                            ` : ''}
                            <button type="button" class="v-photo-btn" style="flex:0 0 auto;" onclick="goToVillageFromModal('${v.id}')" title="ورود و مشاهده نقشه این روستا">
                                <span>👁️</span>
                            </button>
                        </div>
                    </div>
                `;
            }).join('');

            // Bind drag & drop for each card
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
                            saveCustomVillagePhotoFile(v.id, file);
                        }
                    });
                }
            });
        }

        function triggerPhotoUpload(vid) {
            const input = document.getElementById('fileInput_' + vid);
            if (input) input.click();
        }

        function handleVillageCardUpload(vid, inputEl) {
            const file = inputEl.files && inputEl.files[0];
            if (!file) return;
            saveCustomVillagePhotoFile(vid, file);
        }

        function saveCustomVillagePhotoFile(vid, file) {
            const reader = new FileReader();
            reader.onload = (e) => {
                const dataUrl = e.target.result;
                try {
                    localStorage.setItem('village_custom_photo_' + vid, dataUrl);
                } catch (err) {
                    console.warn('Storage limit reached, saving in session', err);
                }

                // If currently viewing this village, update live map
                if (window._currentVillageViewing && window._currentVillageViewing.id === vid) {
                    const satImg = document.getElementById('villageSatelliteImg');
                    if (satImg) satImg.src = dataUrl;
                }

                const vObj = villages.find(x => x.id === vid);
                const vTitle = vObj ? vObj.name : vid;
                if (typeof showSearchToast === 'function') {
                    showSearchToast(`عکس ماهواره‌ای روستای ${vTitle} با موفقیت بارگذاری و ذخیره شد 📸`);
                }

                renderVillagePhotosGrid();
            };
            reader.readAsDataURL(file);
        }

        function resetVillagePhoto(vid) {
            localStorage.removeItem('village_custom_photo_' + vid);
            const vObj = villages.find(x => x.id === vid);
            const vTitle = vObj ? vObj.name : vid;

            // If viewing this village live, revert live image
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

            const vObj = villages.find(x => x.id === vid);
            if (vObj && typeof enter === 'function') {
                if (typeof window.back === 'function' && phase === 'village') {
                    window.back();
                    setTimeout(() => enter(vObj), 150);
                } else {
                    enter(vObj);
                }
            }
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

        function bindPhotosManagerEvents() {
            const openHeaderBtn = document.getElementById('openVillagePhotosBtn');
            const openTopBarBtn = document.getElementById('vOpenVillagePhotosModalBtn');
            const floatingBtn = document.getElementById('vChangePhotoFloatingBtn');
            const closeBtn = document.getElementById('closePhotosModalBtn');
            const doneBtn = document.getElementById('donePhotosModalBtn');
            const modal = document.getElementById('villagePhotosDialog');
            const viewport = document.getElementById('villageMapViewport');
            const dropOverlay = document.getElementById('villageMapDropOverlay');

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
                        triggerPhotoUpload(cur.id) || openVillagePhotosModal();
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
                    // check if leaving viewport
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

        document.addEventListener('DOMContentLoaded', bindPhotosManagerEvents);
        setTimeout(bindPhotosManagerEvents, 200);
"""

# Insert js_photos_manager right before the closing script tag
idx_end_script = html.rfind("</script>")
assert idx_end_script != -1, "</script> not found"
html = html[:idx_end_script] + js_photos_manager + "\n    " + html[idx_end_script:]
print("6. Injected Photos Manager JavaScript Engine!")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("SUCCESS: Village Photos Manager successfully injected into index.html!")
