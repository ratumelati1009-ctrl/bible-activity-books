"""
pdfkit.py — A tiny, dependency-free PDF writer.

Implements just enough of the PDF spec to produce multi-page, US-Letter
documents with vector graphics, text (built-in Helvetica/Times fonts),
lines, rectangles, circles, and simple filled shapes. No external libraries.

Coordinate system: origin (0,0) is bottom-left, units are PDF points (72/in).
Helper methods on Page expose a friendlier top-left-ish drawing model where
convenient, but raw PDF coords are used throughout.
"""

import zlib


# US Letter page size in points
LETTER = (612.0, 792.0)

# Widths (per 1000 units) for the standard 14 fonts we use, Helvetica family.
# We only need approximate widths for centering; use a compact table.
_HELV_WIDTHS = {
    ' ': 278, '!': 278, '"': 355, '#': 556, '$': 556, '%': 889, '&': 667,
    "'": 191, '(': 333, ')': 333, '*': 389, '+': 584, ',': 278, '-': 333,
    '.': 278, '/': 278, '0': 556, '1': 556, '2': 556, '3': 556, '4': 556,
    '5': 556, '6': 556, '7': 556, '8': 556, '9': 556, ':': 278, ';': 278,
    '<': 584, '=': 584, '>': 584, '?': 556, '@': 1015, 'A': 667, 'B': 667,
    'C': 722, 'D': 722, 'E': 667, 'F': 611, 'G': 778, 'H': 722, 'I': 278,
    'J': 500, 'K': 667, 'L': 556, 'M': 833, 'N': 722, 'O': 778, 'P': 667,
    'Q': 778, 'R': 722, 'S': 667, 'T': 611, 'U': 722, 'V': 667, 'W': 944,
    'X': 667, 'Y': 667, 'Z': 611, '[': 278, '\\': 278, ']': 278, '^': 469,
    '_': 556, '`': 333, 'a': 556, 'b': 556, 'c': 500, 'd': 556, 'e': 556,
    'f': 278, 'g': 556, 'h': 556, 'i': 222, 'j': 222, 'k': 500, 'l': 222,
    'm': 833, 'n': 556, 'o': 556, 'p': 556, 'q': 556, 'r': 333, 's': 500,
    't': 278, 'u': 556, 'v': 500, 'w': 722, 'x': 500, 'y': 500, 'z': 500,
    '{': 334, '|': 260, '}': 334, '~': 584,
}
# Bold is slightly wider; use a multiplier approximation.
_HELVB_WIDTHS = {k: int(v * 1.02) + (0 if v > 600 else 20) for k, v in _HELV_WIDTHS.items()}


def _esc(s):
    return s.replace('\\', r'\\').replace('(', r'\(').replace(')', r'\)')


def text_width(s, size, bold=False):
    table = _HELVB_WIDTHS if bold else _HELV_WIDTHS
    total = 0
    for ch in s:
        total += table.get(ch, 556)
    return total / 1000.0 * size


