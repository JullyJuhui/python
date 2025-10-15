import os
from product_db import *
from function import *
from sub import *

while True:
    os.system('cls')
    print()
    print('-----------------------------------')
    print('              상품관리             ')
    print('-----------------------------------')
    print('[1] 상품등록')
    print('[2] 상품검색')
    print('[3] 상품목록')
    print('[4] 상품수정')
    print('[5] 매출관리')
    print('[0] 프로그램종료')
    print('-----------------------------------')

    menu = input('메뉴선택> ')

    if menu == '0':
        cur.close()
        con.close()

        print('프로그램을 종료합니다.')
        break

    elif menu == '1':  #상품등록
        pro = Product()
        pro.code = inputCode('상품코드> ')
        if pro.code == '': continue

        prod = read(pro.code)
        if prod:
            prod.print()
            print('이미 등록된 상품입니다.')

        else:
            pro.name = input('상품이름> ')
            pro.price = inputPrice('상품가격> ')
            insert(pro)

        input('아무키나 누르세요!')

    elif menu == '2':  #상품검색 -> 가격 검색 기능 추가(범위 받아서)
        while True:
            key = inputNum('1.검색|2.가격대> ')
            if key == '': break

            if key == 1:  #1. 검색
                value = input('검색어> ')
                if value == '': break

                products = search(value)
                if len(products) == 0:
                    print('검색 결과가 존재하지 않습니다.')

                else:
                    for product in products:
                        product.print()

            elif key == 2:
                min_price = inputNum('최소가격> ')
                max_price = inputNum('최대가격> ')

                if min_price == '':
                    min_price = 0

                elif max_price == '':
                    max_price = 0

                if min_price > max_price:
                    print('최대가격은 최소가격보다 높아야합니다.')
                    continue

                products = searchPrice(min_price, max_price)
                if len(products) == 0:
                    print('검색 결과가 존재하지 않습니다.')

                else:
                    for product in products:
                        product.print()

        input('아무키나 누르세요!')

    elif menu == '3':  #상품목록 -> 정렬기능 추가
        products = list()

        for product in products:
            product.print()

        input('아무키나 누르세요!')

    elif menu == '4':  #상품수정
        code = inputCode('상품코드> ')
        if code == '': continue

        pro = read(code)
        if pro == None:
            print('등록되지 않은 상품입니다.')

        else:
            name = input(f'상품이름: {pro.name}> ')
            if name != '': pro.name = name

            price = inputPrice(f'상품가격: {pro.price:,}원> ')
            if price != 0: pro.price = price

            pro.print()

            sel = input('수정하실래요(Y)> ')
            if sel == 'Y' or sel == 'y':
                update(pro)
            else:
                print('수정이 취소되었습니다!')
        
        input('아무키나 누르세요!')

    elif menu == '5':  #매출관리
        saleMenu()

    else:  #프로그램종료
        print('[0]~[5]번 메뉴를 선택하세요.')
        input('아무키나 누르세요!')