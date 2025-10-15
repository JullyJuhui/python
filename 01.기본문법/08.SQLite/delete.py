#삭제
import sqlite3
import os

path = os.path.dirname(os.path.realpath(__file__))  #현재 경로 구해서
db_name = path + '/juso.db'

con = sqlite3.connect(db_name)  #db 연결, 오픈 - 1.커넥션 오픈
cursor = con.cursor()  #2.커서 오픈

sql = "delete from juso where seq = ?"
seq = int(input('삭제번호> '))

cursor.execute(sql, (seq,))

con.commit()
cursor.close()
con.close()