names= ['홍길동', '심청이', '강감찬', '이순신', '성춘향']

#1
no = 1
for name in names:
    print(f'{no}:{name}')
    no += 1

print('-'*20)

#2
for index, name in enumerate(names):  #enumerate함수: 리스트의 원소에 순서값을 부여해주는 함수
    print(f'{index+1}:{name}')

print('-'*20)

#3
for index in range(len(names)):
    print(f'{index+1}:{names[index]}')