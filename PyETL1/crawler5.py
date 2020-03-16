import requests
from bs4 import BeautifulSoup
import os

path = './pttmovie/'

if not os.path.exists(path):
    os.mkdir(path)

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/80.0.3987.132 Safari/537.36'}

url = 'https://www.ptt.cc/bbs/movie/index.html'

for i in range(0, 3):
    res = requests.get(url, headers=headers)

    soup = BeautifulSoup(res.text, 'html.parser')

    title = soup.select('div.title a')

    for t in title:

        article_title = t.text
        article_url = 'http://www.ptt.cc' + t['href']

        article_res = requests.get(article_url, headers = headers)

        article_soup = BeautifulSoup(article_res.text, 'html.parser')

        article_content = article_soup.select('div[id="main-content"]')[0].text.split('--')[0]
        # print(article_content)

        try:
            with open(path + '{}.txt'.format(article_title), 'w', encoding='utf-8') as f:
                f.write(article_content)
        except FileNotFoundError as e:
            with open(path + '{}.txt'.format(article_title.replace('/', '_')), 'w', encoding='utf-8') as f:
                f.write(article_content)
        except OSError as e:
            print(e.args)

        print(article_title)
        print(article_url)

        print('------------------------------')

    last_page_url = 'https://www.ptt.cc' + soup.select('a.btn.wide')[1]['href']
    url = last_page_url

    print('換頁換頁換頁換頁換頁換頁換頁換頁換頁換頁換頁換頁換頁換頁換頁換頁換頁換頁換頁換頁換頁換頁換頁換頁')