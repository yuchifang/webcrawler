import requests

# 建立一個 images 資料夾
from pathlib import Path
Path("./images").mkdir(parents=True, exist_ok=True)
# Reference: https://stackoverflow.com/questions/273192/how-can-i-safely-create-a-nested-directory

url = 'https://imgs.xkcd.com/comics/python.png'
res = requests.get(url)

with open(Path("./images/python.png"), "wb") as f:
    f.write(res.content)
