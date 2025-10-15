#할리스 서울 매장정보
import json
import requests

def getAddress():
    with open('data/hollys.json', 'r', encoding='utf-8') as file:
        infos = json.load(file)

        list=[]
        for info in infos:
            name = info['name']
            address = info['address']
            phone = info['phone']

            data = {'name':name, 'address':address, 'phone': phone}
            list.append(data)
        
        return list

#위도, 경도값 받기
def getXY(query):
    # query = '서울특별시 영등포구 여의나루로 60 포스트타워 여의도 1층'
    url = f"https://dapi.kakao.com/v2/local/search/address.json?query={query}"
    headers={'Authorization': 'KakaoAK 314059ac0c339079dbba4a9b47f7bf23'}
    res = requests.request(method="get", url=url, headers=headers)
    data = res.json()
    documents = data['documents']
    x = documents[0]['x']
    y = documents[0]['y']
    return x, y

def getAddress2(address):
        address = address.split(' ')[:4]
        address = ' '.join(address)
        return address

if __name__=="__main__":
    infos = getAddress()
    list_json = []

    for info in infos:
        name = info['name']
        phone = info['phone']
        address = info['address']
        address = address.split(' ')[:4]
        address = ' '.join(address)
        xy = getXY(address)
        x = xy[0]
        y = xy[1]
        #print(address, x, y, name, phone)
        data={'name':name, 'phone':phone, 'address':address, 'x':x, 'y':y}
        list_json.append(data)

with open('data/hollys_location.json', 'w', encoding='utf-8') as file:
    json.dump(list_json, file, indent='\t', ensure_ascii=False)