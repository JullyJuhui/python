#도서검색
import requests
import json
import os

def getBooks(url, query, page, size):
    try:
        #"Authorization: KakaoAK ${REST_API_KEY}"
        headers={'Authorization': 'KakaoAK 314059ac0c339079dbba4a9b47f7bf23'}
        url = f'{url}?query={query}&page={page}&size={size}'
        res = requests.request(method='get', url=url, headers=headers)  #method: get/ post
        data = res.json()
        documents = data['documents']

        if len(documents) == 0:
            print('검색 도서가 없습니다.')
            
        for doc in documents:
            title = doc['title']
            price = doc['sale_price']
            authors = doc['authors']  #배열
            publisher = doc['publisher']

            print(title, price, ', '.join(authors), publisher)

    except Exception as err:
        print('접속오류:', err)

if __name__ == '__main__':
    url = 'https://dapi.kakao.com/v3/search/book'
    query = '파이썬'
    page = 1
    size = 10

    while True:
        os.system('cls')
        query = input('검색> ')
        if query == '': break

        getBooks(url, query, page, size)
        input('아무 버튼이나 누르세요')