# web-scraping-data-extraction

> **Sample / demo build.** This is a small learning project showing a polite way to scrape a page: check robots.txt first, keep a delay between requests, parse listings with BeautifulSoup, and save clean CSV and JSON. Not production code.

## What it shows

* It checks robots.txt before fetching anything, and skips whatever is disallowed.
* It fetches politely: a real user agent, a short pause between requests, and timeout handling.
* It parses listing cards into structured fields (name, category, phone, website).
* It writes the same data to `listings.csv` and `listings.json`.

## Project structure

```
.
├── scraper.py         # Sample scraper (runs offline against the sample page)
├── sample_page.html   # Tiny fake directory page so the demo runs out of the box
└── README.md
```

## How to run the sample

```bash
pip install -r requirements.txt

# Parse the included sample page (no network needed)
python scraper.py

# Or fetch a live URL (robots.txt is checked first)
python scraper.py https://example.com/listings
```

## Notes

* This is a **demonstration**, not a finished product. It handles one page layout, has no proxy rotation, and no retry logic.
* Only scrape sites you are allowed to scrape. Always check robots.txt and the site's terms, and keep your request rate reasonable.
* Never collect personal data or anything behind a login with a script like this.

## Tech

Python · requests · BeautifulSoup · urllib.robotparser · CSV / JSON output
