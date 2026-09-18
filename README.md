# web-scraping-data-extraction

> **Sample / demo build** — a polite web scraping pattern: check robots.txt, rate-limit requests, parse listings with BeautifulSoup, and save clean CSV/JSON output. Built for learning and demonstration, not production use.

## What this sample demonstrates

- **robots.txt compliance** — checks permission before fetching any URL, and skips anything disallowed
- **Polite fetching** — real user agent, delay between requests, timeout handling
- **Parsing** — extracts structured fields (name, category, phone, website) from listing cards with BeautifulSoup
- **Clean output** — writes the same data to both `listings.csv` and `listings.json`

## Project structure

```
.
├── scraper.py         # Sample scraper (works offline against the sample page)
├── sample_page.html   # Tiny fake directory page so the demo runs out of the box
└── README.md
```

## How to run the sample

```bash
pip install -r requirements.txt

# Parse the included sample page (no network needed)
python scraper.py

# Or fetch a live URL — robots.txt is checked first
python scraper.py https://example.com/listings
```

## Notes

- This is a **demonstration**, not a finished product: no proxy rotation, no JavaScript rendering, no CAPTCHA handling.
- Only scrape sites you have the right to scrape. Respect `robots.txt`, terms of service, and rate limits. Never scrape login-walled pages or personal data.
- For JavaScript-heavy sites, swap `requests` for Playwright in `fetch()`.

## Tech

Python · requests · BeautifulSoup · urllib.robotparser · CSV / JSON output
