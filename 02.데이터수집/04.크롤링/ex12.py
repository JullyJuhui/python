from selenium import webdriver
from selenium.webdriver.common.by import By 
import time
import re, time  #정규화/ 현재 시간

from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
#options.add_argument('headless')
browser = webdriver.Chrome(options=options)
#browser.maximize_window()

url = 'https://www.coffeebeankorea.com/store/store.asp'
browser.get(url)

store = browser.find_element(By.ID, 'storeListUL')
lis = store.find_elements(By.TAG_NAME, 'li')

# for li in lis:
#     print(li.get_attribute('data-no'))

lis = [li.get_attribute('data-no') for li in lis]
print(lis)