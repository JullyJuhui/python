#[네이버] - [네이버항공권] 이번달 25일~26일 제주도 항공권 검색
from selenium import webdriver
from selenium.webdriver.common.by import By 
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

browser = webdriver.Chrome(options = options)
browser.maximize_window()

url = 'https://flight.naver.com/'
browser.get(url)
time.sleep(1)

def wait_until(xpath):
    WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.XPATH, xpath))) #찾을때까지 기다려라~~ 하는 거

#7일간 보지않기 버튼
btn = browser.find_element(By.CLASS_NAME, 'FullscreenPopup_suspend')
btn.click()
time.sleep(1)

#가는 날 선택 버튼
date = browser.find_element(By.XPATH, '//button[text()="가는 날"]')  #문서 전체에서 button tag의 텍스트 함수 비교
date.click()
time.sleep(1)

#날짜 선택 - 가는 날(25일)
departure = browser.find_elements(By.XPATH, '//b[text()="25"]')
departure[0].click()  #ex) 다음달 departure[1]
time.sleep(1)

#날짜 선택 - 오는 날(26일)
arrival = browser.find_elements(By.XPATH, '//b[text()="26"]')
arrival[0].click()
time.sleep(1)

#도착 버튼 선택
destination = browser.find_element(By.XPATH, '//b[text()="도착"]')
destination.click()
time.sleep(2)

#도착지 선택(제주)
city = browser.find_element(By.XPATH, '//button[text()="제주"]')
city.click()
time.sleep(1)

#검색 버튼 선택
search = browser.find_element(By.XPATH, '//span[text()="항공권 검색"]')
search.click()
time.sleep(1)


try:
    #첫번째 항공편 하나만
    with open('data/flight.txt', 'w', encoding='utf-8') as file:
        first = '//*[@id="__next"]/div/main/div[4]/div/div[2]/div[2]/div[1]'
        wait_until(first)
        # el = browser.find_element(By.XPATH, first)
        # print(el.text)

        els = browser.find_elements(By.CLASS_NAME, 'domestic_Flight__8bR_b')
        for idx, el in enumerate(els):
            # print(f'[{idx+1}] {el.text}')
            # print('-'*50)
            file.write(f'[{idx+1}] {el.text}\n')
            file.write('-'*50)
            file.write('\n')

except:
    pass

finally:
    browser.quit()
    print('프로그램 종료')