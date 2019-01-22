"""
b = 6


def f2(a):
    print(a)
    print(b)
    b = 9

f2(3)


An UnboundLocalError happened

Python 不要求声明变量，但是假定在函数定义体中赋值的变量是局部变量。

"""

"""
如果在函数中赋值时想让解释器把 b 当成全局变量，要使用 global 声明：
"""

b = 6


def f3(a):
    global b
    print(a)
    print(b)
    b = 9

f3(3)
print(b)

b = 30
print(b)


"""
可以反汇编 7-4 和 7-5 中的 f1, f2 函数来比较它们的字节码

from dis import dis

dis(f1)
dis(f2)
"""
