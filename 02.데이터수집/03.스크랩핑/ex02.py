import requests
from bs4 import BeautifulSoup

#[네이버] - [네이버 증권] - [Top 종목] - [거래상위]
url = 'https://finance.naver.com/'
res = requests.get(url)

soup = BeautifulSoup(res.text, 'lxml')

items = soup.find('tbody', attrs={'id':'nxt_topItems1'})

rank1 = items.find('tr')
#print(1, rank1.a.get_text())

rank2 = rank1.find_next_sibling('tr')
#print(2, rank2.a.get_text())

rank2 = rank2.find_previous_sibling('tr')
#print(1, rank2.a.get_text())

siblings = rank1.find_next_siblings('tr')
#print(3, len(siblings))

rank2 = siblings[1]
#print(4, rank2.a.get_text())

#부모: items
ranks = items.find_all('tr')  #여러개 찾을때 find_all

for index, rank in enumerate(ranks):
    td = rank.find_all('td')  
    price = td[0].get_text()  #0번째 td: 가격
    up_down = td[2].get_text().strip()  #.strip(): 앞뒤 공백 제거
    print(index+1, rank.a.get_text(), price, up_down)  

# rank = items.find('tr')
# for i in range(len(siblings)):
#     print(i+1, rank.a.get_text())
#     rank = rank.find_next_sibling('tr')

#크롤링은 동적이다~~