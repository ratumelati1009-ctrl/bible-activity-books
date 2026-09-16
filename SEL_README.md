# SEL / Emotional Regulation Activity Books (Ages 5–17)

Ten printable **Social-Emotional Learning (SEL)** activity books, each **46 pages**
(US Letter, 8.5" × 11"), written by **Daniel Tesfamariam**. Designed to scale
across a wide age range: simpler activities for younger children (coloring,
tracing, feelings faces, matching, breathing shapes) plus deeper activities for
older kids and teens (journaling, scenario problem-solving, coping-plan building,
self-reflection).

## The Books (`sel-books/`)

| # | Title |
|---|-------|
| 1 | Dazzle's Calm-Down Adventure SEL Toolkit |
| 2 | I Can Calm My Body: Emotional Regulation Activity Book |
| 3 | When I Feel Angry: Kids' Calm-Down Activity Pack |
| 4 | Big Feelings, Calm Choices: SEL Workbook for Kids |
| 5 | I Can Wait! Patience & Waiting Skills Activity Pack |
| 6 | My Calm Corner: Printable SEL Toolkit |
| 7 | Feelings Detective: Social-Emotional Learning Activity Book |
| 8 | What Should I Do? Kids' Social Skills Scenario Cards |
| 9 | Brave Feelings: Coping Skills Activity Book for Kids |
| 10 | One Breath, One Step: Classroom Calm Kit |

## What's in each book
- Color cover + "How to Use This Book" + "Grows With the Reader (Ages 5–17)" + Table of Contents
- Themed parts, each with a divider and multiple activity pages:
  - **Feelings literacy** — feelings faces to color, a feelings thermometer, body-scan
  - **Calm-down tools** — breathing exercises (box, triangle, flower, star), strategy cards, tracing affirmations
  - **Calm choices** — "What Would You Do?" scenarios, checklists, matching
  - **Calm & reflect** — coloring scenes + journaling
  - **Practice week** — daily feelings check-ins + review
- Back matter: My Toolkit summary, "How Far I've Come," personal Calm-Down Plan, gratitude, and notes pages

Each title also has its own hook (e.g. Dazzle the dragon, a Feelings Detective badge,
an anger volcano/thermometer, a worry ladder, a classroom calm kit for teachers).

## How it was built
The sandbox blocks PyPI installs, so these use a small dependency-free PDF writer.
- `pdfkit.py` — minimal PDF 1.4 writer (shared with the other collections)
- `workbook_sel.py` — the `SELBook` engine + activity-page components and line-art scenes
- `build_sel_books.py` — books 1–5 + shared parts + runner (auto-pads to ≥44 pages)
- `sel_books_6_10.py` — books 6–10

## Regenerate
```bash
python3 build_sel_books.py   # writes sel-books/*.pdf and prints a page-count check
```

All output PDFs validate: correct header/xref/EOF, **46 pages each** (≥ the 42-page
minimum), and every content stream decompresses cleanly. Print at 100% scale
(no "fit to page") for correct writing-line and tracing sizing.
