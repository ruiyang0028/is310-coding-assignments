import requests
from bs4 import BeautifulSoup

url = "https://terraria.wiki.gg/wiki/Slime"

headers = {
    "User-Agent": "IS310StudentProject/1.0 (educational project)"
}

response = requests.get(url, headers=headers, timeout=10)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.find("h1")
    if title:
        print("Page title:", title.get_text(strip=True))

    print("Page successfully downloaded!")
else:
    print("Request failed:", response.status_code)
