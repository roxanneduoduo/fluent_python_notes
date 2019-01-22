from vector2d_v3 import Vector2d


v1 = Vector2d(1.1, 2.2)
dumped = bytes(v1)
print(dumped)
print(len(dumped))
v1.typecode = 'f'
dumpf = bytes(v1)
print(dumpf)
print(len(dumpf))
print(v1.typecode, Vector2d.typecode)
