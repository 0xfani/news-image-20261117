"""Draws entry.png: the world's news of Tuesday 17 November 2026 in one picture.

Run once on the build machine (needs Pillow and the Windows fonts):
    uv run --with pillow python make_image.py
The entry program (main.py) only copies the finished entry.png.
"""
import math
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
S = 2  # draw at 2x, then downsample for clean edges
FONTS = "C:/Windows/Fonts/"

PAPER = (246, 242, 232)
CARD = (255, 255, 255)
INK = (22, 26, 36)
GREY = (78, 84, 96)
NAVY = (16, 30, 62)
GOLD = (232, 186, 74)
WATER = (64, 120, 176)


def font(name, size):
    return ImageFont.truetype(FONTS + name, int(size * S))


F_KICK = font("arialbd.ttf", 19)
F_DATE = font("georgiab.ttf", 56)
F_TAG = font("arialbd.ttf", 16)
F_HEAD = font("arialbd.ttf", 29)
F_SUB = font("arial.ttf", 17.5)
F_FOOT = font("arialbd.ttf", 16)
F_SRC = font("arial.ttf", 13)
F_ICON = font("arialbd.ttf", 22)

img = Image.new("RGB", (W * S, H * S), PAPER)
d = ImageDraw.Draw(img)


def p(*xy):
    return [v * S for v in xy]


def pts(seq):
    return [(x * S, y * S) for x, y in seq]


def rect(x0, y0, x1, y1, fill, outline=None, width=1, r=0):
    if r:
        d.rounded_rectangle(p(x0, y0, x1, y1), r * S, fill=fill, outline=outline, width=width * S)
    else:
        d.rectangle(p(x0, y0, x1, y1), fill=fill, outline=outline, width=width * S)


def poly(seq, fill):
    d.polygon(pts(seq), fill=fill)


def circle(cx, cy, r, fill):
    d.ellipse(p(cx - r, cy - r, cx + r, cy + r), fill=fill)


def line(seq, fill, width):
    d.line(pts(seq), fill=fill, width=int(width * S), joint="curve")


def star(cx, cy, R, r, fill, n=5, rot=-90):
    out = []
    for i in range(2 * n):
        a = math.radians(rot + i * 180 / n)
        rad = R if i % 2 == 0 else r
        out.append((cx + rad * math.cos(a), cy + rad * math.sin(a)))
    poly(out, fill)


def text(x, y, s, f, fill, anchor="la"):
    d.text((x * S, y * S), s, font=f, fill=fill, anchor=anchor)


def wrap(s, f, width):
    words, lines, cur = s.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if f.getlength(t) <= width * S:
            cur = t
        else:
            lines.append(cur)
            cur = w
    lines.append(cur)
    return lines


# ---------- pictograms (each fits a 130 x 130 box at x, y) ----------

def ic_bridge(x, y):
    rect(x, y + 98, x + 130, y + 130, WATER)
    for px in (x + 4, x + 22, x + 40, x + 88, x + 106, x + 124):
        rect(px - 2, y + 62, px + 2, y + 100, (96, 98, 106))
    rect(x, y + 56, x + 46, y + 63, (60, 62, 70))
    rect(x + 84, y + 56, x + 130, y + 63, (60, 62, 70))
    d.arc(p(x + 40, y + 30, x + 88, y + 90), 200, 250, fill=(60, 62, 70), width=4 * S)
    d.arc(p(x + 40, y + 30, x + 88, y + 90), 290, 340, fill=(60, 62, 70), width=4 * S)
    poly([(x + 50, y + 66), (x + 58, y + 62), (x + 82, y + 100), (x + 72, y + 103)], (60, 62, 70))
    star(x + 66, y + 34, 26, 11, (244, 120, 40), n=9)
    star(x + 66, y + 34, 14, 6, (255, 214, 64), n=7)
    text(x + 65, y + 116, "KERCH", F_TAG, (255, 255, 255), "mm")


def ic_ship_fire(x, y):
    rect(x, y + 100, x + 130, y + 130, WATER)
    circle(x + 40, y + 22, 16, (150, 150, 150))
    circle(x + 62, y + 14, 20, (120, 120, 120))
    circle(x + 86, y + 24, 14, (165, 165, 165))
    poly([(x + 8, y + 84), (x + 122, y + 84), (x + 110, y + 104), (x + 20, y + 104)], (120, 30, 30))
    rect(x + 92, y + 64, x + 110, y + 84, (230, 230, 230))
    for fx, fh in ((x + 30, 46), (x + 48, 58), (x + 66, 42)):
        poly([(fx - 12, y + 84), (fx + 12, y + 84), (fx, y + 84 - fh)], (244, 110, 30))
        poly([(fx - 6, y + 84), (fx + 6, y + 84), (fx, y + 84 - fh * 0.55)], (255, 210, 60))
    text(x + 65, y + 118, "HORMUZ", F_TAG, (255, 255, 255), "mm")


