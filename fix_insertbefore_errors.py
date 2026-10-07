with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Fix Match 1
old_match1 = """                        if (badgeHtml && !summary.querySelector('.accordion-badge')) {
                            const wrap = document.createElement('div');
                            wrap.style.display = 'flex';
                            wrap.style.alignItems = 'center';
                            wrap.style.gap = '10px';
                            wrap.style.flexWrap = 'wrap';
                            
                            if (titleEl) {
                                titleEl.style.fontSize = '13.5px';
                                titleEl.style.fontWeight = '800';
                                summary.insertBefore(wrap, titleEl);
                                wrap.appendChild(titleEl);
                                wrap.insertAdjacentHTML('beforeend', badgeHtml);
                            }
                        }"""

new_match1 = """                        if (badgeHtml && !summary.querySelector('.accordion-badge')) {
                            if (titleEl) {
                                titleEl.style.fontSize = '13.5px';
                                titleEl.style.fontWeight = '800';
                                if (titleEl.parentNode === summary) {
                                    const wrap = document.createElement('div');
                                    wrap.style.display = 'flex';
                                    wrap.style.alignItems = 'center';
                                    wrap.style.gap = '10px';
                                    wrap.style.flexWrap = 'wrap';
                                    summary.insertBefore(wrap, titleEl);
                                    wrap.appendChild(titleEl);
                                    wrap.insertAdjacentHTML('beforeend', badgeHtml);
                                } else if (titleEl.parentNode) {
                                    titleEl.parentNode.insertAdjacentHTML('beforeend', badgeHtml);
                                }
                            }
                        }"""

assert old_match1 in html, "old_match1 not found"
html = html.replace(old_match1, new_match1, 1)
print("1. Fixed Match 1 in getVillageAccordions!")

# 2. Fix Match 2
old_match2 = "scrollWrap.parentNode.insertBefore(filterBar, scrollWrap);"
new_match2 = "if (scrollWrap && scrollWrap.parentNode && scrollWrap.parentNode.contains(scrollWrap)) { scrollWrap.parentNode.insertBefore(filterBar, scrollWrap); }"

assert old_match2 in html, "old_match2 not found"
html = html.replace(old_match2, new_match2, 1)
print("2. Fixed Match 2 in setupSmartTableFilters!")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("SUCCESS: Fixed both insertBefore calls!")
