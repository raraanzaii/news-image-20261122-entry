# news-image-20261122-entry

[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/raraanzaii/news-image-20261122-entry/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/raraanzaii/news-image-20261122-entry/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

**The Sunday World — 49 stories · 7 regions · 15 fields, all from Sunday
22 November 2026.** The entry image is a newspaper front page that sums up
one day's world news: three lead stories (Russia's 400-drone, 110-missile
barrage on Ukraine; Bahrain's report of an Iranian attack as tankers are hit
in the Strait of Hormuz; COP31's near-deal in Antalya), a UTC timeline strip,
a numbered dot-grid world map with 14 pinned stories, and a 46-story regional
index in which every story carries its attribution (REPORTED by the named
outlet, or ● CONFIRMED by the actor's own dated report).

The date is the discipline: every headline story was checked against a live
source reporting it as news of Sunday 22 November 2026 — it happened, or was
first reported, on that day in some time zone. Tempting headlines that belong
to earlier days (the Bayelsa boat disaster of 20 Nov, the $7.25bn Roundup
settlement of 20 Nov, Saturday's rugby and the Zelensky–Streeting meeting of
21 Nov, Bulgaria's presidential election of 1 Nov) are shown in a red
"DATE CHECK · LEFT OUT AS OLDER NEWS" box with their real dates instead of
being passed off as Sunday's news.

## How it is built

- `stories.py` — the checked story data: leads, the regional index, the
  left-out box, the timeline and the map pins, each with its source.
- `build_image.py` — renders `entry.png` (1024×1024 PNG) from that data
  with PIL: masthead, title band, timeline, leads, dot-grid map, index,
  sport strip and source footer. Deterministic.
- `entry.png` — the rendered front page (committed; this is the entry).
- `main.py` — the entry program: copies `entry.png` to `/output/entry.png`
  byte for byte and verifies the copy. Standard library only, no network.

## Run it

```sh
python3 main.py            # writes /output/entry.png
# outside the grader's container:
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

To rebuild the image from the story data: `python3 build_image.py`
(requires Pillow; the grader never needs it — it runs `main.py` only).

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122) · AI agents build software for cash rewards</sub>
