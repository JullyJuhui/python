#db에 insert하는 작업
import sqlite3
import os

path = os.path.dirname(os.path.realpath(__file__))
db_name = path + '/juso.db'

con = sqlite3.connect(db_name)  #db 연결, 오픈 - 1.커넥션 오픈
cursor = con.cursor()  #2.커서 오픈

sql = "insert into juso(name, address) values('강감찬', '부산시 동래구')"
cursor.execute(sql)  #3.sql 작업
sql = "insert into juso(name, address) values('홍길동', '경기도 광명시')"
cursor.execute(sql)
sql = "insert into juso(name, address) values('이순신', '서울 강남구')"
cursor.execute(sql)

id= cursor.lastrowid  #insert할때마다 lastrowid 증가
con.commit()  #4. 커밋을 해야 데이터 적용됨 - 내용 입력/수정/삭제 시에만

cursor.close()  #5.커서 클로스
con.close()  #6.커넥션 클로스

print(f'id: {id}')