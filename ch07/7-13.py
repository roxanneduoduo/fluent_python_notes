def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        count += 1
        total += new_value
        return total / count

    return averager


avg = make_averager()
avg(10)

"""
An UnboundLocalError generated.

当 count 是数字或任何不可变类型时，
count += 1 语句的作用其实与 count = count + 1 一样。
因此我们在 averager 的定义体中为 count 赋值了，这会把 count 变成局部变量。
total 变量也受这个问题影响。

为解决这个问题，Python引入 nonlocal 声明。看示例 7-14
"""
