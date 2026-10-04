import React from 'react';
import { REGIONAL_HEALTH_INFO } from '../data/villages';
import { X, Activity, Clock, AlertTriangle, Building, Stethoscope } from 'lucide-react';

interface ServicesModalProps {
  onClose: () => void;
  villageName?: string;
}

export const ServicesModal: React.FC<ServicesModalProps> = ({ onClose, villageName = 'سوره' }) => {
  return (
    <div
      className="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-6 bg-black/75 backdrop-blur-md animate-fade-in"
      onClick={onClose}
    >
      <div
        className="relative w-full max-w-3xl max-h-[90vh] flex flex-col bg-[#142a29] text-[#f3ebdd] rounded-2xl shadow-2xl overflow-hidden border border-[#c6a15b]/40"
        onClick={(e) => e.stopPropagation()}
        dir="rtl"
      >
        {/* Header */}
        <div className="flex items-center justify-between px-6 py-4 bg-[#1b3836] border-b border-[#c6a15b]/20 flex-shrink-0">
          <div className="flex items-center gap-3">
            <div className="p-2.5 rounded-xl bg-[#c6a15b]/20 text-[#edd395] border border-[#c6a15b]/40">
              <Stethoscope className="w-6 h-6" />
            </div>
            <div>
              <div className="text-[11px] font-bold text-[#edd395]">پایش زیرساخت سلامت و خدمات</div>
              <h2 className="text-xl font-black text-white">خدمات و دسترسی‌های بهداشتی منطقه</h2>
            </div>
          </div>

          <button
            onClick={onClose}
            className="p-2 rounded-full text-stone-300 hover:text-white hover:bg-white/10 transition-transform active:scale-90"
            aria-label="بستن"
          >
            <X className="w-6 h-6" />
          </button>
        </div>

        {/* Content */}
        <div className="flex-1 overflow-y-auto p-6 space-y-6">
          {/* Note Banner */}
          <div className="p-4 rounded-xl bg-amber-500/10 border border-amber-500/30 text-xs text-amber-200 flex items-start gap-3">
            <AlertTriangle className="w-5 h-5 text-amber-400 flex-shrink-0 mt-0.5" />
            <div>
              <strong className="block text-amber-300 mb-0.5 font-bold">اطلاعات مرجع کل حوزه غرب خرمشهر</strong>
              مراکز و زمان‌های ذکرشده شرح زیرساخت‌های کل منطقه (سوره، جدیده، پل‌نو، شلمچه) است و عملکرد اختصاصی یک روستا به تنهایی نیست.
            </div>
          </div>

          {/* Cards Grid */}
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
            {REGIONAL_HEALTH_INFO.centers.map((center, idx) => (
              <div
                key={idx}
                className="p-5 rounded-2xl bg-white/5 border border-white/10 hover:border-[#c6a15b]/40 transition-all space-y-3"
              >
                <div className="flex items-center justify-between">
                  <span className="text-xs px-2.5 py-1 rounded-full bg-[#c6a15b]/20 text-[#edd395] font-bold">
                    {center.badge}
                  </span>
                  {idx === 0 ? (
                    <Building className="w-5 h-5 text-[#c6a15b]" />
                  ) : idx === 1 ? (
                    <Activity className="w-5 h-5 text-[#c6a15b]" />
                  ) : (
                    <Clock className="w-5 h-5 text-[#c6a15b]" />
                  )}
                </div>

                <h3 className="text-base font-bold text-white">{center.title}</h3>
                <p className="text-xs text-stone-300 leading-relaxed">{center.desc}</p>
              </div>
            ))}
          </div>

          {/* Emergency Access Table */}
          <div className="bg-[#102221] p-5 rounded-2xl border border-stone-700/60">
            <h4 className="text-sm font-bold text-[#edd395] mb-3 flex items-center gap-2">
              <Clock className="w-4 h-4" />
              زمان‌بندی انتقال فوریت‌ها به مراکز تخصصی خرمشهر
            </h4>
            <div className="grid grid-cols-1 sm:grid-cols-3 gap-3 text-xs">
              <div className="p-3 rounded-xl bg-white/5 border border-white/5">
                <span className="text-stone-400 block mb-1">تا بیمارستان ولیعصر خرمشهر:</span>
                <strong className="text-white font-mono text-sm">۲۵ الی ۳۰ دقیقه</strong>
              </div>
              <div className="p-3 rounded-xl bg-white/5 border border-white/5">
                <span className="text-stone-400 block mb-1">تا بیمارستان آیت‌الله طالقانی:</span>
                <strong className="text-white font-mono text-sm">۳۵ دقیقه (آبادان)</strong>
              </div>
              <div className="p-3 rounded-xl bg-white/5 border border-white/5">
                <span className="text-stone-400 block mb-1">خانه بهداشت سوره ۱ و ۲:</span>
                <strong className="text-emerald-400 font-mono text-sm">حداکثر ۱۰ دقیقه</strong>
              </div>
            </div>
          </div>
        </div>

        {/* Footer */}
        <div className="px-6 py-3 bg-[#112423] border-t border-[#c6a15b]/20 text-[11px] text-stone-400 flex items-center justify-between">
          <span>{REGIONAL_HEALTH_INFO.source}</span>
          <span className="text-[#c6a15b] font-bold">جمعیت بین‌المللی امام‌رضایی‌ها</span>
        </div>
      </div>
    </div>
  );
};
