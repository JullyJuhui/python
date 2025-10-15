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

url = 'https://www.weather.go.kr/w/index.do'
browser.get(url)

#전국
all = browser.find_element(By.XPATH, '//a[text()="전국"]')
all.click()
time.sleep(1)

#어제
xpath= '//*[@id="content-body"]/div[4]/div/div/div[1]/ul/li[1]/a/span'
yesterday = browser.find_element(By.XPATH, xpath)
yesterday.click()
time.sleep(1)

#id 찾고 그 안에서 찾기
soup = BeautifulSoup(browser.page_source, 'lxml')
local = soup.find('div', {'id': 'minmax'})
citys = local.find_all('dl', {'class': re.compile('^po2_')})

for idx, city in enumerate(citys):
    name = city.dt.getText()
    min = city.find('span', {'class': 'red'}).getText()
    max = city.find('span', {'class': 'blue'}).getText()

    print(idx+1, name, max, min)