"""
workbook_sel_teen.py — Teen/young-adult SEL components (ages 10-19).

Extends the existing SEL engine (workbook_sel.SELBook + pdfkit) with more
mature, reflective, less "cartoon" page builders suited to older kids and
teens: self-assessment rating scales, CBT-style thought reframing, a mood
tracker, a stress log, values & goals work, boundary scripts, coping-skill
menus, and deeper journaling / reflection.

All builders take an SELBook instance `wb` and append pages.
"""

import workbook_sel as s
import pdfkit

PW, PH = s.PW, s.PH
MARGIN, CW = s.MARGIN, s.CW
INK, SLATE, GRAY, RULE = s.INK, s.SLATE, s.GRAY, s.RULE
CARD, SOFT = s.CARD, s.SOFT


# ---------------- low-level shared bits ----------------
def _scale_legend(p, wb, y, low="Never", high="Always"):
    p.set_fill(*GRAY)
    p.text_right(PW - MARGIN, y, f"1 = {low}      5 = {high}", 9)
    return y - 16


def rating_scale(wb, kicker, heading, intro, statements, low="Never", high="Always"):
    """Self-assessment: statements rated 1-5 with bubbles on the right."""
    p, y, n = wb.page(kicker, heading)
    y = wb.intro_box(p, y, intro)
    y = _scale_legend(p, wb, y, low, high)
    for st in statements:
        if y < 74:
            break
        p.set_fill(*INK)
        endy = p.wrap_text(MARGIN, y, st, 10.8, CW - 165, leading=14)
        bx = PW - MARGIN - 150
        for k in range(5):
            cx = bx + k * 30
            p.set_stroke(*wb.accent); p.set_line_width(1)
            p.circle(cx, y - 3, 8, fill=False, stroke=True)
            p.set_fill(*GRAY); p.text_center(cx, y - 6.5, str(k + 1), 8)
            p.set_fill(*INK)
        y = min(endy, y - 6) - 20
    if y > 90:
        y = wb.subhead(p, y, "What my answers tell me")
        wb.write_lines(p, y, 2, spacing=26)
    return p


def thought_reframe(wb, kicker="Reframe", heading="Catch It, Check It, Change It"):
    """CBT-style thought-reframing worksheet."""
    p, y, n = wb.page(kicker, heading)
    y = wb.intro_box(p, y, "Our thoughts shape our feelings. Sometimes an automatic thought is unhelpful or "
                           "untrue. You can CATCH the thought, CHECK if it's fair and true, and CHANGE it into "
                           "a more balanced one. This is a skill - it gets easier with practice.")
    steps = [
        ("1. The situation (just the facts):", 2),
        ("2. The automatic thought that popped up:", 2),
        ("3. The feeling it gave me (and how strong, 0-10):", 1),
        ("4. Check it: Is it 100% true? What's the evidence? Am I mind-reading or catastrophizing?", 2),
        ("5. A more balanced, fair thought:", 2),
        ("6. How I feel now:", 1),
    ]
    for label, lines in steps:
        if y < 80:
            break
        p.set_fill(*wb.accent)
        endy = p.wrap_text(MARGIN, y, label, 11, CW, bold=True, leading=14)
        y = wb.write_lines(p, endy - 6, lines, spacing=24)
        y -= 8
    return p


