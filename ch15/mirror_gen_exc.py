import contextlib


@contextlib.contextmanager
def looking_glass():
    import sys
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])
    
    sys.stdout.write = reverse_write
    msg = ''
    try:
        yield 'JABBERWOCKY'
    except ZeroDivisionError:
        msg = 'Please DO NOT divide by zero!'
    finally:
        sys.stdout.write = original_write
        if msg:
            print(msg)


if __name__ == '__main__':
    with looking_glass() as what:
        print('Alice, Kitty and Snowdrop')
        print(what)

    print(what)


"""
in generator that decorated by @contextmanager,
yield has no relation with Iteration.
our example works more like coroutine:
execute code until some point and stop,
and then let customer code executing, 
and then return to coroutine to executing remainder code.
"""