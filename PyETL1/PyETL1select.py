import requests
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/joke/index.html'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/80.0.3987.132 Safari/537.36'}

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')

list1 = soup.select('a#logo')
print(list1[0])
print(list1[0].text)
print('https://www.ptt.cc' + list1[0]['href'])

titles = soup.select('div.title')

for item in titles:
    print(item.text)