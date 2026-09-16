"""
workbook.py — Reusable Christian homeschool activity components.

Builds on pdfkit.py. Provides a Workbook class with a consistent visual
theme plus a library of printable activity page builders:
 - cover, title/section pages, table of contents
 - memory verse (trace + copy lines)
 - coloring page prompts with simple line-art
 - letter/word tracing
 - matching (draw a line to match)
 - word search
 - maze
 - count & write / simple math with a Bible theme
 - dot-to-dot
 - fill-in-the-blank verse
 - prayer / gratitude journaling
 - crossword-style word bank
 - "I can draw" reflection boxes
"""

import math
import random
import pdfkit

# Theme palette
NAVY = (0.16, 0.22, 0.42)
GOLD = (0.85, 0.65, 0.13)
TEAL = (0.13, 0.55, 0.55)
CORAL = (0.90, 0.42, 0.38)
SKY = (0.53, 0.75, 0.90)
GREEN = (0.35, 0.62, 0.36)
PURPLE = (0.52, 0.38, 0.66)
INK = (0.12, 0.12, 0.15)
GRAY = (0.55, 0.55, 0.58)
LIGHT = (0.93, 0.95, 0.98)
LINE = (0.72, 0.74, 0.80)

MARGIN = 54.0
PW, PH = pdfkit.LETTER


