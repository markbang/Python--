for i in range(1,10):
    with open('C:\\Users\\LENOVO\\Desktop\\作业\\上机作业\\'+str(i)+'.txt','r',encoding='utf-8') as m:
        n = m.read()
    with open('C:\\Users\\LENOVO\\Desktop\\作业\\上机作业\\10224804419王棒棒.txt','a') as f:
        f.write(f'第{i}题：\n')
        f.write(n)
        f.write('\n')
print('合成成功！')