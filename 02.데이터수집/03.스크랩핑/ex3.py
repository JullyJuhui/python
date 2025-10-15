import requests
from bs4 import BeautifulSoup
import re
import csv  #comma seperated values

file_name = 'data/코스닥거래상위1~100.csv'
file = open(file_name, 'w', encoding='utf-8-sig', newline = '')
writer = csv.writer(file)

#[top종목] - [거래상위] - [더보기] - [코스닥]
url = 'https://finance.naver.com/sise/sise_quant.naver?sosok=1'
res = requests.get(url)

soup = BeautifulSoup(res.text, 'lxml')

table = soup.find('table', attrs={'class':'type_2'})
rows = table.find_all('tr')

# data=[]
for row in rows:
    cols = row.find_all('td')
    if len(cols) <= 1: continue
    
    data = [re.sub('\t|\n|하락|상승|보합', '', col.getText()) for col in cols]  #re.sub(a, b, c): c내용중에서 a를 b로 바꿔라
    # for col in cols:
    #     data.append(col.getText())
    
    writer.writerow(data)