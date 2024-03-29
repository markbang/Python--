# 计算abc/a+b+c 从100到999之和
sum_num = 0
for a in range(1,10):
    for b in range(0,10):
        for c in range(0,10):
            sum_num += int(str(a)+str(b)+str(c))/(a+b+c)
print(sum_num)