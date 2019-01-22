def gen_AB():
    print('start')
    yield 'A'
    print('Continue')
    yield 'B'
    print('end')


for c in gen_AB():
    print('-->', c)
