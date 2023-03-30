import requests
from bs4 import BeautifulSoup


with open("data.html") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")
all_links = soup.find_all(class_="listItem_name__Qq_Y8")

for items in all_links:
    items_text = items.text
    items_href = items.get("href")
    print(f"{items_text}: {items_href}")

