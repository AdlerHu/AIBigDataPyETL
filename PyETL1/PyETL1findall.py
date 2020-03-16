import requests
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/joke/index.html'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/80.0.3987.132 Safari/537.36'}

res = requests.get(url, headers=headers)

soup = BeautifulSoup(res.text, 'html.parser')

title = soup.find_all('a', {'id': 'logo'})
# title = soup.find_all('a', id='logo')

print(title[0])
print(title[0].text)
print('https://www.ptt.cc' + title[0]['href'])


# test = soup.find_all('a', class_='board')
test = soup.findAll('a', {'class': 'board'})

print(test)