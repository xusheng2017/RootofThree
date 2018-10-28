


import requests

#import re
       

url = 'http://maoyan.com/board/4'

headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
        }



def get_one_page(url , headears):
    response = requests.get(url , headers = headers)
    print(response.text)
    response.encoding = 'utf-8'
    if response.status_code == 200:
        return response.text
    return None
    
    
def main():
    print('hello lemon')
    html = get_one_page(url , headers)
    if html == None:
        print('get html error')
    else:
        print(html)