"""
workbook_story.py — Illustrated social-story + activity engine for young kids.
Dependency-free (uses pdfkit.py).

A "social story" gently walks a child through a situation and models calm,
kind choices. This engine provides:
  - a warm cover, for-grown-ups note, contents
  - STORY SPREAD pages: a big framed line-art illustration + 1-3 short
    narration sentences (large, readable text)
  - format components: calming cards, feelings workbook pages, role-play
    cards, matching game, scenario cards, breathing cards, conversation
    cards, calm-down toolkit, tracing, coloring, journaling, certificate

All builders take a StoryBook instance `wb` and append pages.
"""

import math
import pdfkit

# palette
INK = (0.13, 0.14, 0.17)
SLATE = (0.29, 0.32, 0.39)
GRAY = (0.47, 0.50, 0.56)
RULE = (0.80, 0.82, 0.87)
TRACE = (0.80, 0.82, 0.88)
CARD = (0.955, 0.965, 0.98)
SOFT = (0.93, 0.96, 0.97)

# accents
TEAL = (0.11, 0.60, 0.60);   SUN = (0.98, 0.78, 0.25)
CORAL = (0.95, 0.45, 0.42);  SKY = (0.36, 0.66, 0.86)
PURPLE = (0.55, 0.40, 0.72); MINT = (0.42, 0.76, 0.58)
BLUE = (0.24, 0.46, 0.78);   PEACH = (0.98, 0.66, 0.44)
GREEN = (0.30, 0.66, 0.40);  LAVEN = (0.66, 0.58, 0.85)
ROSE = (0.90, 0.44, 0.58);   AQUA = (0.30, 0.72, 0.74)
ORANGE = (0.95, 0.55, 0.22); INDIGO = (0.32, 0.34, 0.62)
GOLD = (0.92, 0.72, 0.20);   BERRY = (0.72, 0.26, 0.45)

PW, PH = pdfkit.LETTER
MARGIN = 56.0
CW = PW - 2 * MARGIN


