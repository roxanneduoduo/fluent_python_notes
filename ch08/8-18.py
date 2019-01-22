"""
WeakValueDictionary 简介

WeakValueDictionary 类实现的是一种可变映射，里面的值是对象的弱引用。
被引用的对象在程序中的其它地方被当作垃圾回收后，对应的键会自动从 WeakValueDictionary 中删除。
因此，WeakValueDictionary 经常用于缓存。

"""
import weakref


class Cheese:

    def __init__(self, kind):
        self.kind = kind

    def __repr__(self):
        return 'Cheese(%r)' % self.kind


stock = weakref.WeakValueDictionary()
catalog = [
    Cheese('Red Leicester'),
    Cheese('Tilsit'),
    Cheese('Brie'),
    Cheese('Parmesan')
    ]

for cheese in catalog:
    stock[cheese.kind] = cheese

print(sorted(stock.keys()))

del catalog
print(sorted(stock.keys()))

del cheese
print(sorted(stock.keys()))


"""
WeakKeyDictionary

WeakSet

弱引用的局限
不是每个 Python 对象都可以作为弱引用的目标 （或称所指对象）
基本的 list 和 dict 实例不能作为所指对象，但是它们的子类可以轻松解决这个问题。
"""
