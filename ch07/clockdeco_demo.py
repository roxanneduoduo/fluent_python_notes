import time
from clockdeco import clock


@clock
def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


@clock
def smooze(seconds):
    time.sleep(seconds)


if __name__ == '__main__':
    print('*' * 40, 'Calling smooze(.123)')
    smooze(.123)
    print('*' * 40, 'Calling factorial(6)')
    print('6! = ', factorial(6))

    print(factorial.__name__)
    """
    现在 factorial 保存的是 clocked 函数的引用，因此它的属性 __name__ 是 clocked
    这个装饰器的缺点就是遮盖了被装饰函数的 __name__ 和 __doc__ 属性
    """
