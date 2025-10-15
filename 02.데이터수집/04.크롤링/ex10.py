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

#예보
xpath = '//*[@id="content-body"]/div[4]/div/div/div[1]/ul/li[3]/a/span'
forecast = browser.find_element(By.XPATH, xpath)
forecast.click()
time.sleep(1)

#날짜 선택 반복문
for i in range(1, 8):
    xpath = f'//*[@id="local-weather"]/div/div[{i}]/h3/a'
    day = browser.find_element(By.XPATH, xpath)
    title = day.text.replace('\n', '')
    print(f'-------------------------{title}---------------------------')
    day.click()

    soup = BeautifulSoup(browser.page_source, 'lxml')
    local = soup.find('div', {'id': 'weather'})
    citys = local.find_all('dl', {'class': re.compile('^po_')})

    for city in citys:
        name = city.dt.getText()
        temp = city.span.getText()
        weather = city.i.getText()

        print(name, temp, weather)
