"""Turns a static Design-canvas artboard (.dc.html) into a plain HTML page.

Strips the canvas runtime (support.js, <x-dc>, <helmet>, the x-dc script block) so the
page opens directly in a browser. Only for artboards without template holes.
"""
import re, sys, pathlib

src, dst = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
html = src.read_text(encoding="utf-8")
html = html.replace('<script src="./support.js"></script>\n', '')
m = re.search(r'<helmet>(.*?)</helmet>\n?', html, flags=re.S)
helmet = m.group(1) if m else ''
html = html.replace(m.group(0), '') if m else html
html = html.replace('</head>', helmet.strip() + '\n</head>')
html = html.replace('<x-dc>\n', '').replace('</x-dc>\n', '')
html = re.sub(r'<script type="text/x-dc".*?</script>\n', '', html, flags=re.S)
if '{{' in html:
    sys.exit(f"{src.name}: has template holes, needs the canvas runtime")
dst.write_text(html, encoding="utf-8")
print(dst)
