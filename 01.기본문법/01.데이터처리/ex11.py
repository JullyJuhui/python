#문자열 함수
str = 'python is amazing'
print(1, str.lower())  #모두 소문자
print(2, str.upper())  #모두 대문자
print(3, str.capitalize())  #맨앞만 대문자
print(4, str[0].islower())  #소문자인지 아닌지
print(5, len(str))  #문자열의 길이
print(6, str.replace('python', '파이썬'))  #대체

index = str.index('a')
print(7, index)
print("***", str.index('a', index + 1))
print(str[index:])
print(str[index:].upper())

print(8, str.find('a')) #인덱스값 출력
print(8, str.find('ab'))  #오류 대신 -1 return 
#=> index 대신 find가 낫다 왜? 오류가 안나니까!

print(9, str.count('i'))