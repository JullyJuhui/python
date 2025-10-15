from flask import Flask, render_template, request, send_file
from io import BytesIO
import pandas as pd
import FinanceDataReader as fdr
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import re

app = Flask(__name__, template_folder='temp', static_folder='static')

@app.route('/data')
def data():
    code = request.args['code']
    start = request.args['start']
    end = request.args['end']
    df = fdr.DataReader(code, start, end)
    df = df.head()
    table = df.to_html(classes='table table-striped table-hover')

    return table

def get_kinfo():
    url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%98%A4%EB%8A%98+%EC%A3%BC%EC%8B%9D&ackey=q0cawb0j'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')

    rows = soup.find_all('span', attrs={'class':re.compile('spt_con')})

    prices=[]
    for price in rows:    
        prices.append(price.find('strong').getText())

    img1 = 'https://ssl.pstatic.net/imgfinance/chart/mobile/mini/' + 'KOSPI_end_up.png'
    img2 = 'https://ssl.pstatic.net/imgfinance/chart/mobile/mini/' + 'KOSDAQ_end_up.png'

    rows = soup.find_all('span', attrs={'class':'n_ch'})

    return prices, [img1, img2], rows

def updown(n_list):
    if "+" in n_list[1]:
        n_list[0] = "▲ " + n_list[0]

    elif "-" in n_list[1]:
        n_list[0] = "▼ " + n_list[0]

#코스피 정보 전달
@app.route('/kinfo1')
def info1():
    prices, imges, rows = get_kinfo()
    rates = rows[0].find_all('em')
    kospi = [rates[0].getText(), rates[1].getText()]
    updown(kospi)

    data = {'title':'KOSPI', 'graph':imges[0], 'price':prices[0], 'num':kospi}

    return data

#코스닥 정보 전달
@app.route('/kinfo2')
def info2():
    prices, imges, rows = get_kinfo()
    rates = rows[1].find_all('em')
    kosdaq = [rates[0].getText(), rates[1].getText()]
    updown(kosdaq)

    data = {'title':'KOSDAQ', 'graph':imges[1], 'price':prices[1], 'num':kosdaq}

    return data

def get_ninfo():
    url = 'https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bjA3&pkid=194&qvt=0&query=%EB%82%98%EC%8A%A4%EB%8B%A5%20%EC%A2%85%ED%95%A9'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')

    price = soup.find('span', attrs={'class':re.compile('spt_con')}).find('strong').getText()

    return price

#코스닥 정보 전달
@app.route('/ninfo')
def ninfo():
    price = get_ninfo()
    data = {'title':'NASDAQ', 'price':price}

    return data

@app.route('/img1')
def img1():
    code = request.args['code']
    start = request.args['start']
    end = request.args['end']
    df = fdr.DataReader(code, start, end)

    df['year'] = df.index.year
    df['month'] = df.index.month

    group = df.groupby(['year', 'month'])[['Close', 'Volume']].mean()
    group.reset_index(inplace=True)

    plt.figure(figsize=(10,4))
    plt.plot(group.index, group['Close'], marker='s', color='deeppink')

    xticks = [x for x in group.index]
    plt.xticks(xticks, [f"{group.loc[idx, 'year']}-{group.loc[idx, 'month']}" for idx in xticks], rotation=45)

    img = BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    return send_file(img, mimetype='img1/png')

@app.route('/img2')
def img2():
    code = request.args['code']
    start = request.args['start']
    end = request.args['end']
    df = fdr.DataReader(code, start, end)

    df['year'] = df.index.year
    df['month'] = df.index.month

    group = df.groupby(['year', 'month'])[['Close', 'Volume']].mean()
    group.reset_index(inplace=True)

    plt.figure(figsize=(10,4))
    plt.bar(group.index, group['Volume'], color='orange')

    xticks = [x for x in group.index]
    plt.xticks(xticks, [f"{group.loc[idx, 'year']}-{group.loc[idx, 'month']}" for idx in xticks], rotation=45)

    img = BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    return send_file(img, mimetype='img2/png')

#홈 페이지 출력
@app.route('/')
def index():
    return render_template('index.html', pageName='home.html', title='주가예측')

#국내주식 페이지 출력
@app.route('/ko')
def ko():
    return render_template('index.html', pageName='ko_stock.html', 
                           title='국내 랭킹')

#미국주식 페이지 출력 예정***
@app.route('/kospi')
def usa():
    return render_template('index.html', pageName='kospi.html', 
                           title='KOSPI 코스피')

if __name__=='__main__':
    app.run(port=5000, debug=True)