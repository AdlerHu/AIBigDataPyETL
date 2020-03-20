import requests
from bs4 import BeautifulSoup
import time
import random
import os

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/80.0.3987.132 Safari/537.36'}
url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
url_head = 'https://www.ptt.cc'

# 建立另一個資料夾
path = './pttGossiping/'
if not os.path.exists(path):
    os.mkdir(path)

ss = requests.session()
ss.cookies['over18'] = '1'

for i in range(0, 3):
    res = ss.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    last_page_url = url_head + soup.select('a.btn.wide')[1]['href']
    title = soup.select('div.title a')

    for t in title:
        article_title = t.text
        article_url = url_head + t['href']

        # 依序進入各個文章
        article_res = ss.get(article_url, headers=headers)
        soup = BeautifulSoup(article_res.text, 'html.parser')

        try:
            # 標題、作者、日期的資訊
            result = soup.select('span.article-meta-value')
            author = result[0].text
            date = result[3].text
            # article_content = soup.select('div[id="main-content"]')[0].text.split('--')[0]
            article_content = soup.select('div#main-content')[0].text.split('2020')[1].split('--')[0]

            # 推、噓、箭頭
            answers = soup.select('div.push span.f1.hl.push-tag')

            push = 0
            boo = 0
            arrow = 0

            for answer in answers:
                if answer.text == '→ ':
                    arrow += 1
                elif answer.text == '噓 ':
                    boo += 1
                else:
                    push += 1

            print(article_title)
            print(author)
            print(date)
            print('推:', push)
            print('噓:', boo)
            print('→:', arrow)

            print('---------------split---------------')

            article_content += '---------------split--------------- \n'
            article_content += '標題: {} \n'.format(article_title)
            article_content += '作者: {} \n'.format(author)
            article_content += '時間: {} \n'.format(date)
            article_content += '推: {} \n'.format(push)
            article_content += '噓: {} \n'.format(boo)
            article_content += '箭頭: {} \n'.format(arrow)
            article_content += article_url

            try:
                with open(path + '{}.txt'.format(article_title), 'w', encoding='utf-8') as f:
                    f.write(article_content)

            except FileNotFoundError as err:
                print('寫入失敗')

        except OSError as err:
            print('讀取失敗')

        except IndexError as err:
            print('WTF')

    url = last_page_url

    time.sleep(random.randrange(3))
    print('換頁換頁換頁換頁換頁換頁換頁換頁換頁換頁換頁換頁換頁換頁換頁換頁換頁換頁')
