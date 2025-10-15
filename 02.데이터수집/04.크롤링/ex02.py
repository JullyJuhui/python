from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import keys  #키보드 입력받기

import time

brower = webdriver.Chrome()
brower.get('http://naver.com')

button = brower.find_element(By.CLASS_NAME, 'MyView-module__link_login___HpHMW')
button.click()
time.sleep(2)

id = brower.find_element(By.ID, 'id')
id.send_keys('sjuh2001')

pw = brower.find_element(By.ID, 'pw')
pw.send_keys('')
time.sleep(2)

login = brower.find_element(By.ID, 'log.login')
login.click()

time.sleep(100)