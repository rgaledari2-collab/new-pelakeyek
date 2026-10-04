import React, { useState, useMemo } from 'react';
import { VillageData, OrphanRecord, UnderprivilegedRecord } from '../data/villages';
import {
  X,
  Users,
  Home,
  GraduationCap,
  HeartHandshake,
  Search,
  ShieldCheck,
  ShieldAlert,
  Building2,
  FileSpreadsheet,
  ChevronDown,
  ChevronUp,
  MapPin,
  HeartPulse,
} from 'lucide-react';

interface VillageDossierModalProps {
  village: VillageData;
  onClose: () => void;
  privacyMode: boolean;
  onTogglePrivacy: () => void;
}

export const VillageDossierModal: React.FC<VillageDossierModalProps> = ({
  village,
  onClose,
  privacyMode,
  onTogglePrivacy,
}) => {
  const [searchTerm, setSearchTerm] = useState('');
  const [activeTab, setActiveTab] = useState<'overview' | 'schools' | 'orphans' | 'underprivileged' | 'disability'>('overview');

  const maskNationalId = (id: string | undefined): string => {
    if (!id || id === '—' || id === '*' || id.includes('عراقی')) return id || '—';
    if (!privacyMode) return id;
    if (id.length < 5) return '***';
    return id.substring(0, 3) + '****' + id.substring(id.length - 2);
  };

  const maskPhone = (phone: string | undefined): string => {
    if (!phone || phone === '—' || phone === '*') return phone || '—';
    if (!privacyMode) return phone;
    const clean = phone.replace(/[^0-9]/g, '');
    if (clean.length < 8) return '۰۹*********';
    return clean.substring(0, 4) + '***' + clean.substring(clean.length - 3);
  };

  // Filter orphans by search term
  const filteredOrphans = useMemo(() => {
    if (!village.orphans) return [];
    if (!searchTerm.trim()) return village.orphans;
    const q = searchTerm.toLowerCase();
    return village.orphans.filter(
      (o) =>
        o.childName.toLowerCase().includes(q) ||
        o.childLastName.toLowerCase().includes(q) ||
        o.guardianName.toLowerCase().includes(q) ||
        o.address.toLowerCase().includes(q) ||
        o.schoolName.toLowerCase().includes(q)
    );
  }, [village.orphans, searchTerm]);

  // Filter underprivileged families
  const filteredUnderprivileged = useMemo(() => {
    if (!village.underprivileged) return [];
    if (!searchTerm.trim()) return village.underprivileged;
    const q = searchTerm.toLowerCase();
    return village.underprivileged.filter(
      (u) => u.fullName.toLowerCase().includes(q) || u.address.toLowerCase().includes(q)
    );
  }, [village.underprivileged, searchTerm]);

  return (
    <div
      className="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-6 bg-black/75 backdrop-blur-md animate-fade-in"
      onClick={onClose}
    >
      <div
        className="relative w-full max-w-5xl max-h-[92vh] flex flex-col bg-[#faf6ef] text-[#111111] rounded-2xl shadow-2xl overflow-hidden border border-[#c6a15b]/40"
        onClick={(e) => e.stopPropagation()}
        dir="rtl"
      >
        {/* Header Bar */}
        <div className="flex items-center justify-between px-6 py-4 bg-[#f0e9d9] border-b border-[#111111]/10 flex-shrink-0">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-xl bg-[#8B322C] text-[#f3ebdd] flex items-center justify-center font-black text-xl shadow-md">
              {village.name.charAt(0)}
            </div>
            <div>
              <div className="text-[11px] font-bold text-[#DD5746]">شناسنامه آماری و اجتماعی</div>
              <h2 className="text-xl font-extrabold text-[#8B322C] flex items-center gap-2">
                روستای {village.name}
              </h2>
            </div>
          </div>

          <div className="flex items-center gap-2">
            {/* Privacy Toggle Button inside Modal */}
            <button
              onClick={onTogglePrivacy}
              className={`px-3 py-1.5 text-xs font-bold rounded-lg transition-all flex items-center gap-1.5 ${
                privacyMode
                  ? 'bg-emerald-100 text-emerald-800 border border-emerald-300'
                  : 'bg-amber-100 text-amber-800 border border-amber-300'
              }`}
              title="تغییر وضعیت ماسک اطلاعات شخصی"
            >
              {privacyMode ? (
                <>
                  <ShieldCheck className="w-4 h-4 text-emerald-700" />
                  <span className="hidden sm:inline">ماسک اطلاعات فعال</span>
                </>
              ) : (
                <>
                  <ShieldAlert className="w-4 h-4 text-amber-700" />
                  <span className="hidden sm:inline">حالت بازرسی کامل</span>
                </>
              )}
            </button>

            <button
              onClick={onClose}
              className="p-2 rounded-full text-[#8B322C] hover:bg-[#8B322C]/10 transition-transform active:scale-90"
              aria-label="بستن"
            >
              <X className="w-6 h-6" />
            </button>
          </div>
        </div>

        {/* Navigation Tabs */}
        <div className="flex overflow-x-auto gap-2 px-6 py-2.5 bg-[#e8dfc8]/60 border-b border-[#111111]/10 text-xs font-bold flex-shrink-0">
          <button
            onClick={() => setActiveTab('overview')}
            className={`px-4 py-2 rounded-xl transition-all whitespace-nowrap flex items-center gap-1.5 ${
              activeTab === 'overview'
                ? 'bg-[#8B322C] text-white shadow-sm'
                : 'text-[#555] hover:bg-[#f0e9d9]'
            }`}
          >
            <Home className="w-4 h-4" />
            نمای کلی و زیرساخت
          </button>

          {village.schools && (
            <button
              onClick={() => setActiveTab('schools')}
              className={`px-4 py-2 rounded-xl transition-all whitespace-nowrap flex items-center gap-1.5 ${
                activeTab === 'schools'
                  ? 'bg-[#8B322C] text-white shadow-sm'
                  : 'text-[#555] hover:bg-[#f0e9d9]'
              }`}
            >
              <GraduationCap className="w-4 h-4" />
              مدارس و دانش‌آموزان
              <span className="px-1.5 py-0.2 text-[10px] rounded-full bg-white/20">
                {village.schools.reduce((acc, s) => acc + s.total, 0)}
              </span>
            </button>
          )}

          {village.orphans && (
            <button
              onClick={() => setActiveTab('orphans')}
              className={`px-4 py-2 rounded-xl transition-all whitespace-nowrap flex items-center gap-1.5 ${
                activeTab === 'orphans'
                  ? 'bg-[#8B322C] text-white shadow-sm'
                  : 'text-[#555] hover:bg-[#f0e9d9]'
              }`}
            >
              <HeartHandshake className="w-4 h-4" />
              ایتام تحت پایش
              <span className="px-1.5 py-0.2 text-[10px] rounded-full bg-white/20">
                {village.orphans.length}
              </span>
            </button>
          )}

          {village.underprivileged && (
            <button
              onClick={() => setActiveTab('underprivileged')}
              className={`px-4 py-2 rounded-xl transition-all whitespace-nowrap flex items-center gap-1.5 ${
                activeTab === 'underprivileged'
                  ? 'bg-[#8B322C] text-white shadow-sm'
                  : 'text-[#555] hover:bg-[#f0e9d9]'
              }`}
            >
              <Users className="w-4 h-4" />
              خانوارهای کم‌برخوردار
              <span className="px-1.5 py-0.2 text-[10px] rounded-full bg-white/20">
                {village.underprivileged.length}
              </span>
            </button>
          )}

          {village.disabilityStats && (
            <button
              onClick={() => setActiveTab('disability')}
              className={`px-4 py-2 rounded-xl transition-all whitespace-nowrap flex items-center gap-1.5 ${
                activeTab === 'disability'
                  ? 'bg-[#8B322C] text-white shadow-sm'
                  : 'text-[#555] hover:bg-[#f0e9d9]'
              }`}
            >
              <HeartPulse className="w-4 h-4" />
              آمار کم‌توانی و سلامت
            </button>
          )}
        </div>

        {/* Content Body */}
        <div className="flex-1 overflow-y-auto p-6 space-y-6">
          {/* TAB 1: OVERVIEW & INFRASTRUCTURE */}
          {activeTab === 'overview' && (
            <div className="space-y-6">
              {/* Top Key Metrics */}
              <div className="grid grid-cols-2 sm:grid-cols-4 gap-4">
                <div className="p-4 rounded-xl bg-white border border-[#c6a15b]/30 shadow-sm flex flex-col justify-between">
                  <span className="text-xs text-stone-500 font-bold">جمعیت ساکن</span>
                  <div className="text-3xl font-black text-[#8B322C] mt-2">
                    {village.population ? village.population.toLocaleString('fa-IR') : '—'}
                  </div>
                  <span className="text-[11px] text-[#DD5746] mt-1">نفر بر اساس آخرین سرشماری</span>
                </div>

                <div className="p-4 rounded-xl bg-white border border-[#c6a15b]/30 shadow-sm flex flex-col justify-between">
                  <span className="text-xs text-stone-500 font-bold">تعداد خانوار</span>
                  <div className="text-3xl font-black text-[#8B322C] mt-2">
                    {village.households ? village.households.toLocaleString('fa-IR') : '—'}
                  </div>
                  <span className="text-[11px] text-[#DD5746] mt-1">خانواده مستقر</span>
                </div>

                <div className="p-4 rounded-xl bg-white border border-[#c6a15b]/30 shadow-sm flex flex-col justify-between">
                  <span className="text-xs text-stone-500 font-bold">دانش‌آموزان ابتدایی</span>
                  <div className="text-3xl font-black text-[#8B322C] mt-2">
                    {village.schools
                      ? village.schools.reduce((acc, s) => acc + s.total, 0).toLocaleString('fa-IR')
                      : '—'}
                  </div>
                  <span className="text-[11px] text-[#DD5746] mt-1">محصلین در پایه‌های مختلف</span>
                </div>

                <div className="p-4 rounded-xl bg-white border border-[#c6a15b]/30 shadow-sm flex flex-col justify-between">
                  <span className="text-xs text-stone-500 font-bold">پرونده‌های حمایتی</span>
                  <div className="text-3xl font-black text-[#8B322C] mt-2">
                    {((village.orphans?.length || 0) + (village.underprivileged?.length || 0)).toLocaleString(
                      'fa-IR'
                    )}
                  </div>
                  <span className="text-[11px] text-[#DD5746] mt-1">ایتام و خانوارهای کم‌برخوردار</span>
                </div>
              </div>

              {/* Geographic and administrative details */}
              <div className="bg-[#f0e9d9] p-5 rounded-2xl border border-[#111111]/10">
                <h3 className="text-sm font-extrabold text-[#8B322C] flex items-center gap-2 mb-3">
                  <MapPin className="w-4 h-4" />
                  مشخصات اداری و موقعیت جغرافیایی
                </h3>
                <div className="grid grid-cols-1 sm:grid-cols-3 gap-3 text-xs">
                  <div className="bg-white/80 p-3 rounded-xl border border-stone-300">
                    <span className="text-stone-500 block mb-1">استان / شهرستان:</span>
                    <strong className="text-stone-800 text-sm">{village.province}، {village.county}</strong>
                  </div>
                  <div className="bg-white/80 p-3 rounded-xl border border-stone-300">
                    <span className="text-stone-500 block mb-1">بخش و دهستان:</span>
                    <strong className="text-stone-800 text-sm">{village.district}</strong>
                  </div>
                  <div className="bg-white/80 p-3 rounded-xl border border-stone-300">
                    <span className="text-stone-500 block mb-1">مختصات ماهواره‌ای:</span>
                    <strong className="text-[#8B322C] font-mono text-sm">{village.coordinates}</strong>
                  </div>
                </div>
              </div>

              {/* Infrastructure List */}
              {village.infrastructure && (
                <div>
                  <h3 className="text-base font-extrabold text-[#8B322C] flex items-center gap-2 mb-3">
                    <Building2 className="w-5 h-5 text-[#c6a15b]" />
                    زیرساخت‌ها، اماکن عمومی و آموزشی
                  </h3>
                  <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-3">
                    {village.infrastructure.map((inf, idx) => (
                      <div
                        key={idx}
                        className="bg-white p-4 rounded-xl border border-[#c6a15b]/30 shadow-sm flex items-start justify-between"
                      >
                        <div>
                          <div className="font-bold text-stone-900">{inf.name}</div>
                          <div className="text-xs text-stone-500 mt-1">مساحت عرصه: {inf.area}</div>
                        </div>
                        <div className="bg-[#8B322C]/10 text-[#8B322C] font-extrabold text-xs px-2.5 py-1 rounded-full">
                          {inf.stat} {inf.unit}
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              )}
            </div>
          )}

          {/* TAB 2: SCHOOLS */}
          {activeTab === 'schools' && village.schools && (
            <div className="space-y-4">
              <div className="flex items-center justify-between">
                <h3 className="text-base font-extrabold text-[#8B322C] flex items-center gap-2">
                  <GraduationCap className="w-5 h-5 text-[#c6a15b]" />
                  آمار تفکیکی مدارس و پایه‌های تحصیلی
                </h3>
              </div>

              <div className="overflow-x-auto rounded-xl border border-[#111111]/15 bg-white shadow-sm">
                <table className="w-full text-center text-xs sm:text-sm">
                  <thead className="bg-[#f0e9d9] text-[#111111] font-extrabold border-b border-[#8B322C]">
                    <tr>
                      <th className="py-3 px-4 text-right">نام مدرسه</th>
                      <th className="py-3 px-2">پیش‌دبستانی</th>
                      <th className="py-3 px-2">پایه اول</th>
                      <th className="py-3 px-2">پایه دوم</th>
                      <th className="py-3 px-2">پایه سوم</th>
                      <th className="py-3 px-2">پایه چهارم</th>
                      <th className="py-3 px-2">پایه پنجم</th>
                      <th className="py-3 px-2">پایه ششم</th>
                      <th className="py-3 px-4 bg-[#c6a15b]/20">مجموع دانش‌آموزان</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-stone-200">
                    {village.schools.map((s, idx) => (
                      <tr key={idx} className="hover:bg-amber-50/50">
                        <td className="py-3 px-4 text-right font-bold text-stone-800">{s.schoolName}</td>
                        <td className="py-3 px-2">{s.preSchool}</td>
                        <td className="py-3 px-2">{s.grade1}</td>
                        <td className="py-3 px-2">{s.grade2}</td>
                        <td className="py-3 px-2">{s.grade3}</td>
                        <td className="py-3 px-2">{s.grade4}</td>
                        <td className="py-3 px-2">{s.grade5}</td>
                        <td className="py-3 px-2">{s.grade6}</td>
                        <td className="py-3 px-4 font-black text-[#8B322C] bg-[#c6a15b]/10">{s.total}</td>
                      </tr>
                    ))}
                    {/* Totals row */}
                    <tr className="bg-[#f0e9d9] font-extrabold text-stone-900 border-t-2 border-[#8B322C]">
                      <td className="py-3 px-4 text-right">جمع کل</td>
                      <td className="py-3 px-2">
                        {village.schools.reduce((acc, s) => acc + (typeof s.preSchool === 'number' ? s.preSchool : 0), 0) || '—'}
                      </td>
                      <td className="py-3 px-2">{village.schools.reduce((acc, s) => acc + s.grade1, 0)}</td>
                      <td className="py-3 px-2">{village.schools.reduce((acc, s) => acc + s.grade2, 0)}</td>
                      <td className="py-3 px-2">{village.schools.reduce((acc, s) => acc + s.grade3, 0)}</td>
                      <td className="py-3 px-2">{village.schools.reduce((acc, s) => acc + s.grade4, 0)}</td>
                      <td className="py-3 px-2">{village.schools.reduce((acc, s) => acc + s.grade5, 0)}</td>
                      <td className="py-3 px-2">{village.schools.reduce((acc, s) => acc + s.grade6, 0)}</td>
                      <td className="py-3 px-4 font-black text-[#8B322C] bg-[#c6a15b]/30">
                        {village.schools.reduce((acc, s) => acc + s.total, 0)}
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          )}

          {/* TAB 3: ORPHANS */}
          {activeTab === 'orphans' && village.orphans && (
            <div className="space-y-4">
              <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
                <div>
                  <h3 className="text-base font-extrabold text-[#8B322C] flex items-center gap-2">
                    <HeartHandshake className="w-5 h-5 text-[#DD5746]" />
                    فهرست ایتام تحت پوشش روستای {village.name} ({village.orphans.length} پرونده)
                  </h3>
                  <p className="text-xs text-stone-500 mt-1">
                    شامل مشخصات سرپرست، سن، مقطع تحصیلی، نیازهای درمانی و تماس
                  </p>
                </div>

                {/* Search Bar */}
                <div className="relative w-full sm:w-72">
                  <Search className="w-4 h-4 text-stone-400 absolute right-3 top-1/2 -translate-y-1/2" />
                  <input
                    type="text"
                    placeholder="جستجوی نام، سرپرست یا آدرس..."
                    value={searchTerm}
                    onChange={(e) => setSearchTerm(e.target.value)}
                    className="w-full pl-3 pr-9 py-2 bg-white text-xs border border-stone-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-[#8B322C]"
                  />
                </div>
              </div>

              {/* Data Table */}
              <div className="overflow-x-auto rounded-xl border border-[#111111]/15 bg-white shadow-sm">
                <table className="w-full text-xs text-right whitespace-nowrap">
                  <thead className="bg-[#f0e9d9] text-[#111111] font-bold border-b border-[#8B322C]">
                    <tr>
                      <th className="py-3 px-3">ردیف</th>
                      <th className="py-3 px-3">نام و نام خانوادگی</th>
                      <th className="py-3 px-3">نام پدر</th>
                      <th className="py-3 px-3">کد ملی کودک</th>
                      <th className="py-3 px-3">سن</th>
                      <th className="py-3 px-3">پایه تحصیلی</th>
                      <th className="py-3 px-3">مدرسه</th>
                      <th className="py-3 px-3">نام سرپرست</th>
                      <th className="py-3 px-3">کد ملی سرپرست</th>
                      <th className="py-3 px-3">وضعیت سلامت</th>
                      <th className="py-3 px-3">آدرس</th>
                      <th className="py-3 px-3">شماره تماس</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-stone-200">
                    {filteredOrphans.map((o, idx) => (
                      <tr key={o.id} className="hover:bg-amber-50/50">
                        <td className="py-2.5 px-3 font-mono text-stone-500">{idx + 1}</td>
                        <td className="py-2.5 px-3 font-extrabold text-[#8B322C]">
                          {o.childName} {o.childLastName}
                        </td>
                        <td className="py-2.5 px-3">{o.fatherName}</td>
                        <td className="py-2.5 px-3 font-mono text-stone-600">{maskNationalId(o.childNationalId)}</td>
                        <td className="py-2.5 px-3">{o.childAge}</td>
                        <td className="py-2.5 px-3">{o.educationLevel}</td>
                        <td className="py-2.5 px-3 text-stone-700">{o.schoolName}</td>
                        <td className="py-2.5 px-3 font-medium">{o.guardianName}</td>
                        <td className="py-2.5 px-3 font-mono text-stone-600">{maskNationalId(o.guardianNationalId)}</td>
                        <td className="py-2.5 px-3">
                          <span
                            className={`px-2 py-0.5 rounded-full text-[10px] ${
                              o.healthStatus.includes('دندان') || o.healthStatus.includes('حلق')
                                ? 'bg-rose-100 text-rose-800 font-bold'
                                : 'bg-stone-100 text-stone-700'
                            }`}
                          >
                            {o.healthStatus}
                          </span>
                        </td>
                        <td className="py-2.5 px-3 text-stone-600 max-w-[220px] truncate" title={o.address}>
                          {o.address}
                        </td>
                        <td className="py-2.5 px-3 font-mono text-stone-700">{maskPhone(o.phone)}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>
          )}

          {/* TAB 4: UNDERPRIVILEGED HOUSEHOLDS */}
          {activeTab === 'underprivileged' && village.underprivileged && (
            <div className="space-y-4">
              <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
                <div>
                  <h3 className="text-base font-extrabold text-[#8B322C] flex items-center gap-2">
                    <Users className="w-5 h-5 text-[#DD5746]" />
                    فهرست خانوارهای کم‌برخوردار روستای {village.name} ({village.underprivileged.length} خانوار)
                  </h3>
                  <p className="text-xs text-stone-500 mt-1">
                    بانک اطلاعاتی سرپرستان خانوار جهت تخصیص بسته‌های معیشتی و خدمات عمرانی
                  </p>
                </div>

                <div className="relative w-full sm:w-72">
                  <Search className="w-4 h-4 text-stone-400 absolute right-3 top-1/2 -translate-y-1/2" />
                  <input
                    type="text"
                    placeholder="جستجوی نام یا آدرس..."
                    value={searchTerm}
                    onChange={(e) => setSearchTerm(e.target.value)}
                    className="w-full pl-3 pr-9 py-2 bg-white text-xs border border-stone-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-[#8B322C]"
                  />
                </div>
              </div>

              <div className="overflow-x-auto rounded-xl border border-[#111111]/15 bg-white shadow-sm">
                <table className="w-full text-xs text-right whitespace-nowrap">
                  <thead className="bg-[#f0e9d9] text-[#111111] font-bold border-b border-[#8B322C]">
                    <tr>
                      <th className="py-3 px-3">ردیف</th>
                      <th className="py-3 px-4">نام و نام خانوادگی سرپرست</th>
                      <th className="py-3 px-3">کد ملی</th>
                      <th className="py-3 px-4">شماره تماس</th>
                      <th className="py-3 px-6">نشانی محل سکونت</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-stone-200">
                    {filteredUnderprivileged.map((u, idx) => (
                      <tr key={u.id} className="hover:bg-amber-50/50">
                        <td className="py-2.5 px-3 font-mono text-stone-500">{idx + 1}</td>
                        <td className="py-2.5 px-4 font-bold text-stone-900">{u.fullName}</td>
                        <td className="py-2.5 px-3 font-mono text-stone-600">{maskNationalId(u.nationalId)}</td>
                        <td className="py-2.5 px-4 font-mono text-stone-700">{maskPhone(u.phone)}</td>
                        <td className="py-2.5 px-6 text-stone-700">{u.address}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>
          )}

          {/* TAB 5: DISABILITY STATS */}
          {activeTab === 'disability' && village.disabilityStats && (
            <div className="space-y-4">
              <h3 className="text-base font-extrabold text-[#8B322C] flex items-center gap-2">
                <HeartPulse className="w-5 h-5 text-[#DD5746]" />
                پایش معلولیت‌ها و نیازهای توانبخشی روستای {village.name}
              </h3>

              <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
                {village.disabilityStats.map((item, idx) => {
                  const maxVal = Math.max(...village.disabilityStats!.map((d) => d.count));
                  const percentage = Math.round((item.count / maxVal) * 100);

                  return (
                    <div
                      key={idx}
                      className="bg-white p-4 rounded-xl border border-stone-200 shadow-sm flex flex-col justify-between"
                    >
                      <div className="flex items-center justify-between mb-2">
                        <span className="font-bold text-stone-800 text-sm">{item.label}</span>
                        <span className="text-xl font-black text-[#8B322C]">{item.count} نفر</span>
                      </div>
                      {/* Bar indicator */}
                      <div className="w-full h-2.5 bg-stone-100 rounded-full overflow-hidden">
                        <div
                          className="h-full bg-gradient-to-l from-[#8B322C] to-[#DD5746] rounded-full transition-all duration-500"
                          style={{ width: `${percentage}%` }}
                        />
                      </div>
                    </div>
                  );
                })}
              </div>
            </div>
          )}
        </div>

        {/* Modal Footer Note */}
        <div className="px-6 py-3 bg-[#f0e9d9] border-t border-[#111111]/10 flex flex-col sm:flex-row items-center justify-between text-[11px] text-stone-600 gap-2 flex-shrink-0">
          <span>
            سامانه ثبت داده‌های عملیاتی پایگاه‌های جهادی امام‌رضایی‌ها در شهرستان خرمشهر
          </span>
          <span className="font-mono text-stone-500">منطقه عملیاتی شلمچه و حومه غربی</span>
        </div>
      </div>
    </div>
  );
};
