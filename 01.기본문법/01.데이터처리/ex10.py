#문자열 슬라이싱

jumin = "990120-2155011"

#남자? 남자-3,1 여자-4,2
gender = jumin[7]
result = jumin[7] == '3' or jumin[7] == '1'

print(f'{gender}의 결과는 {result} (false: 여, true:남)')

#년도
yy = jumin[:2]  #인덱스 0부터 2전까지 (0 ~ 1)
print(yy)

mm = jumin[2:4]  #인덱스 2부터 4전까지 (2 ~ 3)
print(mm)

dd = jumin[4:6]  #인덱스 4부터 6전까지 (4 ~ 5)
print(dd)

print(f'{yy}년 {mm}월 {dd}일')

#뒤에서 가져오기~~~~~~~
print(jumin[-7:])
