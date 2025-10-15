#입력받기 input
name = input("이름> ")
age = input("나이> ")

#출력: ,
print('이름은', name, '입니다.')

# 출력: 연결자 +
print('이름은 ' + name + '입니다.')
print(age, type(age))  #age 타입: str

#출력: 포멧
print(f'이름: {name}, 나이: {age}')