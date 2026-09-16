"""
workbook_teen.py — Christian study workbook engine for ages 13-19.

Reuses the dependency-free pdfkit.py PDF writer, but the page library targets
teens / young adults: devotionals, inductive Bible study, word studies,
reflection & journaling, apologetics / worldview questions, discussion prompts,
self-assessments, memory-verse study, application challenges, and note pages.

Design goals:
 - Clean, mature editorial layout (no cartoon coloring/tracing).
 - Every page has real written content plus space to respond.
 - Books assemble to 42+ pages easily by composing sections.
"""

import math
import pdfkit

# Mature palette
INK = (0.11, 0.12, 0.15)
SLATE = (0.22, 0.26, 0.33)
GRAY = (0.42, 0.45, 0.50)
FAINT = (0.68, 0.70, 0.75)
RULE = (0.80, 0.82, 0.86)
PAPER = (0.96, 0.97, 0.98)
CARD = (0.94, 0.955, 0.975)

# Accent schemes (main, secondary)
NAVY = (0.13, 0.20, 0.38);   GOLD = (0.78, 0.60, 0.16)
TEAL = (0.09, 0.42, 0.45);   AMBER = (0.85, 0.55, 0.15)
MAROON = (0.45, 0.13, 0.20); SAND = (0.80, 0.66, 0.40)
FOREST = (0.16, 0.36, 0.24); LIME = (0.55, 0.65, 0.25)
INDIGO = (0.24, 0.22, 0.45); COPPER = (0.72, 0.45, 0.22)
CHAR = (0.20, 0.22, 0.26);   STEELB = (0.30, 0.50, 0.68)

PW, PH = pdfkit.LETTER
MARGIN = 60.0
CW = PW - 2 * MARGIN  # content width


