def f1(a):
    print(a)
    print(b)


f1(3)
"""
when execute it, a NameError exception happened
obviously, the variable b is not defined

but if execute below code in Python intepreter:

>>> b = 6
>>> f1(3)
3
6

"""
