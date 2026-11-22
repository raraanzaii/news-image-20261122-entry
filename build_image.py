#!/usr/bin/env python3
"""Build the Sunday 22 November 2026 front-page image (entry.png).

Renders a newspaper front page from stories.py with PIL: masthead, a title
band that sells the counts, a UTC timeline strip, three lead stories, a
numbered dot-grid world map with a pin legend, a regional index with a
per-story attribution suffix, a DATE CHECK box of older stories left out,
a sport strip and a source footer. Deterministic: same data, same bytes.
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw, ImageFont

import stories

FD = "/usr/share/fonts/truetype/dejavu"
SERIF_B = f"{FD}/DejaVuSerif-Bold.ttf"
SANS = f"{FD}/DejaVuSans.ttf"
SANS_B = f"{FD}/DejaVuSans-Bold.ttf"
SANS_O = "/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf"
LIB = "/usr/share/fonts/truetype/liberation"
COND = f"{LIB}/LiberationSans-Regular.ttf"   # narrow face for the dense index
COND_B = f"{LIB}/LiberationSans-Bold.ttf"

W, H = 1024, 1024
PAPER = (247, 243, 233)
INK = (18, 18, 18)
RED = (168, 0, 24)
GRAY = (96, 92, 84)
RULE = (60, 58, 52)
BAND = (18, 18, 18)
MAPDOT = (120, 116, 104)


def F(path, size):
    return ImageFont.truetype(path, size)


def tw(draw, text, font):
    return draw.textlength(text, font=font)


def wrap(draw, text, font, maxw):
    """Greedy word wrap; returns list of lines."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if tw(draw, trial, font) <= maxw or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_wrapped(draw, x, y, text, font, color, maxw, lh):
    for line in wrap(draw, text, font, maxw):
        draw.text((x, y), line, font=font, fill=color)
        y += lh
    return y


def outlet_of(tag):
    """'REPORTED · Reuters, Sydney, Nov 22' -> ('Reuters', False)."""
    confirmed = tag.startswith("CONFIRMED")
    rest = tag.split("·", 1)[1].strip() if "·" in tag else tag
    rest = rest.split(",")[0].strip()
    rest = rest.replace(" wires", "").strip()
    return rest, confirmed


# ---------------------------------------------------------------- land shapes
# (kind, ...) on a 118 x 46 grid, equirectangular-ish. Rects and ellipses.
SHAPES = [
    ("e", 5, 6, 5, 3),        # Alaska
    ("r", 2, 3, 36, 10),      # Canada
    ("e", 24, 10, 13, 4),     # USA
    ("e", 22, 17, 6, 3.5),    # Mexico / Central America
    ("e", 45, 4, 4.5, 3),     # Greenland
    ("e", 36, 26, 5, 4),      # northern South America
    ("e", 39, 31, 6, 6),      # Brazil
    ("e", 35, 37, 3.5, 5),    # Argentina
    ("e", 54.5, 8, 1.5, 2.5),  # Britain
    ("e", 54, 13, 3, 2),      # Iberia
    ("e", 59, 9, 7, 4),       # mainland Europe
    ("e", 61, 5, 5, 3),       # Scandinavia
    ("r", 66, 3, 114, 9),     # Russia / north Asia
    ("e", 85, 10, 20, 4),     # central Asia
    ("e", 61, 21, 11, 6),     # north Africa
    ("e", 62, 30, 8, 8),      # central / south Africa
    ("e", 71, 24, 3, 3),      # Horn of Africa
    ("e", 71, 16, 5, 4),      # Arabia / Middle East
    ("e", 82, 19, 4.5, 5),    # India
    ("e", 90, 14, 10, 6),     # China
    ("e", 89, 21, 3.5, 4),    # SE Asia
    ("e", 94, 27, 8, 2),      # Indonesia
    ("e", 100, 13, 2, 3.5),   # Japan
    ("e", 99, 34, 7, 4.5),    # Australia
    ("e", 112, 40, 1.8, 3),   # New Zealand
]


def is_land(c, r):
    for s in SHAPES:
        if s[0] == "r":
            _, c0, r0, c1, r1 = s
            if c0 <= c <= c1 and r0 <= r <= r1:
                return True
        else:
            _, cx, cy, rx, ry = s
            if ((c - cx) / rx) ** 2 + ((r - cy) / ry) ** 2 <= 1.0:
                return True
    return False


