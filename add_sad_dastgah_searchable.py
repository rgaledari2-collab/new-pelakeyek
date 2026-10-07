import json

with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

s_idx = text.find("const searchableData = [")
e_idx = text.find("];\n\n            let currentSearchCategory", s_idx)
data_str = text[s_idx + len("const searchableData = "):e_idx + 1]
data = json.loads(data_str)

new_items = [
    # School
    {
        "type": "school",
        "title": "مدرسه علویه و راهیان نور صد دستگاه",
        "subtitle": "۲ مرکز آموزشی (ابتدایی و متوسطه اول) · ۶۹۵ دانش‌آموز · صد دستگاه",
        "badge": "مدرسه",
        "village": "صد دستگاه",
        "targetVillageId": "sad-dastgah",
        "section": "stats",
        "keyword": "مدرسه علویه راهیان نور صد دستگاه ابتدایی متوسطه اول 695 دانش آموز"
    },
    # Mosque
    {
        "type": "culture",
        "title": "مسجد صاحب‌الزمان صد دستگاه",
        "subtitle": "کانون فرهنگی، مذهبی و محرومیت‌زدایی محله · صد دستگاه",
        "badge": "فرهنگی",
        "village": "صد دستگاه",
        "targetVillageId": "sad-dastgah",
        "section": "stats",
        "keyword": "مسجد صاحب الزمان صد دستگاه مذهبی فرهنگی کانون"
    },
    # 3 Orphans
    {
        "type": "person",
        "personType": "orphan",
        "title": "دنیا عریضاوی",
        "subtitle": "یتیم تحت حمایت · سن: ۱۹ · دانشجو · سرپرست: صدیقه زباری · صد دستگاه",
        "badge": "یتیم",
        "guardian": "صدیقه زباری",
        "father": "هاشم",
        "nationalId": "1820612635",
        "age": "۱۹",
        "phone": "09356466599",
        "address": "صد دستگاه – منازل بندر - ردیف ۴ – پلاک ۱۰",
        "village": "صد دستگاه",
        "targetVillageId": "sad-dastgah",
        "school": "دانشگاه",
        "health": "سالم",
        "keyword": "دنیا عریضاوی هاشم صدیقه زباری 1820612635 181621234 09356466599 صد دستگاه دانشجو یتیم مددجو"
    },
    {
        "type": "person",
        "personType": "orphan",
        "title": "مرام طیبی",
        "subtitle": "یتیم تحت حمایت · سن: ۱۷ · یازدهم (شهدای شمخانی) · سرپرست: سمیه سلیمانی · صد دستگاه",
        "badge": "یتیم",
        "guardian": "سمیه سلیمانی",
        "father": "احمد",
        "nationalId": "1820699374",
        "age": "۱۷",
        "phone": "09307879842",
        "address": "صد دستگاه – پشت مدرسه راهیان نور – پلاک ۱",
        "village": "صد دستگاه",
        "targetVillageId": "sad-dastgah",
        "school": "شهدای شمخانی",
        "health": "سالم",
        "keyword": "مرام طیبی احمد سمیه سلیمانی 1820699374 1090318480 09307879842 صد دستگاه یازدهم شهدای شمخانی یتیم"
    },
    {
        "type": "person",
        "personType": "orphan",
        "title": "رسول عنبی",
        "subtitle": "یتیم تحت حمایت · سن: ۱۷ · دهم (شهر) · سرپرست: ملکه عنبی (عمه) · صد دستگاه",
        "badge": "یتیم",
        "guardian": "ملکه عنبی (عمه)",
        "father": "جاسم",
        "nationalId": "1811448712",
        "age": "۱۷",
        "phone": "09165764199 - 09168107791",
        "address": "صد دستگاه – منازل اداره بندر – پلاک ۹",
        "village": "صد دستگاه",
        "targetVillageId": "sad-dastgah",
        "school": "شهر",
        "health": "سالم",
        "keyword": "رسول عنبی جاسم ملکه عنبی 1811448712 1820514536 09165764199 09168107791 صد دستگاه دهم یتیم"
    }
]

