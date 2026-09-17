"""
workbook_games.py — Interactive matching / sorting / role-play / game engine.
Dependency-free (uses pdfkit.py). Designed to scale for ages 5-19.

Components:
  - cover, how-to-play (for grown-ups), contents, section dividers
  - matching cards (cut-out pairs) + draw-a-line matching
  - sorting mats + cut-out sorting cards
  - sequencing activity (order the steps/days)
  - scenario-matching (situation -> response/emotion)
  - busy-book color sorting
  - role-play / pretend-play cards
  - discussion sorting (with talk-about prompts for older kids)
  - bingo card generator (unique cards) + call list
  - role-play scenario deck (with reflection lines)
  - answer keys, reflection/journal, certificate

All builders take a GameBook instance `wb` and append pages.
"""

import math
import random
import pdfkit

INK = (0.13, 0.14, 0.17)
SLATE = (0.29, 0.32, 0.39)
GRAY = (0.47, 0.50, 0.56)
RULE = (0.80, 0.82, 0.87)
DASH = (0.66, 0.69, 0.75)
CARD = (0.955, 0.965, 0.98)
SOFT = (0.93, 0.96, 0.97)

TEAL = (0.11, 0.60, 0.60);   SUN = (0.98, 0.78, 0.25)
CORAL = (0.95, 0.45, 0.42);  SKY = (0.36, 0.66, 0.86)
PURPLE = (0.55, 0.40, 0.72); MINT = (0.42, 0.76, 0.58)
BLUE = (0.24, 0.46, 0.78);   PEACH = (0.98, 0.66, 0.44)
GREEN = (0.30, 0.66, 0.40);  LAVEN = (0.66, 0.58, 0.85)
ROSE = (0.90, 0.44, 0.58);   AQUA = (0.30, 0.72, 0.74)
ORANGE = (0.95, 0.55, 0.22); INDIGO = (0.32, 0.34, 0.62)
GOLD = (0.92, 0.72, 0.20);   BERRY = (0.72, 0.26, 0.45)

PW, PH = pdfkit.LETTER
MARGIN = 54.0
CW = PW - 2 * MARGIN


