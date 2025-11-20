import matplotlib.pyplot as plt

# 创建一个新的图形
fig, ax = plt.subplots()

# 绘制水平线
for i in range(5):
    ax.axhline(i, color='black')

# 绘制垂直线
for i in range(5):
    ax.axvline(i, color='black')

# 设置坐标轴范围
ax.set_xlim(-0.5, 4.5)
ax.set_ylim(-0.5, 4.5)

# 关闭坐标轴刻度和标签
ax.axis('off')

# 显示图形
plt.show()