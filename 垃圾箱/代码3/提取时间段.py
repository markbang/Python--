# 提取出时间段
import pandas as pd
import re

# 读取数据
data = pd.read_excel(r'C:\Users\LENOVO\Desktop\Python文件\垃圾箱\代码3\时间段与店铺数.xlsx')

# 编写正则表达式
pattern = re.compile(r'(?P<part_time>\b\d{1,2}:\d{2}-\d{1,2}:\d{2}\b)')
time_list = []
for i in range(len(data)):
    results = pattern.finditer(data['营业时间'][i])
    for result in results:
        time_list.append(result.group('part_time'))
time_num = {'0时':0, '1时':0, '2时':0, '3时':0, '4时':0, '5时':0, '6时':0, '7时':0, '8时':0, '9时':0, '10时':0, '11时':0, '12时':0, '13时':0, '14时':0, '15时':0, '16时':0, '17时':0, '18时':0, '19时':0, '20时':0, '21时':0, '22时':0, '23时':0, '24时':0}
for time in time_list:
    start = int(time.split('-')[0].split(':')[0])
    end = int(time.split('-')[1].split(':')[0])
    deferen = end - start
    for i in range(start, end+1):
        time_num[str(i)+'时'] += 1
print(time_num)