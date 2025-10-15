import requests
from bs4 import BeautifulSoup
import time

def create_soup(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')

    return soup

def weather(query):
    url = f'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query={query}&ackey=gx5an56h'
    soup = create_soup(url)

    # loc = soup.find('h2', attrs={'class':'title'}).getText()
    temp = soup.find('div', attrs={'class':'temperature_text'})

    if temp:
        temp = temp.getText()
    else:
        temp = ''

    return temp

def exchange():
    url = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query=%ED%99%98%EC%9C%A8&oquery=exchage&tqi=jMxXwsqo1fsssMGmOhVsssssteK-062121&ackey=ki1aqwuh'
    soup = create_soup(url)
    rate = soup.find('span', attrs={'class': 'spt_con dw'}).find('strong')

    if rate:
        rate = rate.getText()
    else:
        rate = ''
    return rate

def stock(query):
    url = f'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query={query}&ackey=4gjooy4x'
    soup = create_soup(url)
    price = soup.find('div', attrs={'class': 'spt_con dw'}).find('strong')

    if price:
        price = price.getText()
    else:
        price = ''
    return price

if __name__=='__main__':
    print(weather('부산 날씨'))


