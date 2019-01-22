'''
Callable Objects

Except user defined function, call operator () also can apply on other objects.
Jugde if an object can be called, you can use the built-in function callable().

Python data model document list 7 callable objects:
1. user defined functions: defined by def sentence or lambda expression.

2. built-in functions

3. built-in methods

4. methods

5. class

6. instance

7. generator function
'''

print(abs, str, 13)
print([callable(obj) for obj in (abs, str, 13)])


'''
Then let's make the instance of class callable

Not only Python function is real object, any Python object can behave like function.
for this, you just need realize method __call__.
'''

import random


class BingoCage:
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)
        
    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')
        
    def __call__(self):
        return self.pick()
    
    
bingo = BingoCage(range(3))
print(bingo.pick())
print(bingo())
print(callable(bingo))



