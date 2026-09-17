# Social Stories + Activity Books (Early Childhood)

Ten printable illustrated **social-story** books with matching activities,
written by **Daniel Tesfamariam**. Each is US Letter (8.5" x 11"), **45 pages**,
and print-ready. A social story gently walks a child through a situation and
models calm, kind choices, then lets them practice with activities.

## The Books (`social-stories/`)

| # | Title | Age | Format |
|---|-------|-----|--------|
| 1 | What to Do When I Feel Angry | 4-8 | Social story + calming cards |
| 2 | My First Day of School Feelings | 4-7 | Story + feelings workbook |
| 3 | Coping With Separation Anxiety | 4-8 | Printable story + activities |
| 4 | One Breath, One Step: Managing Overwhelm | 5-9 | SEL workbook + breathing cards |
| 5 | How to Ask an Adult for Help | 4-8 | Social story + role-play cards |
| 6 | Waiting Patiently and Taking Turns | 3-7 | Story + matching game |
| 7 | Handling Losing and Disappointment | 5-10 | Scenario cards + worksheets |
| 8 | Making Friends and Joining a Group | 5-9 | Social story + conversation cards |
| 9 | Safe Ways to Handle Big Feelings | 4-8 | Calm-down toolkit |
| 10 | Solving Conflicts With Kind Words | 6-10 | Role-play game + workbook |

## What's in each book
- Warm color cover + "How to Share This Book" (for grown-ups) + Table of Contents
- A **multi-page illustrated social story** - a big framed line-art picture with large,
  read-aloud narration - that models the feeling and calm, kind choices
- The title's **suggested format activities**: calming cards, feelings workbook,
  role-play cards, matching game, scenario cards, conversation cards, breathing
  cards, or a calm-down toolkit
- Practice pages: feelings faces to color, tracing, "What Would You Do?" scenarios,
  journaling, a personal plan, a calm-down toolkit, and a **certificate**

## How it was built
The sandbox blocks PyPI installs, so these use a small dependency-free PDF writer.
- `pdfkit.py` - minimal PDF 1.4 writer (with Unicode-punctuation normalization)
- `workbook_story.py` - the `StoryBook` engine, story-spread pages, line-art (kids/faces), and activity components
- `build_story_books.py` - books 1-5 + shared front/back matter + runner
- `story_books_6_10.py` - books 6-10

## Regenerate
```bash
python3 build_story_books.py   # writes social-stories/*.pdf + a page-count check
```

All output PDFs validate: correct header/xref/EOF, **45 pages each** (>= the 42-page
minimum), and every content stream decompresses cleanly. Print at 100% scale
(no "fit to page") for correct sizing; the "cards" pages are designed to be cut out.