class StoryBook:
    def __init__(self, title, subtitle, ages, fmt,
                 accent=TEAL, accent2=SUN, writer="Daniel Tesfamariam",
                 series="Little Feelings Social Stories"):
        self.writer = writer
        self.doc = pdfkit.Document(title=title, author=writer)
        self.title = title
        self.subtitle = subtitle
        self.ages = ages
        self.fmt = fmt
        self.accent = accent
        self.accent2 = accent2
        self.series = series
        self.toc = []
        self._pageno = 0

    def save(self, path):
        return self.doc.save(path)

    # ---------- chrome ----------
    def _new(self):
        self._pageno += 1
        return self.doc.add_page(), self._pageno

    def _footer(self, p, n):
        p.set_stroke(*RULE); p.set_line_width(0.6)
        p.line(MARGIN, 40, PW - MARGIN, 40)
        p.set_fill(*GRAY)
        p.text(MARGIN, 28, self.title, 7.5)
        p.text_right(PW - MARGIN, 28, str(n), 8, bold=True)

    def _header(self, p, kicker, heading):
        p.set_fill(*self.accent)
        p.round_rect(MARGIN - 10, PH - 92, CW + 20, 70, 14, fill=True, stroke=False)
        p.set_fill(1, 1, 1)
        p.text(MARGIN + 8, PH - 42, kicker.upper(), 10, bold=True)
        p.text(MARGIN + 8, PH - 70, heading, 19, bold=True)

    def page(self, kicker, heading):
        p, n = self._new()
        self._header(p, kicker, heading)
        self._footer(p, n)
        return p, PH - 116, n

    # ---------- simple people / face art ----------
    def face(self, p, cx, cy, r, mood="happy", color=None):
        p.set_stroke(*INK); p.set_line_width(1.6)
        if color:
            p.set_fill(*color); p.circle(cx, cy, r, fill=True, stroke=True)
        else:
            p.circle(cx, cy, r, fill=False, stroke=True)
        p.set_fill(*INK)
        ex = r * 0.34
        if mood == "angry":
            p.line(cx - ex - 5, cy + r*0.42, cx - ex + 6, cy + r*0.28)
            p.line(cx + ex + 5, cy + r*0.42, cx + ex - 6, cy + r*0.28)
        p.circle(cx - ex, cy + r*0.12, r*0.09, fill=True, stroke=False)
        p.circle(cx + ex, cy + r*0.12, r*0.09, fill=True, stroke=False)
        p.set_stroke(*INK); p.set_line_width(1.6)
        if mood == "happy":
            self._arc(p, cx, cy - r*0.10, r*0.48, 200, 340)
        elif mood == "sad":
            self._arc(p, cx, cy - r*0.55, r*0.48, 20, 160)
        elif mood == "angry":
            self._arc(p, cx, cy - r*0.55, r*0.42, 20, 160)
        elif mood == "calm":
            p.line(cx - r*0.4, cy - r*0.28, cx + r*0.4, cy - r*0.28)
        elif mood == "worried":
            self._wavy(p, cx - r*0.4, cy - r*0.32, r*0.8, r*0.12)
        elif mood == "surprised":
            p.circle(cx, cy - r*0.32, r*0.18, fill=False, stroke=True)
        elif mood == "excited":
            self._arc(p, cx, cy - r*0.12, r*0.5, 200, 340)

    def kid(self, p, cx, cy, s, mood="happy", color=None):
        """A simple full-body child figure, height ~ 3.2*s."""
        # head
        self.face(p, cx, cy + s*1.4, s*0.7, mood, color=color)
        p.set_stroke(*INK); p.set_line_width(1.6)
        # body
        p.round_rect(cx - s*0.7, cy - s*0.9, s*1.4, s*1.6, s*0.4, fill=False, stroke=True)
        # arms
        p.line(cx - s*0.7, cy + s*0.4, cx - s*1.3, cy - s*0.1)
        p.line(cx + s*0.7, cy + s*0.4, cx + s*1.3, cy - s*0.1)
        # legs
        p.line(cx - s*0.3, cy - s*0.9, cx - s*0.4, cy - s*1.9)
        p.line(cx + s*0.3, cy - s*0.9, cx + s*0.4, cy - s*1.9)

    def _arc(self, p, cx, cy, r, a0, a1, steps=16):
        pts = []
        for i in range(steps + 1):
            a = math.radians(a0 + (a1 - a0) * i / steps)
            pts.append((cx + r*math.cos(a), cy + r*math.sin(a)))
        p.polygon(pts, fill=False, stroke=True, close=False)

    def _wavy(self, p, x, y, w, amp, waves=3, steps=24):
        pts = []
        for i in range(steps + 1):
            t = i/steps
            pts.append((x + w*t, y + amp*math.sin(t*waves*math.pi)))
        p.polygon(pts, fill=False, stroke=True, close=False)

    def _star(self, p, cx, cy, r, fill=False):
        p.star(cx, cy, r, points=5, fill=fill, stroke=True)

    def _sun(self, p, cx, cy, r):
        for i in range(12):
            a = i*math.pi/6
            p.line(cx + r*1.3*math.cos(a), cy + r*1.3*math.sin(a),
                   cx + r*1.7*math.cos(a), cy + r*1.7*math.sin(a))
        p.circle(cx, cy, r, fill=False, stroke=True)

    # ---------- reusable blocks ----------
    def intro_box(self, p, y, text):
        lines = _wrapn(text, 11, CW - 36)
        h = 24 + lines*15 + 12
        p.set_fill(*SOFT); p.round_rect(MARGIN, y - h, CW, h, 10, fill=True, stroke=False)
        p.set_fill(*self.accent); p.rect(MARGIN, y - h, 5, h, fill=True, stroke=False)
        p.set_fill(*SLATE); p.wrap_text(MARGIN + 18, y - 20, text, 11, CW - 34, leading=15)
        return y - h - 12

    def instruction(self, p, y, text):
        p.set_fill(*self.accent2); p.round_rect(MARGIN, y - 30, CW, 30, 8, fill=True, stroke=False)
        p.set_fill(*INK); p.text(MARGIN + 14, y - 20, text, 11.5, bold=True)
        return y - 44

    def subhead(self, p, y, text):
        p.set_fill(*self.accent); p.text(MARGIN, y, text, 13, bold=True)
        p.set_stroke(*self.accent2); p.set_line_width(2)
        p.line(MARGIN, y - 6, MARGIN + 46, y - 6)
        return y - 22

    def paragraph(self, p, y, text, size=11, color=INK, gap=8, bold=False):
        p.set_fill(*color)
        endy = p.wrap_text(MARGIN, y, text, size, CW, leading=size*1.4, bold=bold)
        return endy - gap

    def write_lines(self, p, y, count, spacing=26, indent=0):
        for i in range(count):
            yy = y - i*spacing
            if yy < 54:
                break
            p.set_stroke(*RULE); p.set_line_width(0.7)
            p.line(MARGIN + indent, yy, PW - MARGIN, yy)
        return y - count*spacing - 6

    def checklist(self, p, y, items, box=True):
        for it in items:
            if y < 58:
                break
            p.set_stroke(*self.accent); p.set_line_width(1.2)
            if box:
                p.rect(MARGIN, y - 10, 12, 12, fill=False, stroke=True)
            else:
                p.circle(MARGIN + 6, y - 4, 6, fill=False, stroke=True)
            p.set_fill(*INK)
            endy = p.wrap_text(MARGIN + 24, y, it, 11, CW - 24, leading=15)
            y = min(endy, y - 12) - 8
        return y

    def draw_box(self, p, y, label, height):
        p.set_fill(*self.accent); p.text(MARGIN, y, label, 11.5, bold=True)
        p.set_stroke(*RULE); p.set_line_width(1.2)
        p.round_rect(MARGIN, y - 12 - height, CW, height, 10, fill=False, stroke=True)
        return y - 12 - height - 12

    # ---------- front matter ----------
    def cover(self):
        p, _ = self.doc.add_page(), None
        self._pageno += 1
        p.set_fill(*self.accent); p.rect(0, 0, PW, PH, fill=True, stroke=False)
        p.set_fill(1, 1, 1); p.round_rect(40, 150, PW - 80, PH - 320, 22, fill=True, stroke=False)
        # sky
        p.set_stroke(1, 1, 1); p.set_line_width(2)
        self._sun(p, 118, PH - 92, 24)
        # series
        p.set_fill(1, 1, 1)
        p.text_center(PW/2, PH - 128, self.series.upper(), 11, bold=True)
        # scene: two kids
        p.set_stroke(*INK)
        self.kid(p, PW/2 - 70, PH - 300, 30, "happy", color=self.accent2)
        self.kid(p, PW/2 + 70, PH - 300, 30, "calm", color=SKY)
        # ground line
        p.set_stroke(*INK); p.set_line_width(1.4)
        p.line(110, PH - 360, PW - 110, PH - 360)
        # title
        p.set_fill(*self.accent)
        endy = p.wrap_text(0, PH - 400, self.title, 29, PW - 150, bold=True, center_x=PW/2, leading=33)
        p.set_fill(*SLATE)
        endy = p.wrap_text(0, endy - 14, self.subtitle, 13.5, PW - 190, center_x=PW/2, leading=18)
        p.set_fill(*self.accent)
        p.text_center(PW/2, endy - 8, "Written by " + self.writer, 13, bold=True)
        # badges
        p.set_fill(*self.accent2); p.round_rect(PW/2 - 150, 176, 300, 38, 12, fill=True, stroke=False)
        p.set_fill(*INK); p.text_center(PW/2, 188, self.ages + "   -   " + self.fmt, 11.5, bold=True)
        p.set_fill(1, 1, 1)
        p.text_center(PW/2, 116, "A read-aloud social story with activities", 11, bold=True)
        p.text_center(PW/2, 98, "Home  -  Classroom  -  Counseling", 9)
        return p

    def for_grownups(self, what_it_helps, how_to_use):
        p, y, n = self.page("For Grown-Ups", "How to Share This Book")
        y = self.paragraph(p, y, "Social stories gently walk a child through a situation and model calm, kind "
                                 "choices. Read this book together, more than once. The repetition is what "
                                 "helps - it lets a child rehearse the feelings and choices before the real "
                                 "moment happens.")
        y = self.intro_box(p, y, what_it_helps)
        y = self.subhead(p, y, "How to use it")
        y = self.checklist(p, y, how_to_use, box=False)
        return p

    def contents(self):
        p, y, n = self.page("Contents", "What's Inside")
        for i, t in enumerate(self.toc, start=1):
            if y < 58:
                break
            p.set_fill(*self.accent); p.circle(MARGIN + 8, y + 4, 9, fill=True, stroke=False)
            p.set_fill(1, 1, 1); p.text_center(MARGIN + 8, y + 0.5, str(i), 9, bold=True)
            p.set_fill(*INK); p.text(MARGIN + 26, y, t, 11.5)
            y -= 24
        return p

    def section(self, title, subtitle, mood="happy", color=None):
        p, _ = self.doc.add_page(), None
        self._pageno += 1
        col = color or self.accent
        p.set_fill(*col); p.rect(0, 0, PW, PH, fill=True, stroke=False)
        p.set_fill(1, 1, 1); p.round_rect(50, PH/2 - 150, PW - 100, 300, 22, fill=True, stroke=False)
        self.face(p, PW/2, PH/2 + 66, 44, mood, color=self.accent2)
        p.set_fill(*col)
        p.wrap_text(0, PH/2 - 6, title, 25, PW - 160, bold=True, center_x=PW/2, leading=29)
        p.set_fill(*SLATE)
        p.wrap_text(0, PH/2 - 66, subtitle, 13, PW - 200, center_x=PW/2, leading=18)
        self._footer(p, self._pageno)
        return p

    # ---------- STORY SPREAD ----------
    def story(self, illustration, sentences, page_label="Story"):
        """One story page: framed illustration on top, big narration below."""
        p, n = self._new()
        self._footer(p, n)
        # illustration frame (upper ~55%)
        fx, fy, fw, fh = MARGIN, PH - 430, CW, 360
        p.set_fill(0.985, 0.99, 1.0)
        p.round_rect(fx, fy, fw, fh, 16, fill=True, stroke=False)
        p.set_stroke(*self.accent); p.set_line_width(2)
        p.round_rect(fx, fy, fw, fh, 16, fill=False, stroke=True)
        p.set_stroke(*INK); p.set_line_width(1.8)
        illustration(self, p, fx + fw/2, fy + fh/2)
        # narration text box below
        ty = fy - 40
        p.set_fill(*INK)
        for sent in sentences:
            ty = p.wrap_text(MARGIN + 6, ty, sent, 17, CW - 12, leading=25, bold=False)
            ty -= 14
        return p


