# 由于票房是很多很多电影的，所以需要合并信息，此处用到的是pandas的merge函数，根据电影名字进行合并
# 读取票房信息
import pandas as pd
box_office=pd.read_csv(r'C:\Users\LENOVO\Desktop\Python文件\项目爬虫\详细信息(包括电影评价人数、评分等)\票房.csv',encoding='utf-8')
# 读取电影详细信息
movie_info=pd.read_csv(r'C:\Users\LENOVO\Desktop\Python文件\项目爬虫\详细信息(包括电影评价人数、评分等)\movie_info.csv',encoding='utf-8')
# 合并信息
movie_info=pd.merge(movie_info,box_office,how='left',on='电影名称')
# 保存信息
movie_info.to_csv('详细信息.csv',encoding='utf-8',index=False)