class Teenbook:
    def __init__(self, title, subtitle, accent=NAVY, accent2=GOLD, series="Faith Foundations Study Series", writer="Daniel Tesfamariam"):
        self.writer = writer
        self.doc = pdfkit.Document(title=title, author=writer)
        self.title = title
        self.subtitle = subtitle
        self.accent = accent
        self.accent2 = accent2
        self.series = series
        self.ages = "Ages 13–19"
        self._pageno = 0
        self.toc = []

    def save(self, path):
        return self.doc.save(path)

    # ---------------- chrome ----------------
    def _new(self):
        self._pageno += 1
        return self.doc.add_page(), self._pageno

    def _footer(self, p, n):
        p.set_stroke(*RULE); p.set_line_width(0.6)
        p.line(MARGIN, 44, PW - MARGIN, 44)
        p.set_fill(*GRAY)
        p.text(MARGIN, 32, self.title, size=7.5)
        p.text_right(PW - MARGIN, 32, str(n), size=8, bold=True)

    def _running_head(self, p, section):
        p.set_fill(*GRAY)
        p.text(MARGIN, PH - 40, self.series.upper(), size=7.5, bold=True)
        p.text_right(PW - MARGIN, PH - 40, section.upper(), size=7.5, bold=True)
        p.set_stroke(*RULE); p.set_line_width(0.6)
        p.line(MARGIN, PH - 48, PW - MARGIN, PH - 48)

    def _heading(self, p, kicker, title, y=PH - 92):
        p.set_fill(*self.accent2)
        p.rect(MARGIN, y + 20, 34, 4, fill=True, stroke=False)
        p.set_fill(*self.accent)
        p.text(MARGIN, y, kicker.upper(), size=10, bold=True)
        p.set_fill(*INK)
        endy = p.wrap_text(MARGIN, y - 22, title, 20, CW, bold=True, leading=24)
        return endy - 10

    def page(self, section, kicker, title):
        p, n = self._new()
        self._running_head(p, section)
        self._footer(p, n)
        y = self._heading(p, kicker, title)
        return p, y, n

    # ---------------- shared elements ----------------
    def rule(self, p, y):
        p.set_stroke(*RULE); p.set_line_width(0.6)
        p.line(MARGIN, y, PW - MARGIN, y)
        return y - 14

    def paragraph(self, p, y, text, size=11, gap=8, color=INK, bold=False):
        p.set_fill(*color)
        endy = p.wrap_text(MARGIN, y, text, size, CW, bold=bold, leading=size * 1.42)
        return endy - gap

    def subhead(self, p, y, text):
        p.set_fill(*self.accent)
        p.text(MARGIN, y, text, 12.5, bold=True)
        p.set_stroke(*self.accent2); p.set_line_width(1.2)
        p.line(MARGIN, y - 6, MARGIN + 40, y - 6)
        return y - 22

    def scripture_block(self, p, y, verse, ref):
        # measure height by wrapping into a scratch estimate
        lines = self._wrap_count(verse, 12, CW - 48, bold=False)
        h = 34 + lines * 17 + 14
        p.set_fill(*CARD)
        p.round_rect(MARGIN, y - h, CW, h, 8, fill=True, stroke=False)
        p.set_fill(*self.accent)
        p.rect(MARGIN, y - h, 5, h, fill=True, stroke=False)
        p.set_fill(*self.accent)
        p.text(MARGIN + 22, y - 20, ref.upper(), 9.5, bold=True)
        p.set_fill(*INK)
        endy = p.wrap_text(MARGIN + 22, y - 38, '"' + verse + '"', 12, CW - 44, leading=17)
        return y - h - 12

    def callout(self, p, y, label, text):
        lines = self._wrap_count(text, 10.5, CW - 40)
        h = 26 + lines * 15 + 10
        p.set_fill(*PAPER)
        p.round_rect(MARGIN, y - h, CW, h, 6, fill=True, stroke=False)
        p.set_stroke(*self.accent2); p.set_line_width(1)
        p.round_rect(MARGIN, y - h, CW, h, 6, fill=False, stroke=True)
        p.set_fill(*self.accent2)
        p.text(MARGIN + 16, y - 18, label.upper(), 9, bold=True)
        p.set_fill(*SLATE)
        p.wrap_text(MARGIN + 16, y - 34, text, 10.5, CW - 32, leading=15)
        return y - h - 12

    def write_lines(self, p, y, count, spacing=26, indent=0):
        p.set_stroke(*RULE); p.set_line_width(0.7)
        x0 = MARGIN + indent
        for i in range(count):
            yy = y - i * spacing
            if yy < 60:
                break
            p.line(x0, yy, PW - MARGIN, yy)
        return y - count * spacing - 6

    def numbered_questions(self, p, y, questions, lines_each=2, spacing=24):
        for i, q in enumerate(questions, start=1):
            if y < 90:
                break
            p.set_fill(*self.accent)
            p.text(MARGIN, y, f"{i}.", 11, bold=True)
            p.set_fill(*INK)
            endy = p.wrap_text(MARGIN + 20, y, q, 11, CW - 20, leading=15)
            y = endy - 8
            y = self.write_lines(p, y, lines_each, spacing=spacing, indent=20)
            y -= 8
        return y

    def checklist(self, p, y, items):
        for it in items:
            if y < 70:
                break
            p.set_stroke(*self.accent); p.set_line_width(1.1)
            p.rect(MARGIN, y - 9, 11, 11, fill=False, stroke=True)
            p.set_fill(*INK)
            endy = p.wrap_text(MARGIN + 22, y, it, 11, CW - 22, leading=15)
            y = min(endy, y - 12) - 8
        return y

    def scale_row(self, p, y, label):
        p.set_fill(*INK)
        p.wrap_text(MARGIN, y, label, 10.5, CW - 150, leading=14)
        # 1..5 bubbles on the right
        bx = PW - MARGIN - 140
        for k in range(5):
            cx = bx + k * 28
            p.set_stroke(*self.accent); p.set_line_width(1)
            p.circle(cx, y - 3, 8, fill=False, stroke=True)
            p.set_fill(*GRAY)
            p.text_center(cx, y - 6.5, str(k + 1), 8)
        return y - 30

    def _wrap_count(self, s, size, width, bold=False):
        words = s.split(); lines = 0; cur = ""
        for w in words:
            trial = (cur + " " + w).strip()
            if pdfkit.text_width(trial, size, bold=bold) <= width or not cur:
                cur = trial
            else:
                lines += 1; cur = w
        if cur:
            lines += 1
        return max(lines, 1)

    # ---------------- front matter ----------------
    def cover(self):
        p, _ = self.doc.add_page(), None
        self._pageno += 1
        # full-bleed accent
        p.set_fill(*self.accent); p.rect(0, 0, PW, PH, fill=True, stroke=False)
        # bottom deep band
        p.set_fill(*self._darker(self.accent, 0.6)); p.rect(0, 0, PW, 150, fill=True, stroke=False)
        # top hairline motif
        p.set_stroke(*self.accent2); p.set_line_width(2)
        for i in range(6):
            yy = PH - 70 - i * 8
            p.line(MARGIN, yy, MARGIN + 90 + i * 6, yy)
        # series
        p.set_fill(*self.accent2)
        p.text(MARGIN, PH - 120, self.series.upper(), 11, bold=True)
        # title
        p.set_fill(1, 1, 1)
        endy = p.wrap_text(MARGIN, PH - 170, self.title, 34, CW, bold=True, leading=38)
        # rule
        p.set_fill(*self.accent2)
        p.rect(MARGIN, endy - 6, 120, 3, fill=True, stroke=False)
        # subtitle
        p.set_fill(0.90, 0.92, 0.96)
        suby = p.wrap_text(MARGIN, endy - 32, self.subtitle, 14, CW - 40, leading=20)
        # writer byline
        p.set_fill(*self.accent2)
        p.text(MARGIN, suby - 6, "Written by " + self.writer, 13, bold=True)
        # central line-art emblem: open book + cross
        self._emblem(p, PW / 2, PH / 2 - 60, 120)
        # age badge
        p.set_fill(*self.accent2)
        p.round_rect(MARGIN, 100, 210, 40, 8, fill=True, stroke=False)
        p.set_fill(*self._darker(self.accent, 0.5))
        p.text(MARGIN + 18, 113, self.ages + "  •  Homeschool & Youth Groups", 11, bold=True)
        # footer tag
        p.set_fill(0.85, 0.88, 0.92)
        p.text(MARGIN, 66, "Personal Study  •  Small Groups  •  Reproducible for one household or class", 9)
        return p

    def _emblem(self, p, cx, cy, w):
        # open book
        p.set_stroke(1, 1, 1); p.set_line_width(2)
        p.line(cx, cy - w * 0.28, cx, cy + w * 0.28)
        p.polygon([(cx, cy + w * 0.28), (cx - w * 0.62, cy + w * 0.14),
                   (cx - w * 0.62, cy - w * 0.34), (cx, cy - w * 0.20)], fill=False, stroke=True)
        p.polygon([(cx, cy + w * 0.28), (cx + w * 0.62, cy + w * 0.14),
                   (cx + w * 0.62, cy - w * 0.34), (cx, cy - w * 0.20)], fill=False, stroke=True)
        # page lines
        for i in range(3):
            yy = cy + w * 0.05 - i * w * 0.10
            p.line(cx - w * 0.50, yy, cx - w * 0.10, yy + w * 0.03)
            p.line(cx + w * 0.10, yy + w * 0.03, cx + w * 0.50, yy)
        # cross rising above
        p.set_fill(*self.accent2)
        p.rect(cx - 4, cy + w * 0.30, 8, w * 0.42, fill=True, stroke=False)
        p.rect(cx - 18, cy + w * 0.52, 36, 8, fill=True, stroke=False)

    def _darker(self, c, f):
        return (c[0] * f, c[1] * f, c[2] * f)

    def how_to_use(self, intro, verse, ref, tips):
        p, y, n = self.page("Introduction", "How to Use This Study", "Getting the Most From This Workbook")
        y = self.paragraph(p, y, intro)
        y = self.scripture_block(p, y, verse, ref)
        y = self.subhead(p, y, "A Few Suggestions")
        y = self.checklist(p, y, tips)
        return p

    def contents_page(self):
        p, y, n = self.page("Contents", "Table of Contents", "What's Inside")
        for i, t in enumerate(self.toc, start=1):
            if y < 70:
                break
            p.set_fill(*self.accent)
            p.text(MARGIN, y, f"{i:>2}", 10.5, bold=True)
            p.set_fill(*INK)
            p.text(MARGIN + 26, y, t[0], 11, bold=(t[1] == 'unit'))
            y -= 20
        return p

    def unit_divider(self, unit_no, unit_title, theme_verse, ref, overview):
        p, n = self.doc.add_page(), None
        self._pageno += 1
        p.set_fill(*self.accent); p.rect(0, PH - 300, PW, 300, fill=True, stroke=False)
        p.set_fill(*self.accent2); p.rect(0, PH - 306, PW, 6, fill=True, stroke=False)
        p.set_fill(*self.accent2)
        p.text(MARGIN, PH - 120, f"UNIT {unit_no}", 14, bold=True)
        p.set_fill(1, 1, 1)
        p.wrap_text(MARGIN, PH - 150, unit_title, 26, CW, bold=True, leading=30)
        p.set_fill(0.9, 0.92, 0.96)
        p.wrap_text(MARGIN, PH - 220, '"' + theme_verse + '"  — ' + ref, 12.5, CW - 30, leading=18)
        # overview below band
        p.set_fill(*INK)
        y = PH - 340
        y = self.subhead(p, y, "Unit Overview")
        self.paragraph(p, y, overview)
        self._footer(p, self._pageno)
        return p