class GameBook:
    def __init__(self, title, subtitle, ages, skill, fmt,
                 accent=TEAL, accent2=SUN, writer="Daniel Tesfamariam",
                 series="Play & Learn Activity Games"):
        self.writer = writer
        self.doc = pdfkit.Document(title=title, author=writer)
        self.title = title
        self.subtitle = subtitle
        self.ages = ages
        self.skill = skill
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
        p.line(MARGIN, 38, PW - MARGIN, 38)
        p.set_fill(*GRAY)
        p.text(MARGIN, 27, self.title, 7.5)
        p.text_right(PW - MARGIN, 27, str(n), 8, bold=True)

    def _header(self, p, kicker, heading):
        p.set_fill(*self.accent)
        p.round_rect(MARGIN - 8, PH - 90, CW + 16, 66, 12, fill=True, stroke=False)
        p.set_fill(1, 1, 1)
        p.text(MARGIN + 8, PH - 42, kicker.upper(), 10, bold=True)
        p.text(MARGIN + 8, PH - 68, heading, 18, bold=True)

    def page(self, kicker, heading):
        p, n = self._new()
        self._header(p, kicker, heading)
        self._footer(p, n)
        return p, PH - 112, n

    # ---------- text helpers ----------
    def intro_box(self, p, y, text):
        lines = _wrapn(text, 11, CW - 34)
        h = 22 + lines * 15 + 12
        p.set_fill(*SOFT); p.round_rect(MARGIN, y - h, CW, h, 10, fill=True, stroke=False)
        p.set_fill(*self.accent); p.rect(MARGIN, y - h, 5, h, fill=True, stroke=False)
        p.set_fill(*SLATE); p.wrap_text(MARGIN + 18, y - 19, text, 11, CW - 32, leading=15)
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
        return p.wrap_text(MARGIN, y, text, size, CW, leading=size * 1.4, bold=bold) - gap

    def write_lines(self, p, y, count, spacing=26, indent=0):
        for i in range(count):
            yy = y - i * spacing
            if yy < 52:
                break
            p.set_stroke(*RULE); p.set_line_width(0.7)
            p.line(MARGIN + indent, yy, PW - MARGIN, yy)
        return y - count * spacing - 6

    def checklist(self, p, y, items, box=True):
        for it in items:
            if y < 56:
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

    def _scissors(self, p, x, y):
        p.set_stroke(*DASH); p.set_line_width(0.8)
        p.set_dash(4, 3)
        p.line(x, y, PW - MARGIN, y)
        p.clear_dash()

    # ---------- simple icon (labeled token) ----------
    def token(self, p, cx, cy, r, label, color):
        p.set_fill(*color); p.circle(cx, cy, r, fill=True, stroke=False)
        p.set_stroke(*INK); p.set_line_width(1.2); p.circle(cx, cy, r, fill=False, stroke=True)
        p.set_fill(1, 1, 1)
        p.text_center(cx, cy - 4, label[:2].upper(), r * 0.5, bold=True)

    # ---------- front matter ----------
    def cover(self):
        p, _ = self.doc.add_page(), None
        self._pageno += 1
        p.set_fill(*self.accent); p.rect(0, 0, PW, PH, fill=True, stroke=False)
        p.set_fill(1, 1, 1); p.round_rect(40, 150, PW - 80, PH - 320, 22, fill=True, stroke=False)
        # playful card/token motif
        cols = [self.accent2, SKY, CORAL, MINT, LAVEN]
        for i, c in enumerate(cols):
            cx = 110 + i * ((PW - 220) / 4)
            p.set_fill(*c); p.round_rect(cx - 26, PH - 300, 52, 66, 8, fill=True, stroke=False)
            p.set_stroke(*INK); p.set_line_width(1.2)
            p.round_rect(cx - 26, PH - 300, 52, 66, 8, fill=False, stroke=True)
            p.set_fill(1, 1, 1); p.text_center(cx, PH - 272, str(i + 1), 22, bold=True)
        p.set_fill(1, 1, 1)
        p.text_center(PW / 2, PH - 128, self.series.upper(), 11, bold=True)
        p.set_fill(*self.accent)
        endy = p.wrap_text(0, PH - 360, self.title, 27, PW - 150, bold=True, center_x=PW / 2, leading=31)
        p.set_fill(*SLATE)
        endy = p.wrap_text(0, endy - 12, self.subtitle, 13.5, PW - 190, center_x=PW / 2, leading=18)
        p.set_fill(*self.accent)
        p.text_center(PW / 2, endy - 8, "Written by " + self.writer, 13, bold=True)
        p.set_fill(*self.accent2); p.round_rect(PW / 2 - 165, 176, 330, 38, 12, fill=True, stroke=False)
        p.set_fill(*INK); p.text_center(PW / 2, 188, self.ages + "   -   " + self.fmt, 11, bold=True)
        p.set_fill(1, 1, 1)
        p.text_center(PW / 2, 116, "Cut-out cards, sorting mats, games & role-play", 11, bold=True)
        p.text_center(PW / 2, 98, "Home  -  Classroom  -  Group activities", 9)
        return p

    def how_to_play(self, what_it_teaches, tips):
        p, y, n = self.page("For Grown-Ups", "How to Play & Learn")
        y = self.paragraph(p, y, "This activity book turns learning into play. Print the pages, cut out the "
                                 "cards along the dashed lines, and use the mats and games again and again. "
                                 "Playing the same game more than once is where the learning sticks.")
        y = self.intro_box(p, y, what_it_teaches)
        y = self.subhead(p, y, "Tips for grown-ups")
        y = self.checklist(p, y, tips, box=False)
        y = self.subhead(p, y, "Ages 5-19: how it grows")
        self.checklist(p, y, [
            "Younger (5-9): match, sort, and color with hands-on cards.",
            "Middle (10-13): play the games and explain WHY each answer fits.",
            "Older (14-19): use the discussion and reflection prompts to go deeper.",
        ], box=False)
        return p

    def contents(self):
        p, y, n = self.page("Contents", "What's Inside")
        for i, t in enumerate(self.toc, start=1):
            if y < 56:
                break
            p.set_fill(*self.accent); p.circle(MARGIN + 8, y + 4, 9, fill=True, stroke=False)
            p.set_fill(1, 1, 1); p.text_center(MARGIN + 8, y + 0.5, str(i), 9, bold=True)
            p.set_fill(*INK); p.text(MARGIN + 26, y, t, 11.5)
            y -= 23
        return p

    def divider(self, title, subtitle, color=None):
        p, _ = self.doc.add_page(), None
        self._pageno += 1
        col = color or self.accent
        p.set_fill(*col); p.rect(0, 0, PW, PH, fill=True, stroke=False)
        p.set_fill(1, 1, 1); p.round_rect(50, PH / 2 - 140, PW - 100, 280, 22, fill=True, stroke=False)
        # cards motif
        for i, c in enumerate([self.accent2, SKY, CORAL]):
            cx = PW / 2 - 70 + i * 70
            p.set_fill(*c); p.round_rect(cx - 22, PH / 2 + 30, 44, 56, 6, fill=True, stroke=False)
            p.set_stroke(*INK); p.set_line_width(1.1)
            p.round_rect(cx - 22, PH / 2 + 30, 44, 56, 6, fill=False, stroke=True)
        p.set_fill(*col)
        p.wrap_text(0, PH / 2 - 4, title, 24, PW - 160, bold=True, center_x=PW / 2, leading=28)
        p.set_fill(*SLATE)
        p.wrap_text(0, PH / 2 - 60, subtitle, 13, PW - 200, center_x=PW / 2, leading=18)
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
# Game / activity components
# =====================================================================
def cut_out_cards(wb, kicker, heading, cards, cols=2, rows=3, sub=""):
    """A page of cut-out cards. cards: list of (title, text). Up to cols*rows per page."""
    p, y, n = wb.page(kicker, heading)
    if sub:
        p.set_fill(*GRAY); p.text(MARGIN, y, sub, 10, italic=True); y -= 16
    p.set_fill(*GRAY); p.text_right(PW - MARGIN, y + 2, "Cut along the dashed lines.", 9)
    y -= 8
    gw = CW
    gh = y - 60
    cardw = gw / cols
    cardh = gh / rows
    for i, (t, d) in enumerate(cards[:cols * rows]):
        col = i % cols; row = i // cols
        x = MARGIN + col * cardw
        cy = y - row * cardh
        # dashed cut border
        p.set_stroke(*DASH); p.set_line_width(0.8); p.set_dash(4, 3)
        p.rect(x + 6, cy - cardh + 6, cardw - 12, cardh - 12, fill=False, stroke=True)
        p.clear_dash()
        # card content
        p.set_fill(*wb.accent); p.circle(x + 26, cy - 26, 12, fill=True, stroke=False)
        p.set_fill(1, 1, 1); p.text_center(x + 26, cy - 30, str(i + 1), 11, bold=True)
        p.set_fill(*INK)
        p.wrap_text(x + 46, cy - 30, t, 12, cardw - 60, bold=True, leading=15)
        p.set_fill(*SLATE)
        p.wrap_text(x + 18, cy - 56, d, 9.8, cardw - 34, leading=13)
    return p


