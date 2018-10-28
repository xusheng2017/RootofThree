import requests

req = requests.get('https://www.baidu.com')
req.encoding = 'utf-8'
print(type(req))
print(req.status_code)
print(type(req.text))
print(req.text)
print(req.cookies)