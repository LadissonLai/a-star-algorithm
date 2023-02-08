import numpy as np

import point


class FixedMap:
    def __init__(self, width=7, height=5):
        self.width = width
        self.height = height
        self.obstacle_point = []
        self.GenerateObstacle()

    def GenerateObstacle(self):
        self.obstacle_point.append(point.Point(3, 1))
        self.obstacle_point.append(point.Point(3, 2))
        self.obstacle_point.append(point.Point(3, 3))

    def IsObstacle(self, i, j):
        for p in self.obstacle_point:
            if i == p.x and j == p.y:
                return True
        return False
