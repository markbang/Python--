import pymysql
db = pymysql.connect(host='localhost',
                     user='root',
                     password='root123456')
cursor = db.cursor()
print(cursor.execute('SELECT VERSION();'))
data = cursor.fetchone()
print('Database version:', data)
db.close()