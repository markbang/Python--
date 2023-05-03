import jieba
import pandas as pd
import numpy as np

from pyecharts import options as opts
from pyecharts.globals import ThemeType
from pyecharts.globals import SymbolType
from pyecharts.charts import Pie, Bar, Map, WordCloud, Page

df_mv=pd.read_excel(r"电影清单.xlsx")
print(df_mv)




"""这里是进行地区名字替代"""
places=('河北省 山西省 辽宁省 吉林省 黑龙江省 江苏省 浙江省 安徽省 福建省 江西省 山东省 河南省 湖北省 湖南省 广东省 海南省 四川省 贵州省 云南省 陕西省 甘肃省 青海省 台湾省 内蒙古自治区 广西壮族自治区  西藏自治区 宁夏回族自治区 新疆维吾尔自治区 北京市 天津市 上海市 重庆市 香港特别行政区 澳门特别行政区')
oldplace=places.split(" ")
newplace=[]
for i in oldplace:
    if "省" in i: i=i[:-1]
    elif"市" in i: i=i[:-1]
    elif"内蒙古" in i:i=i[0:3]
    elif "自治区" in i: i=i[0:2]
    elif"特别行政区"in i: i=i[:-5]
    newplace.append(i)
place=dict(zip(oldplace,newplace))

map = (
    Map()
    .add("店铺数量",
         [['广东',200],['广西',100],['湖南',19,]], "china",name_map=place)
    #关闭地区名称显示
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False)
    )
    #设置标题和图例
    .set_global_opts(
        title_opts=opts.TitleOpts(title="商家店铺地址分布图"),
        visualmap_opts=opts.VisualMapOpts(max_=200),
    )

)
map.render()

#import pandas as pd 
#df_mv=pd.read_csv("") 
