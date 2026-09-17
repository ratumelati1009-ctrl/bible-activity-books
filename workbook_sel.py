"""
workbook_sel.py — Social-Emotional Learning (SEL) / emotional-regulation
activity-book engine for ages 5-17. Dependency-free (uses pdfkit.py).

Designed to scale across a wide age range: every book mixes
 - simple activities for younger kids (coloring, tracing, feelings faces,
   matching, breathing shapes), and
 - deeper activities for older kids/teens (journaling, scenario
   problem-solving, coping-plan building, self-reflection, thermometers).

Public helper: SELBook(...) plus composite page builders at the bottom.
"""

import math
import pdfkit

# ---- warm SEL palette ----
INK = (0.13, 0.14, 0.17)
SLATE = (0.28, 0.31, 0.38)
GRAY = (0.46, 0.49, 0.55)
FAINT = (0.72, 0.74, 0.80)
RULE = (0.80, 0.82, 0.87)
TRACE = (0.80, 0.82, 0.88)

# accent schemes
TEAL = (0.11, 0.60, 0.60);    SUN = (0.98, 0.78, 0.25)
CORAL = (0.95, 0.45, 0.42);   SKY = (0.36, 0.66, 0.86)
PURPLE = (0.55, 0.40, 0.72);  MINT = (0.42, 0.76, 0.58)
BLUE = (0.24, 0.46, 0.78);    PEACH = (0.98, 0.66, 0.44)
GREEN = (0.30, 0.66, 0.40);   LAVEN = (0.66, 0.58, 0.85)
ROSE = (0.90, 0.44, 0.58);    AQUA = (0.30, 0.72, 0.74)
ORANGE = (0.95, 0.55, 0.22);  INDIGO = (0.32, 0.34, 0.62)
BERRY = (0.72, 0.26, 0.45);   LIME = (0.60, 0.74, 0.28)
OCEAN = (0.10, 0.48, 0.62);   GOLD = (0.92, 0.72, 0.20)

CARD = (0.955, 0.965, 0.98)
SOFT = (0.93, 0.96, 0.97)

PW, PH = pdfkit.LETTER
MARGIN = 56.0
CW = PW - 2 * MARGIN


