"""Build the repository's printable Python guide. See docs/python_guide/README.md."""

from __future__ import annotations

import ast
import hashlib
import html
import json
import re
import subprocess
import sys
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / ".book-tools"))

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, Preformatted, Table, TableStyle

SOURCE = ROOT / "docs" / "python_guide"
OUT = ROOT / "docs" / "ultimate_python_core_guide.pdf"
MD_OUT = OUT.with_suffix(".md")
PREVIEW = ROOT / ".book-preview"
W, H = A4
LEFT, RIGHT, TOP, BOTTOM = 49, 49, 78, 49
WIDTH = W - LEFT - RIGHT
NAVY = colors.HexColor("#132C46")
TEAL = colors.HexColor("#087F8C")
INK = colors.HexColor("#24364B")
GRAY = colors.HexColor("#62758A")
LIGHT = colors.HexColor("#F0F4F8")


class CodeBlock(Preformatted):
    """Give code a restrained background without changing copied source text."""

    def draw(self):
        self.canv.saveState()
        self.canv.setFillColor(LIGHT)
        self.canv.roundRect(-7, -4, self.width + 14, self.height + 8, 3,
                            fill=1, stroke=0)
        self.canv.restoreState()
        super().draw()


def register_fonts():
    fonts = Path("C:/Windows/Fonts")
    for name, filename in [("Body", "calibri.ttf"), ("Body-Bold", "calibrib.ttf"),
                           ("Body-Italic", "calibrii.ttf"), ("Mono", "consola.ttf")]:
        pdfmetrics.registerFont(TTFont(name, str(fonts / filename)))
    pdfmetrics.registerFontFamily("Body", normal="Body", bold="Body-Bold", italic="Body-Italic")


def inline(text):
    text = html.escape(text, quote=False)
    text = re.sub(r"`([^`]+)`", r'<font name="Mono" size="9">\1</font>', text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)",
                  r'<link href="\2" color="#087F8C"><u>\1</u></link>', text)
    return text


def expand_excerpt(match):
    relative, symbol = match.group(1), match.group(2)
    path = ROOT / relative
    text = path.read_text(encoding="utf-8")
    tree = ast.parse(text)
    node = next(n for n in tree.body if isinstance(n, (ast.FunctionDef, ast.ClassDef))
                and n.name == symbol)
    first = min([node.lineno] + [d.lineno for d in getattr(node, "decorator_list", [])])
    excerpt = "\n".join(text.splitlines()[first - 1:node.end_lineno])
    # Keep source exact, including its explanatory docstrings.
    return f"Repository excerpt: `{relative}:{first}`.\n\n```python\n{excerpt}\n```"


def load_pages():
    refs = json.loads((SOURCE / "references.json").read_text(encoding="utf-8"))
    pages = []
    for file in sorted(SOURCE.glob("[0-9][0-9]_*.md")):
        content = file.read_text(encoding="utf-8")
        content = re.sub(r"\{\{code:([^:}]+):([^}]+)\}\}", expand_excerpt, content)
        content = re.sub(r"\[\[(R\d+)\]\]",
                         lambda m: f"[{m[1]}: {refs[m[1]]['title']}]({refs[m[1]]['url']})", content)
        for chunk in content.split("<!-- page -->"):
            if chunk.strip():
                pages.append(chunk.strip())
    return pages, refs


def styles(size):
    return {
        "body": ParagraphStyle("body", fontName="Body", fontSize=size,
             leading=size * 1.28, textColor=INK, spaceAfter=7),
        "h2": ParagraphStyle("h2", fontName="Body-Bold", fontSize=size + 2.2,
             leading=size * 1.4, textColor=TEAL, spaceBefore=7, spaceAfter=5),
        "code": ParagraphStyle("code", fontName="Mono", fontSize=8.5,
             leading=10.5, textColor=INK, backColor=LIGHT, borderPadding=8,
             spaceBefore=3, spaceAfter=11),
        "small": ParagraphStyle("small", fontName="Body", fontSize=8.6,
             leading=11, textColor=GRAY, spaceAfter=6),
    }


