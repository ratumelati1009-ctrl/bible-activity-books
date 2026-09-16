# Christian Homeschool Activity Books

Ten printable, reproducible Christian activity workbooks generated as PDFs. Each
book is US Letter (8.5" x 11"), 11 pages, with a color cover, a parent/teacher
welcome page, a table of contents, and 8 activity pages.

## The Books (`books/`)

| # | Title | Ages |
|---|-------|------|
| 1 | Christian Bible Learning Workbook | 5–8 |
| 2 | Bible Stories & Activities Homeschool Workbook | 6–10 |
| 3 | Faith, Kindness & Courage Christian Activity Book | 6–9 |
| 4 | My First Bible Learning Activity Workbook | 3–6 |
| 5 | Christian Character Building Activity Book | 7–11 |
| 6 | Bible Heroes Learning Workbook for Kids | 6–10 |
| 7 | God's Creation Christian Homeschool Activity Pack | 5–9 |
| 8 | Prayer, Faith & Gratitude Activity Workbook | 6–10 |
| 9 | Bible Memory Verse Practice Workbook for Kids | 6–11 |
| 10 | Christian Preschool & Kindergarten Bible Activity Book | 4–6 |

## Activity types included
Coloring pages (line art), letter/word tracing, memory-verse trace & copy,
matching, word search (auto-generated & solvable), mazes (auto-generated DFS),
count & write, fill-in-the-blank with word banks, true/false, connect-the-dots,
and prayer/gratitude/reflection journaling pages.

## How it was built
The sandbox blocks PyPI, so instead of `reportlab` these use a small,
dependency-free PDF writer.

- `pdfkit.py` — minimal PDF 1.4 writer (vector shapes + Helvetica text, FlateDecode streams).
- `workbook.py` — themed `Workbook` class and the activity-page library.
- `build_books.py` — defines the content of all 10 books and renders them.

## Regenerate
```bash
python3 build_books.py   # writes books/*.pdf
```

All output PDFs validate: correct header/xref/EOF, 11 pages each, all content
streams decompress cleanly. Print at 100% scale (no "fit to page") for correct
handwriting-line sizing.