class SELBook:
    def __init__(self, title, subtitle, ages="Ages 5-17",
                 accent=TEAL, accent2=SUN, writer="Daniel Tesfamariam",
                 series="Calm & Confident SEL Series"):
        self.writer = writer
        self.doc = pdfkit.Document(title=title, author=writer)
        self.title = title
        self.subtitle = subtitle
        self.ages = ages
        self.accent = accent
        self.accent2 = accent2
        self.series = series
        self.toc = []
        self._pageno = 0

    def save(self, path):
        return self.doc.save(path)

    # ---------------- chrome ----------------
    def _new(self):
        self._pageno += 1
        return self.doc.add_page(), self._pageno

    def _footer(self, p, n):
        p.set_stroke(*RULE); p.set_line_width(0.6)
        p.line(MARGIN, 42, PW - MARGIN, 42)
        p.set_fill(*GRAY)
        p.text(MARGIN, 30, self.title, size=7.5)
        p.text_right(PW - MARGIN, 30, str(n), size=8, bold=True)

    def _header(self, p, kicker, heading):
        # rounded top banner
        p.set_fill(*self.accent)
        p.round_rect(MARGIN - 10, PH - 96, CW + 20, 74, 14, fill=True, stroke=False)
        p.set_fill(1, 1, 1)
        p.text(MARGIN + 8, PH - 44, kicker.upper(), 10, bold=True)
        p.text(MARGIN + 8, PH - 74, heading, 20, bold=True)
        # little sun/emblem
        self._mini_face(p, PW - MARGIN - 26, PH - 59, 16, self.accent2, mood="happy")

    def page(self, kicker, heading):
        p, n = self._new()
        self._header(p, kicker, heading)
        self._footer(p, n)
        return p, PH - 118, n

    # ---------------- little drawings ----------------
    def _mini_face(self, p, cx, cy, r, color, mood="happy"):
        p.set_fill(*color)
        p.circle(cx, cy, r, fill=True, stroke=False)
        p.set_fill(*INK)
        p.circle(cx - r * 0.35, cy + r * 0.15, r * 0.11, fill=True, stroke=False)
        p.circle(cx + r * 0.35, cy + r * 0.15, r * 0.11, fill=True, stroke=False)
        p.set_stroke(*INK); p.set_line_width(1.4)
        if mood == "happy":
            self._arc(p, cx, cy - r * 0.05, r * 0.5, 200, 340)
        elif mood == "sad":
            self._arc(p, cx, cy - r * 0.5, r * 0.5, 20, 160)
        elif mood == "angry":
            p.line(cx - r * 0.5, cy - r * 0.35, cx + r * 0.5, cy - r * 0.35)
        elif mood == "calm":
            p.line(cx - r * 0.45, cy - r * 0.25, cx + r * 0.45, cy - r * 0.25)
        elif mood == "worried":
            self._arc(p, cx, cy - r * 0.55, r * 0.45, 20, 160)

    def face(self, p, cx, cy, r, mood, color=None):
        """Outline face (for coloring / feelings charts)."""
        p.set_stroke(*INK); p.set_line_width(1.6)
        if color:
            p.set_fill(*color); p.circle(cx, cy, r, fill=True, stroke=True)
        else:
            p.circle(cx, cy, r, fill=False, stroke=True)
        p.set_fill(*INK)
        ex = r * 0.34
        if mood in ("angry",):
            # angry eyebrows
            p.line(cx - ex - 5, cy + r * 0.42, cx - ex + 6, cy + r * 0.28)
            p.line(cx + ex + 5, cy + r * 0.42, cx + ex - 6, cy + r * 0.28)
        p.circle(cx - ex, cy + r * 0.12, r * 0.09, fill=True, stroke=False)
        p.circle(cx + ex, cy + r * 0.12, r * 0.09, fill=True, stroke=False)
        p.set_stroke(*INK); p.set_line_width(1.6)
        if mood == "happy":
            self._arc(p, cx, cy - r * 0.1, r * 0.48, 200, 340)
        elif mood == "sad":
            self._arc(p, cx, cy - r * 0.55, r * 0.48, 20, 160)
        elif mood == "angry":
            self._arc(p, cx, cy - r * 0.55, r * 0.42, 20, 160)
        elif mood == "calm":
            p.line(cx - r * 0.4, cy - r * 0.28, cx + r * 0.4, cy - r * 0.28)
        elif mood == "worried":
            # wavy mouth
            self._wavy(p, cx - r * 0.4, cy - r * 0.32, r * 0.8, r * 0.12)
        elif mood == "surprised":
            p.circle(cx, cy - r * 0.32, r * 0.18, fill=False, stroke=True)
        elif mood == "excited":
            self._arc(p, cx, cy - r * 0.12, r * 0.5, 200, 340)

    def _arc(self, p, cx, cy, r, a0, a1, steps=16):
        pts = []
        for i in range(steps + 1):
            a = math.radians(a0 + (a1 - a0) * i / steps)
            pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
        p.polygon(pts, fill=False, stroke=True, close=False)

    def _wavy(self, p, x, y, w, amp, waves=3, steps=24):
        pts = []
        for i in range(steps + 1):
            t = i / steps
            pts.append((x + w * t, y + amp * math.sin(t * waves * math.pi)))
        p.polygon(pts, fill=False, stroke=True, close=False)

    def _cloud(self, p, cx, cy, s):
        for (dx, dy, rr) in [(-s * 0.6, 0, s * 0.45), (0, s * 0.1, s * 0.6),
                             (s * 0.6, 0, s * 0.45), (0, -s * 0.2, s * 0.5)]:
            p.circle(cx + dx, cy + dy, rr, fill=False, stroke=True)

    def _star(self, p, cx, cy, r, fill=False):
        p.star(cx, cy, r, points=5, fill=fill, stroke=True)

    # ---------------- reusable blocks ----------------
    def intro_box(self, p, y, text):
        lines = _wrapn(text, 11, CW - 36)
        h = 24 + lines * 15 + 12
        p.set_fill(*SOFT)
        p.round_rect(MARGIN, y - h, CW, h, 10, fill=True, stroke=False)
        p.set_fill(*self.accent)
        p.rect(MARGIN, y - h, 5, h, fill=True, stroke=False)
        p.set_fill(*SLATE)
        p.wrap_text(MARGIN + 18, y - 20, text, 11, CW - 34, leading=15)
        return y - h - 12

    def instruction(self, p, y, text):
        p.set_fill(*self.accent2)
        p.round_rect(MARGIN, y - 30, CW, 30, 8, fill=True, stroke=False)
        p.set_fill(*INK)
        p.text(MARGIN + 14, y - 20, text, 11.5, bold=True)
        return y - 44

    def subhead(self, p, y, text):
        p.set_fill(*self.accent)
        p.text(MARGIN, y, text, 13, bold=True)
        p.set_stroke(*self.accent2); p.set_line_width(2)
        p.line(MARGIN, y - 6, MARGIN + 46, y - 6)
        return y - 22

    def paragraph(self, p, y, text, size=11, color=INK, gap=8, bold=False):
        p.set_fill(*color)
        endy = p.wrap_text(MARGIN, y, text, size, CW, leading=size * 1.4, bold=bold)
        return endy - gap

    def write_lines(self, p, y, count, spacing=26, indent=0, dashed=False):
        x0 = MARGIN + indent
        for i in range(count):
            yy = y - i * spacing
            if yy < 56:
                break
            p.set_stroke(*RULE); p.set_line_width(0.7)
            p.line(x0, yy, PW - MARGIN, yy)
        return y - count * spacing - 6

    def checklist(self, p, y, items, box=True):
        for it in items:
            if y < 60:
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
        p.set_fill(*self.accent)
        p.text(MARGIN, y, label, 11.5, bold=True)
        p.set_stroke(*RULE); p.set_line_width(1.2)
        p.round_rect(MARGIN, y - 12 - height, CW, height, 10, fill=False, stroke=True)
        return y - 12 - height - 12

    # ---------------- front matter ----------------
    def cover(self):
        p, _ = self.doc.add_page(), None
        self._pageno += 1
        # background
        p.set_fill(*self.accent)
        p.rect(0, 0, PW, PH, fill=True, stroke=False)
        # big soft panel
        p.set_fill(1, 1, 1)
        p.round_rect(40, 150, PW - 80, PH - 320, 22, fill=True, stroke=False)
        # top clouds & sun
        p.set_stroke(1, 1, 1); p.set_line_width(2)
        self._sun_rays(p, 120, PH - 90, 26)
        p.set_stroke(0.95, 0.97, 1.0)
        self._cloud(p, PW - 150, PH - 80, 30)
        # series
        p.set_fill(1, 1, 1)
        p.text_center(PW / 2, PH - 130, self.series.upper(), 11, bold=True)
        # emotion faces row inside panel
        moods = ["happy", "sad", "angry", "worried", "calm"]
        cols = [self.accent2, SKY, CORAL, LAVEN, MINT]
        n = len(moods)
        span = PW - 200
        x0 = 100
        for i, (m, c) in enumerate(zip(moods, cols)):
            cx = x0 + span * i / (n - 1)
            self.face(p, cx, PH - 250, 30, m, color=c)
        # title
        p.set_fill(*self.accent)
        endy = p.wrap_text(0, PH - 330, self.title, 30, PW - 150, bold=True,
                           center_x=PW / 2, leading=34)
        # subtitle
        p.set_fill(*SLATE)
        endy = p.wrap_text(0, endy - 14, self.subtitle, 14, PW - 190,
                           center_x=PW / 2, leading=19)
        # writer
        p.set_fill(*self.accent)
        p.text_center(PW / 2, endy - 8, "Written by " + self.writer, 13, bold=True)
        # age badge
        p.set_fill(*self.accent2)
        p.round_rect(PW / 2 - 95, 175, 190, 40, 12, fill=True, stroke=False)
        p.set_fill(*INK)
        p.text_center(PW / 2, 188, self.ages + "  •  Printable", 13, bold=True)
        # bottom tag
        p.set_fill(1, 1, 1)
        p.text_center(PW / 2, 110, "Home  •  Classroom  •  Counseling  •  Calm Corners", 11, bold=True)
        p.text_center(PW / 2, 92, "Reproducible for one home or classroom", 9)
        return p

    def _sun_rays(self, p, cx, cy, r):
        for i in range(12):
            a = i * math.pi / 6
            p.line(cx + r * 1.25 * math.cos(a), cy + r * 1.25 * math.sin(a),
                   cx + r * 1.7 * math.cos(a), cy + r * 1.7 * math.sin(a))
        p.circle(cx, cy, r, fill=False, stroke=True)

    def welcome(self, intro_paras, for_grownups):
        p, y, n = self.page("Welcome", "How to Use This Book")
        for para in intro_paras:
            y = self.paragraph(p, y, para)
        y = self.subhead(p, y, "For Grown-Ups")
        y = self.checklist(p, y, for_grownups, box=False)
        y = self.intro_box(p, y, "Tip: There are no wrong answers here. Every feeling is okay. "
                                 "What matters is what we choose to DO with big feelings.")
        return p

    def how_it_scales(self):
        p, y, n = self.page("Guide", "Grows With the Reader (Ages 5-17)")
        y = self.paragraph(p, y, "This book is built for a wide range of ages. Younger children can color, "
                                 "trace, and point to feelings faces. Older kids and teens can use the same "
                                 "pages for journaling, deeper reflection, and building real coping plans.")
        y = self.subhead(p, y, "Younger (about 5-9)")
        y = self.checklist(p, y, [
            "Color the feelings faces and calm-down pictures.",
            "Trace the calming words and short affirmations.",
            "Do the breathing shapes with a grown-up.",
        ], box=False)
        y = self.subhead(p, y, "Older kids & teens (about 10-17)")
        y = self.checklist(p, y, [
            "Write in the journal and reflection spaces.",
            "Work through the 'What would you do?' scenarios.",
            "Build and personalize your own coping toolkit and calm-down plan.",
        ], box=False)
        return p

    def contents(self):
        p, y, n = self.page("Contents", "What's Inside")
        for i, t in enumerate(self.toc, start=1):
            if y < 60:
                break
            p.set_fill(*self.accent)
            p.circle(MARGIN + 8, y + 4, 9, fill=True, stroke=False)
            p.set_fill(1, 1, 1)
            p.text_center(MARGIN + 8, y + 0.5, str(i), 9, bold=True)
            p.set_fill(*INK)
            p.text(MARGIN + 26, y, t, 11.5)
            y -= 24
        return p

    def divider(self, title, subtitle, mood="calm", color=None):
        p, _ = self.doc.add_page(), None
        self._pageno += 1
        col = color or self.accent
        p.set_fill(*col)
        p.rect(0, 0, PW, PH, fill=True, stroke=False)
        p.set_fill(1, 1, 1)
        p.round_rect(50, PH / 2 - 150, PW - 100, 300, 22, fill=True, stroke=False)
        self.face(p, PW / 2, PH / 2 + 70, 46, mood, color=self.accent2)
        p.set_fill(*col)
        p.wrap_text(0, PH / 2 - 5, title, 26, PW - 160, bold=True, center_x=PW / 2, leading=30)
        p.set_fill(*SLATE)
        p.wrap_text(0, PH / 2 - 70, subtitle, 13, PW - 200, center_x=PW / 2, leading=18)
        self._footer(p, self._pageno)
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
# Composite activity pages
# =====================================================================
def feelings_faces_color(wb, kicker, heading, moods_labels):
    """Grid of outline faces to color + label (younger friendly)."""
    p, y, n = wb.page(kicker, heading)
    y = wb.instruction(p, y, "Color each face. Say the feeling out loud!")
    cols = 3
    cellw = CW / cols
    r = 34
    i = 0
    row_y = y - 20
    for (mood, label) in moods_labels:
        col = i % cols
        if col == 0 and i != 0:
            row_y -= 130
        cx = MARGIN + cellw * col + cellw / 2
        if row_y - 130 < 60:
            break
        wb.face(p, cx, row_y - 34, r, mood)
        p.set_fill(*INK)
        p.text_center(cx, row_y - 92, label, 11, bold=True)
        # small write line
        p.set_stroke(*RULE); p.set_line_width(0.7)
        p.line(cx - 40, row_y - 104, cx + 40, row_y - 104)
        i += 1
    return p


