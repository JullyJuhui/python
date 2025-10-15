#숫자 체크 함수
#숫자면 true, 아니면 false

def isNumber(str): #숫자 체크함수
    if str.isnumeric():
        return True
    
    else:
        print('숫자를 입력하세요!')
        return False

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

while True:
    score = input('점수> ')

    if score == '':
        break

    if isNumber(score):
        level = grade(int(score))
        print(f'평점:{level}')

