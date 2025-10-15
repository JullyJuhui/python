#딕셔너리: dict
students = {1:'홍길동', 2:'강감찬', 3:'이순신'}
print(type(students))

#cls 커멘드창 클리어

#검색
print(1, students.get(2)) #강감찬
print(2, students.get(4)) #None
print(3, students[2]) #강감찬

#입력
students[5] = '유재석'
print(4, students)

#수정
students[1]='김길동'
print(5, students)

#삭제
students.pop(2)
print(6, students)

#전부삭제
students.clear()
print(6, students)