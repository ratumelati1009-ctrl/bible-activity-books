"""
merge_pdfs.py — Merge the 10 workbook PDFs into one combined download.

Our PDFs are all produced by pdfkit.py with a known, simple structure
(FlateDecode content streams, Helvetica fonts, one content stream per page).
Rather than write a general PDF parser, we re-extract each page's content
stream and re-emit a single fresh PDF using pdfkit's writer. This keeps the
output a clean, valid single file.

We add a combined cover + master table of contents at the front.
"""

import re
import zlib
import glob
import os
import pdfkit

BOOKS_DIR = "books"
OUTPUT = "Christian_Study_Workbooks_Ages_13-19_COMPLETE_COLLECTION.pdf"

TITLES = {
    "01": "Christian Bible Learning Workbook",
    "02": "Bible Stories & Application Study Workbook",
    "03": "Faith, Kindness & Courage Study Workbook",
    "04": "Foundations of Faith Study Workbook",
    "05": "Christian Character & Integrity Study Workbook",
    "06": "Bible Heroes & Their Faith Study Workbook",
    "07": "God's Creation, Science & Faith Study Workbook",
    "08": "Prayer, Faith & Gratitude Study Workbook",
    "09": "Scripture Memory & Meditation Study Workbook",
    "10": "Owning Your Faith Study Workbook",
}


def extract_page_streams(path):
    """Return a list of decompressed content-stream byte strings, in page order.

    pdfkit emits objects in creation order: fonts, then one content stream per
    page (in page order), then the pages tree, then page objects. Each content
    stream is `<< /Length N /Filter /FlateDecode >>\nstream\n...\nendstream`.
    We pull them out in file order, which matches page order.
    """
    data = open(path, "rb").read()
    streams = re.findall(rb"stream\n(.*?)\nendstream", data, re.S)
    out = []
    for s in streams:
        try:
            out.append(zlib.decompress(s))
        except Exception:
            pass
    return out


def main():
    files = sorted(glob.glob(os.path.join(BOOKS_DIR, "*.pdf")))
    doc = pdfkit.Document(
        title="Christian Study Workbooks for Ages 13-19 - Complete Collection",
        author="Christian Homeschool Press")
    PW, PH = pdfkit.LETTER

    # ---- master cover ----
    c = doc.add_page()
    c.set_fill(0.13, 0.20, 0.38)
    c.rect(0, 0, PW, PH, fill=True, stroke=False)
    c.set_fill(0.078, 0.12, 0.228)
    c.rect(0, 0, PW, 150, fill=True, stroke=False)
    c.set_fill(0.78, 0.60, 0.16)
    c.text(60, PH - 120, "THE COMPLETE COLLECTION", 12, bold=True)
    c.set_fill(1, 1, 1)
    c.wrap_text(60, PH - 165, "Christian Study Workbooks", 36, PW - 120, bold=True, leading=40)
    c.set_fill(0.78, 0.60, 0.16)
    c.rect(60, PH - 250, 130, 3, fill=True, stroke=False)
    c.set_fill(0.90, 0.92, 0.96)
    c.wrap_text(60, PH - 278, "Ten complete study workbooks for teens and young adults, ages 13-19 — devotionals, inductive Bible study, word studies, reflection, and application.", 14, PW - 130, leading=20)
    # emblem: open book + cross
    cx, cy = PW / 2, 380
    c.set_stroke(1, 1, 1); c.set_line_width(2)
    c.line(cx, cy - 34, cx, cy + 34)
    c.polygon([(cx, cy + 34), (cx - 74, cy + 17), (cx - 74, cy - 41), (cx, cy - 24)], fill=False, stroke=True)
    c.polygon([(cx, cy + 34), (cx + 74, cy + 17), (cx + 74, cy - 41), (cx, cy - 24)], fill=False, stroke=True)
    c.set_fill(0.78, 0.60, 0.16)
    c.rect(cx - 4, cy + 36, 8, 50, fill=True, stroke=False)
    c.rect(cx - 18, cy + 62, 36, 8, fill=True, stroke=False)
    c.set_fill(0.78, 0.60, 0.16)
    c.round_rect(60, 110, 250, 40, 8, fill=True, stroke=False)
    c.set_fill(0.078, 0.12, 0.228)
    c.text(78, 123, "10 Books  •  510 Pages  •  Ages 13-19", 12, bold=True)
    c.set_fill(0.85, 0.88, 0.92)
    c.text(60, 70, "Christian Homeschool Press  •  Reproducible for one household or class", 9)

    # ---- master contents ----
    toc = doc.add_page()
    toc.set_fill(0.13, 0.20, 0.38)
    toc.rect(0, PH - 90, PW, 90, fill=True, stroke=False)
    toc.set_fill(1, 1, 1)
    toc.text(60, PH - 58, "What's Inside", 22, bold=True)
    y = PH - 130
    # (page numbers are approximate: cover+toc = 2, then 51 per book)
    page_cursor = 3
    for f in files:
        base = os.path.basename(f)
        num = base[:2]
        title = TITLES.get(num, base)
        toc.set_fill(0.13, 0.20, 0.38)
        toc.circle(72, y + 4, 11, fill=True, stroke=False)
        toc.set_fill(1, 1, 1)
        toc.text_center(72, y + 0.5, str(int(num)), 10, bold=True)
        toc.set_fill(0.11, 0.12, 0.15)
        toc.text(94, y, title, 12, bold=True)
        toc.set_fill(0.42, 0.45, 0.50)
        toc.text_right(PW - 60, y, f"p. {page_cursor}", 11)
        y -= 30
        page_cursor += 51

    # ---- append every page of every book ----
    total_pages = 2
    for f in files:
        for stream in extract_page_streams(f):
            pg = doc.add_page()
            pg._ops.append(stream.decode("latin-1"))
            total_pages += 1

    doc.save(OUTPUT)
    return OUTPUT, total_pages


if __name__ == "__main__":
    path, pages = main()
    size = os.path.getsize(path)
    print(f"[OK] {path}  pages={pages}  bytes={size:,}")
