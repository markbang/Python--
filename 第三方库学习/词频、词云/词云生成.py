import jieba
import wordcloud
from imageio import imread
f = open(r'C:\Users\LENOVO\Desktop\Python文件\第三方库学习\词频、词云\20大报告.txt', 'r', encoding='utf-8')
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = ' '.join(ls)
bg_pic = imread(r'C:\Users\LENOVO\Desktop\Python文件\词频、词云\中国地图.png')
w = wordcloud.WordCloud(font_path='msyh.ttc', width=1000, height=700, background_color='white',stopwords={'和', '的','是', '在'},mask=bg_pic)
w.generate(txt)
w.to_file('grwprdcloud.png')