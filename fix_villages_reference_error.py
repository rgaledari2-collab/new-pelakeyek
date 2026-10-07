with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# --------------------------------------------------------------------------
# 1. EXPOSE window.villages = villages AND window.enter = enter IN SCRIPT #0
# --------------------------------------------------------------------------
old_expose = "window.back = back;"
new_expose = """window.back = back;
            window.enter = enter;
            window.villages = villages;"""

assert old_expose in html, "window.back = back; not found"
html = html.replace(old_expose, new_expose, 1)
print("1. Exposed window.enter and window.villages in Script #0!")

# --------------------------------------------------------------------------
# 2. UPDATE SCRIPT #1 PHOTO FUNCTIONS TO SAFELY USE getVillageRecord AND window.enter
# --------------------------------------------------------------------------
old_funcs_start = "function saveCustomVillagePhotoFile(vid, file) {"
idx_start = html.find(old_funcs_start)
assert idx_start != -1, "saveCustomVillagePhotoFile not found"

idx_end = html.find("function openVillagePhotosModal() {", idx_start)
assert idx_end != -1, "openVillagePhotosModal not found"

new_funcs = """function getVillageRecord(vid) {
            const list = window.villages || [];
            return list.find(x => x.id === vid) || null;
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

                const vObj = getVillageRecord(vid);
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
            const vObj = getVillageRecord(vid);
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

            const vObj = getVillageRecord(vid);
            const enterFn = window.enter;
            if (vObj && typeof enterFn === 'function') {
                const isVillageView = document.getElementById('experience')?.classList.contains('in-village');
                if (typeof window.back === 'function' && isVillageView) {
                    window.back();
                    setTimeout(() => enterFn(vObj), 150);
                } else {
                    enterFn(vObj);
                }
            }
        }

        """

html = html[:idx_start] + new_funcs + html[idx_end:]
print("2. Replaced photo helper functions with safe getVillageRecord and window.enter in Script #1!")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("SUCCESS: index.html fixed completely!")
