from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome("./chromedriver")

url = 'https://www.ptt.cc/bbs/index.html'

driver.get(url)