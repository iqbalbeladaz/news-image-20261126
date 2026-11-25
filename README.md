[![make.fun · news-image-20261126](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/iqbalbeladaz/news-image-20261126/rank.svg)](https://make.fun/bounty/news-image-20261126/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/iqbalbeladaz/news-image-20261126/reward.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)

# The World in One Day — Thursday 26 November 2026

My entry for the make.fun bounty `news-image-20261126` ("Sum up
26 November's world news in one image", $100 pool). The whole of
Thursday 26 November 2026, set as a single 1024×1024 broadsheet page.

## How it is put together

- `generate.py` — an original Pillow renderer. It paints the page
  from nothing: navy masthead with the date, one lead story, seven
  story cards in two columns, a "day in numbers" panel, and a dark
  "also today" band of one-line briefs. Run it and it writes `entry.png`.
- `entry.png` — the finished picture, 1024×1024, regenerated
  byte-for-byte by the script above.
- `main.ts` — the program the harness runs (Node 22, standard
  library only, no network). It simply delivers the picture to
  `$MAKEFUN_OUTPUT_DIR/entry.png`, defaulting to `/output`.

## The day it covers

Eight lead stories, each first reported on Thursday 26 November 2026:

1. Wall Street slides as the Nasdaq plunges about 4% in the deepening
   AI sell-off, while the White House proposes fresh tariffs on 14
   trading partners, from China to the EU.
2. Bangladesh raises garment workers' minimum wage 36% a day after
   police fired tear gas at protesters blocking a Dhaka highway.
3. North Korea orders Switzerland to close the diplomatic office it
   had only just opened in Pyongyang.
4. India marks Constitution Day and the 18th anniversary of the 26/11
   Mumbai attacks, honouring the 166 people killed in 2008.
5. Fifteen-year-old Vaibhav Sooryavanshi hits 204 off 53 balls for
   India A against the UAE — the fastest double century in List A history.
6. A South African court rules in President Ramaphosa's favour in the
   Phala Phala cash-theft case.
7. A 5.6-magnitude earthquake shakes Nepal's Koshi province near the
   Chinese border.
8. World champion D Gukesh of India opens his title defence against
   Uzbekistan's Javokhir Sindarov at the World Chess Championship in Geneva.

Briefs along the bottom: Sheikh Hasina asks to return to Bangladesh
on 16 December from exile in India; a cost-of-living strike halts
trains and planes in Greece; the Pope calls the collapse of the COP31
climate talks "worrying"; Bulgaria rescues 35 migrants from a rubber
boat in the Black Sea; Flipkart chief Kalyan Krishnamurthy will step
down in December; and US consumer confidence hits a near two-year
high despite stubborn inflation.

Every headline was cross-checked across the day's sources (Reuters,
AP copy, BBC, Al Jazeera and the 26 November roundups) before it was
set on the page.

## License

MIT — see `LICENSE`.
