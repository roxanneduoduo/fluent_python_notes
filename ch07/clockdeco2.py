import time
import functools


def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_list = []
        if args:
            arg_list.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
            arg_list.append(', '.join(pairs))

        arg_str = ', '.join(arg_list)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked


@clock
def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


@clock
def smooze(seconds):
    time.sleep(seconds)


@clock
def hello(people, world, count=5):
    for i in range(count):
        print('hello {}, {}'.format(people, world))


if __name__ == '__main__':
    print('*' * 40, 'Calling smooze(.123)')
    smooze(.123)
    print('*' * 40, 'Calling factorial(6)')
    print('6! = ', factorial(6))

    print(factorial.__name__)

    print('*' * 40, 'Calling hello("emily", "earth", count=7)')
    hello("emily", "earth", count=7)
