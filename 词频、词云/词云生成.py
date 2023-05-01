import jieba
import wordcloud
f = open(r'C:\Users\LENOVO\Desktop\Python文件\词频、词云\20大报告.txt', 'r', encoding='utf-8')
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = ' '.join(ls)
w = wordcloud.WordCloud(font_path='msyh.ttc', width=1000, height=700, background_color='white')
w.generate(txt)
w.to_file('grwprdcloud.png')