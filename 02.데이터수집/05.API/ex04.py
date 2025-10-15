import requests
import os

def getData(query):
    url = f"https://dapi.kakao.com/v2/local/search/keyword.json?query={query}"
    headers={'Authorization': 'KakaoAK 314059ac0c339079dbba4a9b47f7bf23'}
    res = requests.get(url, headers=headers)
    
    data = res.json()['documents']
    return data

if __name__ == '__main__':
    os.system('cls')

    while True:
        print()
        query = input('검색어> ')
        if query=='':break

        data = getData(query)
        if len(data)==0: print('검색결과가 없습니다.')

        for item in data:
            name = item['place_name']
            address = item['address_name']
            phone = item['phone']
            x = item['x']
            y = item['y']

            print(name, address, phone)