

import requests


url = "https://www.sogou.com/"
response = requests.get(url)
print(response.text)

with open('./text.html',"w") as file:
    file.write(response.text)