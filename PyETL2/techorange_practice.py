import requests
from bs4 import BeautifulSoup
import json
import time

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/80.0.3987.132 Safari/537.36'}
url = 'https://buzzorange.com/techorange/wp-admin/admin-ajax.php'

for k in range(1, 6):
    data_str = '''action: fm_ajax_load_more
    nonce: 0bb223c976
    page: {}'''.format(k)

    data = {i.split(': ')[0]: i.split(': ')[1] for i in data_str.split('\n')}

    res = requests.post(url, headers=headers, data=data)
    jdata = json.loads(res.text)

    # get html-like string
    html = jdata['data']
    soup = BeautifulSoup(html, 'html.parser')

    title_list = soup.select('h4.entry-title a')

    for i in title_list:
        article_title = i.text
        article_url = i['href']

        print(article_title)
        print(article_url)
        print('------------------------------')

    time.sleep(3)
    print('換頁換頁換頁換頁換頁換頁換頁換頁換頁換頁換頁換頁換頁換頁換頁換頁')