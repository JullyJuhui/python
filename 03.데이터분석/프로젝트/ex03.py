import os
import pandas as pd
from ex04 import submenu

file_name = 'data/학생정보.csv'

def inputNum(title):
    while True:
        num = input(title)

        if num == '':
            return ''
        
        elif not num.isnumeric():
            print('숫자로 입력하세요!')

        else:
            return int(num)

while True:
    info = pd.read_csv(file_name, index_col='지원번호')
    info.fillna('', inplace=True)  #null을 공백으로 채우기
    cols = list(info.columns)
    
    os.system('cls')
    print('-' * 53)
    print('******************** 학 생 정 보 ********************')
    print('-' * 53)
    print('1.등록|2.목록|3.검색|4.삭제|5.수정|6.성적관리|0.종료')
    print('-' * 53)

    menu = input('메뉴선택> ')
    if menu == '0':
        break

    elif menu == '6':
        submenu()

    elif menu == '1':  #등록
        new_no = info.index.max() + 1
        print(f'지원번호> {new_no}')
        name = input('이름> ')
        if name == '': continue

        school = input('학교> ')

        height = inputNum('키> ')
        if height=='': height=0

        sw = input('SW특기> ')

        info.loc[new_no] = [name, school, height, sw]
        sel = input('정말로 등록하시겠습니까?(Y)> ')
        if sel == 'Y' or sel=='y':
            info.to_csv(file_name) 

        input('아무키나 누르세요!')

    elif menu == '2':  #목록
        for idx in info.index:
            row = info.loc[idx]
            print(f'지원번호: {idx}', end=' ')
            for col in cols:
                print(f'{col}: {row[col]}', end=' ')
            print()
            print('-' * 65)

        input('아무키나 누르세요!')

    elif menu == '3':  #검색
        while True:
            sel = input('1:이름|2:학교|3:SW특기> ')
            if sel == '': break

            word = input('검색어> ')
            if sel == '1': filt = info['이름'].str.contains(word)
            elif sel == '2': filt = info['학교'].str.contains(word)
            elif sel == '3': 
                word = word.upper()
                filt = info['SW특기'].str.upper().str.contains(word)

            idxs = info[filt].index
            if len(idxs)==0: print('해당 데이터가 존재하지 않습니다.')
            else:
                for idx in idxs:
                    row = info.loc[idx]
                    print(f"지원번호: {idx}", end='  ')
                    for col in cols:
                        print(f"{col}: {row[col]}", end='  ')
                    print()
                    print('-' * 65)

        input('아무키나 누르세요!')  

    elif menu == '4':  #삭제
        no = inputNum('삭제 번호>')
        if no in info.index:
            row = info.loc[no]
            for col in cols:
                print(f'{col}: {row[col]}')

            sel = input('정말로 삭제하시겠습니까?(Y)')
            if sel == 'Y' or sel == 'y':
                info.drop(index=no, inplace=True)
                info.to_csv(file_name)
                print('삭제성공!')

        else:
            print('해당 지원번호가 존재하지 않습니다.')
        input('아무키나 누르세요!')

    elif menu == '5':  #수정
        no = inputNum('수정 번호> ')
        if no in info.index:
            row = info.loc[no]
            name = input(f'{cols[0]}:{row[cols[0]]}> ')  #이름
            if name == '': name = row['이름']

            school = input(f"학교: {row['학교']}> ")
            if school == '': school = row['학교']

            height = inputNum(f"키: {row['키']}> ")
            if height == '': height = row['키']

            sw = input(f"SW특기: {row['SW특기']}> ")
            if sw == '': sw = row['SW특기']

            sel = input('정말로 수정하시겠습니까?(Y)')

            if sel == 'Y' or sel=='y':
                info.loc[no] = [name, school, height, sw]
                info.to_csv(file_name)
                print('수정완료!')

        else:
            print('해당 지원번호가 존재하지 않습니다.')
        input('아무키나 누르세요!')

    else:
        input('0~6번을 누르세요!')