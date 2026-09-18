#!/usr/bin/env python3
"""
Sample web scraping script — demonstration only.

Shows a polite scraping pattern: check robots.txt, use a real user agent,
rate-limit requests, parse listings with BeautifulSoup, and save clean
CSV/JSON output.

Usage:
    python scraper.py                          # parses the included sample page
    python scraper.py https://example.com/x    # fetches a live URL (robots.txt checked first)
"""
import csv
import json
import sys
import time
from pathlib import Path
from urllib.parse import urlparse
from urllib.robotparser import RobotFileParser

import requests
from bs4 import BeautifulSoup

USER_AGENT = "TanveerBuilds-SampleScraper/1.0 (demo)"
REQUEST_DELAY = 2.0  # seconds between requests — be polite


def allowed_by_robots(url):
    """Return True only if robots.txt permits fetching this URL."""
    parts = urlparse(url)
    rp = RobotFileParser()
    rp.set_url(f"{parts.scheme}://{parts.netloc}/robots.txt")
    try:
        rp.read()
    except Exception:
        return False  # if robots.txt can't be read, don't scrape
    return rp.can_fetch(USER_AGENT, url)


def fetch(url):
    if not allowed_by_robots(url):
        print(f"Blocked by robots.txt, skipping: {url}")
        return None
    time.sleep(REQUEST_DELAY)
    resp = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=15)
    resp.raise_for_status()
    return resp.text


def parse_listings(html):
    """Parse business listings out of the sample directory page layout."""
    soup = BeautifulSoup(html, "lxml")
    results = []
    for card in soup.select(".listing"):
        name = card.select_one(".listing-name")
        category = card.select_one(".listing-category")
        phone = card.select_one(".listing-phone")
        website = card.select_one(".listing-website")
        results.append({
            "name": name.get_text(strip=True) if name else "",
            "category": category.get_text(strip=True) if category else "",
            "phone": phone.get_text(strip=True) if phone else "",
            "website": website.get("href", "") if website else "",
        })
    return results


def save_csv(rows, path):
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "category", "phone", "website"])
        writer.writeheader()
        writer.writerows(rows)


def save_json(rows, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(rows, f, indent=2, ensure_ascii=False)


def main():
    if len(sys.argv) > 1:
        html = fetch(sys.argv[1])
        if html is None:
            return
    else:
        sample = Path(__file__).parent / "sample_page.html"
        print(f"No URL given — parsing the included sample page ({sample.name}).")
        html = sample.read_text(encoding="utf-8")

    rows = parse_listings(html)
    print(f"Parsed {len(rows)} listings.")
    save_csv(rows, "listings.csv")
    save_json(rows, "listings.json")
    print("Wrote listings.csv and listings.json")


if __name__ == "__main__":
    main()
