# 将csv文件里面的评论内容提取出来，然后生成词云
import jieba
import wordcloud
import imageio
import numpy as np
import pandas as pd
f = open('评论路径.txt', 'r', encoding='utf-8')
t = f.read()
f.close()
for path in eval(t):
    movie_name = path.split('\\')[-1].split('.')[0][:-2]
    df = pd.read_csv(path,encoding='utf-8')
    comment = df[1].tolist()
    ls = jieba.lcut(str(comment))
    txt = ' '.join(ls)
    bg_pic = imageio.v2.imread(f'C:\\Users\\LENOVO\\Desktop\\Python文件\\项目爬虫\\重要电影词云\\评论mask\\{movie_name}.jpg').astype(np.uint8)
    mask = np.array(bg_pic)
    stopwords = {'和','的','是','在','以','大','了','等','多'}
    w = wordcloud.WordCloud(font_path='msyh.ttc', width=1000, height=700,background_color='white',
                            stopwords=stopwords,mask=mask)
    w.generate(txt)
    w.to_file(f'{movie_name}词云.png')