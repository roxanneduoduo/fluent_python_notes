import itertools
import operator


"""
itertools.chain
itertools.chain.from_iterable
itertools.product
zip     # built-in
itertools.zip_longest

itertools.combinations(it, out_len)
itertools.combinations_with_replacement(it, out_len)
itertools.count(start=0, step=1)
itertools.cycle(it)
itertools.permutations(it, out_len=None)
itertools.repeat(item, [times])
"""


for f, args in zip(
    [
        itertools.chain,
        itertools.chain,
        itertools.chain.from_iterable,
        zip,
        zip,
        itertools.zip_longest,
    ],
    [
        ('ABC', range(2)),
        (enumerate('ABC'),),
        (enumerate('ABC'),),
        ('ABC', range(5)),
        ('ABC', range(5), [10, 20, 30, 40]),
        ('ABC', range(5))
    ]
):
    print(list(f(*args)))

print(list(itertools.zip_longest('ABC', range(5),  fillvalue='?')))


suits = 'spades hearts diamonds clubs'
for args in (
    ('ABC', range(2)),
    ('AK', suits),
    ('ABC',)
):
    print(list(itertools.product(*args)))


print(list(itertools.product('ABC', repeat=2)))
print(list(itertools.product(range(2), repeat=3)))

rows = itertools.product('AB', range(2), repeat=2)

for row in rows:
    print(row)


ct = itertools.count()

print(next(ct))
print((next(ct), next(ct), next(ct)))
print(list(itertools.islice(itertools.count(1, .3), 3)))


cy = itertools.cycle('ABC')
print(next(cy))
print(list(itertools.islice(cy, 7)))


rp = itertools.repeat(7)
print((next(rp), next(rp)))
print(list(itertools.repeat(8, 4)))
print(list(map(operator.mul, range(11), itertools.repeat(5))))


for f in (
    itertools.combinations,
    itertools.combinations_with_replacement,
    itertools.permutations):
    print(list(f('ABC', 2)))

print(list(itertools.product('ABC', repeat=2)))
