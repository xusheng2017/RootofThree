

import requests	
from requests.exceptions import RequestException
import re
import json
import time
import pandas
import sqlite3


def get_onepage_html(url):
	try:
		headers = {
			'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
		}
		response = requests.get(url , headers = headers)
		if response.status_code == 200:
			return response.text	
		return None
	except RequestException as e:
		raise e
	

def get_onepage_info(html):
	#                                    index[0]                  image[1]                     title[2]             actor[3]                  time[4]               socre[5]              socre[6]         
	re_str_test = '<dd>.*?board-index.*?>(.*?)</i>.*?<img data-src="(.*?)".*?"name".*?data-val.*?>(.*?)</a>.*?"star">(.*?)</p>.*?"releasetime">(.*?)</p>.*?"integer">(.*?)</i>.*?"fraction">(.*?)</i></p>.*?</dd>'
	pattern = re.compile(re_str_test ,re.S)
	items = re.findall(pattern, html)
	for item in items:
		yield{
			'index' : item[0],
			'image' : item[1],
			'title' : item[2],
			'actor' : item[3].strip()[3:],
			'time'  : item[4].strip()[5:],
			'score' : item[5] + item[6]
		}


def write_to_file(content):
	with open('maoyan_info.txt' , 'a' , encoding = 'utf-8') as f:
		f.write(json.dumps(content , ensure_ascii = False ) + '\n')





def write_to_excel(content):
	#用pandas呈现并打印新闻的内容
	df = pandas.DataFrame(content)
	#print(df.head(5))
	#将新闻内容以excel的方式导入到当前目录的
	df.to_excel('maoyan.xlsx')


#写入sqlite3数据库
def write_file_to_sqlite3(content):
	df = pandas.DataFrame(content)
	print(type(df))
	with sqlite3.connect('maoyan.sqlite') as db:
		df.to_sql('maoyan' , con = db)

#读取sqlite3数据库
def read_file_from_sqlite3(sqlite):
	with  sqlite3.connect(sqlite) as db:
		df2 = pandas.read_sql_query('select	* from maoyan', con = db)
		print(df2)

def main():
	url = 'http://maoyan.com/board/4?offset='
	all_items = []
	for i in range(2):
		time.sleep(1)
		new_url = url + str(i * 10)
		#print(new_url)
		html= get_onepage_html(new_url)
		items = get_onepage_info(html)
		for item in items:
			all_items.append(item)
	write_to_excel(all_items)
	write_to_file(all_items)
	write_file_to_sqlite3(all_items)
	read_file_from_sqlite3('maoyan.sqlite')
	for item in all_items:
		pass
		#print(item)


if __name__ == '__main__':
	main()
'''	
	html = get_onepage_html(url, headers)
	#print(html)
	items = get_onepage_info(html)
	print(type(items))
	for item in items:
		print(item)
'''












