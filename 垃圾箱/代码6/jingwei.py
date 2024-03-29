import json

with open(r'C:\Users\LENOVO\Desktop\Python文件\垃圾箱\代码6\经纬.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 将里面星级大于四的放到一个json文件，小于4的放到另一个文件
with open(r'C:\Users\LENOVO\Desktop\Python文件\垃圾箱\代码6\经纬1.json', 'w', encoding='utf-8') as f1:
    for item in data:
        if float(item['星级']) > 4:
            f1.write(json.dumps(item, ensure_ascii=False) + ',' + '\n')
with open(r'C:\Users\LENOVO\Desktop\Python文件\垃圾箱\代码6\经纬2.json', 'w', encoding='utf-8') as f2:
    for item in data:
        if float(item['星级']) <= 4:
            f2.write(json.dumps(item, ensure_ascii=False) +',' + '\n')