#!/usr/bin/env python3
import sys
from pathlib import Path
import markdown

def render(md_path: Path) -> None:
    html_path = md_path.with_suffix('.html')
    text = md_path.read_text(encoding='utf-8')
    body = markdown.markdown(text)
    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>{md_path.stem}</title>
</head>
<body>
{body}
</body>
</html>
"""
    html_path.write_text(html, encoding='utf-8')
    print(f'{md_path} -> {html_path}')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f'Usage: {sys.argv[0]} FILE.md [FILE2.md ...]')
        sys.exit(1)
    for arg in sys.argv[1:]:
        render(Path(arg))