def ic_capitol_radiation(x, y):
    rect(x + 8, y + 104, x + 92, y + 116, (210, 214, 222))
    rect(x + 14, y + 84, x + 86, y + 104, (232, 234, 240))
    for k in range(8):
        cx = x + 20 + k * 9
        rect(cx, y + 86, cx + 3, y + 103, (170, 176, 190))
    rect(x + 34, y + 70, x + 66, y + 84, (226, 228, 236))
    d.pieslice(p(x + 30, y + 44, x + 70, y + 96), 180, 360, fill=(240, 242, 246), outline=(160, 166, 180), width=S)
    rect(x + 47, y + 36, x + 53, y + 46, (200, 204, 214))
    circle(x + 96, y + 40, 30, (252, 208, 40))
    for a in (-90, 30, 150):
        d.pieslice(p(x + 72, y + 16, x + 120, y + 64), a - 30, a + 30, fill=INK)
    circle(x + 96, y + 40, 9, (252, 208, 40))
    circle(x + 96, y + 40, 6, INK)


def ic_philippines(x, y):
    x0, y0, x1, y1 = x + 4, y + 40, x + 126, y + 112
    ym = (y0 + y1) / 2
    rect(x0, y0, x1, ym, (0, 56, 168))
    rect(x0, ym, x1, y1, (206, 17, 38))
    poly([(x0, y0), (x0, y1), (x0 + 62, ym)], (255, 255, 255))
    star(x0 + 20, ym, 11, 6, (252, 209, 22), n=8)
    # airliner arriving
    poly([(x + 30, y + 22), (x + 104, y + 12), (x + 112, y + 16), (x + 104, y + 21), (x + 32, y + 28)], NAVY)
    poly([(x + 64, y + 18), (x + 86, y + 2), (x + 94, y + 3), (x + 80, y + 20)], NAVY)
    poly([(x + 62, y + 24), (x + 80, y + 38), (x + 88, y + 37), (x + 78, y + 22)], NAVY)


def ic_mexico_china(x, y):
    x0, y0 = x + 2, y + 14
    rect(x0, y0, x0 + 26, y0 + 54, (0, 104, 71))
    rect(x0 + 26, y0, x0 + 52, y0 + 54, (255, 255, 255))
    rect(x0 + 52, y0, x0 + 78, y0 + 54, (206, 17, 38))
    circle(x0 + 39, y0 + 27, 7, (140, 90, 40))
    rect(x0, y0, x0 + 78, y0 + 54, None, outline=(150, 150, 150), width=1)
    x1, y1 = x + 50, y + 62
    rect(x1, y1, x1 + 78, y1 + 54, (222, 41, 16), outline=(255, 255, 255), width=2)
    star(x1 + 16, y1 + 16, 10, 4, (255, 222, 0))
    for sx, sy in ((30, 7), (35, 13), (35, 21), (30, 27)):
        star(x1 + sx, y1 + sy, 3.4, 1.4, (255, 222, 0))


def ic_sa_nigeria(x, y):
    x0, y0 = x + 2, y + 14
    rect(x0, y0, x0 + 26, y0 + 54, (0, 135, 81))
    rect(x0 + 26, y0, x0 + 52, y0 + 54, (255, 255, 255))
    rect(x0 + 52, y0, x0 + 78, y0 + 54, (0, 135, 81))
    rect(x0, y0, x0 + 78, y0 + 54, None, outline=(150, 150, 150), width=1)
    a, b = x + 50, y + 62
    c, e = a + 78, b + 54
    m = (b + e) / 2
    rect(a, b, c, m, (222, 56, 49))
    rect(a, m, c, e, (0, 35, 149))
    line([(a, b), (a + 30, m), (c, m)], (255, 255, 255), 16)
    line([(a, e), (a + 30, m)], (255, 255, 255), 16)
    line([(a, b), (a + 30, m), (c, m)], (0, 122, 77), 10)
    line([(a, e), (a + 30, m)], (0, 122, 77), 10)
    poly([(a, b + 10), (a, e - 10), (a + 22, m)], (255, 182, 18))
    poly([(a, b + 15), (a, e - 15), (a + 15, m)], (0, 0, 0))
    rect(a, b, c, e, None, outline=(150, 150, 150), width=1)


def ic_turkey_tv(x, y):
    rect(x + 6, y + 30, x + 124, y + 108, (40, 42, 50), r=8)
    rect(x + 14, y + 38, x + 116, y + 100, (120, 124, 132))
    for i in range(0, 62, 6):
        line([(x + 14, y + 38 + i), (x + 116, y + 38 + i)], (140, 144, 152), 2)
    rect(x + 22, y + 56, x + 108, y + 82, (200, 16, 30))
    text(x + 65, y + 69, "OFF AIR", F_TAG, (255, 255, 255), "mm")
    line([(x + 40, y + 108), (x + 30, y + 124)], (40, 42, 50), 4)
    line([(x + 90, y + 108), (x + 100, y + 124)], (40, 42, 50), 4)
    fx, fy = x + 74, y + 2
    rect(fx, fy, fx + 52, fy + 34, (227, 10, 23))
    circle(fx + 18, fy + 17, 10, (255, 255, 255))
    circle(fx + 21, fy + 17, 8, (227, 10, 23))
    star(fx + 32, fy + 17, 6, 2.5, (255, 255, 255), rot=180)


