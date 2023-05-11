import jieba
import wordcloud
import imageio
import numpy as np
f = open('20大报告.txt', 'r', encoding='utf-8')
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = ' '.join(ls)
bg_pic = imageio.v2.imread(r'C:\Users\LENOVO\Desktop\Python文件\项目爬虫\重要电影词云\评论mask\让子弹飞.jpg').astype(np.uint8)
mask = np.array(bg_pic)
stopwords = {'和','的','是','在','以','大','了','等','多'}
w = wordcloud.WordCloud(font_path='msyh.ttc', width=1000, height=700,background_color='white',
                        stopwords=stopwords,mask=mask)
w.generate(txt)
w.to_file('20大词云.png')