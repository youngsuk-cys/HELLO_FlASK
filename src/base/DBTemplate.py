import pymysql

# 이게 메타 클래스네 (type) 은 type 상속받는 다는 의미.
class Singleton(type):
    __instances = {}      # 클래스의 인스턴스를 저장할 속성

    def __call__(cls, *args, **kwargs):    # 클래스로 인스턴스를 만들 때 호출되는 메서드
        if cls not in cls.__instances:     # 클래스로 인스턴스를 생성하지 않았는지 확인
            cls.__instances[cls] = super().__call__(*args, **kwargs)
                                           # 생성하지 않았으면 인스턴스를 생성하여 속성에 저장
        return cls.__instances[cls]        # 클래스로 인스턴스를 생성했으면 인스턴스 반환

class Database(metaclass=Singleton):

    def __init__(self):
        self.db= pymysql.connect(host='localhost',
                                  user='spring5',
                                  password='1',
                                  db='demo',
                                  charset='utf8')
        self.cursor= self.db.cursor(pymysql.cursors.DictCursor)

    def execute(self, query, args={}):
        self.cursor.execute(query, args) 
 
    def executeOne(self, query, args={}):
        self.cursor.execute(query, args)
        row= self.cursor.fetchone()
        return row
 
    def executeAll(self, query, args={}):
        self.cursor.execute(query, args)
        row= self.cursor.fetchall()
        return row
 
    def commit():
        self.db.commit()