#!/usr/bin/env python3
"""Render the 26 November 2026 world-news broadsheet (1024x1024 PNG).

Draws the whole page from nothing with Pillow: a navy masthead naming
the day, one lead story, seven further story cards in two columns, a
"day in numbers" panel, and a dark "also today" band of one-line briefs.
Run:  python3 generate.py   -> writes entry.png next to this file.
"""

import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 234)
INK = (24, 24, 28)
NAVY = (16, 32, 64)
NAVY_LIGHT = (28, 52, 96)
RED = (178, 34, 34)
GREY = (96, 96, 100)
RULE = (190, 182, 168)
CARD = (255, 255, 255)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap to pixel width; returns list of lines."""
    lines, cur = [], ""
    for word in text.split():
        trial = f"{cur} {word}".strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_wrapped(draw, x, y, text, fnt, width, fill, leading=None):
    lines = wrap(draw, text, fnt, width)
    lh = leading or int(fnt.size * 1.22)
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += lh
    return y


# ---------------------------------------------------------------- stories
LEAD = {
    "kicker": "THE LEAD  ·  MARKETS",
    "headline": "Nasdaq plunges 4% as the AI sell-off deepens and Trump unveils a new tariff plan",
    "deck": (
        "Wall Street's tech rout wipes out the Nvidia rebound in a shortened Thanksgiving week, "
        "as the White House proposes fresh tariffs on 14 trading partners, from China to the EU, "
        "and hot inflation data lands."
    ),
}

STORIES = [
    {
        "kicker": "BANGLADESH",
        "headline": "Bangladesh raises garment workers' pay 36% after street protests",
        "deck": "The minimum wage rises for millions of garment workers, a day after police fired tear gas at Dhaka protesters.",
    },
    {
        "kicker": "NORTH KOREA",
        "headline": "North Korea orders Switzerland to shut its Pyongyang office",
        "deck": "Pyongyang tells Bern to close the diplomatic office it had only just opened, in a new chill for its few foreign ties.",
    },
    {
        "kicker": "INDIA",
        "headline": "India marks Constitution Day and 18 years since the 26/11 attacks",
        "deck": "Ceremonies honour the 166 killed in the 2008 Mumbai attacks, on the anniversary of the Constitution's adoption.",
    },
    {
        "kicker": "CRICKET",
        "headline": "Fifteen-year-old smashes the fastest double century in List A history",
        "deck": "Vaibhav Sooryavanshi hits 204 off 53 balls for India A against the UAE in Doha \u2014 the quickest double hundred in the format.",
    },
    {
        "kicker": "SOUTH AFRICA",
        "headline": "Court hands Ramaphosa a win in the Phala Phala cash-theft case",
        "deck": "Judges rule in the president's favour over the probe into cash stolen from his farm.",
    },
    {
        "kicker": "NEPAL",
        "headline": "A 5.6-magnitude quake shakes Nepal's Koshi province",
        "deck": "The tremor strikes near the Chinese border; no major damage is reported in the first hours.",
    },
    {
        "kicker": "CHESS",
        "headline": "Gukesh defends his crown against Sindarov in Geneva",
        "deck": "World champion D Gukesh of India opens his title match against Uzbekistan's Javokhir Sindarov.",
    },
]

BRIEFS = [
    "Sheikh Hasina asks to return to Bangladesh on 16 December, from exile in India.",
    "Greece grinds to a halt as a cost-of-living strike stops trains and planes.",
    "Pope calls the collapse of the COP31 climate talks \u201cworrying\u201d.",
    "Bulgaria rescues 35 migrants from a rubber boat in the Black Sea.",
    "Flipkart chief Kalyan Krishnamurthy will step down in December, reports say.",
    "US consumer confidence hits a near two-year high despite stubborn inflation.",
]


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---------------------------------------------------------- masthead
    d.rectangle([0, 0, W, 132], fill=NAVY)
    d.rectangle([0, 132, W, 136], fill=RED)
    title = font(SERIF, 58)
    d.text((36, 18), "THE WORLD IN ONE DAY", font=title, fill=(255, 255, 255))
    sub = font(SANS_BOLD, 24)
    d.text((36, 92), "Thursday, 26 November 2026", font=sub, fill=(255, 214, 130))
    d.text((W - 36, 92), "Eight stories  ·  One day", font=font(SANS, 20),
           fill=(200, 208, 224), anchor="ra")

    # ---------------------------------------------------------- lead story
    lx, ly, lw, lh = 36, 152, W - 72, 180
    d.rectangle([lx, ly, lx + lw, ly + lh], fill=CARD, outline=RULE, width=2)
    d.rectangle([lx, ly, lx + 10, ly + lh], fill=RED)
    x = lx + 28
    y = ly + 14
    d.text((x, y), LEAD["kicker"], font=font(SANS_BOLD, 17), fill=RED)
    y += 26
    y = draw_wrapped(d, x, y, LEAD["headline"], font(SERIF, 26), lw - 56, INK, leading=32)
    y += 6
    draw_wrapped(d, x, y, LEAD["deck"], font(SANS, 17), lw - 56, (60, 60, 66), leading=22)

    # ---------------------------------------------------------- story cards
    col_w = (W - 72 - 24) // 2
    col_x = [36, 36 + col_w + 24]
    top = 344
    card_h = 116
    gap = 10
    # left column: stories 0..3, right column: stories 4..6 + numbers panel
    left = STORIES[:4]
    right = STORIES[4:]
    for ci, group in enumerate((left, right)):
        cx = col_x[ci]
        cy = top
        for s in group:
            d.rectangle([cx, cy, cx + col_w, cy + card_h], fill=CARD, outline=RULE, width=1)
            d.rectangle([cx, cy, cx + col_w, cy + 4], fill=NAVY_LIGHT)
            x = cx + 14
            yy = cy + 12
            d.text((x, yy), s["kicker"], font=font(SANS_BOLD, 14), fill=RED)
            yy += 21
            yy = draw_wrapped(d, x, yy, s["headline"], font(SERIF, 19), col_w - 28, INK, leading=22)
            yy += 3
            draw_wrapped(d, x, yy, s["deck"], font(SANS, 14), col_w - 28, (70, 70, 76), leading=17)
            cy += card_h + gap
        if ci == 1:
            # numbers panel fills the remaining right-column slot
            ph = card_h
            d.rectangle([cx, cy, cx + col_w, cy + ph], fill=NAVY, outline=NAVY)
            x = cx + 14
            yy = cy + 12
            d.text((x, yy), "THE DAY IN NUMBERS", font=font(SANS_BOLD, 14), fill=(255, 214, 130))
            yy += 22
            for line in ("Nasdaq  \u22124.0%     Nvidia  \u22128.6%",
                         "204 off 53 balls     1,220 IPL sign-ups",
                         "36% pay rise     5.6 quake in Nepal"):
                d.text((x, yy), line, font=font(SANS, 15), fill=(235, 238, 244))
                yy += 22
            d.text((x, yy), "Wall Street heads for its worst November since 2008.",
                   font=font(SANS, 13), fill=(180, 190, 205))

    # ---------------------------------------------------------- briefs band
    by = top + 4 * (card_h + gap) + 8
    bh = 132
    d.rectangle([36, by, W - 36, by + bh], fill=(30, 30, 34))
    d.text((52, by + 10), "ALSO TODAY", font=font(SANS_BOLD, 15), fill=(255, 214, 130))
    yy = by + 34
    for b in BRIEFS:
        d.text((52, yy), "\u2022  " + b, font=font(SANS, 14), fill=(232, 232, 230))
        yy += 16

    # ---------------------------------------------------------- footer
    fy = by + bh + 8
    d.line([36, fy, W - 36, fy], fill=RULE, width=1)
    d.text((36, fy + 8),
           "The World in One Day \u2014 26 November 2026  ·  Sources: Reuters, AP, BBC, Al Jazeera",
           font=font(SANS, 14), fill=GREY)
    d.text((W - 36, fy + 8), "make.fun  ·  news-image-20261126",
           font=font(SANS, 14), fill=GREY, anchor="ra")

    out = Path(__file__).with_name("entry.png")
    img.save(out, optimize=True)
    print(f"wrote {out} ({out.stat().st_size} bytes, {img.size[0]}x{img.size[1]})")


if __name__ == "__main__":
    main()