# ---------- higher-level composite study pages ----------
def devotional(wb, section, title, opener, verse, ref, body_paras, reflect_qs, prayer_prompt):
    p, y, n = wb.page(section, "Devotional", title)
    y = wb.paragraph(p, y, opener, size=11)
    y = wb.scripture_block(p, y, verse, ref)
    for para in body_paras:
        y = wb.paragraph(p, y, para)
    y = wb.subhead(p, y, "Reflect")
    y = wb.numbered_questions(p, y, reflect_qs, lines_each=2)
    if y > 110:
        y = wb.callout(p, y, "Prayer Prompt", prayer_prompt)
    return p


def inductive_study(wb, section, title, passage_ref, passage_text, observe_qs, interpret_qs, apply_qs):
    # Page A: passage + observe
    p, y, n = wb.page(section, "Inductive Bible Study — Observe", title)
    y = wb.paragraph(p, y, "Read the passage slowly, more than once. First notice what it actually says before deciding what it means.", size=10.5, color=GRAY)
    y = wb.scripture_block(p, y, passage_text, passage_ref)
    y = wb.subhead(p, y, "Observation — What does it say?")
    wb.numbered_questions(p, y, observe_qs, lines_each=2)
    # Page B: interpret + apply
    p2, y2, n2 = wb.page(section, "Inductive Bible Study — Interpret & Apply", title)
    y2 = wb.subhead(p2, y2, "Interpretation — What does it mean?")
    y2 = wb.numbered_questions(p2, y2, interpret_qs, lines_each=2)
    y2 = wb.subhead(p2, y2, "Application — What will I do?")
    wb.numbered_questions(p2, y2, apply_qs, lines_each=2)
    return p2


