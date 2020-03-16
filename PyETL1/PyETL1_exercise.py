import requests
from bs4 import BeautifulSoup

studentID = '200'
studentName = 'Adler'

url = 'http://932ddf15.ngrok.io/test?studentID=' + studentID + '&' + 'studentName=' + studentName
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/80.0.3987.132 Safari/537.36'}
ss = requests.session()
res = ss.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')

data = {}
key = soup.select('input')[0]['name']
value = soup.select('input')[0]['value']
data[key] = value

res = ss.post(url, headers=headers, data=data)
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.prettify())