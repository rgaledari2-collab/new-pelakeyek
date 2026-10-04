import React from 'react';
import { X, ShieldAlert, Code2, Sparkles, CheckCircle2, AlertTriangle, Layers, Database, Lock, Cpu } from 'lucide-react';

interface ArchitectureAnalysisModalProps {
  onClose: () => void;
}

export const ArchitectureAnalysisModal: React.FC<ArchitectureAnalysisModalProps> = ({ onClose }) => {
  return (
    <div
      className="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-6 bg-black/80 backdrop-blur-md animate-fade-in"
      onClick={onClose}
    >
      <div
        className="relative w-full max-w-4xl max-h-[92vh] flex flex-col bg-[#142a29] text-[#f3ebdd] rounded-2xl shadow-2xl overflow-hidden border border-[#c6a15b]/40"
        onClick={(e) => e.stopPropagation()}
        dir="rtl"
      >
        {/* Header */}
        <div className="flex items-center justify-between px-6 py-4 bg-[#1b3836] border-b border-[#c6a15b]/20 flex-shrink-0">
          <div className="flex items-center gap-3">
            <div className="p-2.5 rounded-xl bg-amber-500/20 text-amber-300 border border-amber-500/30">
              <Cpu className="w-6 h-6" />
            </div>
            <div>
              <div className="text-[11px] font-bold text-[#edd395]">گزارش تخصصی مهندسی نرم‌افزار و امنیت</div>
              <h2 className="text-xl font-extrabold text-white">تحلیل فنی و معماری سامانه اطلس سوره</h2>
            </div>
          </div>

          <button
            onClick={onClose}
            className="p-2 rounded-full text-stone-300 hover:text-white hover:bg-white/10 transition-transform"
            aria-label="بستن"
          >
            <X className="w-6 h-6" />
          </button>
        </div>

        {/* Content Body */}
        <div className="flex-1 overflow-y-auto p-6 space-y-6 text-sm leading-relaxed">
          {/* Executive Summary */}
          <div className="p-4 rounded-xl bg-[#1d3d3a] border border-[#c6a15b]/30">
            <h3 className="text-base font-bold text-[#edd395] flex items-center gap-2 mb-2">
              <Sparkles className="w-5 h-5 text-[#c6a15b]" />
              خلاصه اجرایی و هدف سامانه
            </h3>
            <p className="text-stone-300 text-xs sm:text-sm">
              این پروژه یک سامانه اطلس جغرافیایی–آماری و داشبورد پرونده‌محور (Dossier System) برای روستاهای منطقه خرمشهر و شلمچه تحت پوشش «جمعیت بین‌المللی امام‌رضایی‌ها» است. هدف آن ترکیب نقشه هوایی تعاملی با اطلاعات جمعیت‌شناختی، سلامت، مدارس، ایتام و خانوارهای کم‌برخوردار جهت تصمیم‌گیری، پایش و خدمات‌رسانی جهادی است.
            </p>
          </div>

          {/* 1. Critical Vulnerabilities & Privacy */}
          <div className="p-5 rounded-xl bg-rose-950/40 border border-rose-500/40 space-y-3">
            <div className="flex items-center gap-2 text-rose-300 font-extrabold text-base">
              <ShieldAlert className="w-5 h-5 text-rose-400" />
              ۱. آسیب‌پذیری بحرانی: حریم خصوصی و امنیت داده‌های هویتی (Data Privacy)
            </div>
            <p className="text-xs sm:text-sm text-rose-100/90 leading-relaxed">
              در سورس کلاینت فایل HTML ارائه شده، کدهای ملی واقعی، شماره تماس‌های شخصی، نشانی دقیق منزل، سن و وضعیت سلامت ده‌ها کودک یتیم و سرپرستان خانوار کم‌برخوردار روستاهای سوره، پل نو و عریض به صورت متن آشکار (Plain Text) و هاردکد قرار گرفته است:
            </p>
            <ul className="list-disc list-inside space-y-1 text-xs text-rose-200">
              <li><strong>افشای اطلاعات محرمانه مددجویان:</strong> هر کاربری با راست‌کلیک و View Source می‌تواند کلیه شماره‌ها و آدرس‌های خانوارها را استخراج کند.</li>
              <li><strong>راهکار مهندسی:</strong> پیاده‌سازی مکانیزم ماسک امنیتی کلاینت و سرور (مانند <code className="bg-rose-900/60 px-1.5 py-0.5 rounded font-mono">۰۹۱۶***۳۸۹۳</code>)، احراز هویت مبتنی بر نقش (RBAC)، و واکشی اطلاعات حساس صرفاً از طریق API امن با دسترسی اپراتور خیریه.</li>
            </ul>
          </div>

          {/* 2. Architecture & Code Smells */}
          <div className="p-5 rounded-xl bg-amber-950/40 border border-amber-500/40 space-y-3">
            <div className="flex items-center gap-2 text-amber-300 font-extrabold text-base">
              <Code2 className="w-5 h-5 text-amber-400" />
              ۲. چالش‌های معماری و مهندسی کد (Code Smells)
            </div>
            <ul className="space-y-2 text-xs sm:text-sm text-amber-100/90">
              <li className="flex items-start gap-2">
                <AlertTriangle className="w-4 h-4 text-amber-400 flex-shrink-0 mt-1" />
                <div>
                  <strong>دستکاری غیراصولی DOM با <code className="font-mono bg-black/30 px-1 rounded">outerHTML</code>:</strong> در تابع <code className="font-mono bg-black/30 px-1 rounded">enter(v)</code> المان <code className="font-mono bg-black/30 px-1 rounded">#stats-content</code> با رشته‌های چند هزار خطی جایگزین می‌شود. اگر کاربر بین روستاهای مختلف جابه‌جا شود، مرجع المان در حافظه یا ساختار تکراری ممکن است ناپایدار گردد.
                </div>
              </li>
              <li className="flex items-start gap-2">
                <AlertTriangle className="w-4 h-4 text-amber-400 flex-shrink-0 mt-1" />
                <div>
                  <strong>عدم جداسازی لایه داده از نما (Separation of Concerns):</strong> جداول HTML سنگین درون رشته‌های جاوااسکریپت تجمیع شده‌اند. این شیوه نگهداری، ویرایش و تست داده‌ها را غیرممکن می‌سازد. مدل داده باید در قالب تایپ‌اسکریپت و ساختار JSON نرمال‌سازی شود.
                </div>
              </li>
              <li className="flex items-start gap-2">
                <AlertTriangle className="w-4 h-4 text-amber-400 flex-shrink-0 mt-1" />
                <div>
                  <strong>وابستگی به فایل‌های محلی ایزوله:</strong> ارجاع به فونت‌های لوکال <code className="font-mono bg-black/30 px-1 rounded">./YekanBakh_1.woff2</code> و تصاویر <code className="font-mono bg-black/30 px-1 rounded">./map.webp</code> و <code className="font-mono bg-black/30 px-1 rounded">./extracted_webp_1.webp</code> در صورتی که فایل‌ها منتقل نشوند منجر به شکست استایل و خطای 404 می‌شود.
                </div>
              </li>
            </ul>
          </div>

          {/* 3. Strengths */}
          <div className="p-5 rounded-xl bg-emerald-950/40 border border-emerald-500/40 space-y-3">
            <div className="flex items-center gap-2 text-emerald-300 font-extrabold text-base">
              <CheckCircle2 className="w-5 h-5 text-emerald-400" />
              ۳. نقاط قوت طراحی و تجربه کاربری (UX/UI Highlights)
            </div>
            <ul className="space-y-1.5 text-xs sm:text-sm text-emerald-100/90 list-disc list-inside">
              <li><strong>مفهوم بصری خلاقانه:</strong> پویانمایی ورود و پرواز به مختصات جغرافیایی روستاها (Arrival & Fly-to effect).</li>
              <li><strong>طراحی پرونده‌ای (Dossier Design):</strong> استفاده از تم کرم/خاک رس/تراکوتا در دیالوگ آماری که حس اسناد رسمی و پرونده‌های میدانی خیریه را به زیبایی القا می‌کند.</li>
              <li><strong>پشتیبانی از ژست‌های لمسی (Pinch to Zoom & Pan):</strong> قابلیت درگ و زوم با ماوس و تاچ در نقشه هوایی.</li>
            </ul>
          </div>

          {/* 4. Modern Recommendations */}
          <div className="p-5 rounded-xl bg-[#102221] border border-[#c6a15b]/40 space-y-3">
            <div className="flex items-center gap-2 text-[#edd395] font-extrabold text-base">
              <Layers className="w-5 h-5 text-[#c6a15b]" />
              ۴. راهکارهای ارتقا و بهینه‌سازی اعمال‌شده در این نسخه
            </div>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
              <div className="p-3 rounded-lg bg-white/5 border border-white/5 space-y-1">
                <strong className="text-white block font-bold">۱. بازنویسی با React 19 و TypeScript:</strong>
                <p className="text-stone-300">تبدیل ساختار اسکریپتی شکننده به کامپوننت‌های ماژولار، ری‌اکتیو و ایزوله.</p>
              </div>
              <div className="p-3 rounded-lg bg-white/5 border border-white/5 space-y-1">
                <strong className="text-white block font-bold">۲. سوئیچ حریم خصوصی (Privacy Shield):</strong>
                <p className="text-stone-300">ماسک‌سازی خودکار کدهای ملی و شماره‌های تماس مددجویان با امکان کنترل دسترسی.</p>
              </div>
              <div className="p-3 rounded-lg bg-white/5 border border-white/5 space-y-1">
                <strong className="text-white block font-bold">۳. موتور جستجوی درجا در جداول:</strong>
                <p className="text-stone-300">قابلیت جستجوی فوری در میان نام‌ها، سرپرستان، مدارس و آدرس‌ها بدون بارگذاری مجدد.</p>
              </div>
              <div className="p-3 rounded-lg bg-white/5 border border-white/5 space-y-1">
                <strong className="text-white block font-bold">۴. استایل‌دهی مدرن با Tailwind CSS v4:</strong>
                <p className="text-stone-300">حذف هزار خط CSS سفارشی تکراری و ارتقا به فونت استاندارد Vazirmatn و آیکون‌های برداری Lucide.</p>
              </div>
            </div>
          </div>
        </div>

        {/* Footer */}
        <div className="px-6 py-3 bg-[#112423] border-t border-[#c6a15b]/20 text-[11px] text-stone-400 flex items-center justify-between">
          <span>تهیه شده توسط هوش مهندسی Google AI Studio</span>
          <button
            onClick={onClose}
            className="px-4 py-1.5 rounded-lg bg-[#c6a15b] hover:bg-[#edd395] text-stone-900 font-bold transition-all text-xs"
          >
            متوجه شدم
          </button>
        </div>
      </div>
    </div>
  );
};
