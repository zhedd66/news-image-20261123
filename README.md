# The World in One Day — 23 November 2026

Entry for the make.fun competition `news-image-20261123`:
"Sum up 23 November's world news in one image."

One 1024x1024 infographic poster summing up Monday 23 November 2026:

- **COP31, Antalya** — the UN climate summit ends with no deal; the EU and
  some 130 parties reject a text with no fossil-fuel phase-out (first such
  collapse since 2009).
- **Dymer, near Kyiv** — a Russian strike kills 10+; rescuers pull a
  7-year-old boy alive from the rubble.
- **Markets** — an AI-bubble selloff: Nikkei -5.06%, S&P 500 -3.7%; gold jumps.
- **Washington** — Democrats clinch 258 U.S. House seats, the largest
  majority for either party since 1992.
- **Hormuz** — Iran hits Bahrain and tankers; Trump "inclined" to resume
  the conflict if there is no deal by the New Year.
- Ticker: Banten (Indonesia) candy-factory fire, 24 dead; Delta delays
  1,000+ flights at Atlanta; Liverpool 4-0 Manchester United.

Sources: Reuters, Associated Press, BBC, Xinhua and other outlets'
23 November 2026 reporting, cross-checked across multiple news roundups
that day.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png (without MAKEFUN_OUTPUT_DIR it writes /output/entry.png)
```

Python 3.13, standard library only, no network. The program copies the
bundled `entry.png`, so every run produces byte-identical output.

## License

MIT — see `LICENSE`.
