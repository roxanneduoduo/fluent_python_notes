# when Python execute the decorator?

"""
decorator has been executing immediately after the decorated function defined.
it's usually is when import modules
"""


registry = []


def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func


@register
def f1():
    print('running f1()')


@register
def f2():
    print('running f2()')


def f3():
    print('running f3()')


def main():
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()


if __name__ == '__main__':
    main()


"""
execute this file, and see the output result in terminal

as you can see,
function register has been execute before other functions (execute twice)

if import this file as module, output as below:

running register(<function f1 at 0x0000000001ECC048>)
running register(<function f2 at 0x0000000001ECC1E0>)


this just explain:
decorator has been executed when import module,
and decorated function executed when calling.


"""