def _wrapn(s, size, width, bold=False):
    words = s.split(); lines = 1; cur = ""
    for w in words:
        trial = (cur + " " + w).strip()
        if pdfkit.text_width(trial, size, bold=bold) <= width or not cur:
            cur = trial
        else:
            lines += 1; cur = w
    return lines


# =====================================================================
# Format components (activities)
# =====================================================================
def cards_page(wb, kicker, heading, intro, cards, cols=2, cardh=96):
    """Generic printable 'cards' grid: list of (title, text)."""
    p, y, n = wb.page(kicker, heading)
    y = wb.intro_box(p, y, intro)
    cardw = (CW - 16) / cols
    top = y - 2
    for i, (t, d) in enumerate(cards):
        col = i % cols; row = i // cols
        cx = MARGIN + col*(cardw + 16)
        cy = top - row*(cardh + 12)
        if cy - cardh < 60:
            break
        p.set_fill(*CARD); p.round_rect(cx, cy - cardh, cardw, cardh, 12, fill=True, stroke=False)
        p.set_stroke(*wb.accent); p.set_line_width(1.4)
        # dashed cut border feel
        p.round_rect(cx, cy - cardh, cardw, cardh, 12, fill=False, stroke=True)
        p.set_fill(*wb.accent); p.circle(cx + 20, cy - 20, 11, fill=True, stroke=False)
        p.set_fill(1, 1, 1); p.text_center(cx + 20, cy - 24, str(i + 1), 10, bold=True)
        p.set_fill(*INK); p.text(cx + 38, cy - 24, t, 11.5, bold=True)
        p.set_fill(*SLATE); p.wrap_text(cx + 14, cy - 44, d, 9.6, cardw - 26, leading=12.5)
    return p