class Page:
    def __init__(self, doc, width, height):
        self.doc = doc
        self.width = width
        self.height = height
        self._ops = []

    # ---- state ----
    def set_fill(self, r, g, b):
        self._ops.append(f"{r:.3f} {g:.3f} {b:.3f} rg")

    def set_stroke(self, r, g, b):
        self._ops.append(f"{r:.3f} {g:.3f} {b:.3f} RG")

    def set_line_width(self, w):
        self._ops.append(f"{w:.2f} w")

    def set_dash(self, on=6, off=4):
        self._ops.append(f"[{on} {off}] 0 d")

    def clear_dash(self):
        self._ops.append("[] 0 d")

    # ---- primitives ----
    def line(self, x1, y1, x2, y2):
        self._ops.append(f"{x1:.2f} {y1:.2f} m {x2:.2f} {y2:.2f} l S")

    def rect(self, x, y, w, h, fill=False, stroke=True):
        op = "f" if (fill and not stroke) else ("B" if (fill and stroke) else "S")
        self._ops.append(f"{x:.2f} {y:.2f} {w:.2f} {h:.2f} re {op}")

    def round_rect(self, x, y, w, h, r, fill=False, stroke=True):
        k = 0.5523 * r
        x2, y2 = x + w, y + h
        p = []
        p.append(f"{x + r:.2f} {y:.2f} m")
        p.append(f"{x2 - r:.2f} {y:.2f} l")
        p.append(f"{x2 - r + k:.2f} {y:.2f} {x2:.2f} {y + r - k:.2f} {x2:.2f} {y + r:.2f} c")
        p.append(f"{x2:.2f} {y2 - r:.2f} l")
        p.append(f"{x2:.2f} {y2 - r + k:.2f} {x2 - r + k:.2f} {y2:.2f} {x2 - r:.2f} {y2:.2f} c")
        p.append(f"{x + r:.2f} {y2:.2f} l")
        p.append(f"{x + r - k:.2f} {y2:.2f} {x:.2f} {y2 - r + k:.2f} {x:.2f} {y2 - r:.2f} c")
        p.append(f"{x:.2f} {y + r:.2f} l")
        p.append(f"{x:.2f} {y + r - k:.2f} {x + r - k:.2f} {y:.2f} {x + r:.2f} {y:.2f} c")
        op = "f" if (fill and not stroke) else ("B" if (fill and stroke) else "S")
        self._ops.append(" ".join(p) + " " + op)

    def circle(self, cx, cy, r, fill=False, stroke=True):
        k = 0.5523 * r
        p = []
        p.append(f"{cx + r:.2f} {cy:.2f} m")
        p.append(f"{cx + r:.2f} {cy + k:.2f} {cx + k:.2f} {cy + r:.2f} {cx:.2f} {cy + r:.2f} c")
        p.append(f"{cx - k:.2f} {cy + r:.2f} {cx - r:.2f} {cy + k:.2f} {cx - r:.2f} {cy:.2f} c")
        p.append(f"{cx - r:.2f} {cy - k:.2f} {cx - k:.2f} {cy - r:.2f} {cx:.2f} {cy - r:.2f} c")
        p.append(f"{cx + k:.2f} {cy - r:.2f} {cx + r:.2f} {cy - k:.2f} {cx + r:.2f} {cy:.2f} c")
        op = "f" if (fill and not stroke) else ("B" if (fill and stroke) else "S")
        self._ops.append(" ".join(p) + " " + op)

    def polygon(self, pts, fill=False, stroke=True, close=True):
        if not pts:
            return
        p = [f"{pts[0][0]:.2f} {pts[0][1]:.2f} m"]
        for (x, y) in pts[1:]:
            p.append(f"{x:.2f} {y:.2f} l")
        if close:
            p.append("h")
        op = "f" if (fill and not stroke) else ("B" if (fill and stroke) else "S")
        self._ops.append(" ".join(p) + " " + op)

    def star(self, cx, cy, r_out, r_in=None, points=5, fill=True, stroke=True):
        import math
        if r_in is None:
            r_in = r_out * 0.42
        pts = []
        for i in range(points * 2):
            r = r_out if i % 2 == 0 else r_in
            a = math.pi / 2 + i * math.pi / points
            pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
        self.polygon(pts, fill=fill, stroke=stroke)

    def heart(self, cx, cy, size, fill=True, stroke=True):
        s = size
        p = []
        p.append(f"{cx:.2f} {cy - s*0.6:.2f} m")
        p.append(f"{cx - s:.2f} {cy + s*0.35:.2f} {cx - s*0.9:.2f} {cy + s*0.9:.2f} {cx:.2f} {cy + s*0.4:.2f} c")
        p.append(f"{cx + s*0.9:.2f} {cy + s*0.9:.2f} {cx + s:.2f} {cy + s*0.35:.2f} {cx:.2f} {cy - s*0.6:.2f} c")
        op = "f" if (fill and not stroke) else ("B" if (fill and stroke) else "S")
        self._ops.append(" ".join(p) + " " + op)

    # ---- text ----
    def text(self, x, y, s, size=12, bold=False, italic=False):
        font = "F2" if bold else ("F3" if italic else "F1")
        self._ops.append(
            f"BT /{font} {size:.2f} Tf {x:.2f} {y:.2f} Td ({_esc(s)}) Tj ET"
        )

    def text_center(self, cx, y, s, size=12, bold=False, italic=False):
        w = text_width(s, size, bold=bold)
        self.text(cx - w / 2.0, y, s, size=size, bold=bold, italic=italic)

    def text_right(self, rx, y, s, size=12, bold=False):
        w = text_width(s, size, bold=bold)
        self.text(rx - w, y, s, size=size, bold=bold)

    def wrap_text(self, x, y, s, size, max_width, leading=None, bold=False, center_x=None):
        if leading is None:
            leading = size * 1.35
        words = s.split()
        lines, cur = [], ""
        for w in words:
            trial = (cur + " " + w).strip()
            if text_width(trial, size, bold=bold) <= max_width or not cur:
                cur = trial
            else:
                lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
        cy = y
        for ln in lines:
            if center_x is not None:
                self.text_center(center_x, cy, ln, size=size, bold=bold)
            else:
                self.text(x, cy, ln, size=size, bold=bold)
            cy -= leading
        return cy  # y after last line


