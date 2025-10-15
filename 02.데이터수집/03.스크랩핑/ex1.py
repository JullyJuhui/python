import requests
from bs4 import BeautifulSoup

url = 'https://www.naver.com/'
res = requests.get(url)

soup = BeautifulSoup(res.text, 'lxml')
title = soup.title  #= soup.find('title')

print(1, title)
print(2, title.get_text())  #= getText()

title = soup.find('title')
print(3, title)

a = soup.a
print(4, a)

span = a.span 
print(5, span.getText())

attrs = a.attrs  #딕셔너리 형식
print(6, attrs, type(attrs))  #속성 하나 존재 - href

href = a['href'] #= a.get('href')
print(7, href)

#a태그 전부 찾기
aItems = soup.find_all('a')  #8개

for aItem in aItems:
    print(aItem.span.getText())