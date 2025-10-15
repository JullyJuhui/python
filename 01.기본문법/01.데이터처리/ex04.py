num1 = int(input('숫자1> '))
num2 = int(input('숫자2> '))  #숫자를 입력했지만 str

#입력 받은 num변수 값을 정수로 변환
# num1 = int(num1)
# num2 = int(num2)

add = num1 + num2

#산술연산자
print(f'{num1} + {num2} = {add}') #합
print(f'{num1} - {num2} = {num1 - num2}') #차
print(f'{num1} * {num2} = {num1 * num2}') #곱

#소수점 2자리까지 출력) :.2f
print(f'{num1} / {num2} = {num1 / num2:.2f}') #나누기

print(f'{num1} % {num2} = {num1 % num2}') #나머지
print(f'{num1} // {num2} = {num1 // num2}') #몫