#for문
for i in range(11):
    if i < 10:    
        print(i, end=', ')  #end는 라인 스킵 안됌**

    else:
        print(i)

for i in range(2, 11, 2):
    if i < 10:    
        print(i, end=', ')

    else:
        print(i)

for i in range(1, 10, 2):
    if i < 9:    
        print(i, end=', ')

    else:
        print(i)

names = ['apple', 'banana']
for name in names:
    print(name)