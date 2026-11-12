"""Audit the generated PDF and render a review contact sheet. Requires PyMuPDF/Pillow."""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / ".book-tools"))
import pymupdf
from PIL import Image, ImageDraw


def main():
    output = ROOT / ".book-preview"
    output.mkdir(exist_ok=True)
    document = pymupdf.open(ROOT / "docs/ultimate_python_core_guide.pdf")
    expected = json.loads((output / "build_manifest.json").read_text(encoding="utf-8"))
    assert len(document) == expected["page_count"] <= 100
    assert len(document.get_toc()) == len(document)
    errors, external, internal, texts, titles = [], 0, 0, [], []
    for index, page in enumerate(document):
        text = page.get_text()
        texts.append(text)
        if not text.strip() or "\ufffd" in text or "{{code:" in text or "[[R" in text:
            errors.append({"page": index + 1, "issue": "Missing text or unresolved source marker"})
        for block in page.get_text("dict")["blocks"]:
            for line in block.get("lines", []):
                for span in line["spans"]:
                    x0, y0, x1, y1 = span["bbox"]
                    if x0 < 0 or x1 > page.rect.width + 0.5 or y0 < 0 or y1 > page.rect.height + .5:
                        errors.append({"page": index + 1, "issue": "Text outside page", "text": span["text"]})
                    if index and span["size"] >= 20:
                        titles.append({"page": index + 1, "title": span["text"], "right": x1})
        for link in page.get_links():
            if link["kind"] == pymupdf.LINK_URI:
                external += 1
                if not link["uri"].startswith("https://"):
                    errors.append({"page": index + 1, "issue": "Unexpected external link"})
            elif link["kind"] == pymupdf.LINK_GOTO:
                internal += 1
                if not 0 <= link["page"] < len(document):
                    errors.append({"page": index + 1, "issue": "Broken page destination"})
    full_text = "\n".join(texts)
    counts = {prefix: len(re.findall(rf"\b{prefix}\d{{2}}\s*·", full_text))
              for prefix in ("F", "M", "S", "A")}
    assert counts == {"F": 12, "M": 12, "S": 12, "A": 12}, counts
    assert internal >= 15 and external >= 100
    # Header titles must retain the same printable right margin as body text.
    for title in titles:
        if title["right"] > document[0].rect.width - 40:
            errors.append({"page": title["page"], "issue": "Title exceeds margin", "text": title["title"]})
    pages = [1, 2, 7, 14, 24, 35, 45, 58, 65, 74, 84, 99]
    pages = [p for p in pages if p <= len(document)]
    cell_w, cell_h = 360, 540
    sheet = Image.new("RGB", (cell_w * 4, cell_h * 3), "#DBE3EC")
    draw = ImageDraw.Draw(sheet)
    for position, number in enumerate(pages):
        pix = document[number - 1].get_pixmap(matrix=pymupdf.Matrix(0.58, 0.58), alpha=False)
        im = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        x, y = (position % 4) * cell_w, (position // 4) * cell_h
        sheet.paste(im, (x + 7, y + 26))
        draw.text((x + 9, y + 8), f"PDF page {number}", fill="#132C46")
    sheet.save(output / "contact_sheet.png")
    for number in [2, 14, 65, 84, 99]:
        if number <= len(document):
            document[number - 1].get_pixmap(matrix=pymupdf.Matrix(1.3, 1.3)).save(
                output / f"page_{number:02}.png")
    report = {
        "pages": len(document), "bookmarks": len(document.get_toc()),
        "external_links": external, "internal_links": internal,
        "interview_questions_by_level": counts,
        "extracted_text_characters": len(full_text), "layout_errors": errors,
    }
    (output / "pdf_audit.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
