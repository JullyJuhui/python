import os
import sqlite3

path = os.path.dirname(os.path.realpath(__file__))
db_name = path +'/juso.db'

class Product:
    def __init__(self):
        self.code = 0
        self.name = ''
        self.price = 0

    def print(self):
        print(f"코드: {self.code}, 이름: {self.name}, 가격: {self.price:,}원")

def rowPrint(row):
    if row == None:
        print('해당 상품이 없습니다.')
        
    else:
        product = Product()
        product.code = row[0]
        product.name = row[1]
        product.price = row[2]
        product.print()

        return product
    
def rowPrint2(row):
    product = Product()
    product.code = row[0]
    product.name = row[1]
    product.price = row[2]
    product.print()

    return product

#목록 출력-----------------------------------------------------------
#type: 1.코드 2.이름 3.최저가 4.최고가
def list(type):  
    con = sqlite3.connect(db_name)  #db open
    cursor = con.cursor() #cursor open

    sql = 'select code, name, price from product '
    if type == 1:
        sql += 'order by code'
    elif type == 2:
        sql += 'order by name'
    elif type == 3:
        sql += 'order by price'
    elif type == 4:
        sql += 'order by price desc'

    cursor.execute(sql)
    rows = cursor.fetchall()

    cursor.close()
    con.close()

    return rows

def list_test(type):
    rows = list(type)
    for row in rows:
        rowPrint(row)

#입력-----------------------------------------------------------
def insert(product):
    con = sqlite3.connect(db_name)
    cursor = con.cursor()
    sql = 'insert into product(name, price) values(?, ?)'
    cursor.execute(sql, (product.name, product.price,))
    con.commit()
    cursor.close()
    con.close()

def insert_test():
    product = Product()
    product.name = input('상품이름> ')
    product.price = int(input('상품가격> '))
    insert(product)

#읽기-----------------------------------------------------------
def read(code):
    con = sqlite3.connect(db_name)
    cursor = con.cursor()
    sql = "select * from product where code = ?"
    cursor.execute(sql, (code, ))
    row = cursor.fetchone()
    cursor.close()
    con.close()

    return row

def read_test():
    code = int(input('상품코드> '))
    row = read(code)

    if row == None:
        print('상품코드가 없습니다.')

    else:
        rowPrint(row)

#검색-----------------------------------------------------------
def search(name):
    con = sqlite3.connect(db_name)
    cur = con.cursor()
    sql = 'select * from product where name like ?'
    cur.execute(sql, (f'%{name}%',))

    rows = cur.fetchall()
    
    cur.close()
    con.close()

    return rows

def search_test():
    while True:
        name = input('상품명> ')
        if name == '': break
        rows = search(name)

        for row in rows:
            rowPrint(row)

#삭제-----------------------------------------------------------
def delete(code):
    con = sqlite3.connect(db_name)
    cur = con.cursor()

    sql = 'delete from product where code = ?'
    cur.execute(sql, (code,))
    con.commit()

    cur.close()
    con.close()

def delete_test():
    code = int(input('삭제번호> '))
    row = read(code)

    if row == None:
        print('상품코드가 없습니다.')

    else:
        rowPrint(row)
        delete(code)


#수정-----------------------------------------------------------
def update(product):  #객체
    con = sqlite3.connect(db_name)
    cur = con.cursor()

    sql = "update product set name = ?, price = ? where code = ?"
    cur.execute(sql, (product.name, product.price, product.code,))
    con.commit()

    cur.close()
    con.close()

def update_test():
    code = int(input('수정번호> '))
    row = read(code)
    p = rowPrint(row)

    if p != None:
        name = input(f'상품이름: {p.name}> ')
        if name != "": p.name = name

        price = input(f'상품가격: {p.price:,}> ')
        if price != '': p.price = int(price)

        update(p)
        print('수정완료!')

if __name__ == '__main__':
    update_test()