def feelings_thermometer(wb, kicker="Check-In", heading="My Feelings Thermometer"):
    p, y, n = wb.page(kicker, heading)
    y = wb.intro_box(p, y, "A feelings thermometer shows how BIG a feeling is. Green is calm and okay. "
                           "Yellow is starting to bubble. Red is a very big feeling. Knowing our level "
                           "helps us pick the right calm-down tool.")
    # thermometer drawing
    tx = MARGIN + 60
    top = y - 10
    bot = 90
    width = 46
    zones = [("RED - Big feeling", CORAL), ("YELLOW - Getting bigger", GOLD),
             ("GREEN - Calm & okay", MINT)]
    zh = (top - bot) / 3
    for i, (label, color) in enumerate(zones):
        zy = bot + (2 - i) * zh
        p.set_fill(*color)
        p.round_rect(tx, zy, width, zh - 6, 8, fill=True, stroke=False)
        p.set_fill(*INK)
        p.text(tx + width + 20, zy + zh / 2 - 6, label, 12, bold=True)
        # write line for "what helps"
        p.set_stroke(*RULE); p.set_line_width(0.7)
        p.line(tx + width + 20, zy + zh / 2 - 18, PW - MARGIN, zy + zh / 2 - 18)
    p.set_fill(*INK)
    p.text(tx + width + 20, bot - 20, "What can I do at each level? Write above.", 9)
    return p


