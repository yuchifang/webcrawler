import requests

payload = {'a': 1, 'rick': 'roll'}
res = requests.post('https://httpbin.org/post', data=payload)

print(res.text)