def ic_chip(x, y):
    for i in range(6):
        o = 30 + i * 14
        line([(x + o, y + 14), (x + o, y + 116)], (150, 156, 166), 4)
        line([(x + 14, y + o), (x + 116, y + o)], (150, 156, 166), 4)
    rect(x + 26, y + 26, x + 104, y + 104, (34, 38, 46), r=6)
    rect(x + 34, y + 34, x + 96, y + 96, (118, 185, 0), r=4)
    text(x + 65, y + 66, "CEO?", F_ICON, (255, 255, 255), "mm")


# ---------- the day's stories ----------

STORIES = [
    ("UKRAINE WAR", (36, 92, 178), ic_bridge,
     "Kerch bridge to Crimea knocked out",
     "Ukrainian strike drops a road span; Russia says 2,000+ drones downed"),
    ("IRAN WAR \u00b7 GULF", (204, 74, 24), ic_ship_fire,
     "Iran drones target US radar in Bahrain",
     "Attack intercepted; three more ships ablaze in the Strait of Hormuz"),
    ("UNITED STATES", (16, 30, 62), ic_capitol_radiation,
     "Report of Iran 'dirty bomb' plot on DC",
     "CNN cites US intel; Tehran calls it propaganda, Trump: 'very seriously'"),
    ("ASIA-PACIFIC", (0, 122, 128), ic_philippines,
     "Trump lands in Manila for ASEAN summit",
     "Hundreds arrested at protests; Trump-Xi-Putin summit in Shenzhen next"),
    ("LATIN AMERICA", (0, 122, 70), ic_mexico_china,
     "Mexico's Sheinbaum meets Xi in China",
     "Pledges closer ties on technology, farming, water and tourism"),
    ("AFRICA", (190, 120, 0), ic_sa_nigeria,
     "South Africa rebukes Nigeria's envoy",
     "Pretoria summons Fani-Kayode over a livestream row and his posts"),
    ("TURKEY \u00b7 PRESS", (180, 20, 40), ic_turkey_tv,
     "Turkey seizes opposition S\u00f6zc\u00fc TV",
     "Channel taken off air, executives detained, as Antalya hosts COP31"),
    ("TECH \u00b7 BUSINESS", (96, 60, 160), ic_chip,
     "Nvidia board cool on Huang comeback",
     "Reports say it isn't considering it, though Trump 'would not mind'"),
]

# masthead
rect(0, 0, W, 148, NAVY)
text(W / 2, 30, "THE WORLD'S NEWS IN ONE PICTURE", F_KICK, GOLD, "mm")
text(W / 2, 90, "Tuesday, 17 November 2026", F_DATE, (255, 255, 255), "mm")
rect(0, 148, W, 154, GOLD)

# grid of story cards
TOP, BOTTOM, GAP, MX = 166, 966, 10, 14
cw = (W - 2 * MX - GAP) / 2
ch = (BOTTOM - TOP - 3 * GAP) / 4
for i, (tag, col, icon, head, sub) in enumerate(STORIES):
    cx = MX + (i % 2) * (cw + GAP)
    cy = TOP + (i // 2) * (ch + GAP)
    rect(cx, cy, cx + cw, cy + ch, CARD, outline=(214, 208, 194), width=1, r=6)
    rect(cx, cy, cx + 6, cy + ch, col)
    icon(cx + 16, cy + (ch - 130) / 2)
    tx, tw = cx + 160, cw - 172
    hl, sl = wrap(head, F_HEAD, tw), wrap(sub, F_SUB, tw)
    block = 26 + 34 * len(hl) + 6 + 22 * len(sl)
    ty = cy + max(10, (ch - block) / 2)
    text(tx, ty, tag, F_TAG, col)
    ty += 26
    for ln in hl:
        text(tx, ty, ln, F_HEAD, INK)
        ty += 34
    ty += 6
    for ln in sl:
        text(tx, ty, ln, F_SUB, GREY)
        ty += 22

# footer
text(W / 2, 984, "Every story above happened or was first reported on Tuesday 17 November 2026", F_FOOT, INK, "mm")
text(W / 2, 1006, "Sources: Reuters, AP, BBC, The Guardian, CNN, CNBC, DW, Anadolu, Euronews, Daily Maverick", F_SRC, GREY, "mm")

out = img.resize((W, H), Image.LANCZOS)
out = out.quantize(colors=128, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE)
out.save("entry.png", optimize=True)
print("wrote entry.png", out.size)
