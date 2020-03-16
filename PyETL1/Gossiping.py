import requests
from bs4 import BeautifulSoup
import time
import random

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/80.0.3987.132 Safari/537.36'}
url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
url_head = 'https://www.ptt.cc'

titles = []
title_href = []

ss = requests.session()
ss.cookies['over18'] = '1'

for i in range(0, 5):
    res = ss.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    title = soup.select('div.title a')

    for t in title:
        print(t.text)
        print(url_head + t['href'])
        print("------------------------------------------------------")

    last_page_url = url_head + soup.select('a.btn.wide')[1]['href']
    url = last_page_url

    time.sleep(random.randrange(3))
    print('換頁換頁換頁換頁換頁換頁換頁換頁換頁換頁換頁換頁換頁換頁換頁換頁換頁換頁')