import React from 'react';
import { VillageData, VILLAGES_DATA } from '../data/villages';
import { ShieldCheck, ShieldAlert, Cpu, MapPin, Layers } from 'lucide-react';

interface HeaderProps {
  selectedVillage: VillageData | null;
  onSelectVillage: (village: VillageData | null) => void;
  privacyMode: boolean;
  onTogglePrivacy: () => void;
  onOpenAnalysis: () => void;
  onOpenServices: () => void;
}

export const Header: React.FC<HeaderProps> = ({
  selectedVillage,
  onSelectVillage,
  privacyMode,
  onTogglePrivacy,
  onOpenAnalysis,
  onOpenServices,
}) => {
  return (
    <header className="absolute top-0 inset-x-0 z-40 px-4 sm:px-8 py-4 flex items-center justify-between pointer-events-none">
      {/* Brand area */}
      <div className="flex items-center gap-3 bg-[#142a29]/90 backdrop-blur-md border border-[#c6a15b]/40 px-4 py-2 rounded-2xl shadow-xl pointer-events-auto">
        <div className="w-9 h-9 rounded-xl bg-gradient-to-br from-[#c6a15b] to-[#8a754e] text-stone-900 font-black text-xl flex items-center justify-center shadow-md">
          س
        </div>
        <div>
          <div className="text-xs font-black text-white tracking-tight">
            جمعیت بین‌المللی امام‌رضایی‌ها
          </div>
          <div className="text-[10px] text-[#edd395] font-medium flex items-center gap-1">
            <span>اطلس روستایی خرمشهر و شلمچه</span>
          </div>
        </div>
      </div>

      {/* Action buttons */}
      <div className="flex items-center gap-2 pointer-events-auto">
        {/* Village Quick Selector */}
        <div className="hidden lg:flex items-center bg-[#142a29]/90 backdrop-blur-md border border-[#c6a15b]/40 rounded-2xl p-1 shadow-xl">
          <select
            value={selectedVillage?.id || ''}
            onChange={(e) => {
              const found = VILLAGES_DATA.find((v) => v.id === e.target.value);
              if (found) onSelectVillage(found);
              else onSelectVillage(null);
            }}
            className="bg-transparent text-xs font-bold text-[#f3ebdd] px-3 py-1.5 focus:outline-none cursor-pointer"
          >
            <option value="" className="bg-[#142a29] text-white">انتخاب روستا از فهرست...</option>
            {VILLAGES_DATA.map((v) => (
              <option key={v.id} value={v.id} className="bg-[#142a29] text-white">
                {v.name} {v.population ? `(${v.population.toLocaleString('fa-IR')} نفر)` : ''}
              </option>
            ))}
          </select>
        </div>

        {/* Services quick button */}
        <button
          onClick={onOpenServices}
          className="hidden sm:flex items-center gap-1.5 px-3 py-2 rounded-xl bg-[#142a29]/90 hover:bg-[#1c3a39] text-[#edd395] border border-[#c6a15b]/40 text-xs font-bold transition-all shadow-xl"
        >
          <span>خدمات سلامت</span>
        </button>

        {/* Architecture & Security Analysis Button */}
        <button
          onClick={onOpenAnalysis}
          className="flex items-center gap-1.5 px-3.5 py-2 rounded-xl bg-gradient-to-r from-amber-600/80 to-amber-700/80 hover:from-amber-600 hover:to-amber-700 text-white border border-amber-400/50 text-xs font-bold transition-all shadow-xl active:scale-95"
          title="مشاهده گزارش تحلیل مهندسی و ارزیابی فنی سامانه"
        >
          <Cpu className="w-4 h-4 text-amber-200" />
          <span>تحلیل فنی و معماری</span>
        </button>
      </div>
    </header>
  );
};
