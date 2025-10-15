#숫자 체크 함수
def isNumber(str): 
    if str.isnumeric():
        return True
    
    else:
        print('숫자를 입력하세요!')
        return False

#학점 계산 함수
def grade(score):  #학점 계산함수
    if score >= 90:
        grade = 'A'
    
    elif score >= 80:
        grade = 'B'
    
    elif score >= 70:
        grade = 'C'
    
    elif score >= 60:
        grade = 'D'
    
    else:
        grade = 'F'

    return grade

#과목 입력 함수
def inputNum(title):
    while True:
        str = input(f'{title}> ')

        if str.isnumeric():
            return int(str)
            break

        elif str == '':
            return 0

        else:
            print(f'{title}을(를) 숫자로 입력하세요!')

#메뉴 출력 함수
def menuPrint(title):
    print(f'\n*****************{title}*****************')
    print('------------------------------------------')
    print('|1.입력|2.검색|3.목록|4.삭제|5.수정|0.종료|')
    print('------------------------------------------')