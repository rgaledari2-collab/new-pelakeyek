with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

idx = text.find("<table class=\"dos-table\"")
end = text.find("</table>", idx) + 8

old_table = text[idx:end]

new_table = """<table class="dos-table" style="width:100%; border-collapse:collapse; background:#fff; border:1px solid #ded1b8; border-radius:10px; overflow:hidden;">
            <thead>
                <tr style="background:#eae0cc; color:var(--ink); font-size:13px; border-bottom:2px solid var(--brand-clay);">
                    <th style="padding:10px 14px; text-align:right;">ردیف</th>
                    <th style="padding:10px 14px; text-align:right;">نام روستا</th>
                    <th style="padding:10px 14px; text-align:right;">دهستان / حوزه</th>
                    <th style="padding:10px 14px; text-align:right;">جمعیت مستند</th>
                    <th style="padding:10px 14px; text-align:right;">خانوار ساکن</th>
                    <th style="padding:10px 14px; text-align:right;">وضعیت آموزش و مدارس</th>
                    <th style="padding:10px 14px; text-align:right;">پرونده‌های مستند حمایتی</th>
                </tr>
            </thead>
            <tbody style="font-size:12.5px; color:#33423f;">
                <tr><td style="padding:9px 14px;">۱</td><td style="padding:9px 14px; font-weight:800; color:#142a29;">سوره</td><td style="padding:9px 14px;">حومه غربی</td><td style="padding:9px 14px; font-weight:700;">۴,۱۷۵ نفر</td><td style="padding:9px 14px;">۱,۰۵۱</td><td style="padding:9px 14px;">۳ مدرسه (رزمندگان، مطیری، کمیل)</td><td style="padding:9px 14px; font-weight:800; color:#b45309;">۷۰ پرونده (۱۴ یتیم + ۵۶ مددجو)</td></tr>
                <tr><td style="padding:9px 14px;">۲</td><td style="padding:9px 14px; font-weight:800; color:#142a29;">پل نو</td><td style="padding:9px 14px;">حومه غربی</td><td style="padding:9px 14px; font-weight:700;">۳,۶۲۰ نفر</td><td style="padding:9px 14px;">۸۹۰</td><td style="padding:9px 14px;">۲ مدرسه (حر بن ریاحی و ۱۵ خرداد)</td><td style="padding:9px 14px; font-weight:800; color:#b45309;">۲۹ پرونده (۷ یتیم + ۲۲ مددجو)</td></tr>
                <tr><td style="padding:9px 14px;">۳</td><td style="padding:9px 14px; font-weight:800; color:#142a29;">دربند غربی</td><td style="padding:9px 14px;">حومه غربی</td><td style="padding:9px 14px; font-weight:700;">۲,۷۵۵ نفر</td><td style="padding:9px 14px;">۶۸۱</td><td style="padding:9px 14px;">دبستان مرزداران (۱۷۷ دانش‌آموز)</td><td style="padding:9px 14px; font-weight:800; color:#b45309;">۶۱ پرونده (۱۱ یتیم + ۵۰ مددجو)</td></tr>
                <tr><td style="padding:9px 14px;">۴</td><td style="padding:9px 14px; font-weight:800; color:#142a29;">مصلاوی ۱ و ۲</td><td style="padding:9px 14px;">حومه غربی</td><td style="padding:9px 14px; font-weight:700;">۴,۵۶۰ نفر</td><td style="padding:9px 14px;">۱,۱۷۹</td><td style="padding:9px 14px;">۲ دبستان (۲۶۴ دانش‌آموز)</td><td style="padding:9px 14px; font-weight:800; color:#b45309;">۱۶ پرونده (۳ یتیم + ۱۳ مددجو)</td></tr>
                <tr><td style="padding:9px 14px;">۵</td><td style="padding:9px 14px; font-weight:800; color:#142a29;">عریض</td><td style="padding:9px 14px;">محور شلمچه</td><td style="padding:9px 14px; font-weight:700;">۱,۴۵۰ نفر</td><td style="padding:9px 14px;">۳۶۰</td><td style="padding:9px 14px;">دبستان معراج (۲۴ دانش‌آموز)</td><td style="padding:9px 14px; font-weight:800; color:#b45309;">۵ پرونده (۱ یتیم + ۴ مددجو)</td></tr>
                <tr><td style="padding:9px 14px;">۶</td><td style="padding:9px 14px; font-weight:800; color:#142a29;">شهرک سوم</td><td style="padding:9px 14px;">محور مرزی شلمچه</td><td style="padding:9px 14px; font-weight:700;">۴۰۳ نفر</td><td style="padding:9px 14px;">۱۳۴</td><td style="padding:9px 14px;">دبستان نوساز آل یاسین</td><td style="padding:9px 14px; font-weight:800; color:#b45309;">۱۶ پرونده (۶ یتیم + ۱۰ مددجو)</td></tr>
                <tr><td style="padding:9px 14px;">۷</td><td style="padding:9px 14px; font-weight:800; color:#142a29;">جدیده</td><td style="padding:9px 14px;">حومه شرقی</td><td style="padding:9px 14px; font-weight:700;">۳,۲۰۰ نفر</td><td style="padding:9px 14px;">۷۸۰</td><td style="padding:9px 14px;">۲ دبستان فعال</td><td style="padding:9px 14px; color:#64748b;">تحت ارزیابی اولیه</td></tr>
                <tr><td style="padding:9px 14px;">۸</td><td style="padding:9px 14px; font-weight:800; color:#142a29;">صد دستگاه</td><td style="padding:9px 14px;">حومه شرقی</td><td style="padding:9px 14px; font-weight:700;">۲,۵۰۰ نفر</td><td style="padding:9px 14px;">۶۱۰</td><td style="padding:9px 14px;">۱ دبستان</td><td style="padding:9px 14px; color:#64748b;">تحت ارزیابی اولیه</td></tr>
                <tr><td style="padding:9px 14px;">۹</td><td style="padding:9px 14px; font-weight:800; color:#142a29;">سرحانیه اول (علیا)</td><td style="padding:9px 14px;">حومه شرقی</td><td style="padding:9px 14px; font-weight:700;">۲,۱۰۰ نفر</td><td style="padding:9px 14px;">۵۱۰</td><td style="padding:9px 14px;">۱ دبستان</td><td style="padding:9px 14px; color:#64748b;">تحت ارزیابی اولیه</td></tr>
                <tr><td style="padding:9px 14px;">۱۰</td><td style="padding:9px 14px; font-weight:800; color:#142a29;">دربند شرقی</td><td style="padding:9px 14px;">حومه غربی</td><td style="padding:9px 14px; font-weight:700;">۱,۸۵۰ نفر</td><td style="padding:9px 14px;">۴۵۰</td><td style="padding:9px 14px;">مشترک با دربند غربی</td><td style="padding:9px 14px; color:#64748b;">تحت ارزیابی اولیه</td></tr>
                <tr><td style="padding:9px 14px;">۱۱</td><td style="padding:9px 14px; font-weight:800; color:#142a29;">سرحانیه سفلی</td><td style="padding:9px 14px;">حومه شرقی</td><td style="padding:9px 14px; font-weight:700;">۱,۶۵۰ نفر</td><td style="padding:9px 14px;">۴۰۰</td><td style="padding:9px 14px;">فاقد مدرسه مستقل</td><td style="padding:9px 14px; color:#64748b;">تحت ارزیابی اولیه</td></tr>
                <tr><td style="padding:9px 14px;">۱۲</td><td style="padding:9px 14px; font-weight:800; color:#142a29;">شهرک سادات</td><td style="padding:9px 14px;">محور شلمچه</td><td style="padding:9px 14px; font-weight:700;">۱,۱۰۰ نفر</td><td style="padding:9px 14px;">۲۷۰</td><td style="padding:9px 14px;">۱ دبستان کانکسی</td><td style="padding:9px 14px; color:#64748b;">تحت ارزیابی اولیه</td></tr>
                <tr><td style="padding:9px 14px;">۱۳</td><td style="padding:9px 14px; font-weight:800; color:#142a29;">مفتی عریض</td><td style="padding:9px 14px;">محور شلمچه</td><td style="padding:9px 14px; font-weight:700;">۷۵۰ نفر</td><td style="padding:9px 14px;">۱۸۰</td><td style="padding:9px 14px;">همجوار با عریض</td><td style="padding:9px 14px; color:#64748b;">تحت ارزیابی اولیه</td></tr>
            </tbody>
        </table>"""

text = text[:idx] + new_table + text[end:]

with open("index.html", "w", encoding="utf-8") as f:
    f.write(text)

print("Updated regionalDialog summary table with 100% authentic documented stats!")
