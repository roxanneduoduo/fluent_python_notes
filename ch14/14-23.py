import functools


"""
# built-in functions
all(it)

any(it)

max(it, [key=,][default=])

min(it, [key=,][default=])

sum(it, start=0)


functools.reduce(func, it, [initial])
"""


print(all([1, 2, 3]))
print(all([1, 0, 3]))
print(all([]))
print(any([1, 2, 3]))
print(any([1, 0, 3]))
print(any([0, 0.0]))
print(any([]))

g = (n for n in [0, 0.0, 7, 8])
print(any(g))
print(next(g))
