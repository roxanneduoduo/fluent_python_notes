import re
import reprlib


RE_WORD = re.compile('\w+')


class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence({})'.format(reprlib.repr(self.text))


if __name__ == '__main__':
    s = Sentence('"The time has come," the Walrus said,')
    print(s)
    for word in s:
        print(word)
    print(list(s))

    print(s[0])
    print(s[5])
    print(s[-1])

    s3 = Sentence('Pig and Pepper')
    it = iter(s3)
    print(it)

    while True:
        try:
            print(next(it))
        except StopIteration:
            print('StopIteration')
            break

    print(list(it))
    print(list(iter(s3)))


"""
the reason of Sequence is iterable: function iter()

the built-in function iter() works as below:

1. check if object has __iter__() method, if so, call it and get an Iterator.

2. if object has no __iter__() method, but it has __getitem__() method,
Python can create an Iterator, try to get element by sequence (from index 0)

3. if failed, Python throw TypeError.


any Python Sequence is iterable, because they all has __getitem__() method.
and standard Sequence also has __iter__() method.
so you should do the same for your defined Sequence object.

the way to check if object iterable, use iter() function:
    iter(x)

if x is not iterable, operate the TypeError.

this way is better than isinstance(x, abc.Iterable)
"""
