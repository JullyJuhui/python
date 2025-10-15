from function import menuPrint, inputNum  #숫자일때까지 계속 받아서 리턴하는거

sale = [
    {'code':1, 'name':'냉장고', 'price': 250, 'qnt': 5},
    {'code':2, 'name':'세탁기', 'price': 150, 'qnt': 3}
]

#검색함수
def search(code):
    isFind = False

    for index, s in enumerate(sale):  
        if s['code'] == code:
            isFind = True

            sum = s['price']*s['qnt']
            print(s['code'], s['name'], s['price'], s['qnt'], sum)

            return index

    if isFind == False:
        print('상품이 존재하지 않습니다.')
        return False

def list():
    for index, s in enumerate(sale):  
        sum = s['price']*s['qnt']
        print(index, s['code'], s['name'], s['price'], s['qnt'], sum)

    if len(sale) == 0:
        print('상품이 존재하지 않습니다.')
    else:
        print(f'{len(sale)}개의 상품이 존재합니다.')

#삭제함수
def delete(code):
    index = search(code)
    sale.pop(index)
    print('삭제성공!')
    
def insert():
    #***
    codes = []
    for s in sale:
        codes.append(s.get('code'))

    code = max(codes) + 1
    print(f'상품코드> {code}')
    name = input('상품이름>')
    price = inputNum('상품가격')
    qnt = inputNum('판매수량')

    sale.append({'code':code, 'name':name, 'price':price, 'qnt':qnt})
    print("등록성공!")

while True:
    menuPrint('매출관리')
    menu = input('메뉴선택> ')

    #|1.입력|2.검색|3.목록|4.삭제|5.수정|0.종료|

    if menu == '0':  #종료
        print('프로그램종료합니다.')
        break

    elif menu == '1':  #등록
        insert()

    elif menu == '2':  #검색
        code = inputNum('검색코드')
        search(code)

    elif menu == '3':
        #search(0)
        list()

    elif menu == '4':
        code = inputNum('삭제코드')
        delete(code)

    elif menu == '5':
        pass