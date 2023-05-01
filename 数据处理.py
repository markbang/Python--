import jieba
import wordcloud
c=wordcloud.WordCloud
f=open("hamlet.txt","r",encoding='utf-8').read()
txt=jieba.lcut(f)
w=c(width=1000,font_path='msyh.ttc',height=700,
    background_color='white')
w.generate(f)
w.to_file('hamlet词云.png')