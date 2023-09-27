# 对百度所有专利名称进行词频统计，名称在csv文件第2列

import csv
import jieba
import jieba.analyse
import jieba.posseg as pseg
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import wordcloud

# 读取csv文件
df = pd.DataFrame(pd.read_csv('所有专利.csv', encoding='gbk'))
word_list = []
for i in range(len(df)):
    word_list.append(df.iloc[i, 1])
with open('userdict.txt', 'w', encoding='utf-8') as f:
    for i in word_list:
        f.write(i)
        f.write('\n')
# 分词，进行词频统计
f = open('userdict.txt', 'r', encoding='utf-8')
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = ' '.join(ls)
# 词云
step_word = {'和','的','是','在','以','大','了','等','多','基于','专利','技术','方法',
             '用于','装置','系统','一种',"的",'发明','本发明','本','发明的','本发明的',
             '设备','电子','处理','电子设备','及','and','method','system','device',}


w = wordcloud.WordCloud(font_path='msyh.ttc', width=1000, height=700,background_color='white',
                        stopwords=step_word,mask=None)
w.generate(txt)
w.to_file('专利词云.png')







