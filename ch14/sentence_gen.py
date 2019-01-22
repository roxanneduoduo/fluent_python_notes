import re
import reprlib


RE_WORD = re.compile('\w+')


class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence({})'.format(reprlib.repr(self.text))

    def __iter__(self):
        for word in self.words:
            yield word
        return


"""
The function is the same with [sentence_iter.py],
but this time we use Generator to realize.

in this example, Iterator is actually Generator object.
everytime call __iter__() method, it automatically create an generator.
here __iter__() is the generator function. (because it use "yield" keyword)


when a Python function definition body include "yield" keyword,
it is a generator function.
when call generator function, it return a generator object.
that is, generator function is generator factory.

"""
