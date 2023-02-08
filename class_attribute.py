class itest_Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


if __name__ == '__main__':
    p = itest_Point(1, 1)
    p.parent = "临时赋值的属性"  # python类里面的公有属性可以不声明就使用，太疯狂了
    print(p.parent)
