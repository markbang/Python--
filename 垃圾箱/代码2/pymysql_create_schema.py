import pymysql
db = pymysql.connect(host='localhost',
                     user='root',
                     password='root123456',
                     database='TESTDB')
# sql = '''create table employee(
#          first_name char(20) not null,
#          last_name char(20),
#          age int,
#          sex char(1),
#          income float);'''
cursor = db.cursor()
# cursor.execute(sql)
# cursor.execute('SHOW TABLES;')
# data = cursor.fetchall()
# print(data)
# cursor.execute('DROP TABLE IF EXISTS EMPLOYEE;')
# data = cursor.fetchall()
# print(data)
# sql = '''INSERT INTO EMPLOYEE(FIRST_NAME,
#  LAST_NAME, AGE, SEX, INCOME) VALUES ('Mac', 'Mohan', 20, 'M', 2000)'''
try:
    # cursor.execute(sql)
    # cursor.execute('SELECT * FROM EMPLOYEE;')
    # cursor.execute('UPDATE EMPLOYEE SET AGE=AGE+1 WHERE SEX="M";')
    # cursor.execute('DELETE FROM EMPLOYEE WHERE AGE>20;')
    cursor.execute('')
    # data = cursor.fetchall()
    # db.commit()
except:
    # data = []
    db.rollback()
    print('Error: unable to fetch data')
# for row in data:
#     print(row)
#     fname = row[0]
#     lname = row[1]
#     age = row[2]
#     sex = row[3]
#     income = row[4]
#     print('fname:', fname,'lname:',lname,'age:',age,'sex:',sex,'income:',income)
db.close()
#年少立志出乡关，学不成名誓不还。
#埋骨何须桑梓地，人生无处不青山。