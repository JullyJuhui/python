#수정
import sqlite3
import os

path = os.path.dirname(os.path.realpath(__file__))  #현재 경로 구해서
db_name = path + '/juso.db'

con = sqlite3.connect(db_name)  #1.커넥션 오픈
cursor = con.cursor()  #2.커서 오픈

sql = "update juso set name=?, address=? where seq=?"  #? 미정
seq = int(input('번호> '))
name = input('이름> ')
address = input('주소> ')

cursor.execute(sql, (name, address, seq,))  #?에 넣어주기
con.commit()

cursor.close()
con.close()
