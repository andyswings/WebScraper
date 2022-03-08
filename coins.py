import requests
from bs4 import BeautifulSoup

page = requests.get("https://coinstats.app/coins/litecoin")
soup = BeautifulSoup(page.content, "html.parser")
html = list(soup.children)[1]
# print(list(soup.children))
# print([type(item) for item in list(soup.children)])

print(soup.find_all('span', class_='main-price')[0])
