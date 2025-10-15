#데이터 상수: 정수, 실수, 문자열, 불린
#변수(값을 저장하는 저장소)
#연산자(산술연산자: +,-,*,/,%,//  관계연산자: >,>=,<,<=,==,!=  논리연산자: and, or)

#list
names = ['홍길동', '심청이', '강감찬']
#1 검색
print(1, names[2]) #강감찬

#2 입력
names. append('성춘향')
print(2, names)

names.insert(1, '유재석')
print(2, names)

#3 수정
names[1] = '강호동'
print(3, names)

#4 삭제
names.pop()
print(4, names)

names.pop(1)  #pop에 index지정 -> 지정해서 삭제
print(4, names)

#5 길이, 개수
print(5, len(names))
print(5, names.count(''))

#type
print(6, type(names))  #list