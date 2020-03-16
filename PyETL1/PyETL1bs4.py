from urllib import request
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/joke/index.html'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/80.0.3987.132 Safari/537.36'}

req = request.Request(url, headers=headers)
res = request.urlopen(req).read().decode('utf-8')

# print(res.read().decode('utf-8'))

soup = BeautifulSoup(res, 'html.parser')

print(soup)