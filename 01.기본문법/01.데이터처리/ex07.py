#나이, 성별 입력 받아 여탕에 들어갈 수 있을까요?
#조건: 남자이면서 4세미만 이거나 여자
print("여탕에 입장 가능?")

age = int(input("나이> "))
gen = input("성별> ")

result = (gen == "남" and age < 4) or gen == "여"
print(f'결과는 {result}입니다.')

#남탕
#조건: 여자이면서 3세미만 이거나 남자
print("-"*50)
print("남탕에 입장 가능?")

result = (gen == "여" and age < 3) or gen == "남"
print(f'결과는 {result}입니다.')