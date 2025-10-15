#변수는 메모리에 있어 소실된다. db와 서버?에 저장하는거 배움
address = [
    {'no':1, 'name':'이순신', 'address':'인천 서구 경도동'},
    {'no':2, 'name':'심청이', 'address':'경기도 광명시 철산동'}
]

while True:
    print('\n**************주소관리 프로그램**************')
    print('-'*45)
    print('|1.입력|2.목록|3.검색|4.삭제|5.수정|0.종료|')
    print('-'*45)

    menu = input('메뉴선택> ')

    if menu == '0':
        print('프로그램을 종료합니다.')
        break

    elif menu == '1':  #입력
        no = []
        for adr in address:
            no.append(adr['no'])

        new_no = max(no) + 1

        print(f'번호> {new_no}')
        name = input('이름> ')
        adr = input('주소> ')

        address.append({'no':new_no, 'name':name, 'address':adr})
        print('새로운 주소가 등록되었습니다.')

    elif menu == '2':  #목록
        for adr in address:
            print(adr['no'], adr['name'], adr['address'])

    elif menu == '3':  #검색
        name = input('검색할 이름> ')

        # for adr in address:
        #     if adr['name'] == name:
        #         print(adr['no'], adr['name'], adr['address'])

        # <부분일치 검색>
        # 시작이름으로 검색
        # for adr in address:
        #     if adr['name'].startswith(name):
        #         print(adr['no'], adr['name'], adr['address'])

        #이름의 끝나는 글자로 검색
        # for adr in address:
        #     if adr['name'].endswith(name):
        #         print(adr['no'], adr['name'], adr['address'])

        #포함하는 것 검색
        for adr in address:
            if adr['name'].find(name) != -1:
                print(adr['no'], adr['name'], adr['address'])
        

    elif menu == '4':  #삭제
        no = input('삭제할 번호> ')

        if no == '':
            continue

        for index, adr in enumerate(address):
            if adr['no'] == int(no):
                address.pop(index)
                print(no, '번이 삭제되었습니다.')

    elif menu == '5':  #수정
        no = input('수정할 번호> ')

        if no == '':
            continue

        for adr in address:
            if adr['no'] == int(no):  #수정번호를 찾은 경우
                name = input(f'이름: {adr["name"]} -> ')
                adr1 = input(f'주소: {adr["address"]} -> ')

                if name != '':  #값을 입력: 수정을 하는 경우
                    adr['name'] = name
                
                if adr != '':  #값을 입력: 수정을 하는 경우
                    adr['address'] = adr1

    else:  #종료
        print('0~5번을 다시 입력해주세요.')

