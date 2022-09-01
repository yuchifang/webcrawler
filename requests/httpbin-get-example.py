import requests

payload = {'a': 1, 'rick': 'roll'}
res = requests.get('https://httpbin.org/get', params=payload)

print(res.url)
