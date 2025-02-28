import requests
from bs4 import BeautifulSoup
import os

DOC_URLS = {
    "Segment": "https://segment.com/docs/",
    "mParticle": "https://docs.mparticle.com/",
    "Lytics": "https://docs.lytics.com/",
    "Zeotap": "https://docs.zeotap.com/home/en-us/"
}

def scrape_and_save():
    os.makedirs("docs", exist_ok=True)
    for name, url in DOC_URLS.items():
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        text = soup.get_text()
        with open(f"docs/{name}.txt", "w", encoding="utf-8") as f:
            f.write(text)
if __name__ == "__main__":
    scrape_and_save()
