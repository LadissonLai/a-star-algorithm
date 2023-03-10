# main.py

import numpy as np
import matplotlib.pyplot as plt

from matplotlib.patches import Rectangle

import random_map
import a_star

plt.figure(figsize=(5, 5))

# 根据地图的size随机生成障碍物，使用一个Point列表来存储障碍物
map = random_map.RandomMap(20)

ax = plt.gca()
ax.set_xlim([0, map.size])
ax.set_ylim([0, map.size])

# 绘制栅格地图
for i in range(map.size):
    for j in range(map.size):
        if map.IsObstacle(i, j):
            rec = Rectangle((i, j), width=1, height=1, color='gray')
            ax.add_patch(rec)
        else:
            rec = Rectangle((i, j), width=1, height=1, edgecolor='gray', facecolor='w')
            ax.add_patch(rec)

# 绘制起点为蓝色
rec = Rectangle((0, 0), width=1, height=1, facecolor='b')
ax.add_patch(rec)

# 绘制目标点为红色
rec = Rectangle((map.size - 1, map.size - 1), width=1, height=1, facecolor='r')
ax.add_patch(rec)

plt.axis('equal')
plt.axis('off')
plt.tight_layout()
# plt.show()

# a star 算法计算
a_star = a_star.AStar(map)
# 保存每一步的计算结果
a_star.RunAndSaveImage(ax, plt)
