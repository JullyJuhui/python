#[쿠팡]-[검색어]-[노트북] 1페이지 결과 상품이름, 상품가격
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36')
browser = webdriver.Chrome(options=options)
#browser = webdriver.Chrome()

keyword = '노트북'
url = f'https://www.gmarket.co.kr/n/search?keyword={keyword}'
browser.get(url)

time.sleep(2)
with open('data/gmarket.html', 'w', encoding='utf8') as file:
    file.write(browser.page_source)

#java script
#browser.execute_script('alert("..")')
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
time.sleep(2)

#---------------------------------------------------------
from bs4 import BeautifulSoup
import re
import json

soup = BeautifulSoup(browser.page_source, 'lxml')

items = soup.find_all('div', attrs={'class', 'box__item-container'})
print(len(items))

cnt = 0
list = []
for idx, item in enumerate(items):
    title = item.find('span', {'class': 'text__item'}).getText()
    price = item.find('strong',{'class': 'text text__value'}).getText()
    image = 'https:' + item.find('img', {'class': 'image__item'})['src']
    count = item.find('li', {'class': re.compile('list-item list-item__pay-count')})
    link = item.a['href']

    if count:
        count = int(re.sub('구매|건|,', '', count.getText()))
    else:
        count = 0

    if count >= 100:  #인기상품
        cnt += 1
        print(cnt, title, price, image, f'구매건수: {count}')
        data = {
            'no': cnt,
            'title': title,
            'price': price,
            'count': count,
            'img': image,
            'link': link
        }
        list.append(data)

with open('data/gmarket.json', 'w', encoding='utf-8') as file:
    json.dump(list, file, indent='\t', ensure_ascii=False) #리스트, 파일로 덤프, 들여쓰기, 한글깨지는거 방지

browser.quit()
print('프로그램 종료')