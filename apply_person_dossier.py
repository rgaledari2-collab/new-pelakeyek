import json, re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Dialog HTML to inject before <dialog id="statsDialog"
dossier_dialog_html = """
    <!-- DEDICATED BENEFICIARY DOSSIER MODAL (شناسنامه اختصاصی مددجو و پرونده فردی) -->
    <dialog id="personDossierDialog" class="person-dossier-dialog" style="border:none; padding:0; background:transparent; max-width:680px; width:94vw; border-radius:20px; box-shadow:0 30px 90px rgba(0,0,0,0.85); outline:none;">
        <div class="person-dossier-card" style="background:#132624; border:1px solid #edd395; border-radius:20px; overflow:hidden; color:#f3ebdd; font-family:YekanBakh,sans-serif; position:relative;">
            <!-- Header -->
            <div style="background:linear-gradient(135deg, #1c3835 0%, #0d1e1c 100%); padding:18px 24px; border-bottom:1px solid rgba(237,211,149,0.3); display:flex; justify-content:space-between; align-items:center;">
                <div style="display:flex; align-items:center; gap:12px;">
                    <div id="pdAvatarBadge" style="width:46px; height:46px; border-radius:50%; background:linear-gradient(135deg, #c6a15b, #9e7836); display:flex; align-items:center; justify-content:center; font-size:22px; color:#0b1a18; font-weight:800; border:2px solid #edd395; flex-shrink:0;">
                        👤
                    </div>
                    <div>
                        <div style="display:flex; align-items:center; gap:8px; flex-wrap:wrap;">
                            <h2 id="pdFullName" style="margin:0; font-size:18px; font-weight:800; color:#fff;">نام مددجو</h2>
                            <span id="pdRoleBadge" class="search-badge-orphan">ایتام</span>
                            <span id="pdVillagePill" class="search-village-pill">📍 نام روستا</span>
                        </div>
                        <div style="font-size:12px; color:#cbd5e1; margin-top:3px;">
                            <span>سامانه پرونده‌های حمایتی قرارگاه امام‌رضایی‌ها</span> · <span id="pdCaseId" style="color:var(--gold);">پرونده فعال</span>
                        </div>
                    </div>
                </div>
                <button id="closePersonDossierBtn" type="button" style="background:rgba(255,255,255,0.1); border:1px solid rgba(255,255,255,0.2); color:#fff; width:34px; height:34px; border-radius:50%; display:flex; align-items:center; justify-content:center; cursor:pointer; font-size:16px; transition:all 0.15s ease;">
                    ✕
                </button>
            </div>

            <!-- Body -->
            <div style="padding:22px 24px; max-height:calc(85vh - 160px); overflow-y:auto;">
                <!-- 2-Column Info Grid -->
                <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(260px, 1fr)); gap:14px; margin-bottom:16px;">
                    <!-- Identity Card -->
                    <div style="background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.08); border-radius:12px; padding:14px;">
                        <div style="font-size:12px; font-weight:800; color:var(--gold); margin-bottom:10px; display:flex; align-items:center; gap:6px;">
                            <span>📋</span> <span>مشخصات هویتی و ثبت احوال</span>
                        </div>
                        <div style="display:flex; flex-direction:column; gap:8px; font-size:12.5px;">
                            <div style="display:flex; justify-content:space-between; align-items:center;">
                                <span style="color:#94a3b8;">کد ملی:</span>
                                <div style="display:flex; align-items:center; gap:6px;">
                                    <strong id="pdNationalId" style="font-family:monospace; font-size:14px; color:#edd395;">-</strong>
                                    <button type="button" id="copyPdNidBtn" title="کپی کد ملی" style="background:rgba(237,211,149,0.15); border:1px solid rgba(237,211,149,0.4); color:#edd395; font-size:10px; padding:2px 7px; border-radius:4px; cursor:pointer;">کپی</button>
                                </div>
                            </div>
                            <div style="display:flex; justify-content:space-between;">
                                <span style="color:#94a3b8;">نام پدر:</span>
                                <strong id="pdFatherName">-</strong>
                            </div>
                            <div style="display:flex; justify-content:space-between;">
                                <span style="color:#94a3b8;">سرپرست خانوار:</span>
                                <strong id="pdGuardianName" style="color:#fff;">-</strong>
                            </div>
                        </div>
                    </div>

                    <!-- Contact & Communication Card -->
                    <div style="background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.08); border-radius:12px; padding:14px;">
                        <div style="font-size:12px; font-weight:800; color:var(--gold); margin-bottom:10px; display:flex; align-items:center; gap:6px;">
                            <span>📞</span> <span>اطلاعات تماس و پیگیری</span>
                        </div>
                        <div style="display:flex; flex-direction:column; gap:8px; font-size:12.5px;">
                            <div style="display:flex; justify-content:space-between; align-items:center;">
                                <span style="color:#94a3b8;">شماره همراه:</span>
                                <div style="display:flex; align-items:center; gap:6px;">
                                    <strong id="pdPhone" style="font-family:monospace; font-size:13.5px; color:#6ee7b7;">-</strong>
                                    <a id="callPdPhoneBtn" href="#" style="background:rgba(52,211,153,0.2); border:1px solid rgba(52,211,153,0.5); color:#6ee7b7; text-decoration:none; font-size:10px; padding:2px 8px; border-radius:4px; font-weight:700;">تماس</a>
                                </div>
                            </div>
                            <div style="display:flex; justify-content:space-between;">
                                <span style="color:#94a3b8;">وضعیت سلامت:</span>
                                <strong id="pdHealthStatus" style="color:#fcd34d;">سالم / عادی</strong>
                            </div>
                            <div style="display:flex; justify-content:space-between;">
                                <span style="color:#94a3b8;">مدرسه / تحصیل:</span>
                                <strong id="pdEducation">-</strong>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Detailed Address & Landmark -->
                <div style="background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.07); border-radius:12px; padding:14px; margin-bottom:18px;">
                    <div style="font-size:12px; font-weight:800; color:var(--gold); margin-bottom:6px; display:flex; align-items:center; gap:6px;">
                        <span>📍</span> <span>نشانی میدانی، کروکی و راهنمای دسترسی:</span>
                    </div>
                    <p id="pdAddress" style="margin:0; font-size:12.5px; line-height:1.6; color:#e2e8f0; background:rgba(0,0,0,0.2); padding:10px 14px; border-radius:8px; border:1px dashed rgba(255,255,255,0.1);">
                        -
                    </p>
                </div>

                <!-- Action Buttons Footer -->
                <div style="display:flex; align-items:center; gap:10px; flex-wrap:wrap; border-top:1px solid rgba(255,255,255,0.08); padding-top:16px;">
                    <button type="button" id="pdViewInVillageBtn" style="flex:1; min-width:200px; padding:10px 16px; background:linear-gradient(135deg, #c6a15b 0%, #9e7836 100%); color:#0b1a18; font-weight:800; font-size:13px; border:1px solid #edd395; border-radius:10px; cursor:pointer; display:flex; align-items:center; justify-content:center; gap:8px; transition:all 0.15s ease;">
                        <span>🗺️</span>
                        <span id="pdViewVillageLabel">مشاهده در جدول و نقشه روستا</span>
                    </button>
                    <button type="button" id="pdPrintCardBtn" style="padding:10px 18px; background:rgba(255,255,255,0.08); border:1px solid rgba(255,255,255,0.18); color:#f3ebdd; font-weight:700; font-size:12.5px; border-radius:10px; cursor:pointer; display:flex; align-items:center; gap:6px; transition:all 0.15s ease;">
                        <span>🖨️</span>
                        <span>چاپ شناسنامه مددجو</span>
                    </button>
                    <button type="button" id="pdCopySummaryBtn" style="padding:10px 14px; background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.12); color:#cbd5e1; font-size:12px; border-radius:10px; cursor:pointer; display:flex; align-items:center; gap:6px;">
                        <span>📋</span>
                        <span>کپی خلاصه</span>
                    </button>
                </div>
            </div>
        </div>
    </dialog>
"""

