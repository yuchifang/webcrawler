
'''
practice:

下載 xkcd 前十張圖片 (0~9)，檔名格式為 <編號>-<檔案名稱>
    example: 614-woodpecker.png
有些編號其實會拿到 404 not found 請注意
'''


import requests
from pathlib import Path
Path("./requests/images").mkdir(parents=True, exist_ok=True)

# https://xkcd.com/614/info.0.json example

notGetAllImages = True
imageCount = 1
imageList = []
while notGetAllImages:
    apiLink = f"https://xkcd.com/{imageCount}/info.0.json"
    res = requests.get(apiLink)
    fileImgUrl = res.json()['img']
    fileTitle = res.json()['title']
    imgItem = {}
    imgItem['imgUrl'] = fileImgUrl
    imgItem['name'] = fileTitle
    imgItem['number'] = imageCount
    if (res.ok and fileImgUrl):
        imageList.append(imgItem)

    if (len(imageList) == 10):
        notGetAllImages = False

    imageCount = imageCount + 1


for item in imageList:
    fileName = f"{item['number']}-{item['name']}.png"
    resImg = requests.get(item['imgUrl'])
    with open(Path(f"./requests/images/{fileName}"), 'wb',) as file:
        file.write(resImg.content)

print(imageList)


'''
Hint: res.ok
'''
