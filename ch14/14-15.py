import itertools
import operator


# mapping
"""
itertools.accumulate
itertools.starmap
enumerate       # built-in
map             # built-in

"""

sample = [5, 4, 2, 8, 7, 6, 3, 0, 9, 1]
for par in (
            (sample,),
            (sample, min),
            (sample, max),
            (sample, operator.mul),
            (range(1, 11), operator.mul)
            ):
    print(list(itertools.accumulate(*par)))


print(list(enumerate('albatroz', 1)))

for par in (
            (operator.mul, range(11), range(11)),
            (operator.mul, range(11), [2, 4, 8]),
            (lambda a, b: (a, b), range(11), [2, 4, 8])
            ):
    print(list(map(*par)))

for par in (
    (operator.mul, enumerate('albatroz', 1)),
    (lambda a, b: b/a, enumerate(itertools.accumulate(sample), 1))
):
    print(list(itertools.starmap(*par)))
