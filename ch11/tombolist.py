from random import randrange
from tombola import Tombola


@Tombola.register
class TomboList(list):

    def pick(self):
        if self:
            position = randrange(len(self))
            return self.pop(position)
        else:
            raise LookupError('pop from empty TomboList')

    load = list.extend

    def loaded(self):
        return bool(self)

    def inspect(self):
        return tuple(sorted(self))

# Tombola.register(TomboList)

if __name__ == '__main__':
    print(issubclass(TomboList, Tombola))
    print(issubclass(TomboList, list))

    t = TomboList(range(100))
    print(isinstance(t, TomboList))
    print(isinstance(t, Tombola))

    print(TomboList.__mro__)
