from selenium import webdriver
from selenium.webdriver.common.by import By 
import time
import re, time  #정규화/ 현재 시간

from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
#options.add_experimental_option('detach', True)
options.add_argument('headless')
browser = webdriver.Chrome(options=options)
browser.maximize_window()

url = 'https://www.coffeebeankorea.com/store/store.asp'
browser.get(url)

browser.execute_script("storePop2(142)")
time.sleep(2)
soup = BeautifulSoup(browser.page_source, 'lxml')

#매장이름
name = soup.select('div.store_txt > h2')[0].string
info = soup.select('div.store_txt > table.store_table > tbody > tr > td')
address = info[2].getText()
phone = info[3].string
print('매장이름|', name)
print('매장주소|', address)
print('매장전화|', phone)


import requests
import os

path = 'data/store'
if not os.path.exists(path):
    os.mkdir(path)

#사진
imgs = soup.select('div.slick-slide > img')

for img in imgs:
    src = 'https://www.coffeebeankorea.com/' + img.attrs['src']
    index = src.rindex('/')
    file_name = src[index:]
    print(file_name)

    #이미지 다운로드
    with open(path + file_name, 'wb') as file:
        res = requests.get(src)
        file.write(res.content)