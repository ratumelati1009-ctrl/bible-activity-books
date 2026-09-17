# Interactive Matching, Sorting, Role-Play & Game Books (Ages 5–19)

Ten printable interactive activity books — matching, sorting, sequencing,
role-play, and games — written by **Daniel Tesfamariam**. Each is US Letter
(8.5" × 11"), **43–45 pages**, and print-ready. Content scales across ages 5–19:
hands-on cut-out cards for younger kids, plus discussion and reflection prompts
for older kids and teens.

## The Books (`games-books/`)

| # | Title | Learning skill | Format |
|---|-------|----------------|--------|
| 1 | Match the Bible Character to the Story | Bible knowledge | Matching cards |
| 2 | Creation Days Sequencing Game | Sequencing | Seven-day sorting activity |
| 3 | Good Choice or Poor Choice? | Decision-making | Sorting cards |
| 4 | Match the Emotion to the Situation | Emotional literacy | Scenario-matching game |
| 5 | Fruits and Vegetables Color Sorting | Colors & vocabulary | Busy-book activity |
| 6 | Animal Homes Matching Game | Science | Matching cards & worksheets |
| 7 | Community Helpers Role-Play Kit | Social studies | Pretend-play cards |
| 8 | Kind or Unkind Words? | Social skills | Sorting & discussion game |
| 9 | Bible Story Bingo | Bible recognition | 30 bingo cards |
| 10 | What Would You Do? Christian Scenario Cards | Faith-based problem-solving | Role-play card deck |

## What's in each book
- Playful color cover + "How to Play & Learn" (for grown-ups, with age-scaling notes) + Table of Contents
- The title's core game, built from reusable components:
  - **Cut-out cards** (matching pairs, sorting cards, role-play/scenario cards) along dashed cut lines
  - **Sorting mats** and **draw-a-line matching**
  - **Sequencing** activities, **busy-book color sorting**, **scenario matching**
  - **Discussion sorting** (with talk-about prompts for older kids)
  - a **bingo generator** — Book 9 includes **30 unique bingo cards** plus a caller's list
- Extra practice: journaling/reflection, an **answer key** for grown-ups, and a **certificate**

## How it was built
The sandbox blocks PyPI installs, so these use a small dependency-free PDF writer.
- `pdfkit.py` — minimal PDF 1.4 writer (with Unicode-punctuation normalization)
- `workbook_games.py` — the `GameBook` engine and all game/activity components
- `build_games_books.py` — books 1–5 + shared front/back matter + runner
- `games_books_6_10.py` — books 6–10

## Regenerate
```bash
python3 build_games_books.py   # writes games-books/*.pdf + a page-count check
```

All output PDFs validate: correct header/xref/EOF, **43–45 pages each** (≥ the 42-page
minimum), and every content stream decompresses cleanly. Print at 100% scale
(no "fit to page"); the cards, tokens, and mats are designed to be cut out.
