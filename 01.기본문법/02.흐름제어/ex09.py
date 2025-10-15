jusos = [ #번호, 이름, 주소
    {'no':1, 'name':'홍길동', 'juso':'서울 강서구'},
    {'no':2, 'name':'강감찬', 'juso':'인천 서구'}
]

while True:
    print('\n')
    print('\t  ', '[주소관리프로그램]')
    print('-' * 40)
    print('|1.입력|2.검색|3.수정|4.삭제|0.종료|')
    print('-' * 40)
    
    menu = input('메뉴선택> ')

    if menu == '0':  #종료
        print('프로그램을 종료합니다.')
        break

    # elif menu == '1':  #입력
    #     pass  #continue도 가능

    elif menu == '1':  #입력
        no = input('번호> ')
        name = input('이름> ')
        juso = input('주소> ')

        jusos.append({'no':no, 'name':name, 'juso':juso})
        print('등록완료!')

    elif menu == '2':  #검색
        for j in jusos:
            print(j.get('no'), j.get('name'), j['juso'])
        print('*' * 40)
        print(len(jusos),'명이 존재합니다.')

    elif menu == '3':  #수정
        no = input('번호> ')
        name = input('이름> ')
        juso1 = input('주소> ')

        for juso in jusos:
            if juso['no'] == int(no):
                juso['name'] = name
                juso['juso'] = juso1
                print('수정완료!')

            else:
                print('존재하지 않는 번호입니다.')

    elif menu == '4':  #삭제
        no = input('번호> ')
        i = 0
        for juso in jusos:
            if juso['no'] == int(no):
                jusos.pop(i)
                print('삭제완료!')
            
            else:
                print('삭제할 번호가 없습니다.')
            i += 1

    else:  #예외
        print('0-4를 입력해주세요.')
        


