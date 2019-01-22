"""
Python 对不可变类型施加的把戏

对于元组 t 来说 t[:] 不创建副本，而是返回同一个对象的引用。
此外， tuple(t) 获得的也是同一个元组的引用。
"""

t1 = (1, 2, 3)
t2 = tuple(t1)
print(t2 is t1)

t3 = t1[:]
print(t3 is t1)

"""
str、bytes 和 frozenset 实例也有这种行为。
注意，frozenset 实例不是序列，因此不能使用 fs[:] （fs 是一个frozenset实例）。
但是，fs.copy() 具有相同效果：
它会欺骗你，返回同一个对象的引用，而不是创建一个副本。
"""

T1 = (1, 2, 3)
T3 = (1, 2, 3)
print(T3 is T1)

s1 = 'ABC'
s2 = 'ABC'
print(s2 is s1)

"""
共享字符串字面量是一种优化措施，称为驻留（interning）
"""
