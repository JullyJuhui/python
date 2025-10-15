import requests
from bs4 import BeautifulSoup
import re
from flask import Blueprint, render_template, request
import FinanceDataReader as fdr

bp = Blueprint('today', __name__, url_prefix='/today')

@bp.route('/kospi')
def td_kospi():
    df_stock = fdr.StockListing('KRX')  #한국증시 #뉴욕증시:NYSE
    filt1 = df_stock['Market']=='KOSPI'
    df_stock = df_stock[filt1]
    df = df_stock[['Code', 'Name', 'Close', 'Changes', 'ChagesRatio', 'High', 'Low', 'Volume', 'Marcap']]
    df.columns = ['종목코드', '종목명', '종가', '등락폭', '등락률', '고가', '저가', '거래량', '시가총액']
    df['등락률'] = [f'{n}%' for n in df['등락률']]

    table = df.to_html(classes='table table-striped table-hover')

    return table

@bp.route('/kosdaq')
def td_kosdaq():
    df_stock = fdr.StockListing('KRX')  #한국증시 #뉴욕증시:NYSE
    filt1 = df_stock['Market']=='KOSDAQ'
    df_stock = df_stock[filt1]
    df = df_stock[['Code', 'Name', 'Close', 'Changes', 'ChagesRatio', 'High', 'Low', 'Volume', 'Marcap']]
    df.columns = ['종목코드', '종목명', '종가', '등락폭', '등락률', '고가', '저가', '거래량', '시가총액']
    df['등락률'] = [f'{n}%' for n in df['등락률']]

    table = df.to_html(classes='table table-striped table-hover')

    return table
