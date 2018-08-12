import psycopg2

class Mycursor():

    def __init__(self):
        self.host = 'localhost'
        self.port = 5432
        self.db = 'odx_lm'
        self.user = 'admin_odx'
        self.password = 'odx'
        self.connection = None
        print "connection created"

    def __enter__(self):
        self.connection = psycopg2.connect(host='localhost', database='odx_lm', user='admin_odx', password='odx')
        print "enter in open connection"
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print exc_tb
        print exc_type
        print exc_val
        print "in exit connection "
        self.connection.close()


sql = """select dispatch_type from dispatcher_dispatch where id in(1,2,3)"""
with Mycursor() as curr:
    curr.execute(sql)
    res = curr.fetchall()
    print res

    

