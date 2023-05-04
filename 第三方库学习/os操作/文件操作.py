import os
os.path.exists('test.txt')  # 判断文件是否存在
os.path.isfile('test.txt')  # 判断是否是文件
os.path.isdir('text.txt')  # 判断是否是文件夹
os.path.getsize('test.txt')  # 获取文件大小
os.path.abspath('test.txt')  # 获取绝对路径
os.path.split('test.txt')  # 分割路径
os.path.splitext('test.txt')  # 分割文件名和扩展名
os.path.join('test.txt')  # 拼接路径
os.path.dirname('test.txt')  # 获取文件所在目录
os.path.basename('test.txt')  # 获取文件名
os.path.getatime('test.txt')  # 获取文件最后访问时间
os.path.getmtime('test.txt')  # 获取文件最后修改时间
os.path.getctime('test.txt')  # 获取文件创建时间
