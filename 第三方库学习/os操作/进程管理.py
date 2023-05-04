import os
print(os.getlogin())  # 获取当前登录用户名
print(os.cpu_count())  # 获取CPU核心数
os.rename('test.txt', 'test2.txt')  # 重命名文件
os.getcwd()  # 获取当前工作目录
os.mkdir('test')  # 创建文件夹
os.chdir('test')  # 切换工作目录
os.rmdir('test')  # 删除文件夹
os.remove('test.txt')  # 删除文件
os.listdir('test')  # 列出目录下所有文件
os.system('cmd')  # 执行命令