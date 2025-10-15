from function import *
from db import *
import os
from dept import *

while True:
    os.system('cls')
    menuPrint('학사관리')
    menu = input('메뉴선택> ')

    if menu == '0':  #종료
        cur.close()
        con.close()

        print('프로그램을 종료합니다.')
        break

    elif menu == '6':
        menuDept()

    elif menu == '1':  #입력
        stu = Student()
        stu.id = newID()
        print(f'학생학번> {stu.id}')

        stu.name = input('학생이름> ')
        if stu.name == '': 
            print('학생이름은 반드시 입력하세요.')    
            continue

        stu.code = inputCode('학생학과> ', menu)

        insert(stu)

    elif menu == '2':  #검색
        while True:
            value = input('검색> ')
            if value == '': break

            students = search(value)
            if len(students) == 0:
                print('검색 결과가 없습니다.')

            else:
                for stu in students:
                    stu.print()

    elif menu == '3':  #목록
        keys = ['id', 'name', 'dname']
        while True:
            key = inputNum('1.학번순|2.이름순|3.학과순> ')
            if key == '': break
            elif key < 1 or key > 3:
                print('1~3 숫자를 입력하세요!')
                continue

            students = list(keys[key-1])

            for stu in students:
                stu.print()

    elif menu == '4':  #삭제
        id = input('학번> ')
        if id == '': continue
        
        stu = read(id)
        if stu == None:
            print('삭제할 학생이 없습니다.')

        else:
            stu.print()
            sel = input('삭제하시겠습니까?(Y)> ')
            if sel == 'y' or sel == 'Y':
                delete(id)
        
        input('아무키나 누르세요!')

    elif menu == '5':  #수정
        id = input('학번> ')
        if id == '': continue
        
        stu = read(id)
        if stu == None:
            print('수정할 학생이 없습니다.')

        else:
            stu.print()
            name = input(f'학생이름: {stu.name}> ')
            if name != '': stu.name = name

            code = inputCode(f'학과코드: {stu.code}> ', menu)
            if code != '': stu.code = code

            update(stu)
        input('아무키나 누르세요!')

    else:
        print('0~5 숫자를 입력해주세요!')