def flowables(body, size):
    sty = styles(size)
    lines = body.splitlines()
    result, i = [], 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        if line.startswith("```"):
            code = []
            i += 1
            while i < len(lines) and not lines[i].startswith("```"):
                code.append(lines[i].rstrip())
                i += 1
            # Soft-wrap comments only. Executable code is never visually rewritten.
            formatted = []
            for entry in code:
                if pdfmetrics.stringWidth(entry, "Mono", 8.5) > WIDTH - 18:
                    if entry.lstrip().startswith("#"):
                        indent = entry[:len(entry) - len(entry.lstrip())]
                        formatted.extend(textwrap.wrap(entry.strip(), width=88,
                                          subsequent_indent=indent + "# "))
                    else:
                        raise ValueError(f"Code line too wide: {entry}")
                else:
                    formatted.append(entry)
            result.append(CodeBlock("\n".join(formatted), sty["code"]))
            i += 1
        elif line.startswith("## "):
            result.append(Paragraph(inline(line[3:]), sty["h2"]))
            i += 1
        elif line.startswith("| "):
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r"[:\- ]+", cell) for cell in cells):
                    rows.append([Paragraph(inline(c), sty["small"]) for c in cells])
                i += 1
            if rows:
                count = len(rows[0])
                table = Table(rows, colWidths=[WIDTH / count] * count, hAlign=TA_LEFT)
                table.setStyle(TableStyle([
                    ("BACKGROUND", (0, 0), (-1, 0), LIGHT),
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("LINEBELOW", (0, 0), (-1, -1), .35, colors.HexColor("#D8E2EC")),
                    ("LEFTPADDING", (0, 0), (-1, -1), 7),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 7),
                    ("TOPPADDING", (0, 0), (-1, -1), 5),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
                ]))
                result.append(table)
        else:
            paragraph = [line]
            i += 1
            while i < len(lines) and lines[i].strip() and not lines[i].startswith(("## ", "```", "| ", "- ")):
                paragraph.append(lines[i].strip())
                i += 1
            content = " ".join(paragraph)
            is_small = content.startswith(("References:", "Repository excerpt:", "Source:", "Run:"))
            if content.startswith("- "):
                content = "• " + content[2:]
            result.append(Paragraph(inline(content), sty["small" if is_small else "body"]))
    return result


def page_parts(page):
    lines = page.splitlines()
    assert lines[0].startswith("# "), lines[0]
    title = lines[0][2:]
    section = "CORE PYTHON • LEARN / IMPLEMENT / REVISE"
    start = 1
    if len(lines) > 1 and lines[1].startswith("Section: "):
        section = lines[1][9:]
        start = 2
    return title, section, "\n".join(lines[start:])


def draw_header(pdf, title, section, number, total):
    pdf.setFillColor(TEAL)
    pdf.rect(0, H - 9, W, 9, fill=1, stroke=0)
    pdf.setFont("Body-Bold", 8.3)
    pdf.setFillColor(GRAY)
    pdf.drawString(LEFT, H - 33, section.upper())
    pdf.setFont("Body-Bold", 21)
    pdf.setFillColor(NAVY)
    pdf.drawString(LEFT, H - 61, title)
    pdf.setStrokeColor(colors.HexColor("#D5DFEA"))
    pdf.line(LEFT, 37, W - RIGHT, 37)
    pdf.setFont("Body", 8)
    pdf.setFillColor(GRAY)
    pdf.drawString(LEFT, 24, "THE ULTIMATE CORE PYTHON GUIDE  /  REPOSITORY EDITION")
    pdf.drawRightString(W - RIGHT, 24, f"{number:02d} / {total:02d}")


def draw_cover(pdf, total):
    pdf.setFillColor(NAVY)
    pdf.rect(0, 0, W, H, fill=1, stroke=0)
    pdf.setFillColor(TEAL)
    pdf.rect(LEFT, H - 125, 69, 7, fill=1, stroke=0)
    pdf.setFillColor(colors.white)
    pdf.setFont("Body-Bold", 12)
    pdf.drawString(LEFT, H - 95, "THE REPOSITORY EDITION")
    pdf.setFont("Body-Bold", 44)
    for y, text in [(H-203, "The Ultimate"), (H-254, "Core Python"), (H-305, "Guide")]:
        pdf.drawString(LEFT, y, text)
    pdf.setFont("Body", 18)
    pdf.drawString(LEFT, H - 355, "Learn the ideas. Read the code. Explain the tradeoffs.")
    pdf.setFillColor(colors.HexColor("#C4D9E8"))
    pdf.setFont("Body", 12)
    lines = ["From first variables to a working command-line application.",
             "Theory, repository examples, predicted outputs and practice.",
             "Mock interviews: fresher • mid-level • senior • architect."]
    for index, text in enumerate(lines):
        pdf.drawString(LEFT, H - 400 - index * 22, text)
    x = LEFT
    for index, label in enumerate(["UNDERSTAND", "IMPLEMENT", "TEST", "EXPLAIN"]):
        pdf.setFillColor(TEAL if index % 2 == 0 else colors.HexColor("#23506C"))
        pdf.roundRect(x, 191, 115, 43, 6, fill=1, stroke=0)
        pdf.setFillColor(colors.white)
        pdf.setFont("Body-Bold", 10)
        pdf.drawCentredString(x + 57.5, 208, label)
        x += 127
    pdf.setFont("Body", 11)
    pdf.drawString(LEFT, 120, "Python 3.10+ foundations • CPython-specific details are marked")
    pdf.drawString(LEFT, 98, "Prepared 12 November 2026 • Based on this repository's maintained lessons")
    pdf.setFont("Body-Bold", 11)
    pdf.drawString(LEFT, 56, f"{total} pages  /  21 lessons  /  10 exercises  /  48 answered interview questions")


