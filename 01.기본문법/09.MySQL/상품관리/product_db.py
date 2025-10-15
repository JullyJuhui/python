from DB import *
from classes import *

def list():
    try:
        sql = 'select * from product'
        cur.execute(sql)
        rows = cur.fetchall()

        products = []
        for row in rows:
            product = Product()
            product.code = row['code']
            product.name = row['name']
            product.price = row['price']

            products.append(product)

        return products

    except Exception as err:
        print('상품목록에러:', err)

def insert(product):
    try:
        sql = 'insert into product(code, name, price) values(%s, %s, %s)'
        cur.execute(sql, (product.code, product.name, product.price))
        con.commit()

        print('상품등록완료!')

    except Exception as err:
        print('상품등록에러:', err)

def search(value):
    try:
        sql = 'select * from product where code like %s or name like %s' 
        value = f'%{value}%'
        cur.execute(sql, (value, value))

        rows = cur.fetchall()

        if rows != None:
            products = []
            for row in rows:
                product = Product()
                product.code = row['code']
                product.name = row['name']
                product.price = row['price']

                products.append(product)

            return products


    except Exception as err:
        print('상품검색에러:', err)

def searchPrice(min, max):
    try:
        sql = 'select * from product where price >= %s and price <= %s'
        cur.execute(sql, (min, max))

        rows = cur.fetchall()

        products = []
        for row in rows:
            product = Product()
            product.code = row['code']
            product.name = row['name']
            product.price = row['price']

            products.append(product)

        return products


    except Exception as err:
        print('상품검색에러:', err)

def read(code):
    try:
        sql = f"select * from product where code = '{code}'"  #fix: {code} -> '{code}'
        cur.execute(sql)
        row = cur.fetchone()

        if row != None:
            product = Product()
            product.code = row['code']
            product.name = row['name']
            product.price = row['price']

            return product

    except Exception as err:
        print('상품검색에러:', err)

# def inputCode():
#     while True:
#         code = input('상품코드> ')
#         pro = read(code)  #***

#         if code == '': return ''

#         if not code.isnumeric():
#             print('상품코드는 숫자로 입력하세요!')

#         elif len(code) != 3:
#             print('상품코드는 3자리로 입력하세요!')

#         elif pro != None:
#             pro.print()
#             print('이미 등록된 상품입니다!')

#         else:
#             return code

def inputCode(title):
    while True:
        code = input(title)
   
        if code == '': return ''

        if not code.isnumeric():
            print('상품코드는 숫자로 입력하세요!')

        elif len(code) != 3:
            print('상품코드는 3자리로 입력하세요!')

        else:
            return code
        
def inputPrice(title):
    while True:
        price = input(title)

        if price == '':
            return 0
        
        elif not price.isnumeric():
            print('가격은 숫자로 입력하세요!')

        else:
            return int(price)
        
def update(product):
    try:
        sql = "update product set name = %s, price = %s where code = %s"
        cur.execute(sql, (product.name, product.price, product.code))
        con.commit()

        print('수정완료!')

    except Exception as err:
        print('상품수정오류:', err)

#test
if __name__ == '__main__':
    products = searchPrice(0, 1800000)

    if len(products) == 0:
        print('검색 결과가 존재하지 않습니다.')

    else:
        for product in products:
            product.print()