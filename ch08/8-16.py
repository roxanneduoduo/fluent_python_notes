"""
del 语句删除名称，而不是对象。
del 命令可能导致对象被垃圾回收，但是仅当删除的变量保存的是对象的最后一个引用，或者无法得到对象时。

本示例使用 weakref.finalize 注册一个回调函数，在销毁对象时使用。
"""


import weakref
s1 = {1, 2, 3}
s2 = s1


def bye():
    print('Gone with the wind...')


ender = weakref.finalize(s1, bye)
print(ender.alive)

del s1
print(ender.alive)
s2 = 'spam'
print(ender.alive)
