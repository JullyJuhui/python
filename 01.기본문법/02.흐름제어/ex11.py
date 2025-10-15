product = [
    {'code':1, 'name':'엘지 냉장고', 'price':2500000},  #단위: 원
    {'code':2, 'name':'삼성 세탁기', 'price':1800000},
    {'code':3, 'name':'삼성 냉장고', 'price':2100000},
    {'code':4, 'name':'엘지 전자동 세탁기', 'price':2000000}
]

while True:
    print('\n**************상품관리 프로그램**************')
    print('-'*45)
    print('|1.입력|2.목록|3.검색|4.삭제|5.수정|0.종료|')
    print('-'*45)

    menu = input('메뉴선택> ')

    if menu == '0':  #종료
        print('프로그램을 종료합니다.')
        break

    elif menu == '1':  #입력
        codes = []
        for p in product:
            codes.append(p['code'])
        new_code = max(codes) + 1

        print(f'상품코드> {new_code}')
        new_name = input('상품명> ')
        new_price = int(input('상품가격> '))  #숫자로 받아야함

        product.append({'code':new_code, 'name':new_name, 'price':new_price})

        print('새로운 상품이 등록되었습니다.')

    elif menu == '2':  #목록
        for p in product:
            #왼쪽정렬) :<n    천단위) :,
            print(f'{p["code"]:<5}', end='\t')
            print(f'{p["name"]:<15}', end='\t')
            print(f'{p["price"]:>10,}원')  

    elif menu == '3':  #검색***
        search_name = input('상품명> ')
        for p in product:
            if p['name'].find(search_name) == -1:
                #print(f'{search_name} 상품이 없습니다.')
                pass

            else:
                print(f'{p["code"]:<5}', end='\t')
                print(f'{p["name"]:<15}', end='\t')
                print(f'{p["price"]:>10,}원') 


    elif menu == '4':  #삭제
        del_code = input('삭제할 코드> ')
        hi = 0

        if not del_code.isnumeric():
            print('삭제할 코드는 숫자여야합니다.')
            continue

        for index, p in enumerate(product):
            if p['code'] == int(del_code):
                product.pop(index)
                hi = 1

                print(f'{p["name"]} 상품이 삭제되었습니다.')

        if hi == 0:
            print('등록되지 않은 코드입니다.')

    elif menu == '5':  #수정
        edit_code = input('수정할 코드> ')

        for p in product:
            if p['code'] == int(edit_code):
                #상품명 수정
                new_name = input(f'상품명:{p["name"]}>')
                if new_name != "":
                    p['name'] = new_name

                #상품가격 수정
                new_price = input(f'상품가격:{p["price"]:,}>')
                if new_price != "":
                    p['price'] = int(new_price)  #출력시 포멧을 위해 정수로***

    else:
        print('0~5번을 다시 입력해주세요.')