from coroaverager1 import averager


coro_avg = averager()
coro_avg.send(40)
coro_avg.send(50)
try:
    coro_avg.send('spam')
except TypeError as err:
    print(f'TypeError: {err}')

try:
    coro_avg.send(60)
except StopIteration:
    print(StopIteration)


"""
because send value is a string, coroutine inside throw an exception.
and coroutine has no exception handler, coroutine stop.
next time try to prime coroutine again, throw StopIteration. 
"""

