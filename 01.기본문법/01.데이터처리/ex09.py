#기본함수 (숫자)
print(1, abs(-5))  #절대값
print(2, pow(4, 3)) #4의 3승
print(3, max(5, 2, 10, 1, 17, 8)) #최대값
print(4, min(5, 2, 10, 1, 17, 8)) #최솟값
print(5, round(3.14)) #반올림 - 3
print(6, round(3.141592, 3)) #반올림해서 3째자리까지 출력

#올림, 버림은 기본함수가 아님 -> 모듈 불러오기~~~
from math import*

print(7, floor(4.99))  #버림 -> 소수점 지정 불가! = 매개변수 1개
print(8, ceil(3.14))  #올림
print(9, sqrt(36))

#random
from random import*
print(10, random())  #0이상 1미만
print(10, random() * 10)  #0이상 10미만
print(10, int(random() * 10))  #0 ~ 9

print(11, randint(1, 45)) #1 ~ 45