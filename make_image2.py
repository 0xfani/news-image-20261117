"""Second, denser layout for entry.png: Tuesday 17 November 2026, 28 stories on one front page.
Reuses the canvas helpers and pictograms defined in make_image.py (everything above its story list).
Run once on the build machine:  uv run --with pillow python make_image2.py
"""
from PIL import Image, ImageDraw

_src = open("make_image.py", encoding="utf8").read().split("# ---------- the day's stories ----------")[0]
exec(_src)  # fonts, canvas, rect/poly/text/wrap helpers and the ic_* pictograms

F_K = font("arialbd.ttf", 15)
F_D = font("georgiab.ttf", 50)
F_T = font("arialbd.ttf", 12)
F_H1 = font("arialbd.ttf", 21)
F_B1 = font("arial.ttf", 13.5)
F_H2 = font("arialbd.ttf", 16)
F_B2 = font("arial.ttf", 12.5)
F_L = font("arial.ttf", 13)
F_SEC = font("arialbd.ttf", 15)
F_SRC2 = font("arial.ttf", 11)

EUR, MEA, AME = (36, 92, 178), (204, 74, 24), (16, 30, 62)
ASIA, LAT, AFR = (0, 122, 128), (0, 122, 70), (190, 120, 0)
TECH, CLIM, HEALTH, PRESS = (96, 60, 160), (46, 140, 60), (200, 40, 110), (180, 20, 40)


def ic_ballot(x, y):
    rect(x + 22, y + 58, x + 108, y + 120, (226, 230, 238), outline=(120, 126, 140), width=2)
    rect(x + 46, y + 56, x + 84, y + 62, (60, 64, 76))
    poly([(x + 50, y + 60), (x + 80, y + 60), (x + 86, y + 14), (x + 56, y + 14)], (255, 255, 255))
    line([(x + 56, y + 14), (x + 86, y + 14), (x + 80, y + 60)], (120, 126, 140), 2)
    line([(x + 60, y + 34), (x + 67, y + 42), (x + 80, y + 24)], (36, 92, 178), 5)
    text(x + 65, y + 92, "VOTE", F_TAG, (60, 64, 76), "mm")


def icon(fn, x, y, size):
    """Draw a 130-px pictogram on its own layer and paste it scaled to size."""
    global d
    layer = Image.new("RGBA", (130 * S, 130 * S), (0, 0, 0, 0))
    keep = d
    d = ImageDraw.Draw(layer)
    fn(0, 0)
    d = keep
    layer = layer.resize((int(size * S), int(size * S)), Image.LANCZOS)
    img.paste(layer, (int(x * S), int(y * S)), layer)


def para(x, y, s, f, fill, width, lh, maxl=9):
    for ln in wrap(s, f, width)[:maxl]:
        text(x, y, ln, f, fill)
        y += lh
    return y


HERO = [
    ("EUROPE \u00b7 UKRAINE WAR", EUR, ic_bridge, "Kerch bridge to Crimea knocked out",
     "Ukrainian strike drops a road span; Russia says it downed 2,000+ drones in a day; Kyiv logs a record 17 air-raid alerts"),
    ("MIDDLE EAST \u00b7 IRAN WAR", MEA, ic_ship_fire, "Iran war flares at sea and in the Gulf",
     "Bahrain intercepts Iranian drones aimed at a US radar; three more ships ablaze in the Strait of Hormuz"),
    ("ASIA-PACIFIC", ASIA, ic_philippines, "Trump lands in Manila for ASEAN summit",
     "About 300 arrested at protests; a Trump-Xi-Putin summit is set for Shenzhen on Thursday"),
]
MID = [
    ("UNITED STATES", AME, ic_capitol_radiation, "Iran 'dirty bomb' plot on DC reported",
     "Tehran: 'propaganda'. Trump: 'very seriously'"),
    ("LATIN AMERICA", LAT, ic_mexico_china, "Sheinbaum meets Xi in China",
     "Mexico seeks tech, farm and water ties"),
    ("AFRICA", AFR, ic_sa_nigeria, "South Africa rebukes Nigeria's envoy",
     "Pretoria summons Fani-Kayode over a row"),
    ("TURKEY \u00b7 PRESS", PRESS, ic_turkey_tv, "Turkey seizes opposition S\u00f6zc\u00fc TV",
     "Channel off air, executives detained"),
    ("TECH \u00b7 BUSINESS", TECH, ic_chip, "Nvidia board cool on Huang comeback",
     "Trump says he 'would not mind' it"),
    ("ISRAEL", MEA, ic_ballot, "Netanyahu camp faces meddling claims",
     "Report: Shin Bet wiretapped Arab MPs"),
]
ALSO = [
    (EUR, "EU ministers meet in Brussels; Germany urges Israel to let far more aid into Gaza before winter"),
    (MEA, "UN: Israeli strike hit near a UN fuel convoy in Rafah as Gaza aid deliveries fall short"),
    (MEA, "West Bank village declared a closed military zone; a visiting EU delegation is forced out"),
    (MEA, "Iraq bans Telegram on security grounds, after Jordan blocked the app"),
    (ASIA, "Pakistan says it is still trying to bring the US and Iran back to talks"),
    (AME, "UN chief Guterres urges the US, Russia and China to commit to denuclearisation"),
    (CLIM, "COP31 in Antalya: Europe presses China in a fight over when IPCC reports come out"),
    (EUR, "ECB and Fed officials warn that fast-spreading AI could threaten financial stability"),
    (EUR, "EU Commission forecasts 1.2% growth for the euro zone"),
    (EUR, "Germany's Pistorius calls US criticism of Ukraine's deep strikes 'quite a stupid thing'"),
    (EUR, "Spain's S\u00e1nchez attacks EU plans to send asylum seekers to Rwanda"),
    (AME, "US transport chief Duffy briefs senators on last week's record FAA ground stop"),
    (AME, "Outrage grows over video of ICE agents pepper-spraying a pregnant US citizen"),
    (LAT, "16 Ecuadorian fishermen sue the Trump administration over a US strike on their boat"),
    (HEALTH, "WHO: drug-resistant infections could kill 39 million people by 2050"),
    (MEA, "Saudi king replaces the commander of the coalition's Joint Forces in Yemen"),
    (AFR, "African Union: Africa loses up to $125bn a year to corruption and illicit flows"),
    (MEA, "Press group FPA demands the release of an AFP contributor held in the West Bank"),
    (EUR, "Russian strikes kill at least seven in Ukraine; attacks on the grid leave 50,000 without power"),
    (CLIM, "Erdogan hails the COP31 climate summit in Antalya as the best organised yet"),
    (AFR, "Egypt's el-Sisi pledges simpler business rules and outlines plans for industry, energy and AI"),
    (LAT, "Mexico: press groups demand justice for journalist Eduardo Flores Salado, killed in Acapulco"),
    (TECH, "T\u00fcrkiye re-elected to the council of the UN's telecom agency, the ITU, for a 7th term"),
    (MEA, "Israel's Lieberman elected chair of the Knesset's foreign affairs and defence committee"),
]
TOTAL = len(HERO) + len(MID) + len(ALSO)