class Workbook:
    def __init__(self, title, subtitle, ages, accent=NAVY, accent2=GOLD):
        self.doc = pdfkit.Document(title=title, author="Christian Homeschool Press")
        self.title = title
        self.subtitle = subtitle
        self.ages = ages
        self.accent = accent
        self.accent2 = accent2
        self.toc = []  # (title, page_number)

    def save(self, path):
        return self.doc.save(path)

    # ---------- shared chrome ----------
    def _page(self):
        return self.doc.add_page()

    def _footer(self, p, label):
        p.set_fill(*GRAY)
        p.text(MARGIN, 34, self.title, size=8)
        p.text_right(PW - MARGIN, 34, label, size=8)
        p.set_stroke(*LINE)
        p.set_line_width(0.6)
        p.line(MARGIN, 46, PW - MARGIN, 46)

    def _header(self, p, kicker, heading):
        p.set_fill(*self.accent)
        p.rect(0, PH - 96, PW, 96, fill=True, stroke=False)
        p.set_fill(*self.accent2)
        p.rect(0, PH - 100, PW, 4, fill=True, stroke=False)
        p.set_fill(1, 1, 1)
        p.text(MARGIN, PH - 44, kicker.upper(), size=11, bold=True)
        p.text(MARGIN, PH - 74, heading, size=22, bold=True)
        # little cross emblem
        cx, cy = PW - MARGIN - 14, PH - 58
        p.set_fill(*self.accent2)
        p.rect(cx - 3, cy - 16, 6, 32, fill=True, stroke=False)
        p.rect(cx - 12, cy + 2, 24, 6, fill=True, stroke=False)

    def _content_page(self, kicker, heading, footer_label):
        p = self._page()
        self._header(p, kicker, heading)
        self._footer(p, footer_label)
        return p

    # ---------- decorative helpers ----------
    def _cross(self, p, cx, cy, h, color):
        w = h * 0.62
        p.set_fill(*color)
        p.rect(cx - h * 0.09, cy - h / 2, h * 0.18, h, fill=True, stroke=False)
        p.rect(cx - w / 2, cy + h * 0.12, w, h * 0.18, fill=True, stroke=False)

    def _dove(self, p, cx, cy, s, color):
        p.set_fill(*color)
        # body
        p.polygon([(cx - s, cy), (cx + s * 0.2, cy - s * 0.5),
                   (cx + s, cy + s * 0.1), (cx + s * 0.1, cy + s * 0.2)],
                  fill=True, stroke=False)
        # wing
        p.polygon([(cx - s * 0.2, cy + s * 0.1), (cx + s * 0.3, cy + s * 0.7),
                   (cx + s * 0.5, cy + s * 0.05)], fill=True, stroke=False)

    def _sun(self, p, cx, cy, r, color):
        p.set_stroke(*color)
        p.set_line_width(2)
        for i in range(12):
            a = i * math.pi / 6
            p.line(cx + r * 1.25 * math.cos(a), cy + r * 1.25 * math.sin(a),
                   cx + r * 1.7 * math.cos(a), cy + r * 1.7 * math.sin(a))
        p.set_fill(*color)
        p.circle(cx, cy, r, fill=True, stroke=False)

    # ---------- COVER ----------
    def cover(self):
        p = self._page()
        # background bands
        p.set_fill(*self.accent)
        p.rect(0, 0, PW, PH, fill=True, stroke=False)
        p.set_fill(*self.accent2)
        p.rect(0, PH - 150, PW, 150, fill=True, stroke=False)
        p.set_fill(1, 1, 1)
        p.rect(40, 120, PW - 80, PH - 320, fill=True, stroke=False)

        # top decorative sky with sun and doves
        p.set_fill(*SKY)
        p.rect(40, PH - 300, PW - 80, 148, fill=True, stroke=False)
        self._sun(p, 150, PH - 210, 26, GOLD)
        self._dove(p, 360, PH - 200, 26, (1, 1, 1))
        self._dove(p, 440, PH - 240, 20, (1, 1, 1))
        # rolling hills
        p.set_fill(*GREEN)
        p.polygon([(40, PH - 300), (200, PH - 260), (360, PH - 300),
                   (520, PH - 265), (PW - 40, PH - 300), (PW - 40, PH - 302),
                   (40, PH - 302)], fill=True, stroke=False)

        # big cross in center
        self._cross(p, PW / 2, PH / 2 - 20, 150, self.accent)

        # title text
        p.set_fill(*NAVY)
        p.wrap_text(0, PH - 400, self.title, 30, PW - 160, bold=True, center_x=PW / 2)
        p.set_fill(*self.accent2)
        p.rect(PW / 2 - 60, 260, 120, 3, fill=True, stroke=False)
        p.set_fill(*INK)
        p.wrap_text(0, 235, self.subtitle, 14, PW - 180, center_x=PW / 2)

        # age badge
        p.set_fill(*CORAL)
        p.round_rect(PW / 2 - 85, 150, 170, 40, 12, fill=True, stroke=False)
        p.set_fill(1, 1, 1)
        p.text_center(PW / 2, 163, f"For {self.ages}", 15, bold=True)

        # bottom tag
        p.set_fill(1, 1, 1)
        p.text_center(PW / 2, 70, "Christian Homeschool Press  *  Faith  *  Learning  *  Fun", 11, bold=True)
        p.text_center(PW / 2, 52, "Reproducible for home and classroom use", 9)
        return p

    # ---------- WELCOME / HOW TO USE ----------
    def welcome(self, intro_lines, verse, verse_ref):
        p = self._content_page("Welcome", "For Parents & Teachers", "Welcome")
        y = PH - 140
        p.set_fill(*INK)
        for para in intro_lines:
            y = p.wrap_text(MARGIN, y, para, 12, PW - 2 * MARGIN)
            y -= 8
        # verse card
        y -= 10
        card_h = 110
        p.set_fill(*LIGHT)
        p.round_rect(MARGIN, y - card_h, PW - 2 * MARGIN, card_h, 12, fill=True, stroke=False)
        p.set_stroke(*self.accent2)
        p.set_line_width(2)
        p.round_rect(MARGIN, y - card_h, PW - 2 * MARGIN, card_h, 12, fill=False, stroke=True)
        p.set_fill(*self.accent)
        p.text_center(PW / 2, y - 34, "Our Family Verse", 13, bold=True)
        p.set_fill(*INK)
        p.wrap_text(0, y - 58, '"' + verse + '"', 13, PW - 2 * MARGIN - 40,
                    center_x=PW / 2)
        p.set_fill(*self.accent)
        p.text_center(PW / 2, y - card_h + 16, "— " + verse_ref, 11, bold=True)
        return p

    def table_of_contents(self):
        p = self._content_page("Contents", "What's Inside", "Contents")
        y = PH - 150
        p.set_fill(*INK)
        for i, (t, pg) in enumerate(self.toc, start=1):
            if y < 90:
                break
            p.set_fill(*self.accent)
            p.circle(MARGIN + 8, y + 4, 9, fill=True, stroke=False)
            p.set_fill(1, 1, 1)
            p.text_center(MARGIN + 8, y + 0.5, str(i), 9, bold=True)
            p.set_fill(*INK)
            p.text(MARGIN + 28, y, t, 12)
            p.set_fill(*GRAY)
            p.text_right(PW - MARGIN, y, f"page {pg}", 11)
            p.set_stroke(*LINE)
            p.set_line_width(0.5)
            p.set_dash(1, 3)
            p.line(MARGIN + 28 + pdfkit.text_width(t, 12) + 8, y + 3,
                   PW - MARGIN - 60, y + 3)
            p.clear_dash()
            y -= 26
        return p

    # ---------- ACTIVITY BUILDERS ----------
    def _prompt_box(self, p, y, text):
        p.set_fill(*LIGHT)
        p.round_rect(MARGIN, y - 34, PW - 2 * MARGIN, 34, 8, fill=True, stroke=False)
        p.set_fill(*self.accent)
        p.text(MARGIN + 14, y - 22, text, 12, bold=True)
        return y - 50

    def memory_verse(self, kicker, verse, ref, note=""):
        p = self._content_page(kicker, "Memory Verse", "Memory Verse")
        y = PH - 140
        # display verse
        p.set_fill(*self.accent)
        p.round_rect(MARGIN, y - 90, PW - 2 * MARGIN, 90, 12, fill=True, stroke=False)
        p.set_fill(1, 1, 1)
        end = p.wrap_text(0, y - 30, '"' + verse + '"', 15, PW - 2 * MARGIN - 40,
                          center_x=PW / 2, bold=True)
        p.set_fill(*self.accent2)
        p.text_center(PW / 2, y - 78, "— " + ref, 12, bold=True)
        y -= 120
        p.set_fill(*INK)
        p.text(MARGIN, y, "Trace the words:", 12, bold=True)
        y -= 8
        # light-gray tracing lines of the verse words
        words = (verse + " " + ref).split()
        line = ""
        for w in words:
            trial = (line + " " + w).strip()
            if pdfkit.text_width(trial, 18, bold=True) < PW - 2 * MARGIN:
                line = trial
            else:
                y -= 34
                p.set_fill(0.78, 0.80, 0.85)
                p.text(MARGIN, y, line, 18, bold=True)
                line = w
        if line:
            y -= 34
            p.set_fill(0.78, 0.80, 0.85)
            p.text(MARGIN, y, line, 18, bold=True)
        y -= 40
        p.set_fill(*INK)
        p.text(MARGIN, y, "Now write it in your best handwriting:", 12, bold=True)
        y -= 12
        self._writing_lines(p, y, count=4)
        if note:
            p.set_fill(*GRAY)
            p.text(MARGIN, 60, note, 10, italic=True)
        return p

    def _writing_lines(self, p, y, count=5, spacing=34):
        for i in range(count):
            yy = y - i * spacing
            # top guide
            p.set_stroke(*LINE)
            p.set_line_width(0.6)
            p.line(MARGIN, yy, PW - MARGIN, yy)
            # dashed midline
            p.set_dash(2, 4)
            p.line(MARGIN, yy - spacing * 0.5, PW - MARGIN, yy - spacing * 0.5)
            p.clear_dash()

    def tracing(self, kicker, heading, items, instruction):
        p = self._content_page(kicker, heading, heading)
        y = PH - 132
        y = self._prompt_box(p, y, instruction)
        for word in items:
            # trace version (light) then blank line
            p.set_fill(0.78, 0.80, 0.85)
            p.text(MARGIN, y - 24, word, 26, bold=True)
            p.set_stroke(*LINE)
            p.set_line_width(0.8)
            p.line(MARGIN, y - 30, PW - MARGIN, y - 30)
            p.set_dash(2, 4)
            p.line(MARGIN, y - 14, PW - MARGIN, y - 14)
            p.clear_dash()
            y -= 62
            if y < 100:
                break
        return p

    def coloring(self, kicker, heading, caption, scene):
        p = self._content_page(kicker, heading, "Coloring")
        p.set_fill(*INK)
        p.text_center(PW / 2, PH - 128, caption, 13, bold=True)
        # frame
        fx, fy, fw, fh = MARGIN, 90, PW - 2 * MARGIN, PH - 260
        p.set_stroke(*self.accent)
        p.set_line_width(2)
        p.round_rect(fx, fy, fw, fh, 14, fill=False, stroke=True)
        # scene drawn as black line art centered
        cx, cy = PW / 2, fy + fh / 2
        p.set_stroke(*INK)
        p.set_line_width(1.6)
        scene(p, cx, cy)
        p.set_fill(*GRAY)
        p.text_center(PW / 2, 66, "Color the picture with your favorite colors!", 10, italic=True)
        return p

    def matching(self, kicker, heading, left_items, right_items, instruction):
        p = self._content_page(kicker, heading, "Matching")
        y = PH - 132
        y = self._prompt_box(p, y, instruction)
        n = min(len(left_items), len(right_items))
        top = y - 10
        row_h = (top - 110) / max(n, 1)
        rr = list(right_items)
        random.shuffle(rr)
        lx = MARGIN + 20
        rx = PW - MARGIN - 20
        for i in range(n):
            ly = top - i * row_h
            p.set_fill(*self.accent)
            p.circle(lx, ly, 5, fill=True, stroke=False)
            p.set_fill(*INK)
            p.text(lx + 14, ly - 4, left_items[i], 13)
            # right dot + text
            ry = top - i * row_h
            tw = pdfkit.text_width(rr[i], 13)
            p.text(rx - 14 - tw, ry - 4, rr[i], 13)
            p.set_fill(*self.accent2)
            p.circle(rx, ry, 5, fill=True, stroke=False)
        return p

    def word_search(self, kicker, heading, words, size=11):
        p = self._content_page(kicker, heading, "Word Search")
        words = [w.upper().replace(" ", "") for w in words]
        grid = [[None] * size for _ in range(size)]
        dirs = [(1, 0), (0, 1), (1, 1), (1, -1)]
        placed = []
        rng = random.Random(sum(ord(c) for w in words for c in w) + size)
        for w in words:
            for _ in range(200):
                d = rng.choice(dirs)
                if d[0] >= 0:
                    maxc = size - len(w) if d[0] else size - 1
                else:
                    maxc = size - 1
                r0 = rng.randint(0, size - 1)
                c0 = rng.randint(0, size - 1)
                cells, ok = [], True
                for k in range(len(w)):
                    rr = r0 + d[1] * k
                    cc = c0 + d[0] * k
                    if not (0 <= rr < size and 0 <= cc < size):
                        ok = False
                        break
                    if grid[rr][cc] not in (None, w[k]):
                        ok = False
                        break
                    cells.append((rr, cc))
                if ok:
                    for (rr, cc), ch in zip(cells, w):
                        grid[rr][cc] = ch
                    placed.append(w)
                    break
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for r in range(size):
            for c in range(size):
                if grid[r][c] is None:
                    grid[r][c] = rng.choice(letters)
        # draw grid
        gw = PW - 2 * MARGIN - 150
        cell = gw / size
        gx = MARGIN
        gy = PH - 150
        p.set_fill(*INK)
        for r in range(size):
            for c in range(size):
                x = gx + c * cell
                yy = gy - r * cell
                p.text_center(x + cell / 2, yy - cell / 2 - 4, grid[r][c], 12, bold=True)
        p.set_stroke(*LINE)
        p.set_line_width(0.6)
        for i in range(size + 1):
            p.line(gx, gy - i * cell, gx + size * cell, gy - i * cell)
            p.line(gx + i * cell, gy, gx + i * cell, gy - size * cell)
        # word list
        listx = gx + size * cell + 20
        p.set_fill(*self.accent)
        p.text(listx, gy - 6, "Find these:", 12, bold=True)
        yy = gy - 28
        for w in words:
            p.set_fill(*INK)
            p.text(listx, yy, "[ ] " + w, 11)
            yy -= 20
        return p

    def maze(self, kicker, heading, caption, cols=9, rows=12, seed=1):
        p = self._content_page(kicker, heading, "Maze")
        p.set_fill(*INK)
        p.text_center(PW / 2, PH - 128, caption, 12, bold=True)
        rng = random.Random(seed)
        # DFS maze
        walls_v = [[True] * (cols + 1) for _ in range(rows)]
        walls_h = [[True] * cols for _ in range(rows + 1)]
        visited = [[False] * cols for _ in range(rows)]
        stack = [(0, 0)]
        visited[0][0] = True
        while stack:
            r, c = stack[-1]
            nb = []
            if r > 0 and not visited[r - 1][c]:
                nb.append(('N', r - 1, c))
            if r < rows - 1 and not visited[r + 1][c]:
                nb.append(('S', r + 1, c))
            if c > 0 and not visited[r][c - 1]:
                nb.append(('W', r, c - 1))
            if c < cols - 1 and not visited[r][c + 1]:
                nb.append(('E', r, c + 1))
            if not nb:
                stack.pop()
                continue
            d, nr, nc = rng.choice(nb)
            if d == 'N':
                walls_h[r][c] = False
            elif d == 'S':
                walls_h[r + 1][c] = False
            elif d == 'W':
                walls_v[r][c] = False
            elif d == 'E':
                walls_v[r][c + 1] = False
            visited[nr][nc] = True
            stack.append((nr, nc))
        # entrance/exit
        walls_v[0][0] = False
        walls_v[rows - 1][cols] = False
        # draw
        area_w = PW - 2 * MARGIN
        area_h = PH - 320
        cell = min(area_w / cols, area_h / rows)
        ox = (PW - cell * cols) / 2
        oy = PH - 170
        p.set_stroke(*INK)
        p.set_line_width(1.8)
        for r in range(rows):
            for c in range(cols + 1):
                if walls_v[r][c]:
                    x = ox + c * cell
                    p.line(x, oy - r * cell, x, oy - (r + 1) * cell)
        for r in range(rows + 1):
            for c in range(cols):
                if walls_h[r][c]:
                    yv = oy - r * cell
                    p.line(ox + c * cell, yv, ox + (c + 1) * cell, yv)
        # start/end labels
        p.set_fill(*GREEN)
        p.text(ox - 34, oy - cell / 2 - 4, "START", 9, bold=True)
        p.set_fill(*CORAL)
        p.text(ox + cols * cell + 6, oy - (rows - 0.5) * cell - 4, "END", 9, bold=True)
        return p

    def count_and_write(self, kicker, heading, rows, instruction):
        # rows: list of (label, count, draw_icon_fn)
        p = self._content_page(kicker, heading, "Count & Write")
        y = PH - 132
        y = self._prompt_box(p, y, instruction)
        row_h = 78
        for (label, count, icon) in rows:
            if y < 120:
                break
            p.set_fill(*INK)
            p.text(MARGIN, y - 16, label, 12, bold=True)
            # icons
            ix = MARGIN + 4
            for i in range(count):
                icon(p, ix + 18, y - 44, 14)
                ix += 44
            # answer box
            p.set_stroke(*self.accent)
            p.set_line_width(1.5)
            p.round_rect(PW - MARGIN - 56, y - 58, 46, 46, 8, fill=False, stroke=True)
            y -= row_h
        return p

    def fill_blank(self, kicker, heading, items, instruction, word_bank=None):
        # items: list of (before, blank_answer, after)
        p = self._content_page(kicker, heading, "Fill the Blank")
        y = PH - 132
        y = self._prompt_box(p, y, instruction)
        if word_bank:
            p.set_fill(*LIGHT)
            p.round_rect(MARGIN, y - 30, PW - 2 * MARGIN, 30, 8, fill=True, stroke=False)
            p.set_fill(*self.accent)
            p.text_center(PW / 2, y - 20, "Word Bank:  " + "   ".join(word_bank), 12, bold=True)
            y -= 46
        for (before, answer, after) in items:
            p.set_fill(*INK)
            x = MARGIN
            p.text(x, y, before + " ", 13)
            x += pdfkit.text_width(before + " ", 13)
            # blank line
            blank_w = max(90, pdfkit.text_width(answer, 13) + 30)
            p.set_stroke(*self.accent)
            p.set_line_width(1)
            p.line(x, y - 3, x + blank_w, y - 3)
            x += blank_w + 6
            p.text(x, y, after, 13)
            y -= 44
            if y < 100:
                break
        return p

    def journal(self, kicker, heading, prompts, draw_box=True):
        p = self._content_page(kicker, heading, "Journal")
        y = PH - 132
        for pr in prompts:
            p.set_fill(*self.accent)
            self._cross(p, MARGIN + 8, y - 4, 16, self.accent2)
            p.set_fill(*INK)
            p.wrap_text(MARGIN + 26, y, pr, 12, PW - 2 * MARGIN - 26, bold=True)
            y -= 24
            self._writing_lines(p, y, count=3, spacing=30)
            y -= 3 * 30 + 16
            if y < 130:
                break
        if draw_box and y > 120:
            p.set_fill(*self.accent)
            p.text(MARGIN, y, "Draw a picture:", 12, bold=True)
            p.set_stroke(*LINE)
            p.set_line_width(1.2)
            p.round_rect(MARGIN, 70, PW - 2 * MARGIN, y - 90, 10, fill=False, stroke=True)
        return p

    def dot_to_dot(self, kicker, heading, caption, points, labels=True):
        p = self._content_page(kicker, heading, "Dot to Dot")
        p.set_fill(*INK)
        p.text_center(PW / 2, PH - 128, caption, 12, bold=True)
        p.set_fill(*self.accent)
        for i, (x, y) in enumerate(points, start=1):
            p.circle(x, y, 3.2, fill=True, stroke=False)
            if labels:
                p.set_fill(*INK)
                p.text(x + 6, y + 4, str(i), 11, bold=True)
                p.set_fill(*self.accent)
        p.set_fill(*GRAY)
        p.text_center(PW / 2, 66, "Connect the dots in order, then color your picture!", 10, italic=True)
        return p

    def true_false(self, kicker, heading, statements, instruction):
        p = self._content_page(kicker, heading, "True or False")
        y = PH - 132
        y = self._prompt_box(p, y, instruction)
        for st in statements:
            p.set_fill(*INK)
            endy = p.wrap_text(MARGIN, y, st, 12, PW - 2 * MARGIN - 130)
            # T / F bubbles
            bx = PW - MARGIN - 120
            p.set_stroke(*self.accent)
            p.set_line_width(1.2)
            p.circle(bx, y - 3, 8, fill=False, stroke=True)
            p.set_fill(*INK)
            p.text(bx + 12, y - 7, "True", 11)
            p.set_stroke(*self.accent)
            p.circle(bx + 60, y - 3, 8, fill=False, stroke=True)
            p.set_fill(*INK)
            p.text(bx + 72, y - 7, "False", 11)
            y = min(endy, y - 20) - 18
            if y < 90:
                break
        return p


