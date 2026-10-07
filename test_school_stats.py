import re

with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

# Let us verify the school table parsing in darbandGharbi, soureh, polNow, maslavi, ariz, shahrakSevvom
school_tables = {}

for v_var, v_id in [
    ("darbandGharbiStatsHtml", "darband-gharbi"),
    ("sourehStatsHtml", "soureh"),
    ("polNowStatsHtml", "pol-now"),
    ("maslaviStatsHtml", "maslavi-1"),
    ("arizStatsHtml", "ariz"),
    ("shahrakSevvomStatsHtml", "shahrak-sevvom")
]:
    idx = text.find(f"const {v_var} = `")
    if idx == -1: continue
    end = text.find("`;", idx)
    content = text[idx:end]
    tables = re.findall(r"<table[^>]*>(.*?)</table>", content, re.DOTALL)
    for t in tables:
        if "پایه اول" in t or "پیش دبستانی" in t or "دانش آموز" in t or "دبستان" in t:
            trs = re.findall(r"<tr[^>]*>(.*?)</tr>", t, re.DOTALL)
            print(f"Village {v_id} found school table with {len(trs)} rows")
            break

