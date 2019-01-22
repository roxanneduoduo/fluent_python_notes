# 叠放装饰器

"""
@d1
@d2
def f():
    print('f')

above function is equal to:

def f():
    print('f')

f = d1(d2(f))
"""

# 参数化装饰器

"""
解释源码中的装饰器时，Python把被装饰的函数作为第一个参数传给装饰器函数。

那么怎么让装饰器接收其它参数呢？答案是：
创建一个装饰器工厂函数，把参数传给它，返回一个装饰器，
然后再把它应用到被装饰的函数上。

"""

registry = []


def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func


@register
def f1():
    print('running f1()')


print('running main()')
print('registry ->', registry)
f1()
