#리스트 출력
import sqlite3
import os

path = os.path.dirname(os.path.realpath(__file__))  #현재 경로 구해서
db_name = path + '/juso.db'

con = sqlite3.connect(db_name)  #1.커넥션 오픈
cursor = con.cursor()  #2.커서 오픈

sql = 'drop table if exists juso'
cursor.execute(sql)
con.commit()

sql = 'create table juso('
sql += 'seq integer primary key autoincrement,'
sql += 'name char(20),'
sql += 'address char(200));'
cursor.execute(sql)
con.commit()

cursor.close()
con.close()