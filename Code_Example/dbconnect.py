import pymysql

class DBHelper:

    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.password = ""
        self.db = 'myproject'

    def connection(self):
        self.con = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db, cursorclass=pymysql.cursors.
                                   DictCursor)
        self.cur = self.con.cursor()

    def disconnect(self):
        self.con.close()

    def fetch(self, sql):
        self.connection()
        row_cnt=self.cur.execute(sql)

        result = self.cur.fetchall()

        self.disconnect()
        return result

    def execute(self, sql):
        self.connection()
        self.cur.execute(sql)
        self.disconnect()

    def execute_row(self, sql,param1):
        self.connection()
        self.cur.execute(sql,param1)
        self.disconnect()

