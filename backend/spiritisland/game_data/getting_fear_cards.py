import requests
from bs4 import BeautifulSoup
import json

URL = "https://spiritislandwiki.com/index.php?title=Fear_Card"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/118.0.0.0 Safari/537.36"
}

response = requests.get(URL, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

fear_cards = []

content = soup.find("div", {"id": "mw-content-text"})
if content:
    for tag in content.select("center td > a"):
        text = tag.get_text(strip=True)
        fear_cards.append(text)

print("Found Fear Cards:")
for t in sorted(set(fear_cards)):
    print("-", t)

print(len(fear_cards))

with open("FearCards.json", "w", encoding="utf-8") as f:
    json.dump(fear_cards, f, indent=2, ensure_ascii=False)