def draw_line_matching(wb, kicker, heading, left, right, instruction):
    p, y, n = wb.page(kicker, heading)
    y = wb.instruction(p, y, instruction)
    nrows = min(len(left), len(right))
    top = y - 10
    row_h = (top - 80) / max(nrows, 1)
    rr = list(right); random.Random(len(heading) * 7).shuffle(rr)
    for i in range(nrows):
        ly = top - i * row_h
        p.set_fill(*wb.accent); p.circle(MARGIN + 8, ly, 5, fill=True, stroke=False)
        p.set_fill(*INK)
        p.wrap_text(MARGIN + 22, ly + 4, left[i], 11.5, CW / 2 - 40, leading=13)
        tw = pdfkit.text_width(rr[i], 11.5)
        p.text(PW - MARGIN - 22 - min(tw, CW / 2 - 40), ly - 4, rr[i], 11.5)
        p.set_fill(*wb.accent2); p.circle(PW - MARGIN - 8, ly, 5, fill=True, stroke=False)
    return p


def sorting_mat(wb, kicker, heading, categories, instruction, items_hint=None):
    """Two- or three-column sorting mat with header bins."""
    p, y, n = wb.page(kicker, heading)
    y = wb.instruction(p, y, instruction)
    ncat = len(categories)
    binw = (CW - (ncat - 1) * 12) / ncat
    top = y - 4
    binh = top - 90
    colors = [wb.accent, wb.accent2, SKY, MINT, CORAL]
    for i, cat in enumerate(categories):
        x = MARGIN + i * (binw + 12)
        c = colors[i % len(colors)]
        p.set_fill(*c); p.round_rect(x, top - 34, binw, 34, 8, fill=True, stroke=False)
        p.set_fill(1, 1, 1); p.text_center(x + binw / 2, top - 24, cat, 12, bold=True)
        p.set_stroke(*RULE); p.set_line_width(1.2)
        p.set_dash(4, 3)
        p.rect(x, top - 34 - binh, binw, binh, fill=False, stroke=True)
        p.clear_dash()
    if items_hint:
        p.set_fill(*GRAY)
        p.text(MARGIN, 60, "Sort the cut-out cards into the right bin. " + items_hint, 9, italic=True)
    return p