def breathing_exercise(wb, kicker, heading, name, steps, shape="square"):
    p, y, n = wb.page(kicker, heading)
    y = wb.intro_box(p, y, "Slow breathing tells our body it is safe. Trace the shape slowly with your "
                           "finger while you breathe. Do it 3-5 times.")
    y = wb.subhead(p, y, name)
    # shape trace
    cx, cy = PW / 2, y - 130
    p.set_stroke(*wb.accent); p.set_line_width(2.4)
    if shape == "square":
        s = 100
        p.rect(cx - s, cy - s, 2 * s, 2 * s, fill=False, stroke=True)
        labels = [("Breathe in (4)", cx, cy + s + 14),
                  ("Hold (4)", cx + s + 8, cy),
                  ("Breathe out (4)", cx, cy - s - 22),
                  ("Hold (4)", cx - s - 70, cy)]
        p.set_fill(*INK)
        for (t, lx, ly) in labels:
            p.text(lx - pdfkit.text_width(t, 9) / 2 if lx == cx else lx, ly, t, 9, bold=True)
    elif shape == "triangle":
        s = 110
        p.polygon([(cx, cy + s), (cx - s, cy - s * 0.7), (cx + s, cy - s * 0.7)], fill=False, stroke=True)
    elif shape == "star":
        wb._star(p, cx, cy, 120)
    elif shape == "flower":
        for i in range(6):
            a = i * math.pi / 3
            p.circle(cx + 60 * math.cos(a), cy + 60 * math.sin(a), 42, fill=False, stroke=True)
    y = cy - 150
    for i, s in enumerate(steps, 1):
        p.set_fill(*wb.accent); p.text(MARGIN, y, f"{i}.", 11, bold=True)
        p.set_fill(*INK); endy = p.wrap_text(MARGIN + 18, y, s, 11, CW - 18, leading=15)
        y = endy - 8
        if y < 70:
            break
    return p


