import requests
from bs4 import BeautifulSoup
import json

URL = "https://spiritislandwiki.com/index.php?title=List_of_Event_Cards"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/118.0.0.0 Safari/537.36"
}

response = requests.get(URL, headers=headers)
response.raise_for_status()  # raises error if request fails

soup = BeautifulSoup(response.text, "html.parser")

# On that wiki, event cards are usually listed in <h3> or table elements
# We’ll try to find all the card titles (bold or link text in the Event section)
event_titles = []


# Example: titles in the main content area
content = soup.find("div", {"id": "mw-content-text"})
if content:
    for tag in content.select("td > a"):
        text = tag.get_text(strip=True)
        event_titles.append(text)

print("Found events:")
for t in sorted(set(event_titles)):
    print("-", t)

print(len(event_titles))

with open("EventNames.json", "w", encoding="utf-8") as f:
    json.dump(event_titles, f, indent=2, ensure_ascii=False)