def feelings_faces(wb, kicker, heading, moods_labels, instruction="Color each face. Say the feeling out loud."):
    p, y, n = wb.page(kicker, heading)
    y = wb.instruction(p, y, instruction)
    cols = 3
    cellw = CW / cols
    r = 34
    i = 0
    row_y = y - 20
    for (mood, label) in moods_labels:
        col = i % cols
        if col == 0 and i != 0:
            row_y -= 128
        cx = MARGIN + cellw*col + cellw/2
        if row_y - 128 < 58:
            break
        wb.face(p, cx, row_y - 34, r, mood)
        p.set_fill(*INK); p.text_center(cx, row_y - 92, label, 11, bold=True)
        p.set_stroke(*RULE); p.set_line_width(0.7)
        p.line(cx - 40, row_y - 104, cx + 40, row_y - 104)
        i += 1
    return p


def breathing_card(wb, name, steps, shape="square"):
    p, y, n = wb.page("Calm Breathing", name)
    y = wb.intro_box(p, y, "Trace the shape slowly with your finger while you breathe. Do it a few times until "
                           "your body feels calmer.")
    cx, cy = PW/2, y - 140
    p.set_stroke(*wb.accent); p.set_line_width(2.4)
    if shape == "square":
        s = 100; p.rect(cx - s, cy - s, 2*s, 2*s, fill=False, stroke=True)
    elif shape == "triangle":
        s = 110; p.polygon([(cx, cy + s), (cx - s, cy - s*0.7), (cx + s, cy - s*0.7)], fill=False, stroke=True)
    elif shape == "star":
        wb._star(p, cx, cy, 120)
    elif shape == "flower":
        for i in range(6):
            a = i*math.pi/3
            p.circle(cx + 58*math.cos(a), cy + 58*math.sin(a), 40, fill=False, stroke=True)
    y = cy - 160
    for i, st in enumerate(steps, 1):
        p.set_fill(*wb.accent); p.text(MARGIN, y, f"{i}.", 11, bold=True)
        p.set_fill(*INK); endy = p.wrap_text(MARGIN + 18, y, st, 11, CW - 18, leading=15)
        y = endy - 8
        if y < 66:
            break
    return p


