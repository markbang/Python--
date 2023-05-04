#  自定义函数，设置固定次数的登录
#  由键盘输入密码，密码正确显示“Login success！”，错误显示“Wrong password or invalid input”，并显示剩余输入次数
#  三次错误，显示“Your account has been suspended”，并退出程序
def login():
    for i in range(3):
        password = input("请输入密码：")
        if password == "123456":
            print("Login success！")
            break
        else:
            print("Wrong password or invalid input")
            print("剩余输入次数：{}".format(2 - i))
    print("Your account has been suspended")
    exit()


login()