needy_list = [
    {"name": "مریم غزلاوی", "nid": "1829485121", "phone": "0904467549", "address": "صد دستگاه"},
    {"name": "علی محمدی هلالیان", "nid": "1820064433", "phone": "09386590917", "address": "صد دستگاه"},
    {"name": "نرگس سلمانیان اصل", "nid": "1829411081", "phone": "09045133785", "address": "صد دستگاه"},
    {"name": "سید هاشم مفتی عریض", "nid": "1829654187", "phone": "09375385289", "address": "صد دستگاه"},
    {"name": "حلیمه سلیمانی", "nid": "1820089150", "phone": "09026844921", "address": "صد دستگاه"},
    {"name": "زهرا عسکری", "nid": "1820264580", "phone": "09166339881", "address": "صد دستگاه"},
    {"name": "فروغ عباسیان پور", "nid": "1820688755", "phone": "09034148587", "address": "صد دستگاه"},
    {"name": "سیده کوثر موسوی", "nid": "1940720079", "phone": "09051806711", "address": "صد دستگاه"},
    {"name": "سکینه محمودپور عریض", "nid": "6629861752", "phone": "09036802641", "address": "صد دستگاه"},
    {"name": "علی عباسی کیان", "nid": "1820412326", "phone": "09335463899", "address": "صد دستگاه"},
    {"name": "مرضیه کاشفی سمن", "nid": "3979851109", "phone": "09166331644", "address": "صد دستگاه"},
    {"name": "حسین محمدی اطهر", "nid": "7060016643", "phone": "09169538116", "address": "صد دستگاه"},
    {"name": "محمد مجیل", "nid": "1755060106", "phone": "09368915693", "address": "صد دستگاه"},
    {"name": "ایمان خواجه", "nid": "1820140075", "phone": "0905876667", "address": "صد دستگاه"},
    {"name": "رقیه فیسلی", "nid": "1829962981", "phone": "09023558943", "address": "صد دستگاه"},
    {"name": "عماد فتیلی", "nid": "1820728528", "phone": "09398034496", "address": "صد دستگاه"},
    {"name": "زینب عبادی نژاد", "nid": "1820833054", "phone": "09371679793", "address": "صد دستگاه"},
    {"name": "قدیمه سلیمانی", "nid": "1751976548", "phone": "09388673788", "address": "صد دستگاه"},
    {"name": "حیات جاسم پور بغلانی", "nid": "1818621029", "phone": "09024190333", "address": "صد دستگاه"},
    {"name": "مریم علقمی زاده", "nid": "1829632145", "phone": "09361394346", "address": "صد دستگاه"},
    {"name": "راضیه دریس", "nid": "1828064785", "phone": "09308743894", "address": "صد دستگاه"}
]

for item in needy_list:
    new_items.append({
        "type": "person",
        "personType": "needy",
        "title": item["name"],
        "subtitle": f"خانوار کم‌برخوردار تحت پوشش · صد دستگاه · تماس: {item['phone']}",
        "badge": "مددجو",
        "guardian": "سرپرست خانوار",
        "father": "—",
        "nationalId": item["nid"],
        "age": "—",
        "phone": item["phone"],
        "address": item["address"],
        "village": "صد دستگاه",
        "targetVillageId": "sad-dastgah",
        "school": "—",
        "health": "پایش معیشتی",
        "keyword": f"{item['name']} {item['nid']} {item['phone']} {item['address']} صد دستگاه مددجو کم‌برخوردار پرونده"
    })

data.extend(new_items)
new_json_str = json.dumps(data, ensure_ascii=False)
text = text[:s_idx + len("const searchableData = ")] + new_json_str + text[e_idx + 1:]

with open("index.html", "w", encoding="utf-8") as f:
    f.write(text)

print(f"Added {len(new_items)} items to searchableData. Total searchableData items now: {len(data)}")
