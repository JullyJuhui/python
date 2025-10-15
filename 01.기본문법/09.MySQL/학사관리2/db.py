import pymysql

con = pymysql.connect(
    host = 'localhost', #or '192.168.0.34' / 내부에서 접속시의 ip주소
    user = 'root', 
    password = '1234',
    db = 'haksa',
    charset = 'utf8',
    cursorclass=pymysql.cursors.DictCursor #셀렉트한 커서가 딕셔너리 형태로~~)
)
cur = con.cursor()

class Dept:
    def __init__(self):
        self.dcode = 0
        self.dname = ''

    def print(self):
        print(f'학과코드: {self.dcode}, 학과이름: {self.dname}')

class Student(Dept):
    def __init__(self):
        super().__init__()
        self.id = ''
        self.name = ''
        self.code = 0

    def print(self):
        print(f'학번: {self.id}, 이름: {self.name}, 학과: {self.dname}({self.code})')
        print('-'*60)

#기능 함수---------------------------------------------------------------------------------------------
def list(key):
    try:
        sql = f'select * from vstudent order by {key}'
        cur.execute(sql)
        rows = cur.fetchall()

        list = []
        for row in rows:
            stu = Student()
            stu.id = row['id']  #딕셔너리로 반환해서 'id'로 작성 가능
            stu.name = row['name']  
            stu.code = row['code']
            stu.dname = row['dname']

            list.append(stu)

        return list
    except Exception as err:
        print('목록오류:', err)

def search(value):
    try:
        sql = 'select * from vstudent where id like %s or name like %s or dname like %s'
        value = '%' + value + '%'
        cur.execute(sql, (value, value, value,))
        
        rows = cur.fetchall()

        if rows != None:
            list = []

            for row in rows:
                stu = Student()
                stu.id = row['id']
                stu.name = row['name']
                stu.code = row['code']
                stu.dname = row['dname']

                list.append(stu)

            return list

    except Exception as err:
        print('검색오류:', err)

def insert(stu):
    try:
        sql = 'insert into student(id, name, code) values(%s, %s, %s)'
        cur.execute(sql, (stu.id, stu.name, stu.code))
        con.commit()
        print('학생등록완료!')

    except Exception as err:
        print('등록오류:', err)

def delete(id):
    try:
        sql = 'delete from student where id = %s'
        cur.execute(sql, (id))
        con.commit()
        print('삭제완료!')

    except Exception as err:
        print('삭제오류:', err)

def update(stu):
    try:
        sql = 'update student set name = %s, code = %s where id = %s'
        cur.execute(sql, (stu.name, stu.code, stu.id))
        con.commit()
        print('수정완료!')

    except Exception as err:
        print('수정오류:', err)

#부가적 함수----------------------------------------------------------------------------------------------
def read(id):
    try:
        sql = 'select * from vstudent where id = %s'
        cur.execute(sql, (id))
        row = cur.fetchone()

        if row != None:
            stu = Student()
            stu.id = row['id']
            stu.name = row['name']
            stu.code = row['code']
            stu.dname = row['dname']

            return stu

    except Exception as err:
        print('읽기오류:', err)

def newID():
    try:
        sql = 'select convert(max(id)+1, char(4)) as newID from student'  #convert로 자료형 바꿈
        cur.execute(sql)
        row = cur.fetchone()

        return row['newID']

    except Exception as err:
        print('새 학번:', err)

def listDept():  #Dept 객체를 담은 리스트 반환
    try:
        sql = 'select * from dept'
        cur.execute(sql)
        rows = cur.fetchall()

        list = []
        for row in rows:
            dept = Dept()
            dept.dcode = row['dcode']
            dept.dname = row['dname']

            list.append(dept)

        return list

    except Exception as err:
        print('학과목록:', err)

def inputCode(title, menu):  #학과코드입력함수 - 입력 / 수정
    depts = listDept()
    codes = [dept.dcode for dept in depts]
    print('-'*50)

    for dept in depts:
        print(f'{dept.dcode}.{dept.dname}', end = '|')

    print()
    print('-' * 50)

    while True:
        code = input(title)

        if code == '' and menu == 1:  #입력용
            print('학과코드는 꼭 입력해주세요!')

        if code == '' and menu == 5:  #수정용
            return code

        elif not code.isnumeric():
            print('학과코드는 숫자로 입력하세요!')

        elif codes.count(int(code)) == 0:  #입력받은 코드가 코드스 리스트에 존재하지 않을때
            print(f'{codes} 코드번호를 입력하세요!')

        else:
            return int(code)

#학과등록
def insertDept(dname):
    sql = 'insert into dept(dname) values(%s)'
    cur.execute(sql, (dname))
    con.commit()
    print('학과등록완료!')

#학과읽어오기
def readDept(dcode):
    sql = 'select * from dept where dcode = %s'
    cur.execute(sql, (dcode))

    row = cur.fetchone()

    dept = Dept()
    dept.dcode = row['dcode']
    dept.dname = row['dname']

    return dept

#학과수정
def updateDept(dept):
    sql = 'update dept set dname = %s where dcode = %s'
    cur.execute(sql, (dept.dname, dept.dcode))

    con.commit()
    print('학과수정완료!')


if __name__ == '__main__':
    id = input('학번> ')
    stu = read(id)

    if stu == None:
        print('학생이 없습니다.')

    else:
        stu.print()