def make_contents(pages):
    groups = []
    current = None
    for number, page in enumerate(pages, start=4):
        title, section, _ = page_parts(page)
        if current != section:
            groups.append((section, number, []))
            current = section
        groups[-1][2].append(title)
    midpoint = (len(groups) + 1) // 2
    result = []
    for index, selected in enumerate([groups[:midpoint], groups[midpoint:]], 1):
        lines = [f"# Contents · {index} of 2", "Section: Navigation", ""]
        for section, page, titles in selected:
            description = "; ".join(titles[:4])
            if len(titles) > 4:
                description += f"; plus {len(titles) - 4} further topics"
            last = page + len(titles) - 1
            lines += [f"## [{section}](#page-{page})  ·  {page}–{last}",
                      description + ".", ""]
        lines += ["Select a section title to jump there. PDF bookmarks also list every page.",
                  "Page numbers in this guide are the PDF's physical page numbers."]
        result.append("\n".join(lines))
    return result


def verify_snippets(pages):
    snippets, checked = 0, 0
    for page in pages:
        for match in re.finditer(r"```python([^\n]*)\n(.*?)\n```", page, re.S):
            label, code = match.group(1), match.group(2)
            ast.parse(code, feature_version=(3, 10))
            snippets += 1
            if "verify" in label:
                result = subprocess.run([sys.executable, "-c", code], cwd=ROOT,
                                        capture_output=True, text=True, timeout=20)
                if result.returncode:
                    raise RuntimeError(f"Snippet failed in {page_parts(page)[0]}:\n{result.stderr}")
                checked += 1
    return {"python_blocks_parsed": snippets, "executable_examples_passed": checked}


def main():
    register_fonts()
    pages, refs = load_pages()
    checks = verify_snippets(pages)
    toc = make_contents(pages)
    all_pages = ["# Cover", *toc, *pages]
    if len(all_pages) > 100:
        raise ValueError(f"Guide exceeds 100-page limit: {len(all_pages)}")
    PREVIEW.mkdir(exist_ok=True)
    pdf = canvas.Canvas(str(OUT), pagesize=A4, pageCompression=1)
    pdf.setTitle("The Ultimate Core Python Guide — Repository Edition")
    pdf.setAuthor("Core Python Field Guide")
    pdf.setSubject("Core Python theory, repository implementations, exercises and mock interviews")
    pdf.setKeywords("Python, core Python, beginners, revision, interviews, standard library")
    pdf.bookmarkPage("page-1")
    pdf.addOutlineEntry("Cover", "page-1", 0)
    draw_cover(pdf, len(all_pages))
    pdf.showPage()
    layout = []
    for number, page in enumerate(all_pages[1:], start=2):
        title, section, body = page_parts(page)
        pdf.bookmarkPage(f"page-{number}")
        pdf.addOutlineEntry(title, f"page-{number}", 0)
        available = H - TOP - BOTTOM
        for size in (11.1, 10.8, 10.5, 10.2, 9.9):
            items = flowables(body, size)
            measured = [(item, *item.wrap(WIDTH, available)) for item in items]
            height = sum(h + item.getSpaceBefore() + item.getSpaceAfter()
                         for item, w, h in measured)
            if height <= available:
                break
        else:
            raise ValueError(f"Page {number} overflows: {title}, height {height:.1f}")
        draw_header(pdf, title, section, number, len(all_pages))
        y = H - TOP
        for item, width, height_item in measured:
            y -= item.getSpaceBefore() + height_item
            item.drawOn(pdf, LEFT, y)
            y -= item.getSpaceAfter()
        layout.append({"page": number, "title": title, "body_font": size,
                       "used_height": round(height, 1)})
        pdf.showPage()
    pdf.save()
    markdown = "# The Ultimate Core Python Guide\n\nRepository edition · 12 November 2026\n\n"
    markdown += "\n\n---\n\n".join(
        f'<a id="page-{number}"></a>\n\n' + re.sub(r"```python verify", "```python", p)
        for number, p in enumerate(all_pages[1:], start=2)
    )
    MD_OUT.write_text(markdown + "\n", encoding="utf-8")
    manifest = {
        "page_count": len(all_pages), "references": len(refs), **checks,
        "words": len(re.findall(r"\b[\w'-]+\b", markdown)),
        "repository_sources": {str(p.relative_to(ROOT)).replace("\\", "/"):
                              hashlib.sha256(p.read_bytes()).hexdigest()
                              for base in ("lessons", "projects", "tests")
                              for p in sorted((ROOT / base).rglob("*.py"))},
        "layout": layout,
    }
    (PREVIEW / "build_manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(json.dumps({k: v for k, v in manifest.items() if k not in ("layout", "repository_sources")}, indent=2))
    print(OUT)


if __name__ == "__main__":
    main()
