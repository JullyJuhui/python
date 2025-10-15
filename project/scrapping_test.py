import requests
from bs4 import BeautifulSoup
import re

url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%98%A4%EB%8A%98+%EC%A3%BC%EC%8B%9D&ackey=q0cawb0j'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')

rows = soup.find_all('span', attrs={'class':'n_ch'})

rates = rows[0].find_all('em')
kospi = [rates[0].getText(), rates[1].getText()]

rates = rows[1].find_all('em')
kosdaq = [rates[0].getText(), rates[1].getText()]

def updown(n_list):
    if "+" in n_list[1]:
        n_list[0] = "▲ " + n_list[0]

    elif "-" in n_list[1]:
        n_list[0] = "▼ " + n_list[0]

updown(kospi)
updown(kosdaq)
print(kospi, kosdaq)

