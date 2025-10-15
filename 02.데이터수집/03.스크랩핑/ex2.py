import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')

#[top종목] - [거래상위]
tbody = soup.find('tbody', attrs={'id': '_topItems1'})
trs = tbody.find_all('tr')

list = []
for i, tr in enumerate(trs):
    name = tr.a.getText()
    tds = tr.find_all('td')
    price = tds[0].getText()
    up_down = tr['class']
    up_down_price = tds[1].getText().replace('하락','').replace('상승','').strip()
    up_down_percent = tds[2].getText().strip()
    #print(i+1, name, price, up_down[0], up_down_price, up_down_percent)
    list.append(f'{i+1}, {name}, {price}, {up_down[0]}, {up_down_price}')  #**?

print(list)

file_name = 'data/거래상위.txt'
with open(file_name, 'w', encoding='utf-8') as file: # w: 쓰기, a:추가, r:읽기
    for line in list:
        file.write(line + '\n')