from funtion import *
from jusoDB import *

while True:
    menuPrint('주소관리')
    menu = input('메뉴선택> ')

    if menu == '0':
        print('프로그램을 종료합니다.')
        break

    elif menu == '1':  #입력
        person = Person()
        person.name = input('이름> ')
        person.address = input('주소> ')

        insert(person)
        print('입력완료!')

    elif menu == '2':  #검색
        value = input('검색> ')
        rows = search(value)

        if len(rows) == 0:
            print('검색 결과가 없습니다.')

        else:
            for row in rows:
                person = Person()
                person.seq = row[0]
                person.name = row[1]
                person.address = row[2]
                person.print()

    elif menu == '3':  #목록
        #정렬방법: seq, name, address
        rows = list()
        for row in rows:
            person = Person()
            person.seq = row[0]
            person.name = row[1]
            person.address = row[2]
            person.print()

    elif menu == '4':  #삭제
        seq = inputNum('삭제번호> ')
        row = read(seq)
        
        if row == None:
            print('삭제할 번호가 존재하지 않습니다.')

        else:
            delete(seq)
            print('삭제완료!')

    elif menu == '5':  #수정
        person = Person()
        person.seq = inputNum('수정번호> ')
        row = read(person.seq)
        
        if row == None:
            print('수정할 번호가 존재하지 않습니다.')
        
        else:
            person.name = row[1]
            person.address = row[2]

            name = input(f'이름: {person.name}> ')
            if name != '': person.name = name

            address = input(f'주소: {person.address}> ')
            if address != '': person.address = address

            update(person)
            print('수정완료!')

    else:
        print('0~5번 숫자를 입력하세요!')