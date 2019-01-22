# 14.10 Python 3.3 new syntax: yield from


# defined our function chain (itertools.chain is realized by C in standard library)


def chain(*iterables):
    for it in iterables:
        for i in it:
            yield i


s = 'ABC'
t = tuple(range(3))
print(list(chain(s, t)))
# ['A', 'B', 'C', 0, 1, 2]


# yield from syntax can simplized above function


def chain_simple(*iterables):
    for i in iterables:
        yield from i

print(list(chain_simple(s, t)))
# ['A', 'B', 'C', 0, 1, 2]

# yield from
"""
As you can see "yield from i" completely replace of the inner for loop.

Except replace loop, yield from aslo can create pipe,
directly connect the inner generator with the client of outer generator.
using generator as coroutine, this pipe is very important,
it not just generate value for client code, 
and also can use the value that supported by client code.
"""


# Coroutine
"""

Python 2.2 introduce yield key word to realize generator function.
Python 2.5 realize "PEP 342 - Coroutines via Enhanced Generators".
This proposal add extended methods for generator object,
The most worth to noticed is .send() method.

The same with .__next__() method,
.send() method make generator forwart the the next yield sentence.
However, 
.send() method also allow the client that using the generator send data to itself,
No matter what argument to .send() method, 
this argument will become to the corresponding yield expression value 
in the generator function body.
That is meaning, .send() method allow exchange data between client code and generator.
And .__next__() method only allow client get data from generator.

This is an important "improvement", that even change the nature of generator:
using like this, generator become to coroutine.

        1. generator used for generate data for iteration
        2. Coroutine is the consumer of data
        3. generator and coroutine, these two concepts cannot be confused.
        4. Coroutine is not related with Iteration.
        5. although coroutine use yield to generate data, but it is not related with Iteration.

"""