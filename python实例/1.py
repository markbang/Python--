# 题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# li = [1,2,3,4]
# for i in li:
#     for j in li:
#         for k in li:
#             if i != j and j != k and i != k:
#                 print(i,j,k)


# 题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元
# 的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于
# 40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提
# 成，从键盘输入当月利润I，求应发放奖金总数？

# 1
# I = float(input('当月利润：'))
# if I <= 100000:
#     print('奖金：',I * 0.1)
# elif I <= 200000:
#     print('奖金：',100000 * 0.1 + (I - 100000) * 0.075)
# elif I <= 400000:
#     print('奖金：',100000 * 0.1 + 100000 * 0.075 + (I - 200000) * 0.05)
# elif I <= 600000:
#     print('奖金：',100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + (I - 400000) * 0.03)
# elif I <= 1000000:
#     print('奖金：',100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + 200000 * 0.03 + (I - 600000) * 0.015)
# else:
#     print('奖金：',100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + 200000 * 0.03 + 400000 * 0.015 + (I - 1000000) * 0.01)

# 2
# I = float(input('当月利润：'))
# lirun = [0,100000,200000,400000,600000,1000000]
# rate = [0.1,0.075,0.05,0.03,0.015,0.01]
# bonus = 0
# for i in range(len(lirun)):
#     if I > lirun[i]:
#         if I > 1000000:
#             bonus += (1000000 - lirun[i]) * rate[i]
#         else:
#             bonus += (lirun[i+1] - lirun[i]) * rate[i]
# print('奖金：',bonus)


# 题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
# import math
# for i in range(1000):
#     x = math.sqrt(i + 100)
#     y = math.sqrt(i + 268)
#     if x == int(x) and y == int(y):
#         print(i)
with open('C:\Users\LENOVO\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1',encoding='utf-8') as f:
    f.write('Invoke-Expression (&starship init powershell)')