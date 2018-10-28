import requests

url = 'https://www.zhihu.com/explore'

data = {
	'name' : 'lemon',
	'age' : '25'
}
headers = {
	'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}

req = requests.get(url , headers = headers)

req.encoding = 'utf-8'

print(req.text)