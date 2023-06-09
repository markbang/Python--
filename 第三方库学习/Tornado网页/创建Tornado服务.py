import tornado.ioloop
import tornado.web
import pymysql


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(r"C:\Users\LENOVO\Desktop\Python文件\垃圾箱\代码2\index.html")

    def post(self):
        # 打开数据库连接
        self.db = pymysql.connect(host='localhost',
                                  user='root',
                                  password='root123456',
                                  database='TESTDB')
        # 使用cursor()方法获取操作游标
        self.cursor = self.db.cursor()
        self.set_header("Content-Type", "text/plain")
        if self.get_body_argument("message") == 'select':
            sql = "SELECT * FROM EMPLOYEE WHERE INCOME > 1000;"
            try:
                # 执行SQL语句
                self.cursor.execute(sql)
                # 获取所有记录列表
                results = self.cursor.fetchall()

            except:
                results = []
                print("Error: unable to fetch data")

            for row in results:
                print(row)
                fname = row[0]
                lname = row[1]
                age = row[2]
                sex = row[3]
                income = row[4]
                # 打印结果
                self.write("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
                           (fname, lname, age, sex, income))
            self.write("Done print.")
            # 关闭数据库连接
            self.db.close()


# SQL 查询语句
sql = "SELECT * FROM EMPLOYEE \
       WHERE INCOME > 1000;"


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()

