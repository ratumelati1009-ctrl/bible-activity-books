# Christian Study Workbooks for Ages 13–19

Ten printable Christian study workbooks written for **teens and young adults
(ages 13–19)**. Each book is US Letter (8.5" × 11"), **51 pages**, and print-ready.

Every book follows a consistent, mature structure:
- Color cover + "How to Use This Study" + Table of Contents
- **Six themed units**, each containing:
  - a **devotional** (Scripture + short teaching + reflection questions + prayer prompt)
  - a two-page **inductive Bible study** (Observe → Interpret → Apply)
  - a **word study** (a key biblical term, with verses and dig-deeper questions)
  - a **reflection/journal** page with writing lines
  - an **extra**: small-group discussion, worldview/apologetics, or an application challenge
- Back matter: memory-verse review, a **spiritual self-assessment**, a final reflection, and study-notes pages

## The Books (`books/`)

| # | Title | Focus |
|---|-------|-------|
| 1 | Christian Bible Learning Workbook | How to read, understand & live the Bible |
| 2 | Bible Stories & Application Study Workbook | Bible narratives + what they mean today |
| 3 | Faith, Kindness & Courage Study Workbook | Christlike character under teen pressures |
| 4 | Foundations of Faith Study Workbook | Core truths: God, self, sin, gospel, new life |
| 5 | Christian Character & Integrity Study Workbook | Integrity, honesty, purity, humility, failure |
| 6 | Bible Heroes & Their Faith Study Workbook | Abraham, Moses, Esther, David, Daniel, Jesus |
| 7 | God's Creation, Science & Faith Study Workbook | Origins, wonder & big questions without fear |
| 8 | Prayer, Faith & Gratitude Study Workbook | Honest prayer, trust & thankfulness |
| 9 | Scripture Memory & Meditation Study Workbook | Memorizing verses for identity, anxiety, gospel |
| 10 | Owning Your Faith Study Workbook | Moving from inherited belief to personal faith |

> Note: These replace an earlier young-children edition. The titles map to the
> original list; a few were renamed to fit the teen/young-adult audience
> (e.g. "My First Bible Learning Workbook" → *Foundations of Faith*; the
> preschool book → *Owning Your Faith*).

## How it was built
The sandbox blocks PyPI installs, so these use a small, dependency-free PDF
writer instead of a library like `reportlab`.

- `pdfkit.py` — minimal PDF 1.4 writer (vector shapes + Helvetica text, FlateDecode streams, Unicode-punctuation normalization).
- `workbook_teen.py` — the `Teenbook` layout engine and composite study-page functions.
- `build_teen_books.py` — book 1 + the assembly/factory helpers + runner.
- `teen_books_2_10.py` — content for books 2–10.
- `workbook.py` / `build_books.py` — the earlier young-children engine (kept for reference).

## Regenerate
```bash
python3 build_teen_books.py   # writes books/*.pdf and prints a page-count check
```

All output PDFs validate: correct header/xref/EOF, **51 pages each** (≥ the 42-page
minimum), and every content stream decompresses cleanly. Print at 100% scale
(no "fit to page") for correct writing-line sizing.