def word_study(wb, section, term, definition, verses, questions):
    p, y, n = wb.page(section, "Word Study", term)
    y = wb.callout(p, y, "Meaning", definition)
    y = wb.subhead(p, y, "Where It Appears")
    for (v, r) in verses:
        y = wb.scripture_block(p, y, v, r)
        if y < 150:
            break
    if y > 130:
        y = wb.subhead(p, y, "Dig Deeper")
        wb.numbered_questions(p, y, questions, lines_each=2)
    return p


def worldview(wb, section, title, question, perspectives, prompts):
    p, y, n = wb.page(section, "Faith & Worldview", title)
    y = wb.callout(p, y, "The Question", question)
    y = wb.subhead(p, y, "Think It Through")
    for label, text in perspectives:
        p.set_fill(*wb.accent)
        p.text(MARGIN, y, label, 11, bold=True)
        y = wb.paragraph(p, y - 16, text, size=10.5)
    y = wb.subhead(p, y, "Your Response")
    wb.numbered_questions(p, y, prompts, lines_each=3)
    return p


def memory_study(wb, section, verse, ref, context, why, application):
    p, y, n = wb.page(section, "Memory & Meditation", "Hide This Word in Your Heart")
    y = wb.scripture_block(p, y, verse, ref)
    y = wb.subhead(p, y, "Context")
    y = wb.paragraph(p, y, context, size=10.5)
    y = wb.subhead(p, y, "Why It Matters")
    y = wb.paragraph(p, y, why, size=10.5)
    y = wb.subhead(p, y, "Write It From Memory")
    y = wb.write_lines(p, y, 3, spacing=26)
    if y > 120:
        y = wb.callout(p, y, "Live It Out This Week", application)
    return p


def journal_page(wb, section, title, prompts, lines_after=0):
    p, y, n = wb.page(section, "Reflection & Journal", title)
    for pr in prompts:
        if y < 110:
            break
        p.set_fill(*wb.accent2)
        p.rect(MARGIN, y - 2, 16, 3, fill=True, stroke=False)
        p.set_fill(*INK)
        endy = p.wrap_text(MARGIN, y - 16, pr, 11.5, CW, bold=True, leading=15)
        y = endy - 8
        y = wb.write_lines(p, y, 3, spacing=26)
        y -= 10
    if lines_after and y > 90:
        y = wb.write_lines(p, y, lines_after, spacing=26)
    return p


def discussion_page(wb, section, title, intro, questions):
    p, y, n = wb.page(section, "Small Group Discussion", title)
    y = wb.paragraph(p, y, intro, size=10.5, color=GRAY)
    wb.numbered_questions(p, y, questions, lines_each=2)
    return p


def self_assessment(wb, section, title, intro, statements):
    p, y, n = wb.page(section, "Self-Assessment", title)
    y = wb.paragraph(p, y, intro, size=10.5, color=GRAY)
    # scale legend
    p.set_fill(*GRAY)
    p.text_right(PW - MARGIN, y, "1 = rarely      5 = consistently", 9)
    y -= 18
    for s in statements:
        if y < 80:
            break
        y = wb.scale_row(p, y, s)
    return p


def challenge_page(wb, section, title, intro, challenges):
    p, y, n = wb.page(section, "Application Challenge", title)
    y = wb.paragraph(p, y, intro, size=11)
    y = wb.subhead(p, y, "This Week's Challenges")
    y = wb.checklist(p, y, challenges)
    if y > 120:
        y = wb.subhead(p, y, "What happened when you tried?")
        wb.write_lines(p, y, 4, spacing=26)
    return p


def notes_page(wb, section, title="Study Notes"):
    p, y, n = wb.page(section, "Notes", title)
    wb.write_lines(p, y, 22, spacing=26)
    return p
