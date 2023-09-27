# 统计所有专利年份数量

import pandas as pd

df = pd.DataFrame(pd.read_csv('所有专利.csv', encoding='gbk'))
year_list = []
for i in range(len(df)):
    year_list.append(df.iloc[i, 4])
new_list = []
for n in year_list:
    n = str(n)
    new_list.append(n[0:4])
dic = {}
for i in new_list:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
# 顺序
dic = sorted(dic.items(), key=lambda x: x[0])
print(dic)
