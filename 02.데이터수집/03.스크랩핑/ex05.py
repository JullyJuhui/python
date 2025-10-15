import requests
from bs4 import BeautifulSoup
import csv

file_name = 'data/할리스매장.csv'
file = open(file_name, 'w', encoding='utf-8-sig', newline='')
writer = csv.writer(file)

title=['No', '지역명', '매장명', '주소', '전화']
writer.writerow(title)

#[할리스] - [store] -[매장검색]
for page in range(1, 11):
    url = f'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={page}&sido=%EC%84%9C%EC%9A%B8&gugun=&store='
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')

    table = soup.find('table', attrs={'class':'tb_store'})
    rows = table.find_all('tr')
    
    for idx, row in enumerate(rows):
        if idx == 0: continue        
        cols = row.find_all('td')
        city = cols[0].getText().strip()  #.strip(): 앞,뒤 공백 제거
        name = cols[1].getText().strip()
        address = cols[3].getText().replace(',', ' ').replace('.', '').strip()
        phone = cols[5].getText().replace('.', '').strip()
        
        data = [(page-1)*10+idx, city, name, address, phone]
        writer.writerow(data)