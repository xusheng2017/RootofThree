import urllib.request
import urllib.error
import socket

requset = urllib.request.Request('https://www.baidu.com')
try:
	rec = urllib.request.urlopen(requset , timeout = 0.01)
	rec.encode = 'utf-8'
except urllib.error.URLError as e:
	if isinstance(e.reason , socket.timeout):
		print("time out")
	print(rec.status)
	