# ---------- small reusable line-art icons ----------
def icon_star(p, x, y, s):
    p.star(x, y, s, points=5, fill=False, stroke=True)

def icon_heart(p, x, y, s):
    p.heart(x, y, s * 0.9, fill=False, stroke=True)

def icon_fish(p, x, y, s):
    p.polygon([(x - s, y), (x + s * 0.4, y + s * 0.6), (x + s * 0.4, y - s * 0.6)],
              fill=False, stroke=True)
    p.polygon([(x + s * 0.4, y), (x + s, y + s * 0.5), (x + s, y - s * 0.5)],
              fill=False, stroke=True)

def icon_sheep(p, x, y, s):
    p.circle(x, y, s * 0.7, fill=False, stroke=True)
    p.circle(x - s * 0.6, y + s * 0.2, s * 0.35, fill=False, stroke=True)
    p.line(x - s * 0.4, y - s * 0.6, x - s * 0.4, y - s)
    p.line(x + s * 0.4, y - s * 0.6, x + s * 0.4, y - s)

def icon_leaf(p, x, y, s):
    p.polygon([(x, y - s), (x + s * 0.7, y), (x, y + s), (x - s * 0.7, y)],
              fill=False, stroke=True)

def icon_dove(p, x, y, s):
    p.polygon([(x - s, y), (x + s * 0.2, y - s * 0.5), (x + s, y + s * 0.1)],
              fill=False, stroke=True)


