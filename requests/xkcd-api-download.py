import requests
from pathlib import Path
Path("./images").mkdir(parents=True, exist_ok=True)

url = 'https://xkcd.com/614/info.0.json'
res = requests.get(url)
res_json = res.json() # returns a dictionary
print(res_json)

img_url = res_json['img']
print(img_url)

img_name = img_url.split('/')[-1]
with open(Path(f"./images/{img_name}"), "wb") as f:
    img_res = requests.get(img_url)
    f.write(img_res.content)
