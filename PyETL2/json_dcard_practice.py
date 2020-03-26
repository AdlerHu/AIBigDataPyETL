import json
from urllib import request
import time
import random

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/80.0.3987.132 Safari/537.36'}

url = 'https://www.dcard.tw/service/api/v2/forums/dressup/posts?limit=30&before=233303602'

# read file
with open('jsfile.txt', 'r', encoding='utf-8') as f:
    res = f.read()

jdata = json.loads(res)

for t in jdata:
    article_title = t['title']
    article_url = 'https://www.dcard.tw/f/dressup/p/' + str(t['id'])
    print(article_title)
    print(article_url)

    for img in t['mediaMeta']:
        img_url = img['url']
        print('\t', img_url)

        try:
            request.urlretrieve(img_url, './dcard_img/' + img_url.split('/')[-1])
        except:
            time.sleep(random.randint(3, 5))