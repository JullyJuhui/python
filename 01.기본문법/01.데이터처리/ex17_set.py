#집합: set - 교집합, 차집합, 합집합
java = {'유재석', '홍길동', '심청이'}
print(1, java, type(java))

python = {'심청이', '강호동', '이순신'}
print(2, python, type(python))

#교집합, 합집합, 차집합
print(3, java.intersection(python)) #교집합 :java, python 둘다 가능
print(4, java.union(python)) #합집합 :모든 학생
print(5, java.difference(python)) #차집합 :java만 가능

#추가
java.add('강호동')
print(6, java)

#삭제
java.remove('유재석')
print(7, java)

#타입 바꾸기
java = list(java)
print(8, java, type(java))

java = tuple(java)
print(9, java, type(java))

java = set(java)
print(10, java, type(java))