def sequencing_page(wb, kicker, heading, steps, instruction):
    """Order-the-steps activity: numbered blanks + shuffled clue list."""
    p, y, n = wb.page(kicker, heading)
    y = wb.instruction(p, y, instruction)
    # numbered order slots
    for i in range(len(steps)):
        p.set_fill(*wb.accent); p.circle(MARGIN + 10, y, 12, fill=True, stroke=False)
        p.set_fill(1, 1, 1); p.text_center(MARGIN + 10, y - 4, str(i + 1), 11, bold=True)
        p.set_stroke(*RULE); p.set_line_width(0.8)
        p.round_rect(MARGIN + 30, y - 16, CW - 30, 30, 6, fill=False, stroke=True)
        y -= 40
        if y < 150:
            break
    # word bank (shuffled)
    y -= 4
    p.set_fill(*SOFT); p.round_rect(MARGIN, 66, CW, y - 66, 8, fill=True, stroke=False)
    p.set_fill(*wb.accent); p.text(MARGIN + 12, y - 18, "Clue Bank (in mixed-up order):", 11, bold=True)
    sh = list(enumerate(steps, 1)); random.Random(len(heading)).shuffle(sh)
    yy = y - 38
    for _, st in sh:
        p.set_fill(*INK)
        yy = p.wrap_text(MARGIN + 14, yy, "- " + st, 10.5, CW - 28, leading=13.5) - 4
        if yy < 74:
            break
    return p


def busy_color_sort(wb, kicker, heading, groups, instruction):
    """Color-sorting busy-book page: colored bins + item tokens to sort."""
    p, y, n = wb.page(kicker, heading)
    y = wb.instruction(p, y, instruction)
    # colored bins
    ncat = len(groups)
    binw = (CW - (ncat - 1) * 12) / ncat
    top = y - 4
    binh = 120
    for i, (label, color, items) in enumerate(groups):
        x = MARGIN + i * (binw + 12)
        p.set_fill(*color); p.round_rect(x, top - 30, binw, 30, 8, fill=True, stroke=False)
        p.set_fill(1, 1, 1); p.text_center(x + binw / 2, top - 20, label, 11.5, bold=True)
        p.set_stroke(*RULE); p.set_line_width(1.2); p.set_dash(4, 3)
        p.rect(x, top - 30 - binh, binw, binh, fill=False, stroke=True); p.clear_dash()
    # tokens to cut out
    ty = top - 30 - binh - 24
    p.set_fill(*wb.accent); p.text(MARGIN, ty, "Cut out and sort these:", 11, bold=True)
    ty -= 10
    all_items = []
    for (label, color, items) in groups:
        for it in items:
            all_items.append((it, color))
    random.Random(len(heading)).shuffle(all_items)
    cols = 4
    cellw = CW / cols
    for i, (it, color) in enumerate(all_items):
        col = i % cols; row = i // cols
        cx = MARGIN + col * cellw + cellw / 2
        cyy = ty - 18 - row * 44
        if cyy < 56:
            break
        p.set_stroke(*DASH); p.set_line_width(0.8); p.set_dash(3, 2)
        p.round_rect(cx - cellw / 2 + 6, cyy - 18, cellw - 12, 36, 6, fill=False, stroke=True)
        p.clear_dash()
        p.set_fill(*INK); p.text_center(cx, cyy - 4, it, 10.5, bold=True)
    return p