def coloring_calm(wb, kicker, heading, caption, scene):
    p, y, n = wb.page(kicker, heading)
    p.set_fill(*INK)
    p.text_center(PW / 2, y, caption, 12, bold=True)
    fy = 80
    fh = y - 30 - fy
    p.set_stroke(*wb.accent); p.set_line_width(2)
    p.round_rect(MARGIN, fy, CW, fh, 14, fill=False, stroke=True)
    p.set_stroke(*INK); p.set_line_width(1.6)
    scene(p, PW / 2, fy + fh / 2)
    p.set_fill(*GRAY)
    p.text_center(PW / 2, 64, "Color it in with calm colors that feel good to you.", 9)
    return p


def tracing_affirmations(wb, kicker, heading, phrases):
    p, y, n = wb.page(kicker, heading)
    y = wb.instruction(p, y, "Trace the calming words. Then say them out loud.")
    for ph in phrases:
        p.set_fill(*TRACE)
        p.text(MARGIN, y - 22, ph, 22, bold=True)
        p.set_stroke(*RULE); p.set_line_width(0.8)
        p.line(MARGIN, y - 30, PW - MARGIN, y - 30)
        y -= 56
        if y < 90:
            break
    # extra blank practice line
    if y > 80:
        p.set_fill(*wb.accent)
        p.text(MARGIN, y, "Now write your own calming words:", 11, bold=True)
        wb.write_lines(p, y - 14, 2, spacing=30)
    return p


