from function import inputNum, grade

kor = inputNum('국어')
eng = inputNum('영어')
mat = inputNum('수학')

avg = (int(kor) + int(eng) + int(mat))/3
print(f'평균: {avg:.2f}, 평점: {grade(avg)}')