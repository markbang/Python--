import pandas as pd
with open('评论路径.txt','r',encoding='utf-8')as f:
    content = f.read()
ip_list = []
for i in eval(content):
    df = pd.read_csv(i,encoding='utf-8')
    df_new = df.dropna()
    for ip in df_new.iloc[:,0]:
        ip_list.append(ip)
with open('所有IP.txt','a',encoding='utf-8')as file:
    file.write(str(ip_list))
