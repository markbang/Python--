#从学校数据.txt中提取出地区为china的学校的名字
import re
f=open(r'C:\Users\LENOVO\Desktop\Python文件\垃圾箱\代码4\学校数据.txt','r',encoding='utf-8')
f1=open('提取出的学校名字.txt','w',encoding='utf-8')
obj = re.compile(r'"country": "CN",(?P<j>.*?)"nameOfUniversity": "(?P<name>.*?)",',re.S)
result = obj.finditer(f.read())
for i in result:
    f1.write(i.group('name')+'\n')
f.close()
f1.close()