def unhelpful_thinking(wb, kicker="Thinking Traps", heading="Common Thinking Traps"):
    p, y, n = wb.page(kicker, heading)
    y = wb.intro_box(p, y, "Everyone's brain falls into 'thinking traps' sometimes. Naming them helps you step "
                           "back. Circle the ones you notice most, then write an example.")
    traps = [
        ("All-or-nothing", "Seeing things as total success or total failure, no middle ground."),
        ("Catastrophizing", "Assuming the worst possible outcome will happen."),
        ("Mind-reading", "Believing you know others are judging you - without proof."),
        ("Labeling", "Calling yourself 'stupid' or 'a failure' over one event."),
        ("Filtering", "Only noticing the negatives and ignoring the positives."),
        ("Should statements", "Harsh rules like 'I should always...' that set you up to feel bad."),
    ]
    cols = 2
    cardw = (CW - 16) / cols
    cardh = 84
    top = y - 2
    for i, (t, d) in enumerate(traps):
        col = i % cols; row = i // cols
        cx = MARGIN + col * (cardw + 16)
        cy = top - row * (cardh + 12)
        if cy - cardh < 120:
            break
        p.set_fill(*CARD); p.round_rect(cx, cy - cardh, cardw, cardh, 10, fill=True, stroke=False)
        p.set_stroke(*wb.accent); p.set_line_width(1.3)
        p.round_rect(cx, cy - cardh, cardw, cardh, 10, fill=False, stroke=True)
        p.set_fill(*wb.accent); p.text(cx + 14, cy - 20, t, 11, bold=True)
        p.set_fill(*SLATE); p.wrap_text(cx + 14, cy - 38, d, 9.3, cardw - 26, leading=12)
    # example lines
    ylow = top - 2 * (cardh + 12) - 6
    if ylow > 90:
        p.set_fill(*wb.accent); p.text(MARGIN, ylow, "A thinking trap I fall into, and a real example:", 11, bold=True)
        wb.write_lines(p, ylow - 14, 3, spacing=24)
    return p


def coping_menu(wb, kicker, heading, intro, categories):
    """categories: list of (category_name, [items]). A menu of coping skills."""
    p, y, n = wb.page(kicker, heading)
    y = wb.intro_box(p, y, intro)
    for cat, items in categories:
        if y < 90:
            break
        y = wb.subhead(p, y, cat)
        for it in items:
            if y < 70:
                break
            p.set_stroke(*wb.accent); p.set_line_width(1.1)
            p.rect(MARGIN, y - 9, 11, 11, fill=False, stroke=True)
            p.set_fill(*INK)
            endy = p.wrap_text(MARGIN + 22, y, it, 10.6, CW - 22, leading=13.5)
            y = min(endy, y - 12) - 6
        y -= 8
    return p


def mood_tracker(wb, kicker="Track", heading="Weekly Mood & Energy Tracker"):
    p, y, n = wb.page(kicker, heading)
    y = wb.intro_box(p, y, "Tracking your mood helps you spot patterns - what lifts you up and what drains you. "
                           "Each day, shade your mood level (1 low - 5 high) and note one thing that affected it.")
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    top = y - 6
    row_h = 30
    label_w = 42
    grid_x = MARGIN + label_w
    grid_w = CW - label_w - 150
    cell = grid_w / 5
    # header row
    p.set_fill(*GRAY)
    for k in range(5):
        p.text_center(grid_x + cell * k + cell / 2, top, str(k + 1), 9, bold=True)
    p.text(grid_x + grid_w + 12, top, "What affected it?", 9, bold=True)
    top -= 16
    for d in days:
        yy = top
        p.set_fill(*wb.accent); p.text(MARGIN, yy - row_h / 2 - 3, d, 11, bold=True)
        for k in range(5):
            cx = grid_x + cell * k
            p.set_stroke(*RULE); p.set_line_width(0.8)
            p.rect(cx, yy - row_h + 6, cell - 4, row_h - 8, fill=False, stroke=True)
        # note line
        p.set_stroke(*RULE); p.set_line_width(0.7)
        p.line(grid_x + grid_w + 12, yy - row_h / 2, PW - MARGIN, yy - row_h / 2)
        top -= row_h
    return p


