"""
@decorate
def target():
    print('running target()')


# above function with decorator is equal to below:

def target():
    print('running target()')

target = decorate(target)

"""


def deco(func):
    def inner():
        print('running inner()')
    return inner


@deco
def target():
    print('running target()')

target()
print(target)

"""
use function deco to decorate the function target,
it actually execute the function inner

"""
