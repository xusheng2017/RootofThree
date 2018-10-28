import urllib.request
import urllib.parse


url1 = 'https://www.httpbin.org/post'

data = bytes(urllib.parse.urlencode({'word' : 'hello'}) , encoding = 'utf-8')

rec = urllib.request.urlopen(url1 , data = data)


print(rec.read())