"""
默认做浅复制
"""

l1 = [3, [55, 44], (7, 8, 9)]
l2 = list(l1)
print(l2)
print(l2 == l1)
print(l2 is l1)

"""
还可以用简洁的 l2 = l1[:] 语句创建副本

然而，构造方法或者 [:] 做的都是浅复制
即复制了最外层的容器，副本中的元素是源容器中元素的引用。
如果所有元素都是不可变的，那么这样没有问题，还能节省内存。
但是如果有可变的元素，可能就会导致意向不到的问题。
"""

l1 = [3, [66, 55, 44], (7, 8, 9)]
l2 = list(l1)
l1.append(100)
l1[1].remove(55)
print('l1:', l1)
print('l2:', l2)

l2[1] += [33, 22]
l2[2] += (10, 11)
print('l1:', l1)
print('l2:', l2)