# Check where to inject dialog
idx_stats_dlg = html.find('<dialog id="statsDialog"')
assert idx_stats_dlg != -1, "statsDialog not found"
html = html[:idx_stats_dlg] + dossier_dialog_html + "\n    " + html[idx_stats_dlg:]
print("1. Injected personDossierDialog HTML!")

# 2. Add print and toast CSS
extra_css = """
/* Print Mode for Person Dossier Dialog */
@media print {
    body.printing-person-dossier > *:not(#personDossierDialog) {
        display: none !important;
    }
    body.printing-person-dossier #personDossierDialog {
        display: block !important;
        position: static !important;
        max-width: 100% !important;
        width: 100% !important;
        background: #fff !important;
        color: #000 !important;
        border: 2px solid #000 !important;
        box-shadow: none !important;
        border-radius: 0 !important;
        padding: 0 !important;
    }
    body.printing-person-dossier .person-dossier-card {
        background: #fff !important;
        color: #000 !important;
        border: none !important;
    }
    body.printing-person-dossier button,
    body.printing-person-dossier a {
        display: none !important;
    }
}

.search-toast {
    position: fixed;
    bottom: 24px;
    left: 50%;
    transform: translateX(-50%) translateY(20px);
    background: rgba(20, 42, 41, 0.95);
    border: 1px solid var(--gold);
    color: #fff;
    padding: 10px 20px;
    border-radius: 30px;
    font-size: 13px;
    font-weight: 700;
    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    z-index: 9999;
    opacity: 0;
    pointer-events: none;
    transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
}
.search-toast.show {
    opacity: 1;
    transform: translateX(-50%) translateY(0);
}
"""

idx_style_end = html.find("</style>")
assert idx_style_end != -1, "</style> not found"
html = html[:idx_style_end] + extra_css + "\n" + html[idx_style_end:]
print("2. Injected extra CSS for person dossier & toast!")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Stage 1 complete: HTML & CSS updated successfully!")
