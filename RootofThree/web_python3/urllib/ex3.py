import urllib.request
import urllib.parse


url = 'https://httpbin.org/post'
headers = {
	'Host' : 'httpbin.org',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
}
data = {
	'name' : 'lemon'
}

str_data = bytes(urllib.parse.urlencode(data) , encoding = 'utf-8')

req = urllib.request.Request(url = url , data = str_data  , headers = headers , method = 'POST')
rec = urllib.request.urlopen(req)
print(rec.read().decode('utf-8'))
