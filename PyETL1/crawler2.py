import requests
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/movie/index.html'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/80.0.3987.132 Safari/537.36'}

res = requests.get(url, headers=headers)

soup = BeautifulSoup(res.text, 'html.parser')

# print(soup)

title = soup.select('div.title a')
url_title = 'http://www.ptt.cc'

for t in title:

    article_title = t.text
    article_href = t['href']

    print(article_title)
    print(url_title + article_href)

    print('------------------------------')