def calm_strategy_cards(wb, kicker, heading, cards):
    """cards: list of (title, description). Drawn as a grid of cards."""
    p, y, n = wb.page(kicker, heading)
    y = wb.intro_box(p, y, "These are calm-down tools. Try each one. Circle the ones that work best for YOU, "
                           "then cut them out or copy them for your calm corner.")
    cols = 2
    cardw = (CW - 16) / cols
    cardh = 92
    x0 = MARGIN
    top = y - 4
    i = 0
    for (t, d) in cards:
        col = i % cols
        row = i // cols
        cx = x0 + col * (cardw + 16)
        cy = top - row * (cardh + 12)
        if cy - cardh < 70:
            break
        p.set_fill(*CARD)
        p.round_rect(cx, cy - cardh, cardw, cardh, 12, fill=True, stroke=False)
        p.set_stroke(*wb.accent); p.set_line_width(1.4)
        p.round_rect(cx, cy - cardh, cardw, cardh, 12, fill=False, stroke=True)
        p.set_fill(*wb.accent)
        p.circle(cx + 20, cy - 20, 11, fill=True, stroke=False)
        p.set_fill(1, 1, 1); p.text_center(cx + 20, cy - 24, str(i + 1), 10, bold=True)
        p.set_fill(*INK)
        p.text(cx + 38, cy - 24, t, 11.5, bold=True)
        p.set_fill(*SLATE)
        p.wrap_text(cx + 14, cy - 44, d, 9.5, cardw - 26, leading=12.5)
        i += 1
    return p


def scenario_page(wb, kicker, heading, scenarios):
    """scenarios: list of situation strings. Each gets 'What would you do?' lines."""
    p, y, n = wb.page(kicker, heading)
    y = wb.intro_box(p, y, "Read each situation. There are many good choices! Think it through, then write or "
                           "draw what you could do to stay calm and kind.")
    for i, s in enumerate(scenarios, 1):
        if y < 120:
            break
        p.set_fill(*wb.accent)
        p.circle(MARGIN + 9, y + 3, 10, fill=True, stroke=False)
        p.set_fill(1, 1, 1); p.text_center(MARGIN + 9, y - 0.5, str(i), 10, bold=True)
        p.set_fill(*INK)
        endy = p.wrap_text(MARGIN + 28, y, s, 11.5, CW - 28, leading=15, bold=True)
        y = endy - 6
        p.set_fill(*GRAY); p.text(MARGIN + 28, y, "What could you do?", 9.5, italic=True)
        y = wb.write_lines(p, y - 8, 2, spacing=24, indent=28)
        y -= 10
    return p


def journal_page(wb, kicker, heading, prompts, box_label=None, box_h=0):
    p, y, n = wb.page(kicker, heading)
    for pr in prompts:
        if y < 100:
            break
        p.set_fill(*wb.accent2)
        p.circle(MARGIN + 5, y + 3, 5, fill=True, stroke=False)
        p.set_fill(*INK)
        endy = p.wrap_text(MARGIN + 18, y, pr, 11.5, CW - 18, bold=True, leading=15)
        y = endy - 8
        y = wb.write_lines(p, y, 3, spacing=26)
        y -= 10
    if box_label and y > box_h + 70:
        wb.draw_box(p, y, box_label, box_h)
    return p