def stress_log(wb, kicker="Log", heading="Stress & Trigger Log"):
    p, y, n = wb.page(kicker, heading)
    y = wb.intro_box(p, y, "When you feel stressed or overwhelmed, logging it helps you understand your triggers "
                           "and what actually helps. Fill one row when a stressful moment happens.")
    headers = ["Situation / trigger", "Body & feelings (0-10)", "What I did", "Did it help?"]
    # 4 entry blocks
    for i in range(4):
        if y < 110:
            break
        p.set_fill(*wb.accent); p.circle(MARGIN + 8, y + 2, 9, fill=True, stroke=False)
        p.set_fill(1, 1, 1); p.text_center(MARGIN + 8, y - 1.5, str(i + 1), 9, bold=True)
        yy = y
        for h in headers:
            p.set_fill(*GRAY); p.text(MARGIN + 26, yy - 2, h + ":", 9.5, bold=True)
            p.set_stroke(*RULE); p.set_line_width(0.7)
            p.line(MARGIN + 26 + pdfkit.text_width(h + ": ", 9.5, bold=True), yy - 4,
                   PW - MARGIN, yy - 4)
            yy -= 20
        y = yy - 10
    return p


def values_goals(wb, kicker="Values & Goals", heading="What Matters to Me"):
    p, y, n = wb.page(kicker, heading)
    y = wb.intro_box(p, y, "Knowing what matters to you makes decisions and hard days easier. When you act in line "
                           "with your values, stress often makes more sense and feels more manageable.")
    y = wb.subhead(p, y, "Three values that matter most to me")
    y = wb.write_lines(p, y, 3, spacing=28)
    y -= 4
    y = wb.subhead(p, y, "One goal that fits those values")
    y = wb.write_lines(p, y, 1, spacing=26)
    y = wb.subhead(p, y, "One small step I can take this week")
    y = wb.write_lines(p, y, 2, spacing=26)
    return p


def boundaries_scripts(wb, kicker="Boundaries", heading="Saying It: Boundary Scripts"):
    p, y, n = wb.page(kicker, heading)
    y = wb.intro_box(p, y, "A boundary is a limit that protects your wellbeing. Boundaries can be kind AND firm. "
                           "Practice wording so it's ready when you need it.")
    prompts = [
        "Saying no without over-explaining: \"No thanks, that doesn't work for me.\" My version:",
        "Asking for space: \"I need some time to myself right now.\" My version:",
        "Naming a limit online: \"Please don't share that.\" My version:",
        "Asking for what I need: \"It would help me if...\" My version:",
    ]
    for pr in prompts:
        if y < 90:
            break
        p.set_fill(*wb.accent)
        endy = p.wrap_text(MARGIN, y, pr, 10.8, CW, bold=True, leading=14)
        y = wb.write_lines(p, endy - 6, 2, spacing=24)
        y -= 8
    return p


def reflection_journal(wb, kicker, heading, prompts):
    """Deeper journaling: fewer prompts, more lines each."""
    p, y, n = wb.page(kicker, heading)
    for pr in prompts:
        if y < 110:
            break
        p.set_fill(*wb.accent2)
        p.rect(MARGIN, y - 2, 16, 3, fill=True, stroke=False)
        p.set_fill(*INK)
        endy = p.wrap_text(MARGIN, y - 16, pr, 11.5, CW, bold=True, leading=15)
        y = wb.write_lines(p, endy - 6, 4, spacing=26)
        y -= 12
    return p


def info_page(wb, kicker, heading, paragraphs, subhead=None, bullets=None):
    """Psychoeducation page: explanation text + optional bullet list."""
    p, y, n = wb.page(kicker, heading)
    for para in paragraphs:
        y = wb.paragraph(p, y, para)
    if subhead:
        y = wb.subhead(p, y, subhead)
    if bullets:
        y = wb.checklist(p, y, bullets, box=False)
    return p


def action_plan(wb, kicker, heading, intro, fields):
    """A fill-in plan with labeled sections. fields: list of (label, lines)."""
    p, y, n = wb.page(kicker, heading)
    y = wb.intro_box(p, y, intro)
    for label, lines in fields:
        if y < 80:
            break
        p.set_fill(*wb.accent)
        endy = p.wrap_text(MARGIN, y, label, 11.2, CW, bold=True, leading=14)
        y = wb.write_lines(p, endy - 6, lines, spacing=25)
        y -= 8
    return p
