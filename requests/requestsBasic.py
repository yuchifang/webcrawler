name = "test"
print(f'somesome{name!r}')

import requests
from requests.exceptions import HTTPError
# 錯誤處理
for url in ['https://api.github.com','https://api.github.com/invalid']:
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    else:
        print('Success!')


response = requests.get('https://api.github.com') 

print(response.ok)
print(response.url)
# print(dir(response))
# help(response)


# params= [('q', 'requests+language:python')],
# params= b'q=requests+language:python'

# response.encoding = 'utf-8' before 
# response.text

# print("content",response.content)
# print("text",response.text)

# response.headers 取得 headers
print("response",response.json()['current_user_url'])

