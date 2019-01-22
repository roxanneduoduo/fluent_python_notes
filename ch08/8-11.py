"""
Python 唯一支持的参数传递模型是共享传参 （call by sharing）

共享传参指函数的各个形式参数获得实参中各个引用的副本。
也就是说，函数内部的形参是实参的别名。

这种方案的结果是， 函数可能会修改作为参数传入的可变对象，
但是无法修改那些对象的标识（即不能把一个对象替换成另一个对象）
"""


def f(a, b):
    a += b
    return a


x = 1
y = 2
print(f(x, y))

print(x, y)

a = [1, 2]
b = [3, 4]

print(f(a, b))
print(a, b)

t = (10, 20)
u = (30, 40)

print(f(t, u))
print(t, u)
