"""
弱引用

正是因为有引用，对象才会在内存中存在。
而对象的引用数量归零后，垃圾回收程序会把对象销毁。

但是，有时需要引用对象，而不让对象存在的时间超过所需时间。
这经常用在缓存中。

弱引用不会增加对象的引用数量。
引用的目标对象称为所指对象（referent）。
因此我们说，弱引用不会妨碍所指对象被当作垃圾回收。

弱引用在缓存应用中很有用，因为我们不想仅因为被缓存引用着而始终保存缓存对象。


本示例展示如何使用 weakref.ref 示例获取所指对象。
如果对象存在，调用弱引用可以获取对象；否则返回 None。


"""


import weakref


a_set = {0, 1}
wref = weakref.ref(a_set)
print(wref)
print(wref())

a_set = {2, 3, 4}

print(wref())
print(wref() is None)
print(wref() is None)

"""
try this code in console, get different result and understand it.

"""
