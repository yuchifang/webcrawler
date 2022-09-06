# 字串 % 特別原因

import requests
from bs4 import BeautifulSoup

response = requests.get("https://travel.ettoday.net/category/%E6%A1%83%E5%9C%92/")

soup = BeautifulSoup(response.text,"html.parser")
print(soup.prettify())

