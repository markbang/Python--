import jieba
import wordcloud
from PIL import Image
import numpy as np
f = open('20大报告.txt', 'r', encoding='utf-8')
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = ' '.join(ls)
bg_pic = Image.open(r'牢大.jpg')
print(bg_pic)
mask = np.array(bg_pic)
b = mask
mask = Image.fromarray(b.astype('uint8'))
mask.save('牢大3.jpg')
# stopwords = {'和','的','是','在','以','大','了','等','多'}
# w = wordcloud.WordCloud(font_path='msyh.ttc', width=1000, height=700,background_color='white',
#                         stopwords=stopwords,mask=mask)
# w.generate(txt)
# w.to_file('20大词云.png')