# ---------- coloring scene generators (black line art) ----------
def scene_ark(p, cx, cy):
    # Noah's ark: boat hull + cabin + rainbow arc
    p.line(cx - 120, cy - 20, cx + 120, cy - 20)
    p.polygon([(cx - 120, cy - 20), (cx - 150, cy - 70), (cx + 150, cy - 70),
               (cx + 120, cy - 20)], fill=False, stroke=True)
    p.rect(cx - 80, cy - 20, 160, 60)
    p.polygon([(cx - 95, cy + 40), (cx, cy + 90), (cx + 95, cy + 40)], fill=False, stroke=True)
    # windows
    for dx in (-50, 0, 50):
        p.circle(cx + dx, cy + 8, 12)
    # rainbow arcs
    for i, r in enumerate((150, 135, 120)):
        p.set_line_width(1.4)
        # approximate arc with small segments
        import math as _m
        pts = []
        for a in range(0, 181, 12):
            rad = _m.radians(a)
            pts.append((cx + r * _m.cos(rad), cy + 95 + r * _m.sin(rad) * 0.55))
        p.polygon(pts, fill=False, stroke=True, close=False)
    # water waves
    for wy in (cy - 90, cy - 105):
        pts = []
        for xx in range(int(cx - 150), int(cx + 151), 20):
            pts.append((xx, wy + (6 if (xx // 20) % 2 == 0 else -6)))
        p.polygon(pts, fill=False, stroke=True, close=False)

def scene_creation(p, cx, cy):
    # sun, hills, tree, flowers, birds
    p.circle(cx - 110, cy + 90, 34)
    import math as _m
    for i in range(12):
        a = i * _m.pi / 6
        p.line(cx - 110 + 40 * _m.cos(a), cy + 90 + 40 * _m.sin(a),
               cx - 110 + 56 * _m.cos(a), cy + 90 + 56 * _m.sin(a))
    # hills
    p.polygon([(cx - 160, cy - 40), (cx - 60, cy + 20), (cx + 40, cy - 30),
               (cx + 160, cy + 25), (cx + 160, cy - 40)], fill=False, stroke=True, close=False)
    p.line(cx - 160, cy - 40, cx + 160, cy - 40)
    # tree
    p.rect(cx + 60, cy - 40, 16, 60)
    p.circle(cx + 68, cy + 40, 40)
    # flowers
    for dx in (-120, -90, -60):
        p.circle(cx + dx, cy - 30, 8)
        p.line(cx + dx, cy - 38, cx + dx, cy - 60)
    # birds
    for (bx, by) in ((cx + 20, cy + 110), (cx + 60, cy + 120)):
        p.polygon([(bx - 12, by), (bx, by + 8), (bx + 12, by)], fill=False, stroke=True, close=False)

def scene_shepherd(p, cx, cy):
    # shepherd staff + sheep + heart
    p.line(cx - 90, cy - 70, cx - 90, cy + 80)
    import math as _m
    pts = []
    for a in range(-90, 120, 20):
        rad = _m.radians(a)
        pts.append((cx - 90 + 22 + 22 * _m.cos(rad), cy + 80 + 22 * _m.sin(rad)))
    p.polygon(pts, fill=False, stroke=True, close=False)
    # sheep flock
    for (sx, sy) in ((cx + 20, cy - 20), (cx + 70, cy - 40), (cx + 40, cy - 60)):
        p.circle(sx, sy, 26)
        p.circle(sx - 24, sy + 8, 12)
        p.line(sx - 12, sy - 26, sx - 12, sy - 42)
        p.line(sx + 12, sy - 26, sx + 12, sy - 42)
    p.heart(cx - 30, cy + 70, 20, fill=False, stroke=True)

def scene_praying(p, cx, cy):
    # praying hands (simplified) with rays + heart
    p.polygon([(cx - 30, cy - 80), (cx - 6, cy + 60), (cx - 2, cy + 62),
               (cx - 2, cy - 80)], fill=False, stroke=True)
    p.polygon([(cx + 30, cy - 80), (cx + 6, cy + 60), (cx + 2, cy + 62),
               (cx + 2, cy - 80)], fill=False, stroke=True)
    p.rect(cx - 34, cy - 92, 68, 16)
    import math as _m
    for i in range(9):
        a = _m.radians(20 + i * 17.5)
        p.line(cx + 90 * _m.cos(a), cy + 70 + 90 * _m.sin(a),
               cx + 120 * _m.cos(a), cy + 70 + 120 * _m.sin(a))

def scene_cross_hill(p, cx, cy):
    # three crosses on a hill with sun
    p.polygon([(cx - 160, cy - 70), (cx, cy - 20), (cx + 160, cy - 70),
               (cx + 160, cy - 74), (cx - 160, cy - 74)], fill=False, stroke=True, close=False)
    def cross(x, base, h):
        p.rect(x - 5, base, 10, h)
        p.rect(x - 22, base + h * 0.66, 44, 10)
    cross(cx, cy - 40, 120)
    cross(cx - 90, cy - 55, 80)
    cross(cx + 90, cy - 55, 80)
    p.circle(cx, cy + 120, 30)
