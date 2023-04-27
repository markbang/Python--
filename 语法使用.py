import time
print('正在开始读取文件......')
time.sleep(3)
f=open('haha.txt','r',encoding='utf-8')
for i in f.readlines():
    print(i.strip())
print('读取完成！')
print('请等待几秒关闭文件！')
time.sleep(3)
f.close()
print('文件关闭成功！')
