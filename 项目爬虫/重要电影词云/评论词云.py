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
    clon = ['地点', '评论']
    df = pd.read_csv(path,encoding='utf-8',names=clon)
    comment = df['评论'].tolist()
    str_comment = ''.join(comment)
    ls = jieba.lcut(str_comment)
    txt = ' '.join(ls)
    bg_pic = imageio.v2.imread(f'C:\\Users\\LENOVO\\Desktop\\Python文件\\项目爬虫\\重要电影词云\\评论mask\\{movie_name}.jpg').astype(np.uint8)
    mask = np.array(bg_pic)
    # 这些stopwords是我自己添加的，是经过反复生成后过滤的
    stopwords = {'和','的','是','在','以','大','了','等','多','个','上','下','中','这','那','还','就','还','还是',
                 '有','没有','不是','不','吗','啊','呀','哦','呢','嗯','啦','吧','我','你','他','她','它','我们','你们','都'
                 ,'也','但','看','好','人','太','能','自己','说','更','像','又','电影','让','一个','这个','那个','这部','那部',
                 '真的','很','会','对','要','一部','与','到','就是','但是','可以','这么','这样','那么','那样','这种','那种','什么'
                 ,'得','最后','而','人物','给','想','再','从','因为','被'}
    w = wordcloud.WordCloud(font_path='msyh.ttc', width=1000, height=700,background_color=None,mode='RGBA',
                            stopwords=stopwords,mask=mask)
    w.generate(txt)
    w.to_file(f'{movie_name}词云.png')
    print(f'{movie_name}词云生成成功')
