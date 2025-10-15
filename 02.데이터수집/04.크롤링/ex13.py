from selenium import webdriver
from selenium.webdriver.common.by import By 
import time
import re, time  #정규화/ 현재 시간

from bs4 import BeautifulSoup
import json

options = webdriver.ChromeOptions()
#options.add_experimental_option('detach', True)
options.add_argument('headless')
browser = webdriver.Chrome(options=options)
browser.maximize_window()

keyword = '자바'
url = f'https://www.hanbit.co.kr/search/search_list.html?keyword={keyword}'
browser.get(url)
time.sleep(1)

#더보기 클릭
xpath = '//*[@id="container"]/div[1]/ul/li[3]/a'
more = browser.find_element(By.XPATH, xpath)
more.click()
time.sleep(1)

soup = BeautifulSoup(browser.page_source, 'lxml')
book = soup.find('div', {'class': 'ser_list_wrap'})
books = book.find_all('li', {'class': 'ser_bg'})

list = []
no = 0
for book in books:
    no += 1
    title = book.strong.getText()
    img = book.img['src']
    author = book.span.getText()
    link = 'https://www.hanbit.co.kr' + book.a['href']

    print(title, img, author, link)
    data = {
        'no': no,
        'title': title,
        'image': img,
        'author': author,
        'link': link
    }
    list.append(data)

#json 파일에 저장
with open('data/books.json', 'a', encoding='utf-8') as file:
    json.dump(list, file, indent='\t', ensure_ascii=False)

print('프로그램 종료!')