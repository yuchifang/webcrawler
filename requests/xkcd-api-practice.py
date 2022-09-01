
'''
practice:

下載 xkcd 前十張圖片 (0~9)，檔名格式為 <編號>-<檔案名稱>
    example: 614-woodpecker.png
有些編號其實會拿到 404 not found 請注意
'''

import requests
from pathlib import Path
Path("./images").mkdir(parents=True, exist_ok=True)

# 請開始你的練習


'''
Hint: res.ok
'''
