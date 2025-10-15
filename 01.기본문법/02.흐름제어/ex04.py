# sum = 0
# for i in range(1, 101):
#     sum += i

# print(sum)

# for i in range(1, 101):
#     print(i, end=' ')

#2~100 짝수합계
tot1 = 0
for i in range(2, 101, 2):
    tot1 += i
print(tot1)

#1~99 홀수합계
tot2 = 0
for i in range(1, 100, 2):
    tot2 += i
print(tot2)