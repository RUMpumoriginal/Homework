import csv
from pathlib import Path
import requests
from bs4 import BeautifulSoup

quote = []
authors = []
data = []

HEADERS = {"Nobody": "nothing"}

file_path = Path(__file__).with_name("Life.csv")

respone = requests.get("https://quotes.toscrape.com/tag/life/", headers=HEADERS, timeout=10)

code = respone.text

soup = BeautifulSoup(code, "lxml")

q_data = soup.find_all("span", class_="text")
a_data = soup.find_all("small", class_="author")

for item in q_data:
    quote.append(item.get_text(strip=True))

for item in a_data:
    authors.append(item.get_text(strip=True))

for q_item, a_item in zip(quote, authors):
    data.append({"author": a_item, "text": q_item})

with file_path.open( "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["author", "text"])
    writer.writeheader()
    writer.writerows(data)

