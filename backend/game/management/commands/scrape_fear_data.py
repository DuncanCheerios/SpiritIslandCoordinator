import os

from django.conf import settings
from django.core.management.base import BaseCommand
from game.models import FearCard
import requests
from bs4 import BeautifulSoup
import time


class Command(BaseCommand):
    help = "Scrape and cache Fear Card details with stages"

    WIKI_URL = "https://spiritislandwiki.com/index.php?title=Fear_Cards"

    def handle(self, *args, **kwargs):
        headers = {"User-Agent": "Mozilla/5.0"}
        resp = requests.get(self.WIKI_URL, headers=headers)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")

        for row in soup.select("table.wikitable tr"):
            cols = row.find_all("td")
            if not cols:
                continue

            # Card name and link
            link_tag = cols[-1].find("a")
            if not link_tag or not link_tag.get("href"):
                continue
            name = link_tag.get_text(strip=True)
            card_url = "https://spiritislandwiki.com" + link_tag['href']

            # Optional image from main table
            img_tag = cols[0].find("img")
            image_url = img_tag['src'] if img_tag else ""

            # Fetch individual card page
            try:
                card_resp = requests.get(card_url, headers=headers)
                card_resp.raise_for_status()
                card_soup = BeautifulSoup(card_resp.text, "html.parser")

                # Example: assume stages are in h3 headings like "Stage One", "Stage Two", "Stage Three"
                stage_text = {"stage_one": "", "stage_two": "", "stage_three": ""}

                # table = card_soup.select('table')
                rows = card_soup.find_all('tr')

                stage_text["stage_one"] = rows[2].find_all('td')[-1].get_text()
                stage_text["stage_two"] = rows[3].find_all('td')[-1].get_text()
                stage_text["stage_three"] = rows[4].find_all('td')[-1].get_text()

                image_tag = card_soup.find("img")
                image_url = "https://spiritislandwiki.com" + image_tag.get('src')

                local_image_path = download_image(image_url, name)
                FearCard.objects.update_or_create(
                    name=name,
                    defaults={
                        "stage_one": stage_text["stage_one"],
                        "stage_two": stage_text["stage_two"],
                        "stage_three": stage_text["stage_three"],
                        "image": local_image_path,
                    }
                )
                self.stdout.write(f"Updated {name}")
                time.sleep(0.3)  # polite delay between requests

            except Exception as e:
                self.stderr.write(f"Failed to fetch {name}: {e}")


def download_image(image_url, card_name):
    if not image_url:
        return None
    filename = card_name.replace(" ", "_") + os.path.splitext(image_url)[-1]
    local_path = os.path.join(settings.MEDIA_ROOT, 'fear_cards', filename)
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    resp = requests.get(image_url, stream=True)
    if resp.status_code == 200:
        with open(local_path, 'wb') as f:
            for chunk in resp.iter_content(1024):
                f.write(chunk)
        return f'fear_cards/{filename}'
    return None