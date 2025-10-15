#list 타입 - 여러개의 데이터 저장
names = ['홍길동', '심청이', '강감찬']
print(names, type(names))

names.append('박명수')  #맨뒤에 추가됨
print(names)

names.pop()  #마지막거 빠짐 - stack구조
print(names)

#자리 지정해서 넣기
names.insert(1, '박명수')
names.append('박명수')
print(names)

print(names.count('박명수'))

print(names[0])  #처음
print(names[-1])  #끝
print(names[-2:])

print(names[1:3])