def body_scan(wb, kicker="Body Check", heading="Where Do I Feel It?"):
    p, y, n = wb.page(kicker, heading)
    y = wb.intro_box(p, y, "Big feelings live in our bodies too. Anger might feel hot in your chest. Worry might "
                           "feel like butterflies in your tummy. Color or mark where you feel your feelings.")
    # simple body outline
    cx = MARGIN + 110
    top = y - 10
    p.set_stroke(*INK); p.set_line_width(1.8)
    p.circle(cx, top - 30, 26, fill=False, stroke=True)               # head
    p.round_rect(cx - 40, top - 170, 80, 115, 22, fill=False, stroke=True)  # torso
    p.line(cx - 40, top - 110, cx - 78, top - 150)                    # arms
    p.line(cx + 40, top - 110, cx + 78, top - 150)
    p.line(cx - 18, top - 170, cx - 30, top - 250)                    # legs
    p.line(cx + 18, top - 170, cx + 30, top - 250)
    # key
    kx = cx + 130
    ky = top - 20
    p.set_fill(*INK)
    p.text(kx, ky, "Draw or color:", 11, bold=True)
    for (label, color) in [("Hot / angry feelings", CORAL), ("Fluttery / worried feelings", GOLD),
                           ("Heavy / sad feelings", SKY), ("Calm / good feelings", MINT)]:
        ky -= 30
        p.set_fill(*color); p.circle(kx + 8, ky + 3, 8, fill=True, stroke=False)
        p.set_fill(*INK); p.text(kx + 24, ky, label, 10.5)
    ky -= 44
    p.set_fill(*wb.accent); p.text(kx, ky, "Today my body feels...", 11, bold=True)
    wb.write_lines(p, ky - 14, 3, spacing=24)
    return p


def matching_page(wb, kicker, heading, left, right, instruction):
    p, y, n = wb.page(kicker, heading)
    y = wb.instruction(p, y, instruction)
    nrows = min(len(left), len(right))
    top = y - 10
    row_h = (top - 90) / max(nrows, 1)
    import random
    rr = list(right); random.Random(len(heading)).shuffle(rr)
    for i in range(nrows):
        ly = top - i * row_h
        p.set_fill(*wb.accent); p.circle(MARGIN + 8, ly, 5, fill=True, stroke=False)
        p.set_fill(*INK); p.text(MARGIN + 22, ly - 4, left[i], 12)
        tw = pdfkit.text_width(rr[i], 12)
        p.text(PW - MARGIN - 22 - tw, ly - 4, rr[i], 12)
        p.set_fill(*wb.accent2); p.circle(PW - MARGIN - 8, ly, 5, fill=True, stroke=False)
    return p


def coping_plan(wb, kicker="My Plan", heading="My Personal Calm-Down Plan"):
    p, y, n = wb.page(kicker, heading)
    y = wb.intro_box(p, y, "This is YOUR plan for big feelings. Fill it in and keep it somewhere you'll see it. "
                           "You can update it any time as you learn what helps.")
    steps = [
        "When I notice a big feeling, my body signal is...",
        "Three calm-down tools I will try first are...",
        "A safe person I can talk to is...",
        "Words I can say to myself are...",
        "A calm place I can go is...",
    ]
    for s in steps:
        if y < 90:
            break
        p.set_fill(*wb.accent); p.text(MARGIN, y, s, 11.5, bold=True)
        y = wb.write_lines(p, y - 14, 2, spacing=24)
        y -= 12
    return p


def gratitude_page(wb, kicker="Feel-Good", heading="Good Things & Gratitude"):
    p, y, n = wb.page(kicker, heading)
    y = wb.intro_box(p, y, "Noticing good things helps calm our minds and lift our mood. It doesn't erase hard "
                           "feelings, but it reminds us that good things are here too.")
    y = wb.subhead(p, y, "Three good things about today")
    y = wb.write_lines(p, y, 3, spacing=28)
    y -= 6
    y = wb.subhead(p, y, "Someone I'm thankful for - and why")
    y = wb.write_lines(p, y, 2, spacing=28)
    y -= 6
    if y > 150:
        wb.draw_box(p, y, "Draw something that makes you smile:", min(y - 80, 130))
    return p


def checklist_page(wb, kicker, heading, intro, items):
    p, y, n = wb.page(kicker, heading)
    y = wb.intro_box(p, y, intro)
    y = wb.checklist(p, y, items, box=True)
    return p


