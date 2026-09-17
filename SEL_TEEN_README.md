# Teen SEL / Emotional Regulation Workbooks (Ages 10–19)

Ten printable **Social-Emotional Learning (SEL)** workbooks written for **ages
10–19** (older kids, teens, and young adults), by **Daniel Tesfamariam**. Each is
US Letter (8.5" × 11"), **44 pages**, and print-ready.

These are more mature than a younger-kids activity book: less coloring/tracing,
more psychoeducation, self-assessment, coping tools, CBT-style thought work,
real-life scenarios, journaling, and personal planning.

## The Books (`sel-teen-books/`)

| # | Title | Focus |
|---|-------|-------|
| 1 | Regulate | Understanding & managing big emotions |
| 2 | Under Pressure | Stress & anxiety coping |
| 3 | Scroll Smart | Social media, mood & mental health |
| 4 | Know Your Worth | Self-esteem & confidence |
| 5 | Ride the Wave | Understanding & managing anger |
| 6 | People Skills | Friendships, conflict & boundaries |
| 7 | Bounce Back | Resilience & coping skills |
| 8 | Quiet the Noise | Mindfulness & calm |
| 9 | Motivated Mind | Focus, goals & beating procrastination |
| 10 | Grounded | A guided journal for mood, stress & self-awareness |

## What's in each book
- Color cover + welcome (with a note for grown-ups) + "How This Book Works" + a safety/support note + Table of Contents
- Five themed parts, each opening with a divider, combining:
  - **Psychoeducation** — short, honest explanations of what's happening in the brain/body
  - **Self-assessment** — 1–5 rating scales to notice personal patterns
  - **Coping tools** — breathing exercises, coping menus, grounding
  - **Thought work** — CBT-style thinking-traps and "catch it, check it, change it" reframing
  - **Real-life scenarios** — "What would you do?" situations to work through
- Trackers: weekly mood/energy tracker, stress & trigger log
- Back matter: a personal Wellbeing Plan, a "When You Need More Help" support page, values/goals, boundary scripts, gratitude, and reflection/notes

Each title has its own hook (e.g. the "feeling wave," the "anger escalator,"
the social-media "highlight reel trap," growth mindset and the power of "yet").

## Safety note
These support everyday SEL and self-reflection; they are **not** therapy or
medical advice. Each book includes guidance to reach out to a trusted adult,
counselor, or local crisis/helpline when feelings become unmanageable.

## How it was built
The sandbox blocks PyPI installs, so these use a small dependency-free PDF writer.
- `pdfkit.py` — minimal PDF 1.4 writer (with Unicode-punctuation normalization)
- `workbook_sel.py` — base SEL engine (`SELBook`) + shared activity components
- `workbook_sel_teen.py` — teen-oriented components (rating scales, thought reframing, mood tracker, stress log, values/goals, boundary scripts, etc.)
- `build_sel_teen_books.py` — books 1–2 + shared front/back matter + runner
- `sel_teen_books_3_10.py` — books 3–10

## Regenerate
```bash
python3 build_sel_teen_books.py   # writes sel-teen-books/*.pdf + a page-count check
```

All output PDFs validate: correct header/xref/EOF, **44 pages each** (≥ the 42-page
minimum), and every content stream decompresses cleanly. Print at 100% scale
(no "fit to page") for correct writing-line sizing.
