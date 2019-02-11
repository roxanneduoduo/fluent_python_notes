from inspect import getgeneratorstate


def simple_coro2(a):
    print('-> Started: a =', a)
    b = yield a
    print('-> Received: b =', b)
    c = yield a + b
    print('-> Received: c =', c)


my_coro2 = simple_coro2(14)

print(getgeneratorstate(my_coro2))
next(my_coro2)
print(getgeneratorstate(my_coro2))
my_coro2.send(28)
try:
    my_coro2.send(99)
except StopIteration:
    print('StopIteration')
print(getgeneratorstate(my_coro2))


"""
the key point is, coroutine stop at the position of keyword yield.

as we know, in assginment expression, the right part of "=" is executing before the assignment.
so for "b = yield a",
1. when coroutine code executing forward to this line, the right expression "yield a" is
executed firstly, and it generate (yield) value a to customer, and coroutine suspend.

2. when coroutine has been activated again, the assignment (b = a) is executing, and then executing
forward until the next yield expression. 

in our example, simple_coro2 has 3 procedures, 
every procedure ends at yield expression (or at StopIteration)
and next procedure start from that line, and assign the value of yeild expression to the variable

"""