class Document:
    def __init__(self, title="Workbook", author="Christian Homeschool"):
        self.pages = []
        self.title = title
        self.author = author

    def add_page(self, width=LETTER[0], height=LETTER[1]):
        p = Page(self, width, height)
        self.pages.append(p)
        return p

    def save(self, path):
        objects = []  # list of byte strings (object bodies, without "N 0 obj")

        def add_obj(body):
            objects.append(body)
            return len(objects)  # 1-based object number

        # Reserve: 1=Catalog, 2=Pages, 3..=fonts then pages+contents
        # Fonts
        font1 = add_obj(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>")
        font2 = add_obj(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>")
        font3 = add_obj(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Oblique /Encoding /WinAnsiEncoding >>")

        page_obj_nums = []
        content_obj_nums = []
        for pg in self.pages:
            stream = ("\n".join(pg._ops)).encode("latin-1", "replace")
            comp = zlib.compress(stream)
            body = (b"<< /Length " + str(len(comp)).encode() +
                    b" /Filter /FlateDecode >>\nstream\n" + comp + b"\nendstream")
            cnum = add_obj(body)
            content_obj_nums.append(cnum)
            page_obj_nums.append(None)  # placeholder, fill after we know pages obj num

        # Pages tree object number (create now, fill kids later)
        pages_num = add_obj(b"")  # placeholder body

        # Now create page objects referencing pages_num
        real_page_nums = []
        for i, pg in enumerate(self.pages):
            body = (
                f"<< /Type /Page /Parent {pages_num} 0 R "
                f"/MediaBox [0 0 {pg.width:.2f} {pg.height:.2f}] "
                f"/Resources << /Font << /F1 {font1} 0 R /F2 {font2} 0 R /F3 {font3} 0 R >> >> "
                f"/Contents {content_obj_nums[i]} 0 R >>"
            ).encode()
            real_page_nums.append(add_obj(body))

        kids = " ".join(f"{n} 0 R" for n in real_page_nums)
        objects[pages_num - 1] = (
            f"<< /Type /Pages /Count {len(real_page_nums)} /Kids [{kids}] >>".encode()
        )

        catalog_num = add_obj(f"<< /Type /Catalog /Pages {pages_num} 0 R >>".encode())

        info_num = add_obj(
            ("<< /Title (" + _esc(self.title) + ") /Author (" + _esc(self.author) +
             ") /Producer (pdfkit.py) >>").encode()
        )

        # Serialize
        out = bytearray()
        out += b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n"
        offsets = [0] * (len(objects) + 1)
        for i, body in enumerate(objects, start=1):
            offsets[i] = len(out)
            out += f"{i} 0 obj\n".encode() + body + b"\nendobj\n"

        xref_pos = len(out)
        n = len(objects) + 1
        out += f"xref\n0 {n}\n".encode()
        out += b"0000000000 65535 f \n"
        for i in range(1, n):
            out += f"{offsets[i]:010d} 00000 n \n".encode()
        out += (f"trailer\n<< /Size {n} /Root {catalog_num} 0 R /Info {info_num} 0 R >>\n"
                f"startxref\n{xref_pos}\n%%EOF").encode()

        with open(path, "wb") as f:
            f.write(out)
        return path
