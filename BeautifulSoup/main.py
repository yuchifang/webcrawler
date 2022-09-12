# 字串 % 特別原因

import re
import requests
from bs4 import BeautifulSoup

response = requests.get("https://travel.ettoday.net/category/%E6%A1%83%E5%9C%92/")
soup = BeautifulSoup(response.text,"html.parser")

soup.prettify()

# find 字串的部份
# find(string="someString")
result = soup.find("p")
print(result)
print(result.find_parent())
print(result.find_next_sibling(content="ETtoday旅遊雲"))
# re.compile 是甚麼