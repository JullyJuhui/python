#딕셔너리 타입
students = {1:'홍길동', 2:'심청이', 3:'강감찬'}  #key:value
print(students, type(students))
print(students[2])  #[key]
print(students.get(2))  #.get(key)

students[4] = '박명수'  #없으면 추가/ 있으면 수정이 됨
print(students, type(students))

print('심청이' in students)  #심청이가 students 변수(키)에 있나? - T/F
print(4 in students)

keys = students.keys()
print(keys, type(keys))  #list가 아닌 dict_keys

values = students.values()
print(values, type(values))  #dict_values

print('박명수' in values)  #true


#CURD: 데이터 작업
#create
#update
#read
#delete