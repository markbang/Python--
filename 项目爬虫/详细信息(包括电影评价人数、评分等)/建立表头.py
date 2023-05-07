# 需要合并，建立表头
import pandas as pd
new_col = ['电影名称', '票房（万）']
movie_info = pd.read_csv(r'C:\Users\LENOVO\Desktop\Python文件\项目爬虫\详细信息(包括电影评价人数、评分等)\电影票房\所有票房.csv', encoding='utf-8', names=new_col)
movie_info.drop_duplicates(subset=['电影名称'], inplace=True)
movie_info.to_csv('票房.csv', encoding='utf-8', index=False)


