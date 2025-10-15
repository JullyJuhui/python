class Product:
    def __init__(self):
        self.code = ''
        self.name = ''
        self.price = 0

    def print(self):
        print(f'코드: {self.code}, 상품명: {self.name}, 가격: {self.price:,}원')

class Sale(Product):
    def __init__(self):
        super().__init__()
        self.seq = 0
        self.date = ''
        self.qnt = 0
        self.sum = 0

    def print(self):
        print(f'No: {self.seq}, 코드: {self.code}, 상품명: {self.name}, 판매일: {self.date}')
        print(f'판매가: {self.price:,}원, 수량: {self.qnt}개, 수익: {self.sum:,}원')
        print('-' * 60)

#test
if __name__ == '__main__':
    product = Product()

    product.code = '101'
    product.name = '냉장고'
    product.price = 100

    product.print()


    sale = Sale()
    sale.seq = 1  #seq 자동인데 왜 지정하지라 생각했지만 이건 sql이 아녔다 그냥 클래스 속성일 뿐...
    sale.code = product.code
    sale.name = product.name
    sale.price = 99
    sale.date = '2025-08-29'
    sale.print()