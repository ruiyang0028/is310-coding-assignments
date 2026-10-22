import csv
import time
import requests
from bs4 import BeautifulSoup
from urllib.robotparser import RobotFileParser

BASE_URL = "https://terraria.wiki.gg"
ROBOTS_URL = BASE_URL + "/robots.txt"

HEADERS = {
    "User-Agent": "IS310StudentProject/1.0 (educational project)"
}

PAGES = [
    {
        "type": "Enemy",
        "url": BASE_URL + "/wiki/Slime"
    },
    {
        "type": "Item",
        "url": BASE_URL + "/wiki/Gel"
    }
]


def main():
    # Check the site's robots.txt rules
    robots = RobotFileParser()
    robots.set_url(ROBOTS_URL)

    try:
        robots.read()
    except Exception as error:
        print("Could not check robots.txt:", error)
        print("Stopping to avoid scraping without checking the rules.")
        return

    results = []

    for page in PAGES:
        url = page["url"]

        if not robots.can_fetch(HEADERS["User-Agent"], url):
            print("Scraping is not allowed for:", url)
            continue

        try:
            time.sleep(2)

            response = requests.get(
                url,
                headers=HEADERS,
                timeout=10
            )

            if response.status_code != 200:
                print("Request failed:", url, response.status_code)
                continue

            soup = BeautifulSoup(response.text, "html.parser")

            title_tag = soup.find("h1")
            title = (
                title_tag.get_text(strip=True)
                if title_tag
                else "Title not found"
            )

            content = soup.select_one("#mw-content-text")

            if content:
                # Remove navigation and other page elements
                for element in content.select(
                    "table, .navbox, .mw-editsection, script, style"
                ):
                    element.decompose()

                text = content.get_text(" ", strip=True)
                word_count = len(text.split())
                link_count = len(content.find_all("a", href=True))
            else:
                word_count = 0
                link_count = 0

            results.append({
                "page_type": page["type"],
                "title": title,
                "url": url,
                "word_count": word_count,
                "link_count": link_count
            })

            print("Scraped:", title)
            print("Approximate word count:", word_count)
            print("Links found:", link_count)

        except requests.RequestException as error:
            print("Error requesting page:", error)

    # Save collected data as CSV
    with open(
        "terraria_wiki_data.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as csvfile:
        fieldnames = [
            "page_type",
            "title",
            "url",
            "word_count",
            "link_count"
        ]

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    print("Saved results to terraria_wiki_data.csv")
    print("Pages collected:", len(results))


if __name__ == "__main__":
    main()

