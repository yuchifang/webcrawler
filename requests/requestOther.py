import requests
from pathlib import Path


Path("./images").mkdir(parents=True, exist_ok=True)

url = 'https://imgs.xkcd.com/comics/python.png'
res = requests.get(url)
with open(Path("./images/python.png"), "wb") as f:
    f.write(res.content)
