#!/usr/bin/env python3
"""Generate references/slides-diff.html: 2018 vs 2019 slides side-by-side."""

# row = (slide-2018, slide-2019); None = blank placeholder
PAIRS = [
    (1, 1), (None, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10),
    (10, 11), (11, 12), (12, 13), (13, 14), (14, 15), (15, 16), (16, 17), (17, 18), (18, 19), (19, 20),
    (20, 21), (21, 22), (22, 23), (23, None), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29),
    (30, 30), (31, 31), (32, 32), (33, 33), (34, 34), (35, 35), (36, None), (37, None), (38, 36), (39, 37),
    (40, 38), (None, 39), (None, 40), (None, 41), (None, 42), (None, 43), (None, 44), (None, 45), (None, 46), (None, 47),
    (None, 48), (41, 49), (42, 50), (None, 51), (43, 52),
]

# sanity check: each year's slides appear exactly once
for year, count in (("2018", 43), ("2019", 52)):
    idx = 0 if year == "2018" else 1
    got = sorted(p[idx] for p in PAIRS if p[idx] is not None)
    assert got == list(range(1, count + 1)), f"{year} mismatch: {got}"


def cell(folder, n):
    if n is None:
        return '      <div class="blank"></div>'
    src = f"{folder}/slide-{n:02d}.png"
    return (f'      <a href="{src}" target="_blank">'
            f'<img src="{src}" alt="{folder} slide {n}" loading="lazy"></a>')


rows = []
for a, b in PAIRS:
    rows.append("    <div class=\"row\">\n"
                + cell("slides-2018", a) + "\n"
                + cell("slides-2019", b) + "\n"
                + "    </div>")
rows_html = "\n".join(rows)

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Python Set Practice — 2018 vs 2019 slides</title>
<style>
  :root {{ color-scheme: light dark; }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0;
    font: 15px/1.4 -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
    background: #f4f4f5;
    color: #18181b;
  }}
  @media (prefers-color-scheme: dark) {{
    body {{ background: #18181b; color: #f4f4f5; }}
  }}
  header.page {{
    padding: 16px 24px;
    border-bottom: 1px solid rgba(128,128,128,.3);
  }}
  header.page h1 {{ margin: 0; font-size: 18px; font-weight: 600; }}
  header.page p {{ margin: 4px 0 0; opacity: .7; font-size: 13px; }}
  .cols {{
    position: sticky;
    top: 0;
    z-index: 2;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    padding: 12px 24px;
    background: #e4e4e7;
    border-bottom: 1px solid rgba(128,128,128,.3);
    font-weight: 600;
    text-align: center;
  }}
  @media (prefers-color-scheme: dark) {{
    .cols {{ background: #27272a; }}
  }}
  .grid {{ padding: 16px 24px 48px; }}
  .row {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin-bottom: 16px;
    align-items: start;
  }}
  .row img {{
    display: block;
    width: 100%;
    height: auto;
    border: 1px solid rgba(128,128,128,.35);
    border-radius: 4px;
    background: #fff;
  }}
  .row a {{ display: block; line-height: 0; }}
  .blank {{
    width: 100%;
    aspect-ratio: 2134 / 1600;
    border: 1px dashed rgba(128,128,128,.35);
    border-radius: 4px;
    background: repeating-linear-gradient(
      45deg, transparent, transparent 10px,
      rgba(128,128,128,.06) 10px, rgba(128,128,128,.06) 20px);
  }}
</style>
</head>
<body>
<header class="page">
  <h1>Python Set Practice — slide-by-slide diff</h1>
  <p>2018 deck (43 slides) vs. PyCon Cleveland 2019 deck (52 slides). Click any slide for full size.</p>
</header>
<div class="cols"><div>2018</div><div>2019</div></div>
<div class="grid">
{rows_html}
</div>
</body>
</html>
"""

with open("slides-diff.html", "w", encoding="utf-8") as f:
    f.write(html)
print(f"wrote slides-diff.html with {len(PAIRS)} rows")
