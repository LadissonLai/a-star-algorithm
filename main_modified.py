# main.py

import numpy as np
import matplotlib.pyplot as plt

from matplotlib.patches import Rectangle

import fixed_map
import a_star_modified
import point

plt.figure(figsize=(5, 5))

map = fixed_map.FixedMap()

ax = plt.gca()
ax.set_xlim([0, map.width])
ax.set_ylim([0, map.height])

start = point.Point(1, 2)
end = point.Point(5, 2)

# 绘制栅格地图
for i in range(map.width):
    for j in range(map.height):
        if map.IsObstacle(i, j):
            rec = Rectangle((i, j), width=1, height=1, color='gray')
            ax.add_patch(rec)
        else:
            rec = Rectangle((i, j), width=1, height=1, edgecolor='gray', facecolor='w')
            ax.add_patch(rec)

# 绘制起点为蓝色
rec = Rectangle((start.x, start.y), width=1, height=1, facecolor='b')
ax.add_patch(rec)

# 绘制目标点为红色
rec = Rectangle((end.x, end.y), width=1, height=1, facecolor='r')
ax.add_patch(rec)

plt.axis('equal')
plt.axis('off')
plt.tight_layout()
# plt.show()

# a star 算法计算
a_star = a_star_modified.AStar(map, start, end)
# 保存每一步的计算结果
a_star.RunAndSaveImage(ax, plt)