def scenario_match(wb, kicker, heading, pairs, left_label, right_label, instruction):
    """Match a situation (left) to a response/emotion (right)."""
    left = [a for a, b in pairs]
    right = [b for a, b in pairs]
    p = draw_line_matching(wb, kicker, heading, left, right, instruction)
    return p


def roleplay_cards(wb, kicker, heading, cards, intro):
    """Pretend-play / role-play cards: (role/title, what to do/say)."""
    p, y, n = wb.page(kicker, heading)
    y = wb.intro_box(p, y, intro)
    cols = 2
    cardw = (CW - 14) / cols
    cardh = (y - 60) / 3
    for i, (t, d) in enumerate(cards[:6]):
        col = i % cols; row = i // cols
        x = MARGIN + col * (cardw + 14)
        cy = y - row * (cardh + 4)
        p.set_fill(*CARD); p.round_rect(x, cy - cardh, cardw, cardh - 8, 10, fill=True, stroke=False)
        p.set_stroke(*wb.accent); p.set_line_width(1.3); p.set_dash(4, 3)
        p.round_rect(x, cy - cardh, cardw, cardh - 8, 10, fill=False, stroke=True); p.clear_dash()
        p.set_fill(*wb.accent); p.text(x + 14, cy - 22, t, 12, bold=True)
        p.set_fill(*SLATE); p.wrap_text(x + 14, cy - 40, d, 9.8, cardw - 26, leading=13)
    return p


def discussion_sort(wb, kicker, heading, categories, statements, instruction):
    """Sort statements into categories + a discussion prompt for older kids."""
    p, y, n = wb.page(kicker, heading)
    y = wb.instruction(p, y, instruction)
    # category headers
    ncat = len(categories)
    binw = (CW - (ncat - 1) * 12) / ncat
    for i, cat in enumerate(categories):
        x = MARGIN + i * (binw + 12)
        c = [wb.accent, CORAL, SKY][i % 3]
        p.set_fill(*c); p.round_rect(x, y - 28, binw, 28, 8, fill=True, stroke=False)
        p.set_fill(1, 1, 1); p.text_center(x + binw / 2, y - 19, cat, 11.5, bold=True)
    y -= 40
    # statements list with blank to write category
    for st in statements:
        if y < 120:
            break
        p.set_stroke(*RULE); p.set_line_width(0.8)
        p.rect(PW - MARGIN - 70, y - 14, 62, 20, fill=False, stroke=True)
        p.set_fill(*INK)
        p.wrap_text(MARGIN, y, st, 11, CW - 90, leading=14)
        y -= 30
    if y > 100:
        p.set_fill(*wb.accent); p.text(MARGIN, y, "Talk about it:", 11, bold=True)
        y = wb.write_lines(p, y - 14, 2, spacing=24)
    return p