def matching(wb, kicker, heading, left, right, instruction):
    p, y, n = wb.page(kicker, heading)
    y = wb.instruction(p, y, instruction)
    import random
    nrows = min(len(left), len(right))
    top = y - 10
    row_h = (top - 84) / max(nrows, 1)
    rr = list(right); random.Random(len(heading)).shuffle(rr)
    for i in range(nrows):
        ly = top - i*row_h
        p.set_fill(*wb.accent); p.circle(MARGIN + 8, ly, 5, fill=True, stroke=False)
        p.set_fill(*INK); p.text(MARGIN + 22, ly - 4, left[i], 12)
        tw = pdfkit.text_width(rr[i], 12)
        p.text(PW - MARGIN - 22 - tw, ly - 4, rr[i], 12)
        p.set_fill(*wb.accent2); p.circle(PW - MARGIN - 8, ly, 5, fill=True, stroke=False)
    return p


def scenario_page(wb, kicker, heading, scenarios):
    p, y, n = wb.page(kicker, heading)
    y = wb.intro_box(p, y, "Read each situation together. There are many good choices! Talk it through, then write "
                           "or draw what you could do.")
    for i, s in enumerate(scenarios, 1):
        if y < 118:
            break
        p.set_fill(*wb.accent); p.circle(MARGIN + 9, y + 3, 10, fill=True, stroke=False)
        p.set_fill(1, 1, 1); p.text_center(MARGIN + 9, y - 0.5, str(i), 10, bold=True)
        p.set_fill(*INK)
        endy = p.wrap_text(MARGIN + 28, y, s, 11.5, CW - 28, leading=15, bold=True)
        y = endy - 6
        p.set_fill(*GRAY); p.text(MARGIN + 28, y, "What could you do?", 9.5, italic=True)
        y = wb.write_lines(p, y - 8, 2, spacing=24, indent=28)
        y -= 10
    return p


def tracing_page(wb, kicker, heading, phrases, instruction="Trace the words. Then say them out loud."):
    p, y, n = wb.page(kicker, heading)
    y = wb.instruction(p, y, instruction)
    for ph in phrases:
        p.set_fill(*TRACE); p.text(MARGIN, y - 22, ph, 22, bold=True)
        p.set_stroke(*RULE); p.set_line_width(0.8)
        p.line(MARGIN, y - 30, PW - MARGIN, y - 30)
        y -= 56
        if y < 84:
            break
    return p


def coloring_page(wb, kicker, heading, caption, scene):
    p, y, n = wb.page(kicker, heading)
    p.set_fill(*INK); p.text_center(PW/2, y, caption, 12, bold=True)
    fy = 78
    fh = y - 28 - fy
    p.set_stroke(*wb.accent); p.set_line_width(2)
    p.round_rect(MARGIN, fy, CW, fh, 14, fill=False, stroke=True)
    p.set_stroke(*INK); p.set_line_width(1.6)
    scene(wb, p, PW/2, fy + fh/2)
    p.set_fill(*GRAY); p.text_center(PW/2, 62, "Color it in with colors that feel calm and happy.", 9)
    return p


