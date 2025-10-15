#다중제어
# for i in range(5):  #0~4  행
#     for j in range(5):  #0~4  열
#         print(f'({i},{j})', end='')

#     print()

for i in range(5):  #0~4  행
    for j in range(i+1):  #0~4  열
        print('*', end='')
    print()

#***
for i in range(5, 0, -1):  #0~4  행
    for j in range(i):  #0~4  열
        print('*', end='')
    print()