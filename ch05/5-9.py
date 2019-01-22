'''
Function Introspection
'''

def factorial(n):
    '''return n!'''
    return 1 if n < 2 else n * factorial(n - 1)

print(dir(factorial))


# __dict__

# list properties that function has but general object has not.
'''
['__annotations__', '__call__', '__closure__', '__code__', '__defaults__', '__get__', '__globals__', '__kwdefaults__', '__name__', '__qualname__']
'''
class C: pass
obj = C()
def func(): pass
print(sorted(set(dir(func)) - set(dir(obj))))


