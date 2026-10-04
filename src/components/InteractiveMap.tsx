import React, { useState, useRef, useEffect, useCallback } from 'react';
import { VillageData, VILLAGES_DATA } from '../data/villages';
import { ZoomIn, ZoomOut, Maximize2, MapPin, Compass, Eye, ShieldCheck, Info } from 'lucide-react';

interface InteractiveMapProps {
  onSelectVillage: (village: VillageData) => void;
  selectedVillage: VillageData | null;
  privacyMode: boolean;
  onTogglePrivacy: () => void;
}

export const InteractiveMap: React.FC<InteractiveMapProps> = ({
  onSelectVillage,
  selectedVillage,
  privacyMode,
  onTogglePrivacy,
}) => {
  const containerRef = useRef<HTMLDivElement>(null);
  const [scale, setScale] = useState(1);
  const [position, setPosition] = useState({ x: 0, y: 0 });
  const [isDragging, setIsDragging] = useState(false);
  const [dragStart, setDragStart] = useState({ x: 0, y: 0 });
  const [hoveredVillage, setHoveredVillage] = useState<VillageData | null>(null);

  // Reset or focus
  const resetView = useCallback(() => {
    setScale(1);
    setPosition({ x: 0, y: 0 });
  }, []);

  const zoom = (factor: number) => {
    setScale((prev) => Math.min(3.5, Math.max(0.7, prev * factor)));
  };

  const handlePointerDown = (e: React.PointerEvent) => {
    if ((e.target as HTMLElement).closest('button')) return;
    setIsDragging(true);
    setDragStart({ x: e.clientX - position.x, y: e.clientY - position.y });
    (e.currentTarget as HTMLElement).setPointerCapture(e.pointerId);
  };

  const handlePointerMove = (e: React.PointerEvent) => {
    if (!isDragging) return;
    setPosition({
      x: e.clientX - dragStart.x,
      y: e.clientY - dragStart.y,
    });
  };

  const handlePointerUp = (e: React.PointerEvent) => {
    setIsDragging(false);
    try {
      (e.currentTarget as HTMLElement).releasePointerCapture(e.pointerId);
    } catch {
      // ignore
    }
  };

  const handleWheel = (e: React.WheelEvent) => {
    e.preventDefault();
    const factor = e.deltaY < 0 ? 1.12 : 0.89;
    setScale((prev) => Math.min(3.5, Math.max(0.7, prev * factor)));
  };

  return (
    <div
      ref={containerRef}
      className={`relative w-full h-screen overflow-hidden select-none bg-[#112423] ${
        isDragging ? 'cursor-grabbing' : 'cursor-grab'
      }`}
      onPointerDown={handlePointerDown}
      onPointerMove={handlePointerMove}
      onPointerUp={handlePointerUp}
      onWheel={handleWheel}
      aria-label="نقشه تعاملی منطقه خرمشهر و شلمچه"
    >
      {/* Background Graphic Grid & Satellite / Schematic stylized map */}
      <div
        className="absolute inset-0 transition-transform duration-300 ease-out origin-center"
        style={{
          transform: `translate(${position.x}px, ${position.y}px) scale(${scale})`,
        }}
      >
        {/* SVG Base Map depicting Karun River, Arvand waterway, Shalamcheh rail axis, and terrain */}
        <svg
          viewBox="0 0 1600 1000"
          className="w-full h-full min-w-[1200px] min-h-[800px] pointer-events-none drop-shadow-2xl"
          preserveAspectRatio="xMidYMid slice"
        >
          <defs>
            <radialGradient id="mapGlow" cx="50%" cy="50%" r="50%">
              <stop offset="0%" stopColor="#1e3e3b" stopOpacity="0.8" />
              <stop offset="60%" stopColor="#142a29" stopOpacity="0.9" />
              <stop offset="100%" stopColor="#0d1b1a" stopOpacity="1" />
            </radialGradient>
            <linearGradient id="riverGrad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stopColor="#255150" stopOpacity="0.9" />
              <stop offset="50%" stopColor="#306b6a" stopOpacity="0.8" />
              <stop offset="100%" stopColor="#1b4140" stopOpacity="0.9" />
            </linearGradient>
            <pattern id="palmPattern" width="40" height="40" patternUnits="userSpaceOnUse">
              <circle cx="20" cy="20" r="1.5" fill="#4d6f66" opacity="0.3" />
              <circle cx="10" cy="10" r="1" fill="#395850" opacity="0.2" />
            </pattern>
            <pattern id="gridPattern" width="100" height="100" patternUnits="userSpaceOnUse">
              <path d="M 100 0 L 0 0 0 100" fill="none" stroke="#254743" strokeWidth="0.8" opacity="0.4" />
            </pattern>
          </defs>

          {/* Background fill */}
          <rect width="1600" height="1000" fill="url(#mapGlow)" />
          <rect width="1600" height="1000" fill="url(#gridPattern)" />
          <rect width="1600" height="1000" fill="url(#palmPattern)" />

          {/* Arvand / Karun River flows through the east & south */}
          <path
            d="M 1600 700 C 1450 720, 1300 780, 1200 850 C 1100 920, 950 960, 800 980 L 1600 1000 Z"
            fill="url(#riverGrad)"
            opacity="0.75"
          />
          <path
            d="M 1350 400 C 1300 550, 1280 700, 1200 850"
            fill="none"
            stroke="#3b7d7b"
            strokeWidth="38"
            strokeLinecap="round"
            opacity="0.65"
          />
          {/* River label */}
          <text x="1310" y="580" fill="#a4cfcb" fontSize="16" fontWeight="700" letterSpacing="4" transform="rotate(78 1310 580)">
            اروندرود / شاخه کارون
          </text>

          {/* Shalamcheh Strategic Highway / Axis */}
          <path
            d="M 150 180 Q 500 380, 1100 700 T 1450 820"
            fill="none"
            stroke="#857147"
            strokeWidth="8"
            strokeDasharray="14,8"
            opacity="0.6"
          />
          <text x="520" y="380" fill="#c6a15b" fontSize="13" fontWeight="600" letterSpacing="2" transform="rotate(24 520 380)">
            محور بزرگراه خرمشهر — مرز شلمچه
          </text>

          {/* Railway line */}
          <path
            d="M 140 220 Q 550 430, 1150 740"
            fill="none"
            stroke="#9c7a3d"
            strokeWidth="3"
            strokeDasharray="6,6"
            opacity="0.5"
          />

          {/* Regional Zones */}
          <circle cx="1070" cy="680" r="140" fill="#c6a15b" fillOpacity="0.04" stroke="#c6a15b" strokeWidth="1" strokeDasharray="6 6" />
          <circle cx="880" cy="430" r="110" fill="#c6a15b" fillOpacity="0.03" stroke="#c6a15b" strokeWidth="1" strokeDasharray="4 4" />

          {/* Watermark Logo / Stamp */}
          <g opacity="0.08" transform="translate(680, 420)">
            <circle cx="120" cy="120" r="110" fill="none" stroke="#fff" strokeWidth="6" />
            <text x="120" y="130" textAnchor="middle" fill="#fff" fontSize="24" fontWeight="bold">
              جمعیت امام‌رضایی‌ها · خرمشهر
            </text>
          </g>
        </svg>

        {/* Village Markers (Pins) */}
        <div className="absolute inset-0 pointer-events-auto">
          {VILLAGES_DATA.map((village) => {
            const isSelected = selectedVillage?.id === village.id;
            const hasDetailedData = Boolean(village.orphans || village.underprivileged || village.schools);

            return (
              <button
                key={village.id}
                onClick={() => onSelectVillage(village)}
                onMouseEnter={() => setHoveredVillage(village)}
                onMouseLeave={() => setHoveredVillage(null)}
                style={{
                  left: `${village.x * 100}%`,
                  top: `${village.y * 100}%`,
                }}
                className={`absolute -translate-x-1/2 -translate-y-1/2 flex items-center gap-2.5 px-3 py-1.5 rounded-full transition-all duration-300 focus:outline-none group z-10 ${
                  isSelected
                    ? 'bg-amber-400 text-stone-900 font-extrabold scale-125 shadow-[0_0_25px_rgba(251,191,36,0.8)] z-30 border-2 border-white'
                    : hasDetailedData
                    ? 'bg-[#1a3837]/90 hover:bg-[#204a48] text-[#f3ebdd] border border-[#c6a15b]/60 shadow-[0_4px_16px_rgba(0,0,0,0.5)] hover:scale-110 hover:border-[#edd395] hover:z-20'
                    : 'bg-[#142827]/75 hover:bg-[#1a3837] text-stone-300 border border-stone-600/40 shadow-md hover:scale-105'
                }`}
                title={`روستای ${village.name} - مشاهده پرونده`}
              >
                {/* Pin pulsating dot */}
                <div className="relative flex items-center justify-center">
                  <div
                    className={`w-3 h-3 rounded-full transition-all ${
                      isSelected
                        ? 'bg-stone-900'
                        : hasDetailedData
                        ? 'bg-[#c6a15b]'
                        : 'bg-stone-400'
                    }`}
                  />
                  {hasDetailedData && !isSelected && (
                    <div className="absolute inset-[-4px] rounded-full border border-[#c6a15b] pulse-ring pointer-events-none" />
                  )}
                </div>

                <span className="text-xs sm:text-sm font-bold tracking-tight whitespace-nowrap">
                  {village.name}
                </span>

                {/* Badge indicator if village has orphans / underprivileged data */}
                {hasDetailedData && (
                  <span
                    className={`text-[10px] font-mono px-1.5 py-0.5 rounded-full ${
                      isSelected
                        ? 'bg-stone-900 text-amber-300'
                        : 'bg-[#c6a15b]/20 text-[#edd395] border border-[#c6a15b]/30'
                    }`}
                  >
                    پرونده
                  </span>
                )}
              </button>
            );
          })}
        </div>
      </div>

      {/* Floating Compass / North indicator */}
      <div className="absolute top-20 right-6 z-20 flex flex-col items-center gap-1 bg-[#142a29]/80 backdrop-blur-md border border-[#c6a15b]/30 px-3 py-2 rounded-2xl shadow-xl pointer-events-none">
        <Compass className="w-5 h-5 text-[#c6a15b] animate-spin-slow" />
        <span className="text-[10px] text-[#edd395] font-bold">شمال جغرافیایی</span>
      </div>

      {/* Hover Info Tooltip */}
      {hoveredVillage && (
        <div
          className="absolute bottom-24 right-6 z-20 hidden md:block max-w-xs bg-[#162e2d]/95 backdrop-blur-xl border border-[#c6a15b]/40 rounded-2xl p-4 shadow-2xl transition-all"
        >
          <div className="flex items-center justify-between gap-2 border-b border-[#c6a15b]/20 pb-2 mb-2">
            <span className="text-xs font-semibold text-[#edd395]">پیش‌نمایش مشخصات</span>
            <span className="text-[10px] text-stone-400 font-mono">{hoveredVillage.coordinates}</span>
          </div>
          <h4 className="text-base font-extrabold text-[#f3ebdd] flex items-center gap-2">
            <MapPin className="w-4 h-4 text-[#c6a15b]" />
            روستای {hoveredVillage.name}
          </h4>
          <p className="text-xs text-stone-300 mt-1 leading-relaxed">
            {hoveredVillage.tagline || 'روستای واقع در حوزه طرح خدمات امام‌رضایی‌ها'}
          </p>

          <div className="grid grid-cols-2 gap-2 mt-3 text-xs">
            <div className="bg-[#0f1f1e] p-2 rounded-lg border border-stone-700/50">
              <span className="text-[10px] text-stone-400 block">جمعیت</span>
              <strong className="text-[#edd395] font-bold">
                {hoveredVillage.population ? hoveredVillage.population.toLocaleString('fa-IR') + ' نفر' : 'در حال ثبت'}
              </strong>
            </div>
            <div className="bg-[#0f1f1e] p-2 rounded-lg border border-stone-700/50">
              <span className="text-[10px] text-stone-400 block">خانوارها</span>
              <strong className="text-[#edd395] font-bold">
                {hoveredVillage.households ? hoveredVillage.households.toLocaleString('fa-IR') + ' خانوار' : 'در حال ثبت'}
              </strong>
            </div>
          </div>
        </div>
      )}

      {/* Floating Map Tools (Zoom, Overview, Privacy Toggle) */}
      <div className="absolute bottom-6 left-6 z-20 flex items-center gap-2 bg-[#142a29]/90 backdrop-blur-md border border-[#c6a15b]/40 p-2 rounded-2xl shadow-2xl">
        <button
          onClick={() => zoom(1.25)}
          className="p-2.5 rounded-xl bg-white/10 hover:bg-white/20 text-[#f3ebdd] transition-all"
          title="بزرگ‌نمایی (+)"
          aria-label="بزرگ‌نمایی"
        >
          <ZoomIn className="w-4 h-4" />
        </button>

        <button
          onClick={() => zoom(0.8)}
          className="p-2.5 rounded-xl bg-white/10 hover:bg-white/20 text-[#f3ebdd] transition-all"
          title="کوچک‌نمایی (-)"
          aria-label="کوچک‌نمایی"
        >
          <ZoomOut className="w-4 h-4" />
        </button>

        <button
          onClick={resetView}
          className="px-3 py-2 text-xs font-bold rounded-xl bg-white/10 hover:bg-white/20 text-[#edd395] transition-all flex items-center gap-1.5"
          title="نمای کلی نقشه"
        >
          <Maximize2 className="w-3.5 h-3.5" />
          <span>نمای کامل</span>
        </button>

        <div className="w-[1px] h-6 bg-white/20 mx-1" />

        {/* Privacy Masking Toggle */}
        <button
          onClick={onTogglePrivacy}
          className={`px-3 py-2 text-xs font-bold rounded-xl transition-all flex items-center gap-1.5 ${
            privacyMode
              ? 'bg-emerald-800/60 text-emerald-200 border border-emerald-500/40 hover:bg-emerald-800/80'
              : 'bg-amber-900/60 text-amber-200 border border-amber-500/40 hover:bg-amber-900/80'
          }`}
          title="تغییر وضعیت ماسک اطلاعات هویتی و شماره تماس"
        >
          {privacyMode ? (
            <>
              <ShieldCheck className="w-4 h-4 text-emerald-400" />
              <span>ماسک امنیتی فعال</span>
            </>
          ) : (
            <>
              <Eye className="w-4 h-4 text-amber-300" />
              <span>نمایش کامل داده</span>
            </>
          )}
        </button>
      </div>
    </div>
  );
};
