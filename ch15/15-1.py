with open('else_block.py') as fp:
    src = fp.read(60)

print(len(src))

print(fp)

print(fp.closed, fp.encoding)

try:
    fp.read(60)
except ValueError as err:
    print(f'ValueError: {err}')
