'''
in Python 2, reduce is a built-in function, but in Python 3, it has been put in module
functools

function reduce usually used for get sum result,
but now we have the built-in "sum" function,
it's better to use function sum.
'''

from functools import reduce
from operator import add

print(reduce(add, range(100)))
print(sum(range(100)))