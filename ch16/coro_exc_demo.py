"""
from Python 2.5, customer code can call 2 method on generator object, 
explicit send exception to coroutine.

generator.throw(exc_type[, exc_value[, traceback]])

generator.close()
"""

class DemoException(Exception):
    """exception defined for this demo"""


def demo_exc_handling():
    print('-> coroutine started')
    while True:
        try:
            x = yield
        except DemoException:
            print('*** DemoException handled. Continuing...')
        else:
            print('-> coroutine received: {!r}'.format(x))
    raise RuntimeError('This line should never run.')


if __name__ == '__main__':
    # prime and close coroutine, without exception
    exc_coro = demo_exc_handling()
    next(exc_coro)
    exc_coro.send(11)
    exc_coro.send(22)
    exc_coro.close()
    from inspect import getgeneratorstate
    getgeneratorstate(exc_coro)

    # send DemoException to demo_exc_handling won't stop coroutine
    exc_coro = demo_exc_handling()
    next(exc_coro)
    exc_coro.send(11)
    exc_coro.throw(DemoException)
    getgeneratorstate(exc_coro)

    # if send other exception that has no handler, coroutine stop
    exc_coro = demo_exc_handling()
    next(exc_coro)
    exc_coro.send(11)
    exc_coro.throw(ZeroDivisionError)
    getgeneratorstate(exc_coro)

