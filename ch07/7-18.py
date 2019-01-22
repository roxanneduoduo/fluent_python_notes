"""
Python builtin 3 decorators:

property
classmethod
staticmethod


another usually decorator is functools.wraps,
it help to create work behavior good decorators.


And two worth to care about decorators are:

functools.lru_cache
functools.singleispatch

"""

from clockdeco import clock


@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)


if __name__ == '__main__':
    print(fibonacci(6))


"""
see the output result,
you can see fibonacci(1) called 8 times, and fibonacci(2) called 5 times, ...
so use lru_cache, the performance improved. see 7-19
"""
