from DB import *
from classes import *

def sale_list(value):
    try:
        sql = 'select * from view_sale where code like %s or name like %s'
        value = f'%{value}%'

        cur.execute(sql, (value, value))

        rows = cur.fetchall()

        if rows:
            sales = []
            for row in rows:
                sale = Sale()
                sale.seq = row['seq']
                sale.code = row['code']
                sale.name = row['name']
                sale.date = row['fdate']
                sale.price = row['price']
                sale.qnt = row['qnt']
                sale.sum = row['price'] * row['qnt']

                sales.append(sale)
            
            return sales

    except Exception as err:
        print('매출목록오류:', err)

def sale_insert(sale):
    sql = 'insert into sale(code, date, qnt, price) values(%s, now(), %s, %s)'
    cur.execute(sql, (sale.code, sale.qnt, sale.price))
    con.commit()
    print('매출등록완료!')

#test
if __name__ == '__main__':
    sales = list()

    for sale in sales:
        sale.print()