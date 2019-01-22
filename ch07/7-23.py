"""
为了便于启用或禁用 register 执行的函数注册功能,
我们为它提供了一个可选参数 active，
设为 False 时，不注册被装饰函数。

从概念上看，这个新的 register 函数不是装饰器，而是装饰器工厂函数。
调用它会返回真正的装饰器，这才是应用到目标函数上的装饰器。
"""

registry = set()


def register(active=True):
    def decorate(func):
        print('running register(active=%s) -> decorate(%s)' % (active, func))
        if active:
            registry.add(func)
        else:
            registry.discard(func)

        return func
    return decorate


@register(active=False)
def f1():
    print('running f1()')


@register()
def f2():
    print('running f2()')


def f3():
    print('running f3()')

print(registry)

register()(f3)
print(registry)

register(active=False)(f2)
print(registry)