def journal_page(wb, kicker, heading, prompts, box_label=None, box_h=0):
    p, y, n = wb.page(kicker, heading)
    for pr in prompts:
        if y < 100:
            break
        p.set_fill(*wb.accent2); p.circle(MARGIN + 5, y + 3, 5, fill=True, stroke=False)
        p.set_fill(*INK)
        endy = p.wrap_text(MARGIN + 18, y, pr, 11.5, CW - 18, bold=True, leading=15)
        y = wb.write_lines(p, endy - 6, 3, spacing=26)
        y -= 10
    if box_label and y > box_h + 66:
        wb.draw_box(p, y, box_label, box_h)
    return p


def checklist_page(wb, kicker, heading, intro, items):
    p, y, n = wb.page(kicker, heading)
    y = wb.intro_box(p, y, intro)
    wb.checklist(p, y, items, box=True)
    return p


def toolkit_page(wb, kicker="My Toolkit", heading="My Calm-Down Toolkit"):
    p, y, n = wb.page(kicker, heading)
    y = wb.intro_box(p, y, "Out of all the tools in this book, which ones help YOU most? Draw or write your top "
                           "tools here so you remember them when a big feeling comes.")
    for i in range(1, 6):
        p.set_fill(*wb.accent); p.circle(MARGIN + 9, y + 3, 10, fill=True, stroke=False)
        p.set_fill(1, 1, 1); p.text_center(MARGIN + 9, y - 0.5, str(i), 10, bold=True)
        p.set_stroke(*RULE); p.set_line_width(0.7)
        p.line(MARGIN + 28, y - 3, PW - MARGIN, y - 3)
        y -= 32
    return p


def certificate(wb, name_line, accomplishment):
    p, n = wb._new()
    wb._footer(p, n)
    p.set_stroke(*wb.accent); p.set_line_width(3)
    p.round_rect(MARGIN, 120, CW, PH - 260, 18, fill=False, stroke=True)
    p.set_stroke(*wb.accent2); p.set_line_width(1.4)
    p.round_rect(MARGIN + 12, 132, CW - 24, PH - 284, 14, fill=False, stroke=True)
    wb._star(p, PW/2, PH - 190, 40)
    p.set_fill(*wb.accent)
    p.text_center(PW/2, PH - 250, "CERTIFICATE", 28, bold=True)
    p.set_fill(*INK)
    p.text_center(PW/2, PH - 285, "This certificate is proudly given to", 13)
    p.set_stroke(*RULE); p.set_line_width(0.8)
    p.line(PW/2 - 150, PH - 330, PW/2 + 150, PH - 330)
    p.set_fill(*GRAY); p.text_center(PW/2, PH - 345, "(write your name)", 9)
    p.set_fill(*INK)
    p.wrap_text(0, PH - 385, accomplishment, 14, CW - 60, center_x=PW/2, leading=20)
    p.set_stroke(*RULE); p.set_line_width(0.8)
    p.line(MARGIN + 60, 200, MARGIN + 220, 200)
    p.line(PW - MARGIN - 220, 200, PW - MARGIN - 60, 200)
    p.set_fill(*GRAY)
    p.text_center(MARGIN + 140, 186, "Grown-up", 9)
    p.text_center(PW - MARGIN - 140, 186, "Date", 9)
    return p


# =====================================================================
# Coloring / illustration scenes (black line art)
# =====================================================================
def scene_calm_place(wb, p, cx, cy):
    wb._sun(p, cx - 120, cy + 70, 24)
    for wy in (cy - 40, cy - 70):
        pts = []
        for xx in range(int(cx - 150), int(cx + 151), 20):
            pts.append((xx, wy + (7 if (xx//20) % 2 == 0 else -7)))
        p.polygon(pts, fill=False, stroke=True, close=False)
    p.star(cx + 90, cy - 5, 20, points=5, fill=False, stroke=True)


def scene_two_friends(wb, p, cx, cy):
    wb.kid(p, cx - 55, cy - 10, 26, "happy")
    wb.kid(p, cx + 55, cy - 10, 26, "happy")
    p.set_stroke(wb.accent[0], wb.accent[1], wb.accent[2]); p.set_line_width(1.6)
    p.heart(cx, cy + 70, 18, fill=False, stroke=True)
    p.set_stroke(*INK)
    p.line(cx - 150, cy - 78, cx + 150, cy - 78)


def scene_heart(wb, p, cx, cy):
    p.heart(cx, cy, 70, fill=False, stroke=True)


def scene_star(wb, p, cx, cy):
    wb._star(p, cx, cy, 90)
