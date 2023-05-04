# 用概率统计的方法计算出圆周率，用到random库
# 用到的知识点：random库的使用，概率统计的方法
# 用到的库：random
# 用到的函数：random.random()
# 用到的类：无
from random import random
DATAS=1000000
hits=0.0
for i in range(1,DATAS+1):
    x,y=random(),random()
    dist=pow(x**2+y**2,0.5)
    if dist<=1.0:
        hits+=1
pi=4*(hits/DATAS)
print("圆周率的值是：{}".format(pi))