#리스트 출력
import sqlite3
import os

path = os.path.dirname(os.path.realpath(__file__))  #현재 경로 구해서
db_name = path + '/juso.db'

con = sqlite3.connect(db_name)  #db 연결, 오픈 - 1.커넥션 오픈
cursor = con.cursor()  #2.커서 오픈

sql = "select * from juso"
cursor.execute(sql)

rows = cursor.fetchall()  #커서의 결과를 모두 꺼내오겠다
for row in rows:
    print(f'번호: {row[0]}, 이름: {row[1]}, 주소: {row[2]}')

#커밋 안해도됌 - 내용 입력/수정/삭제 시에만

cursor.close()
con.close()