import pandas as pd

# 读取Excel文件
df = pd.read_excel('垃圾箱\代码6\Lenovo_patents.xls')

# 找出is_IBM=1的ipc号
result = df[df['is_IBM'] == 1]['ipc']

# 提取所有IPC号并去重
unique_ipcs = result.unique()
formatted_ipcs = [ipc.replace(' ', '') for ipc in unique_ipcs]
# 保存到文件
with open('垃圾箱\代码6\IPC.txt', 'w') as file:
    for i in formatted_ipcs:
        file.write(i + '\n')
formatted_ipcs = ' or '.join(formatted_ipcs)
print(formatted_ipcs)