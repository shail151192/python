import psycopg2
import random

params = {
    'host':'localhost',
    'database': 'test',
    'user': 'admin_odx',
    'password': 'odx'
}

conn = psycopg2.connect(**params)
cursor = conn.cursor()
# sql = "select * from student"
#
# with conn.cursor() as cur:
#     cur.execute(sql)
#     res = cur.fetchall()
#     print res
data = []
chars = 'abcdefghijklmnopqrstuvwxyz'
for i in range(0, 10000):
    name = random.choice(chars) + random.choice(chars) + random.choice(chars)
    roll_no = random.randint(1, 100)
    data.append({'name':name, 'roll_no': roll_no})

# res = ('('+ d['name'], d['roll_no'] for d in data)
# res = [(d['name'], d['roll_no']) for d in data]
res = data
cols = res[0].keys()
r= ",".join(['('+",".join(["'{}'".format(d[col]) for col in cols]) + ')' for d in res])

sql = """ INSERT INTO {db_table} ({columns}) VALUES {val}; """.format(
            db_table='student',
            columns = ",".join(cols),
            val = r
        )

try:
    with conn.cursor() as cur:
        res = cur.execute(sql)
        conn.commit()
        print res

except Exception as err:
    print err
