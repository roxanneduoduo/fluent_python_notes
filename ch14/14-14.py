import itertools


# filtering
"""
itertools.compress
itertools.dropwhile
itertools.filterfalse
itertools.islice
itertools.takewhile

filter  # built-in
"""


def vowel(c):
    return c.lower() in 'aeiou'


print(list(filter(vowel, 'Aardvark')))

for method in (
                itertools.filterfalse,
                itertools.dropwhile,
                itertools.takewhile
                ):
    print(list(method(vowel, 'Aardvark')))

print(list(itertools.compress('Aardvark', (1, 0, 1, 1, 0, 1))))

for par in (
            (4,),
            (4, 7),
            (1, 7, 2)
            ):
    print(list(itertools.islice('Aardvark', *par)))
