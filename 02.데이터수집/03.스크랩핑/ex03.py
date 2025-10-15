import requests
from bs4 import BeautifulSoup

#인기검색종목
url = 'https://finance.naver.com/'
res = requests.get(url)

soup = BeautifulSoup(res.text, 'lxml')

top5 = soup.find('div', attrs={'class':'aside_area aside_popular'})
trs = top5.find_all('a')
print(len(trs))

for tr in trs:
    print(tr.get_text())