"""
+=
*=

+=, the special method is __iadd__
*=, the special method is __imul__

for +=, if the class has no __iadd__, it will call __add__

for example, the below expression:
	>>> a += b

if a has __iadd__ method, it call this method, and if a is mutable sequence (like list, bytearray and array.array), 
a changed in place, just like called a.extend(b).
but if a has no __iadd__ method, the expression just like a = a + b:
firstly count a + b, get a new object, and then assign the new object to a.

for *=, the same way
"""

l = [1, 2, 3]

print(id(l))
l *= 2
print(l)
print(id(l))

print()

t = (1, 2, 3)
print(id(t))
t *= 2
print(t)
print(id(t))