def bingo_card(wb, title, words, size=5, seed=0, free_center=True):
    """One bingo card page (size x size grid) drawn from `words`."""
    p, n = wb._new()
    wb._footer(p, n)
    p.set_fill(*wb.accent); p.round_rect(MARGIN, PH - 96, CW, 60, 12, fill=True, stroke=False)
    p.set_fill(1, 1, 1); p.text_center(PW / 2, PH - 66, title, 22, bold=True)
    # letters BINGO
    letters = "BINGO"[:size] if size <= 5 else "BINGO"
    grid_w = min(CW, 460)
    cell = grid_w / size
    gx = (PW - grid_w) / 2
    gy = PH - 130
    rng = random.Random(seed)
    pick = rng.sample(words, min(size * size, len(words)))
    # if not enough words, allow repeats
    while len(pick) < size * size:
        pick.append(rng.choice(words))
    # header letters
    p.set_fill(*wb.accent2)
    for c in range(size):
        p.round_rect(gx + c * cell + 3, gy + 6, cell - 6, 28, 6, fill=True, stroke=False)
        p.set_fill(1, 1, 1)
        p.text_center(gx + c * cell + cell / 2, gy + 13, letters[c % len(letters)], 16, bold=True)
        p.set_fill(*wb.accent2)
    idx = 0
    for r in range(size):
        for c in range(size):
            x = gx + c * cell
            yy = gy - r * cell
            p.set_stroke(*INK); p.set_line_width(1.1)
            p.rect(x, yy - cell, cell, cell, fill=False, stroke=True)
            if free_center and size % 2 == 1 and r == size // 2 and c == size // 2:
                p.set_fill(*wb.accent)
                p.circle(x + cell / 2, yy - cell / 2, cell * 0.34, fill=True, stroke=False)
                p.set_fill(1, 1, 1); p.text_center(x + cell / 2, yy - cell / 2 - 4, "FREE", cell * 0.16, bold=True)
            else:
                word = pick[idx]
                p.set_fill(*INK)
                p.wrap_text(x + 5, yy - cell / 2 + 6, word, min(9, cell * 0.16), cell - 10,
                            center_x=x + cell / 2, leading=10)
            idx += 1
    p.set_fill(*GRAY); p.text_center(PW / 2, 60, "Mark each square you hear. Get a line to win!", 9)
    return p


def journal_page(wb, kicker, heading, prompts):
    p, y, n = wb.page(kicker, heading)
    for pr in prompts:
        if y < 100:
            break
        p.set_fill(*wb.accent2); p.circle(MARGIN + 5, y + 3, 5, fill=True, stroke=False)
        p.set_fill(*INK)
        endy = p.wrap_text(MARGIN + 18, y, pr, 11.5, CW - 18, bold=True, leading=15)
        y = wb.write_lines(p, endy - 6, 3, spacing=26)
        y -= 10
    return p


def answer_key(wb, kicker, heading, pairs):
    """pairs: list of (question/item, answer)."""
    p, y, n = wb.page(kicker, heading)
    y = wb.intro_box(p, y, "For grown-ups: here are suggested answers. Many activities have more than one good "
                           "answer - use these as a guide and talk through the child's thinking.")
    for i, (q, a) in enumerate(pairs, 1):
        if y < 60:
            break
        p.set_fill(*wb.accent); p.text(MARGIN, y, f"{i}.", 10.5, bold=True)
        p.set_fill(*INK)
        endy = p.wrap_text(MARGIN + 20, y, q + "  ->  " + a, 10.5, CW - 20, leading=14)
        y = endy - 8
    return p


def certificate(wb, accomplishment):
    p, n = wb._new()
    wb._footer(p, n)
    p.set_stroke(*wb.accent); p.set_line_width(3)
    p.round_rect(MARGIN, 120, CW, PH - 250, 18, fill=False, stroke=True)
    p.set_stroke(*wb.accent2); p.set_line_width(1.4)
    p.round_rect(MARGIN + 12, 132, CW - 24, PH - 274, 14, fill=False, stroke=True)
    p.star(PW / 2, PH - 180, 40, points=5, fill=False, stroke=True)
    p.set_fill(*wb.accent); p.text_center(PW / 2, PH - 240, "CERTIFICATE OF LEARNING", 24, bold=True)
    p.set_fill(*INK); p.text_center(PW / 2, PH - 275, "Proudly awarded to", 13)
    p.set_stroke(*RULE); p.set_line_width(0.8)
    p.line(PW / 2 - 150, PH - 320, PW / 2 + 150, PH - 320)
    p.set_fill(*GRAY); p.text_center(PW / 2, PH - 335, "(write your name)", 9)
    p.set_fill(*INK)
    p.wrap_text(0, PH - 375, accomplishment, 14, CW - 60, center_x=PW / 2, leading=20)
    return p
