import requests  #인터넷 접속
from bs4 import BeautifulSoup

url = 'https://www.naver.com/'
res = requests.get(url)  #주소 접속 후 가져오기

soup = BeautifulSoup(res.text, 'lxml')  #텍스트를 lxml로 파싱한 결과 soup에 넣음

#title
title = soup.title
print(1, title.get_text())  #이름만 가져오기

#a영역
a = soup.a
print(2, a.span)  #span
print(3, a.span.get_text())  #span 텍스트만 가져오기
print(4, a.attrs)  #속성
print(5, a['href'])  #href 속성만