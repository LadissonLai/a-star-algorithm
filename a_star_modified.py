# a_star.py

import sys
import time

import numpy as np

from matplotlib.patches import Rectangle
import math
import point
import fixed_map


# 小结：强波的这种写法，是一种很简单的考虑：
# 每一步选择最优的路径，不更新原来的路径，不重复以前的路径，
# 每一个节点的成本（实际成本+估计成本）都是独立的，与历史路径没有关系
# 总结：可以这么理解强波的算法。就是一种广度优先的搜索算法，每一步选择距离最近的点走。
# 1、所有的点代价值可以提前计算出来，并且不变
# 2、每一步扩大了可行走的区域，在这些区域里面选择一个最优的来走。直到找到目标点。
# 3、回溯的时候，就只关心每一步的父节点即可完成回溯。

class AStar:
    def __init__(self, map: fixed_map.FixedMap, start: point.Point, end: point.Point):
        self.map = map
        self.open_set = []
        self.close_set = []
        self.start = start
        self.end = end

    def BaseCost(self, p):
        x_dis = math.fabs(p.x - self.start.x)
        y_dis = math.fabs(p.y - self.start.y)
        # Distance to start point
        return x_dis + y_dis + (np.sqrt(2) - 2) * min(x_dis, y_dis)

    def HeuristicCost(self, p):
        x_dis = math.fabs(p.x - self.end.x)
        y_dis = math.fabs(p.y - self.end.y)
        # Distance to end point
        return x_dis + y_dis + (np.sqrt(2) - 2) * min(x_dis, y_dis)

    def TotalCost(self, p):
        return self.BaseCost(p) + self.HeuristicCost(p)

    def IsValidPoint(self, x, y):
        if x < 0 or y < 0:
            return False
        if x >= self.map.width or y >= self.map.height:
            return False
        return not self.map.IsObstacle(x, y)

    def IsInPointList(self, p, point_list):
        for point in point_list:
            if point.x == p.x and point.y == p.y:
                return True
        return False

    def IsInOpenList(self, p):
        return self.IsInPointList(p, self.open_set)

    def IsInCloseList(self, p):
        return self.IsInPointList(p, self.close_set)

    def IsStartPoint(self, p):
        return p.x == self.start.x and p.y == self.end.y

    def IsEndPoint(self, p):
        return p.x == self.end.x and p.y == self.end.y

    def SaveImage(self, plt):
        millis = int(round(time.time() * 1000))
        filename = './' + str(millis) + '.png'
        plt.savefig(filename)

    # 这里处理是有问题的
    def ProcessPoint(self, x, y, parent):
        if not self.IsValidPoint(x, y):
            return  # Do nothing for invalid point
        p = point.Point(x, y)
        if self.IsInCloseList(p):
            return  # Do nothing for visited point
        print('Process Point [', p.x, ',', p.y, ']', ', cost: ', p.cost)
        if not self.IsInOpenList(p):
            p.parent = parent
            p.cost = self.TotalCost(p)
            self.open_set.append(p)

    def SelectPointInOpenList(self):
        index = 0
        selected_index = -1
        min_cost = sys.maxsize
        for p in self.open_set:
            cost = self.TotalCost(p)
            if cost < min_cost:
                min_cost = cost
                selected_index = index
            index += 1
        return selected_index

    def BuildPath(self, p, ax, plt, start_time):
        path = []
        while True:
            path.insert(0, p)  # Insert first
            if self.IsStartPoint(p):
                break
            else:
                p = p.parent
        for p in path:
            rec = Rectangle((p.x, p.y), 1, 1, color='g')
            ax.add_patch(rec)
            plt.draw()
            self.SaveImage(plt)
        end_time = time.time()
        print('===== Algorithm finish in', int(end_time - start_time), ' seconds')

    def RunAndSaveImage(self, ax, plt):
        start_time = time.time()

        start_point = self.start
        start_point.cost = 0
        self.open_set.append(start_point)

        while True:
            index = self.SelectPointInOpenList()
            if index < 0:
                print('No path found, algorithm failed!!!')
                return
            p = self.open_set[index]
            rec = Rectangle((p.x, p.y), 1, 1, color='c')
            ax.add_patch(rec)
            self.SaveImage(plt)

            if self.IsEndPoint(p):
                return self.BuildPath(p, ax, plt, start_time)

            del self.open_set[index]
            self.close_set.append(p)

            # Process all neighbors
            x = p.x
            y = p.y
            self.ProcessPoint(x - 1, y + 1, p)
            self.ProcessPoint(x - 1, y, p)
            self.ProcessPoint(x - 1, y - 1, p)
            self.ProcessPoint(x, y - 1, p)
            self.ProcessPoint(x + 1, y - 1, p)
            self.ProcessPoint(x + 1, y, p)
            self.ProcessPoint(x + 1, y + 1, p)
            self.ProcessPoint(x, y + 1, p)
