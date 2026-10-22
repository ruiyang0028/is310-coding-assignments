import requests
import time
from bs4 import BeautifulSoup

URL = "https://terraria.wiki.gg/wiki/Slime"

HEADERS = {
    "User-Agent": "IS310StudentProject/1.0 (educational project)"
}

# Check the website's scraping rules first
robots_url = "https://terraria.wiki.gg/robots.txt"
robots_response = requests.get(robots_url, headers=HEADERS, timeout=10)
robots_response.raise_for_status()

print("Please review robots.txt before scraping.")
print(robots_response.text[:1000])

# Request the page only after confirming the rules allow it
time.sleep(2)
response = requests.get(URL, headers=HEADERS, timeout=10)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.find("h1")
    if title:
        print("Page title:", title.get_text(strip=True))

    main = soup.select_one("#mw-content-text")
    if main:
        text = main.get_text(" ", strip=True)
        print("Approximate word count:", len(text.split()))

else:
    print("Request failed with status:", response.status_code)

