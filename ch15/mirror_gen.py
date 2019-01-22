import contextlib


"""
contextlib support some class or functions

closing

suppress

@contextmanager

ContextDecorator

ExitStack

"""


@contextlib.contextmanager
def looking_glass():
    import sys
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write
    yield 'JABBERWOCKY'
    sys.stdout.write = original_write


if __name__ == '__main__':
    with looking_glass() as what:
        print('Alice, Kitty and Snowdrop')
        print(what)

    print(what)


"""
@contextmanager decorator maybe feel confused, it has no related with Iteration, 
but it use yield sentence.
that can leading us to coroutine.

in the generator that using @contextmanager, 
yield sentence splite function body to 2 part,
all code before yield sentence: __enter__
all code after yield sentence: __exit__

the yield value will bind to the with sentence as sub-sentence target variable.

"""