from function import *
from haksaDB import *

while True:
    menuPrint('학생관리')
    menu = input('메뉴선택> ')

    if menu == '0':
        print('프로그램을 종료합니다.')
        break

    elif menu == '1':  #입력
        stu = Student()

        stu.id = newID()
        print(f'학번> {stu.id}')

        stu.name = input('이름> ')
        if stu.name == '': continue
        
        stu.dept = inputDept('학과> ', 1)

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
        students = list()

        if students:
            for stu in students:
                stu.print()

    elif menu == '4':  #삭제
        pass

    elif menu == '5':  #수정
        pass

    else:
        print('0~5 숫자를 입력해주세요!')