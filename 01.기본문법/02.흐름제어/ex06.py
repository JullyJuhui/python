names = []
no = int(input('학생수> '))

for i in range(no):
    name = input('이름> ')
    names.append(name)

for index in range(len(names)):
    print(index+1, names[index], end = " ")

print('\n', '-'*30)

for index, name in enumerate(names):
    print(index+1, name, end = " ")