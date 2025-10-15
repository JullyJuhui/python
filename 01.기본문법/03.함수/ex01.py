#함수
#성적 입력시 학점구하는 함수

def grade(score):  #학점
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
    score = input('점수(종료0)> ')
    if score == '0':
        print('프로그램을 종료합니다.')
        break

    elif not score.isnumeric():
        print('숫자를 입력해주세요!')

    else:
        grade1 = grade(int(score))
        print(f"점수: {score}, 학점: {grade1}")