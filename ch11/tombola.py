import abc


class Tombola(abc.ABC):

    @abc.abstractmethod
    def load(self, iterable):
        """add element from iterable object"""

    @abc.abstractmethod
    def pick(self):
        """randomly delete element, and return the element
        if instance is empty, throw `LookupError`
        """

    def loaded(self):
        """if the instance has one element at least, return `True`,
        otherwise `False`."""
        return bool(self.inspect())

    def inspect(self):
        """return a sequenced tuple that composed by current elements."""
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))


if __name__ == '__main__':
    class Fake(Tombola):
        def pick(self):
            return 13

    print(Fake)

    try:
        f = Fake()
    except TypeError as err:
        print('TypeError: {}'.format(err))
