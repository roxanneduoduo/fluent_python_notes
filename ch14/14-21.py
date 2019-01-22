import itertools


"""
itertools.groupby(it, key=None)
reversed  # built-in
itertools.tee(it, n=2)
"""


print(list(itertools.groupby('LLLLAAGGG')))

for char, group in itertools.groupby('LLLLAAAGG'):
    print(char, '->', list(group))


animals = [
    'duck', 'eagle', 'rat',
    'giraffe', 'bear', 'bat',
    'dolphin', 'shark', 'lion'
]
animals.sort(key=len)
print(animals)

for length, group in itertools.groupby(animals, len):
    print(length, '->', list(group))

for length, group in itertools.groupby(reversed(animals), len):
    print(length, '->', list(group))


print(list(itertools.tee('ABC')))

g1, g2 = itertools.tee('ABC')
print(next(g1))
print(next(g2))
print(next(g2))
print(list(g1))
print(list(g2))

print(list(zip(*itertools.tee('ABC'))))
