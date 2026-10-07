with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 5. Add JavaScript logic right before the last })();
js_pure_map = """
            // ========================================================
            // PURE MAP MODE (حالت نقشه خالص / پنهان‌سازی همه پنل‌ها)
            // ========================================================
            function togglePureMapMode(enable) {
                const isPure = (typeof enable === 'boolean') 
                    ? enable 
                    : !document.body.classList.contains('pure-map-mode');

                if (isPure) {
                    document.body.classList.add('pure-map-mode');
                    document.querySelectorAll('dialog[open]').forEach(d => {
                        try { d.close(); } catch(e) {}
                    });
                    if (typeof showSearchToast === 'function') {
                        showSearchToast('حالت نقشه خالص فعال شد (تمام پنل‌ها پنهان شدند). برای خروج کلید Esc را بزنید.');
                    }
                } else {
                    document.body.classList.remove('pure-map-mode');
                    if (typeof showSearchToast === 'function') {
                        showSearchToast('پنل‌ها و کنترل‌های نقشه بازگردانی شدند.');
                    }
                }
            }

            window.togglePureMapMode = togglePureMapMode;

            const pureBtn1 = document.getElementById('pureMapToggleBtn');
            if (pureBtn1) pureBtn1.addEventListener('click', () => togglePureMapMode(true));

            const pureBtn2 = document.getElementById('pureMapToolBtn');
            if (pureBtn2) pureBtn2.addEventListener('click', () => togglePureMapMode(true));

            const exitPureBtn = document.getElementById('exitPureMapBtn');
            if (exitPureBtn) exitPureBtn.addEventListener('click', () => togglePureMapMode(false));

            document.addEventListener('keydown', (e) => {
                if (e.key === 'Escape' && document.body.classList.contains('pure-map-mode')) {
                    togglePureMapMode(false);
                } else if ((e.key === 'm' || e.key === 'M') && !e.target.closest('input, textarea')) {
                    togglePureMapMode();
                }
            });
            // ========================================================
"""

idx_last_script = html.rfind("</script>")
idx_iife = html.rfind("})();", 0, idx_last_script)
assert idx_iife != -1, "})(); before last </script> not found"

html = html[:idx_iife] + js_pure_map + "\n        " + html[idx_iife:]
print("Added Pure Map Mode JavaScript handlers!")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("SUCCESS: Pure Map Mode injected cleanly!")
