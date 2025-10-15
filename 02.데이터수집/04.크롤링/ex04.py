from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('headless')  #브라우저 안보임 - back에서 돌아감
#options.add_argument('window-size=1920x1080')

browser = webdriver.Chrome(options = options)
url = 'http://flight.naver.com'
browser.get(url)

browser.get_screenshot_as_file('data/filght3.png')