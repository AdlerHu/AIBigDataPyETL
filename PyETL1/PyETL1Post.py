import requests
from bs4 import BeautifulSoup

url = 'http://baae0774.ngrok.io/hello_post'
# data = {'username': 'Adler'}

# res = requests.post(url, data=data)
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

# Get the key for form data by 'get'
form_key = soup.select('input')[0]['name']
print(form_key)

data = {form_key: 'Adler'}

res = requests.post(url, data=data)
soup = BeautifulSoup(res.text, 'html.parser')

print(soup.prettify())