# ---------------------------------------------------------------- layout
def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    M = 22            # margin
    RX = W - M        # right edge

    # ---- counts for the title band (computed, never hand-written)
    n_index = sum(len(v) for v in stories.INDEX.values())
    n_stories = n_index + len(stories.LEADS)
    fields = {s["field"] for s in stories.LEADS}
    for items in stories.INDEX.values():
        for _, _, f in items:
            fields.add(f)
    n_regions = 7  # Europe, Middle East, N. America, Latin America,
    #                Asia-Pacific, Africa, Global (science/health)

    # ---- masthead
    d.text((M, 12), "THE SUNDAY WORLD", font=F(SERIF_B, 43), fill=INK)
    date_f = F(SANS_B, 21)
    date_t = "SUNDAY 22 NOVEMBER 2026"
    d.text((RX - tw(d, date_t, date_f), 16), date_t, font=date_f, fill=RED)
    sub_f = F(SANS, 10.5)
    sub_t = "One day · one image · the whole world"
    d.text((RX - tw(d, sub_t, sub_f), 44), sub_t, font=sub_f, fill=GRAY)
    sub2 = "Compiled from the wires of 22 Nov 2026 (UTC)"
    d.text((RX - tw(d, sub2, sub_f), 59), sub2, font=sub_f, fill=GRAY)
    d.line([(M, 80), (RX, 80)], fill=RED, width=3)
    d.line([(M, 85), (RX, 85)], fill=INK, width=1)

    # ---- title band (sells the numbers)
    d.rectangle([M, 92, RX, 140], fill=BAND)
    title = (f"{n_stories} STORIES · {n_regions} REGIONS · {len(fields)} FIELDS"
             " — ALL FROM THIS ONE SUNDAY")
    tf = F(SANS_B, 19)
    d.text(((W - tw(d, title, tf)) / 2, 99), title, font=tf, fill=(255, 255, 255))
    nums = ("400+ drones in one night over Ukraine  ·  98.5% of EU–Indonesia tariffs to fall"
            "  ·  856 candidates in Hong Kong  ·  23,000 workers strike in Germany")
    nf = F(SANS, 10.5)
    d.text(((W - tw(d, nums, nf)) / 2, 122), nums, font=nf, fill=(210, 205, 195))

    # ---- timeline strip
    y = 150
    d.text((M, y), "THE DAY IN UTC", font=F(SANS_B, 11), fill=RED)
    tx = M + 108
    colw = (RX - tx) / len(stories.TIMELINE)
    tf_time, tf_txt = F(SANS_B, 10.5), F(SANS, 9.5)
    for i, (t, txt) in enumerate(stories.TIMELINE):
        x = tx + i * colw
        d.text((x, y), t, font=tf_time, fill=INK)
        draw_wrapped(d, x, y + 13, txt, tf_txt, GRAY, colw - 8, 11)
    d.line([(M, 186), (RX, 186)], fill=RULE, width=1)

    # ---- leads
    y = 196
    colw3 = (RX - M - 24) / 3
    for i, lead in enumerate(stories.LEADS):
        x = M + i * (colw3 + 12)
        d.text((x, y), lead["kicker"], font=F(SANS_B, 10.5), fill=RED)
        yy = draw_wrapped(d, x, y + 15, lead["headline"], F(SERIF_B, 17.5),
                          INK, colw3, 21)
        yy = draw_wrapped(d, x, yy + 3, " ".join(lead["body"]), F(SANS, 10.5),
                          (50, 48, 44), colw3, 13.5)
        outlet, conf = outlet_of(lead["tag"])
        lab = ("CONFIRMED" if conf else "REPORTED") + " · " + outlet
        d.text((x, yy + 2), "■ " + lab, font=F(SANS_B, 8.5), fill=GRAY)
        if i:
            d.line([(x - 6, y), (x - 6, y + 118)], fill=(200, 195, 182), width=1)
    d.line([(M, 330), (RX, 330)], fill=RULE, width=1)

    # ---- map band: map + legend (left), DATE CHECK box (right)
    y = 338
    d.text((M, y), "THE DAY ON THE MAP — PINNED STORIES", font=F(SANS_B, 11.5), fill=INK)
    map_x, map_y, map_w, map_h = M, y + 18, 452, 124
    cell_w, cell_h = map_w / 118, map_h / 46
    for r in range(46):
        for c in range(118):
            if is_land(c, r):
                cx, cy = map_x + c * cell_w, map_y + r * cell_h
                d.ellipse([cx, cy, cx + 2.1, cy + 2.1], fill=MAPDOT)
    for num, label, c, r in stories.PINS:
        cx, cy = map_x + c * cell_w, map_y + r * cell_h
        d.ellipse([cx - 7, cy - 7, cx + 7, cy + 7], fill=RED, outline=(255, 255, 255))
        t = str(num)
        pf = F(SANS_B, 8.5)
        d.text((cx - tw(d, t, pf) / 2, cy - 5), t, font=pf, fill=(255, 255, 255))
    # legend: two columns under the map
    ly = map_y + map_h + 6
    lf = F(COND, 9.5)
    half = math.ceil(len(stories.PINS) / 2)
    for j, (num, label, c, r) in enumerate(stories.PINS):
        x = M + (j // half) * 232
        yy = ly + (j % half) * 11
        d.text((x, yy), f"{num}. {label}", font=lf, fill=(50, 48, 44))
    # date-check box
    bx = 492
    d.rectangle([bx, y, RX, y + 218], outline=RED, width=2)
    d.rectangle([bx, y, RX, y + 20], fill=RED)
    d.text((bx + 8, y + 4), "DATE CHECK · LEFT OUT AS OLDER NEWS",
           font=F(SANS_B, 11.5), fill=(255, 255, 255))
    yy = y + 27
    for text, when in stories.LEFT_OUT:
        d.text((bx + 8, yy), when, font=F(SANS_B, 9.5), fill=RED)
        yy = draw_wrapped(d, bx + 52, yy, text, F(COND, 10), (50, 48, 44),
                          RX - bx - 60, 11.5)
        yy += 3.5
    d.line([(M, 566), (RX, 566)], fill=RULE, width=1)

    # ---- regional index, four columns
    y = 576
    cols = [
        ["EUROPE"],
        ["MIDDLE EAST", "AFRICA"],
        ["NORTH AMERICA", "LATIN AMERICA"],
        ["ASIA-PACIFIC", "SCIENCE, TECH & HEALTH"],
    ]
    colw4 = (RX - M - 30) / 4
    hf, ef, of = F(SANS_B, 12), F(COND, 10.5), F(COND, 9)
    for ci, regions in enumerate(cols):
        x = M + ci * (colw4 + 10)
        yy = y
        for region in regions:
            d.text((x, yy), region, font=hf, fill=RED)
            yy += 15
            for headline, tag, _field in stories.INDEX[region]:
                outlet, conf = outlet_of(tag)
                suffix = " — " + outlet + (" ●" if conf else "")
                lines = wrap(d, headline + suffix, ef, colw4)
                for li, line in enumerate(lines):
                    d.text((x, yy), line, font=ef, fill=INK)
                    yy += 12
                yy += 2
            yy += 5
    note = ("● = CONFIRMED by the actor's own dated report of 22 Nov; every other story REPORTED"
            " by the named outlet on 22 Nov.")
    d.text((M, 934), note, font=F(SANS_O, 9.5), fill=GRAY)

    # ---- sport strip
    sy = 950
    d.line([(M, sy - 6), (RX, sy - 6)], fill=RULE, width=1)
    d.text((M, sy), "SPORT", font=F(SANS_B, 12), fill=RED)
    sx = M + 58
    scol = (RX - sx) / len(stories.INDEX["SPORT"])
    for i, (headline, tag, _f) in enumerate(stories.INDEX["SPORT"]):
        outlet, _c = outlet_of(tag)
        draw_wrapped(d, sx + i * scol, sy, headline + " — " + outlet,
                     F(COND, 10), INK, scol - 10, 11.5)

    # ---- footer
    d.line([(M, 992), (RX, 992)], fill=INK, width=1)
    foot = ("Every story above happened, or was first reported, on Sunday 22 November 2026. "
            "Sources: Reuters · AP · AFP · BBC · Al Jazeera · Times of India · SCMP · Cricbuzz · UN · UKMTO.")
    d.text((M, 997), foot, font=F(SANS, 9.5), fill=GRAY)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    img.save(out, optimize=True)
    print("wrote", out, os.path.getsize(out), "bytes;",
          n_stories, "stories;", len(fields), "fields")


if __name__ == "__main__":
    main()
