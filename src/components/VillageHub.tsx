import React from 'react';
import { VillageData, VILLAGES_DATA } from '../data/villages';
import { ArrowLeft, BarChart3, Stethoscope, ArrowRight, MapPin, Users, School, ArrowUpRight } from 'lucide-react';

interface VillageHubProps {
  village: VillageData;
  onBackToMap: () => void;
  onOpenStats: () => void;
  onOpenServices: () => void;
  onSelectAnotherVillage: (village: VillageData) => void;
}

export const VillageHub: React.FC<VillageHubProps> = ({
  village,
  onBackToMap,
  onOpenStats,
  onOpenServices,
  onSelectAnotherVillage,
}) => {
  return (
    <div className="absolute inset-0 z-30 flex flex-col justify-between bg-gradient-to-b from-[#142e2e]/90 via-[#193a38]/85 to-[#0e1f1e]/95 backdrop-blur-md p-6 animate-fade-in text-[#f3ebdd] overflow-y-auto">
      {/* Top Bar with Back Button */}
      <div className="flex items-center justify-between">
        <button
          onClick={onBackToMap}
          className="flex items-center gap-2 px-4 py-2 rounded-full bg-white/10 hover:bg-white/20 text-[#edd395] border border-[#c6a15b]/40 text-xs font-bold transition-all shadow-lg active:scale-95"
        >
          <ArrowRight className="w-4 h-4" />
          <span>بازگشت به نقشه منطقه</span>
        </button>

        {/* Quick village switcher dropdown / pill */}
        <div className="flex items-center gap-1.5 overflow-x-auto max-w-md py-1">
          {VILLAGES_DATA.slice(0, 5).map((v) => (
            <button
              key={v.id}
              onClick={() => onSelectAnotherVillage(v)}
              className={`px-3 py-1 rounded-full text-xs font-bold transition-all whitespace-nowrap ${
                v.id === village.id
                  ? 'bg-[#c6a15b] text-stone-900 shadow-md'
                  : 'bg-white/5 hover:bg-white/15 text-stone-300 border border-white/10'
              }`}
            >
              {v.name}
            </button>
          ))}
        </div>
      </div>

      {/* Center Content */}
      <div className="max-w-2xl mx-auto w-full my-auto text-center space-y-6 py-6">
        <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-[#c6a15b]/20 border border-[#c6a15b]/30 text-xs font-bold text-[#edd395]">
          <MapPin className="w-3.5 h-3.5 text-[#c6a15b]" />
          <span>حوزه عملیاتی خرمشهر و محور مرزی شلمچه</span>
        </div>

        <div>
          <h1 className="text-5xl sm:text-7xl font-black text-white tracking-tight drop-shadow-md">
            روستای {village.name}
          </h1>
          <p className="text-sm sm:text-base text-stone-300 mt-3 max-w-lg mx-auto leading-relaxed">
            {village.tagline || 'اطلاعات، آمار و وضعیت منطقه تحت پوشش جمعیت بین‌المللی امام‌رضایی‌ها'}
          </p>
        </div>

        {/* Quick Highlights */}
        <div className="grid grid-cols-3 gap-3 max-w-lg mx-auto text-center pt-2">
          <div className="p-3 rounded-2xl bg-white/5 border border-white/10 backdrop-blur-md">
            <span className="text-[11px] text-stone-400 block mb-1">جمعیت</span>
            <strong className="text-base sm:text-xl font-extrabold text-[#edd395]">
              {village.population ? village.population.toLocaleString('fa-IR') : '—'}
            </strong>
          </div>
          <div className="p-3 rounded-2xl bg-white/5 border border-white/10 backdrop-blur-md">
            <span className="text-[11px] text-stone-400 block mb-1">خانوار</span>
            <strong className="text-base sm:text-xl font-extrabold text-[#edd395]">
              {village.households ? village.households.toLocaleString('fa-IR') : '—'}
            </strong>
          </div>
          <div className="p-3 rounded-2xl bg-white/5 border border-white/10 backdrop-blur-md">
            <span className="text-[11px] text-stone-400 block mb-1">حمایت‌ها</span>
            <strong className="text-base sm:text-xl font-extrabold text-[#edd395]">
              {((village.orphans?.length || 0) + (village.underprivileged?.length || 0)).toLocaleString(
                'fa-IR'
              )}
            </strong>
          </div>
        </div>

        {/* Action Cards (Stats & Services) */}
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 max-w-xl mx-auto pt-4 text-right">
          {/* Card 1: Stats & Dossier */}
          <button
            onClick={onOpenStats}
            className="group relative p-6 rounded-2xl bg-white/10 hover:bg-white/15 border border-white/20 hover:border-[#c6a15b] transition-all duration-300 shadow-xl hover:-translate-y-1 text-right flex flex-col justify-between"
          >
            <div className="flex items-center justify-between mb-4">
              <div className="p-3 rounded-xl bg-[#c6a15b]/20 text-[#edd395]">
                <BarChart3 className="w-6 h-6" />
              </div>
              <span className="font-mono text-xs text-stone-400 font-bold">۰۱</span>
            </div>

            <div>
              <h2 className="text-2xl font-black text-white group-hover:text-[#edd395] transition-colors">
                آمار و پرونده‌ها
              </h2>
              <p className="text-xs text-stone-300 mt-1.5 leading-relaxed">
                جمعیت، فهرست مدارس، ایتام، خانوارهای کم‌برخوردار و نیازهای توانبخشی
              </p>
            </div>

            <div className="flex items-center gap-1 text-xs font-bold text-[#c6a15b] mt-5 group-hover:translate-x-[-4px] transition-transform">
              <span>مشاهده جزئیات پرونده</span>
              <ArrowLeft className="w-4 h-4" />
            </div>
          </button>

          {/* Card 2: Services & Healthcare */}
          <button
            onClick={onOpenServices}
            className="group relative p-6 rounded-2xl bg-white/10 hover:bg-white/15 border border-white/20 hover:border-[#c6a15b] transition-all duration-300 shadow-xl hover:-translate-y-1 text-right flex flex-col justify-between"
          >
            <div className="flex items-center justify-between mb-4">
              <div className="p-3 rounded-xl bg-teal-500/20 text-teal-300">
                <Stethoscope className="w-6 h-6" />
              </div>
              <span className="font-mono text-xs text-stone-400 font-bold">۰۲</span>
            </div>

            <div>
              <h2 className="text-2xl font-black text-white group-hover:text-[#edd395] transition-colors">
                خدمات و سلامت
              </h2>
              <p className="text-xs text-stone-300 mt-1.5 leading-relaxed">
                مراکز جامع سلامت، خدمات درمانی، زمان‌های دسترسی و وضعیت بیمارستانی
              </p>
            </div>

            <div className="flex items-center gap-1 text-xs font-bold text-teal-400 mt-5 group-hover:translate-x-[-4px] transition-transform">
              <span>گزارش خدمات منطقه</span>
              <ArrowLeft className="w-4 h-4" />
            </div>
          </button>
        </div>
      </div>

      {/* Bottom Footer */}
      <div className="text-center text-xs text-stone-400">
        جمعیت بین‌المللی امام‌رضایی‌ها · منطقه عملیاتی خرمشهر و شلمچه
      </div>
    </div>
  );
};
