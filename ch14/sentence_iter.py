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
        return SentenceIterator(self.words)


class SentenceIterator:

    def __init__(self, words):
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return word

    def __iter__(self):
        return self


"""
the instance of Sentence is an Iterable

the instance of SentenceIterator is an Iterator

Iterable has __iter__() method, and when call it,
it return an Iterator (SentenceIterator instance)

Iterator has __next__() method, and index from 0, when call __next__() method,
it return element by index, and when IndexError, throw StopIteration
the Iterator has been exhausted.

Iterator also has __iter__() method, but it just return the iterator self.

because Iterator also has __iter__() method, it is also iterable.
but Iterable is not Iterator.

every time call iter(my_iterable) create a new Iterator.
when Iterator has been exhausted, it can't be recovered.
you only can use iter(my_iterable) to create a new Iterator.
"""
