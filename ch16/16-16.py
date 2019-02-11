"""
yield from 
is totally new language structure.

example:
in generator "gen", use "yield from subgen",
subgen get control temporarily, yield value to gen's caller, 
meaning caller can directly control subgen. 
in the meanwhile, gen is block and waiting for subgen end.


in chapter 14, yield from can be used for simply yield expression in for loop:

def gen():
    for c in 'AB':
        yield c
    for i in range(1, 3):
        yield i

print(list(gen()))
# ['A', 'B', 1, 2]

# can change to:

def gen():
    yield from 'AB'
    yield from range(1, 3)

print(list(gen()))
# ['A', 'B', 1, 2]
"""

def chain(*iterables):
    for it in iterables:
        yield from it


s = 'ABC'
t = tuple(range(3))
print(list(chain(s, t)))


"""
yield from x

the first thing of this sentenct "yield from x" is:
call iter(x), get the iterator from it. 
so x can be any Iterable object.

"yield from" not just a replacement for nested for loop.

but also,
its main function is open an two-way channel (pipe), 
connect the most outer caller with the most inner sub-generator.
So both can directly send and yield value, and also directly send exceptions, 
instead of inserting many exception handle code in the middle coroutine.

Delegating generator
    the generator function that include `yield from <iterable>` expression.

Subgenerator
    the generator object that get from expression `yield from <iterable>`

Caller
    PEP 380 use `caller` this term to reference customer code that call "Delegating generator"


"""