# fresh page
rect(0, 0, W, H, PAPER)
rect(0, 0, W, 104, NAVY)
text(W / 2, 20, f"THE WORLD IN ONE DAY \u00b7 {TOTAL} STORIES \u00b7 5 CONTINENTS", F_K, GOLD, "mm")
text(W / 2, 66, "Tuesday 17 November 2026", F_D, (255, 255, 255), "mm")
rect(0, 104, W, 108, GOLD)

# three lead stories
MX, GAP = 12, 8
cw = (W - 2 * MX - 2 * GAP) / 3
for i, (tag, col, ic, head, sub) in enumerate(HERO):
    x, y = MX + i * (cw + GAP), 116
    rect(x, y, x + cw, y + 208, CARD, outline=(214, 208, 194), width=1, r=6)
    rect(x, y, x + cw, y + 5, col)
    text(x + 12, y + 14, tag, F_T, col)
    icon(ic, x + 10, y + 34, 86)
    hy = para(x + 104, y + 34, head, F_H1, INK, cw - 114, 24, 3)
    para(x + 12, max(hy, y + 122) + 4, sub, F_B1, GREY, cw - 24, 17, 4)

# six more with pictograms
ch = 98
for i, (tag, col, ic, head, sub) in enumerate(MID):
    x, y = MX + (i % 3) * (cw + GAP), 332 + (i // 3) * (ch + GAP)
    rect(x, y, x + cw, y + ch, CARD, outline=(214, 208, 194), width=1, r=6)
    rect(x, y, x + 5, y + ch, col)
    icon(ic, x + 12, y + 16, 66)
    text(x + 88, y + 10, tag, F_T, col)
    hy = para(x + 88, y + 27, head, F_H2, INK, cw - 98, 19, 2)
    para(x + 88, hy + 2, sub, F_B2, GREY, cw - 98, 15, 2)

# the rest of the day
sy = 546
text(MX, sy, "ALSO ON TUESDAY 17 NOVEMBER 2026", F_SEC, NAVY)
rect(MX, sy + 22, W - MX, sy + 24, NAVY)
half = (len(ALSO) + 1) // 2
for c in range(2):
    x, y = MX + c * (W / 2), sy + 34
    for col, s in ALSO[c * half:(c + 1) * half]:
        circle(x + 6, y + 8, 5, col)
        y = para(x + 18, y, s, F_L, INK, W / 2 - 40, 16, 2) + 6

# region key and sources
ky = 952
keys = [("Europe", EUR), ("Middle East", MEA), ("Americas", AME), ("Latin America", LAT), ("Asia", ASIA),
        ("Africa", AFR), ("Tech", TECH), ("Climate", CLIM), ("Health", HEALTH)]
kx = MX
for name, col in keys:
    circle(kx + 6, ky + 7, 5, col)
    text(kx + 15, ky, name, F_B2, INK)
    kx += 26 + F_B2.getlength(name) / S
rect(MX, 976, W - MX, 977, (190, 184, 170))
text(W / 2, 992, "Every story here happened or was reported on Tuesday 17 November 2026", F_FOOT, INK, "mm")
text(W / 2, 1012, "Sources: Reuters, AP, BBC, The Guardian, CNN, CNBC, DW, Anadolu, Euronews, Democracy Now, Daily Maverick",
     F_SRC2, GREY, "mm")

out = img.resize((W, H), Image.LANCZOS)
out = out.quantize(colors=160, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE)
out.save("entry.png", optimize=True)
print("wrote entry.png", out.size, TOTAL, "stories")