def notes_page(wb, kicker="Notes", heading="My Notes & Doodles"):
    p, y, n = wb.page(kicker, heading)
    wb.write_lines(p, y, 20, spacing=27)
    return p


# ---------------- coloring scenes (black line art) ----------------
def scene_calm_beach(p, cx, cy):
    # sun, waves, palm-ish, starfish
    p.circle(cx - 120, cy + 80, 30)
    for i in range(12):
        a = i * math.pi / 6
        p.line(cx - 120 + 40 * math.cos(a), cy + 80 + 40 * math.sin(a),
               cx - 120 + 56 * math.cos(a), cy + 80 + 56 * math.sin(a))
    for wy in (cy - 30, cy - 60, cy - 90):
        pts = []
        for xx in range(int(cx - 150), int(cx + 151), 20):
            pts.append((xx, wy + (7 if (xx // 20) % 2 == 0 else -7)))
        p.polygon(pts, fill=False, stroke=True, close=False)
    p.star(cx + 90, cy - 5, 20, points=5, fill=False, stroke=True)


def scene_cozy_room(p, cx, cy):
    # comfy chair + lamp + plant + heart pillow
    p.round_rect(cx - 100, cy - 60, 110, 90, 16, fill=False, stroke=True)
    p.round_rect(cx - 108, cy - 20, 18, 60, 8, fill=False, stroke=True)
    p.heart(cx - 45, cy + 10, 18, fill=False, stroke=True)
    # lamp
    p.line(cx + 70, cy - 60, cx + 70, cy + 40)
    p.polygon([(cx + 50, cy + 40), (cx + 90, cy + 40), (cx + 80, cy + 70), (cx + 60, cy + 70)], fill=False, stroke=True)
    # plant
    p.round_rect(cx + 40, cy - 60, 30, 24, 4, fill=False, stroke=True)
    for dx in (-8, 0, 8):
        p.polygon([(cx + 55 + dx, cy - 36), (cx + 55 + dx + 6, cy + 6), (cx + 55 + dx - 6, cy + 6)], fill=False, stroke=True)


def scene_mountain(p, cx, cy):
    # calm mountains + sun + path
    p.polygon([(cx - 160, cy - 60), (cx - 60, cy + 70), (cx + 20, cy - 10),
               (cx + 90, cy + 60), (cx + 160, cy - 60)], fill=False, stroke=True, close=False)
    p.line(cx - 160, cy - 60, cx + 160, cy - 60)
    p.circle(cx + 60, cy + 90, 26)
    # path
    p.polygon([(cx - 10, cy - 60), (cx + 10, cy - 60), (cx + 40, cy - 140), (cx - 40, cy - 140)], fill=False, stroke=True)


def scene_star_night(p, cx, cy):
    # moon + stars + hills
    p.circle(cx - 100, cy + 80, 30)
    p.set_fill(1, 1, 1)
    p.circle(cx - 88, cy + 88, 26, fill=True, stroke=False)
    for (sx, sy, sr) in [(cx + 40, cy + 100, 12), (cx + 110, cy + 70, 9),
                         (cx - 20, cy + 120, 8), (cx + 80, cy + 120, 10)]:
        p.star(sx, sy, sr, points=5, fill=False, stroke=True)
    for hx in (cx - 160, cx - 40, cx + 90):
        p.polygon([(hx, cy - 80), (hx + 90, cy - 20), (hx + 180, cy - 80)], fill=False, stroke=True, close=False)


def scene_garden(p, cx, cy):
    # flowers + sun + butterfly
    p.line(cx - 160, cy - 70, cx + 160, cy - 70)
    for dx in (-120, -70, -20, 40, 100):
        p.circle(cx + dx, cy - 30, 12)
        for i in range(8):
            a = i * math.pi / 4
            p.circle(cx + dx + 20 * math.cos(a), cy - 30 + 20 * math.sin(a), 8)
        p.line(cx + dx, cy - 42, cx + dx, cy - 70)
    p.circle(cx + 110, cy + 90, 24)
    # butterfly
    p.circle(cx - 60, cy + 70, 16)
    p.circle(cx - 30, cy + 70, 16)
