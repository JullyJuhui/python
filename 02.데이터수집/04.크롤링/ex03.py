from selenium import webdriver

#브라우저 항상 오픈
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)  
browser = webdriver.Chrome(options = options)

browser.maximize_window()  #전체화면

url = 'https://flight.naver.com'
browser.get(url)

browser.get_screenshot_as_file('data/flight.png')  #화면 캡쳐해서 파일로 저장


#브라우저 종료
browser.quit()  