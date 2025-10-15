import requests
import os

def getData(query):
    url = f"https://dapi.kakao.com/v2/search/image?query={query}&size=20"
    headers={'Authorization': 'KakaoAK 314059ac0c339079dbba4a9b47f7bf23'}
    res = requests.get(url, headers=headers)
    
    data = res.json()['documents']
    return data

if __name__ == '__main__':
    query='제니'
    list = getData(query)

    for item in list:
        image_url = item['image_url']
        res=requests.get(image_url)

        if res.status_code == 200:
            print(image_url)
            index = image_url.rindex('/')
            file_name = image_url[index+1:]

            #파일 다운로드 
            with open(f'data/image/{file_name}.jpg', 'wb') as file:
                file.write(res.content)