import sqlite3
import os

path = os.path.dirname(os.path.realpath(__file__))  #현재 경로 구해서
db_name = path + '/juso.db'

class Person:
    def __init__(self):  #생성자: 객체 초기화, 디폴트 값
        self.seq = 0
        self.name = '홍길동'
        self.address = '경기도 광명시'

    #매소드 = 함수
    def print(self):
        print(f'번호: {self.seq}, 이름: {self.name}, 주소: {self.address}')

#목록
def list():
    con = sqlite3.connect(db_name)  #1.커넥션 오픈
    cursor = con.cursor()  #2.커서 오픈
    
    sql = 'select seq, name, address from juso'
    cursor.execute(sql)
    rows = cursor.fetchall()

    cursor.close()
    con.close()

    return rows

#검색
def search(value):
    con = sqlite3.connect(db_name)
    cursor = con.cursor()
    sql = "select * from juso where name like ? or address like ?"
    value = '%' + value + '%'
    cursor.execute(sql, (value, value,))
    rows = cursor.fetchall()

    cursor.close()
    con.close()

    return rows

#읽기
def read(seq):
    con = sqlite3.connect(db_name)
    cursor = con.cursor()
    sql = "select * from juso where seq = ?"
    cursor.execute(sql, (seq,))
    row = cursor.fetchone()

    cursor.close()
    con.close()

    return row

#삭제
def delete(seq):
    con = sqlite3.connect(db_name)
    cursor = con.cursor()
    sql = "delete from juso where seq = ?"
    cursor.execute(sql, (seq,))
    con.commit()
    cursor.close()
    con.close()

#입력
def insert(person):
    con = sqlite3.connect(db_name)
    cursor = con.cursor()
    sql = "insert into juso(name, address) values(?, ?)"
    cursor.execute(sql, (person.name, person.address, ))
    con.commit()
    cursor.close()
    con.close()


#수정
def update(person):  #받는 매개변수가 많을때 클래스로 캡슐화해서 간단히 받는다.
    con = sqlite3.connect(db_name)
    cursor = con.cursor()
    sql = "update juso set name = ?, address = ? where seq = ?"
    cursor.execute(sql, (person.name, person.address, person.seq,))
    con.commit()
    cursor.close()
    con.close()
    

if __name__ == '__main__':
    p = Person()
    p.seq = int(input('수정번호> '))
    row = read(p.seq)

    if row == None:
        print('수정번호가 없습니다.')

    else:
        p.name = row[1]
        p.address = row[2]

        name = input(f'이름: {p.name}> ')
        if name != '': p.name = name
        address = input(f'주소: {p.address}> ')
        if address != '': p.address = address

        update(p)

        print('수정완료!')

    # rows = list()
    # print(f'입력 전: {len(rows)}')  

    # p = Person()
    # p.name = input('이름> ')
    # p.address = input('주소> ')
    # insert(p)

    # rows = list()
    # print(f'입력 후: {len(rows)}')
    
    # for row in rows:
    #     p = Person()
    #     p.seq = row[0]
    #     p.name = row[1]
    #     p.address = row[2]
    #     p.print()