with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

idx = text.find("const match = document.querySelector('#statsDialog mark.search-match-hl')")
if idx == -1:
    print("Already updated or not found!")
    exit(0)

start = text.rfind("// Handle search keywords", 0, idx)
end = text.find("}", text.find("});", text.find("});", idx) + 3) + 3) + 1

target_chunk = text[start:end]
print("Found target chunk length:", len(target_chunk))

new_chunk = """// Handle search keywords or show top of dashboard
                if (keywordToSearch) {
                    requestAnimationFrame(() => {
                        const liveSearch = document.getElementById('liveTableSearch');
                        if (liveSearch) {
                            liveSearch.value = keywordToSearch;
                            liveSearch.dispatchEvent(new Event('input', { bubbles: true }));
                        }

                        setTimeout(() => {
                            const statsDlg = document.getElementById('statsDialog');
                            if (!statsDlg) return;

                            const normKw = (typeof normalizePersianSearch === 'function')
                                ? normalizePersianSearch(keywordToSearch)
                                : keywordToSearch.toLowerCase().trim();

                            const accordions = statsDlg.querySelectorAll('details.dos-accordion');
                            let targetRow = null;

                            accordions.forEach(acc => {
                                const accText = (typeof normalizePersianSearch === 'function')
                                    ? normalizePersianSearch(acc.textContent || '')
                                    : (acc.textContent || '').toLowerCase();

                                if (accText.includes(normKw)) {
                                    acc.open = true;
                                    const rows = acc.querySelectorAll('tbody tr');
                                    rows.forEach(tr => {
                                        const trText = (typeof normalizePersianSearch === 'function')
                                            ? normalizePersianSearch(tr.textContent || '')
                                            : (tr.textContent || '').toLowerCase();

                                        if (trText.includes(normKw) && !targetRow) {
                                            targetRow = tr;
                                        }
                                    });
                                }
                            });

                            if (targetRow) {
                                targetRow.scrollIntoView({ behavior: 'smooth', block: 'center' });
                                targetRow.classList.remove('search-row-highlight');
                                void targetRow.offsetWidth;
                                targetRow.classList.add('search-row-highlight');
                                setTimeout(() => targetRow.classList.remove('search-row-highlight'), 4000);
                            } else {
                                const match = statsDlg.querySelector('mark.search-match-hl') || 
                                              statsDlg.querySelector('details.dos-accordion[open]');
                                if (match) match.scrollIntoView({ behavior: 'smooth', block: 'center' });
                            }
                        }, 250);
                    });
                }"""

text = text[:start] + new_chunk + text[end:]

with open("index.html", "w", encoding="utf-8") as f:
    f.write(text)

print("Successfully updated navigateToVillage!")
