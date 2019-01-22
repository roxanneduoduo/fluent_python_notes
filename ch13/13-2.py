import decimal


ctx = decimal.getcontext()
one_third = decimal.Decimal('1') / decimal.Decimal('3')
print(one_third)
print(one_third == +one_third)
ctx.prec = 28
print(one_third == +one_third)
print(one_third)
print(+one_third)


# when decimal precsion changed, sometimes +x != x
