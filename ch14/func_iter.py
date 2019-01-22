from random import randint


def d6():
    return randint(1, 6)


d6_iter = iter(d6, 1)
print(d6_iter)

for roll in d6_iter:
    print(roll)


"""
in Python iter() usually called when iterate an object: iter(x)

but iter() also has another function: with 2 arguments, 
create generator by using general function or any callable object.

the first argument is callable object, 
used for calling again and again (with no argument).
the second argument is a sentinel, when callable object return this value, 
the iterator throw StopIteration exception, don't generate the sentinel value.


with open('mydata.txt') as fp:
    for line iter(fp.readline, '\n'):
        process_line(line)

the above code read file line by line, until met empty line or the end of file.
"""