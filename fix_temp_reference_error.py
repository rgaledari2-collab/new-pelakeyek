with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

target = """                    `;
                }

                const accordions = [];"""

replacement = """                    `;
                }

                const temp = document.createElement('div');
                temp.innerHTML = raw;
                const accordions = [];"""

assert target in html, "target string not found"
html = html.replace(target, replacement, 1)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("SUCCESS: Declared temp in getVillageAccordions!")
