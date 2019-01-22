# 用函数实现计算历史平均值，使用高阶函数 make_averager


def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return averager

avg = make_averager()

print(avg(10))

print(avg(11))

print(avg(12))

"""
注意，series 是 make_averager 函数的局部变量
可是调用 avg(10) 的时候， make_averager 函数已经返回了，而它的本地作用域也一去不复返了。

在 averager 函数中， series 是自由变量 (free variable)。
这是一个技术术语，指未在本地作用域中绑定的变量。

审查返回的 averager 对象，我们发现 Python 在 __code__ 属性(表示编译后的函数定义体)
中保存局部变量和自由变量的名称：

>>> avg.__code__.co_varnames
('new_value', 'total)
>>> avg.__code__.co_freevars
('series',)

series 的绑定在返回的 avg 函数的 __closure__ 属性中。
avg.__closure__ 中的各个元素对应与 avg.__code__.co_freevars 中的一个名称。
这些元素是 cell 对象， 有个 cell_contents 属性，保存着真正的值。

>>> avg.__code__.co_freevars
('series',)
>>> avg.__closure__
(<cell at 0x107a44f78: list object at 0x107a91a48>,)
>>> avg.__closure__[0].cell_contents
[10, 11, 12]

综上，闭包是一种函数，它会保留定义函数时存在的自由变量的绑定，这样调用函数时，
虽然定义作用域不可用了，但是仍然能使用那些绑定。

注意，只有嵌套在其它函数中的函数才可能需要处理不在全局作用域中的外部变量。

"""

print(avg.__code__.co_varnames)
print(avg.__code__.co_freevars)

print(avg.__closure__)
print(avg.__closure__[0].cell_contents)
