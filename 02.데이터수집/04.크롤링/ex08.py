from selenium import webdriver
from selenium.webdriver.common.by import By 
import time
import re, time  #정규화/ 현재 시간

from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
# options.add_experimental_option('detach', True)
options.add_argument('headless')
browser = webdriver.Chrome(options=options)
browser.maximize_window()

url = 'https://www.weather.go.kr/w/index.do'
browser.get(url)

# all = browser.find_element(By.XPATH, '//a[text()="전국"]')
# all.click()

#id 찾고 그 안에서 찾기
soup = BeautifulSoup(browser.page_source, 'lxml')
local = soup.find('div', {'id': 'weather2'})

citys = local.find_all('dl', {'class': re.compile('^po_')})

now_date = time.strftime('%Y년%m월%d일 %H시%M분%S초')
print(now_date)
for city in citys:
    
    name = city.dt.getText()
    temp = city.span.getText()
    weather = city.i.getText()

    print(name, temp, weather)
    print('-'*30)