# 将csv文件中的评论提取出来
import pandas as pd
import jieba
clon = ['地点','评论']
df = pd.read_csv(r'C:\Users\LENOVO\Desktop\Python文件\项目爬虫\详细信息(包括电影评价人数、评分等)\电影评论\哪吒之魔童降世评论.csv',
                 encoding='utf-8',names=clon)
comment = df['评论'].tolist()
str_comment = ''.join(comment)
print(str_comment)
