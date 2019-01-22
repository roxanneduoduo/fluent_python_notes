# 闭包 closure

"""
闭包和匿名函数是两个不同的概念。

闭包是指延伸了作用域的函数，其中包含函数定义体的引用、但是不在定义体中定义的非全局变量。
函数是不是匿名的没有关系，关键是它能访问定义体之外定义的非全局变量。
"""


# 用面向对象的方法计算历史平均值
class Averager:

    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)

avg = Averager()

print(avg(10))

print(avg(11))

print(avg(12))
