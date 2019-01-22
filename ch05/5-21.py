from functools import reduce
from operator import mul


def fact_1(n):
    return reduce(lambda a, b: a*b, range(1, n+1))

def fact_2(n):
    return reduce(mul, range(1, n+1))