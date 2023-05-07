import matplotlib.pyplot as plt
# subplot()函数多次绘制多图
# 绘制第一个子图：折线图
ax1 = plt.subplot(221)
plt.plot([1, 2, 3], [2, 4, 6])
# 绘制第二个子图：柱状图
ax2 = plt.subplot(222)
plt.bar([1, 2, 3], [2, 4, 6])
# 绘制第三个子图：散点图
ax3 = plt.subplot(223)
plt.scatter([1, 3, 5], [2, 4, 6])
# 绘制第四个子图：直方图
ax4 = plt.subplot(224)
plt.hist([2, 2, 2, 3, 4])
plt.show()