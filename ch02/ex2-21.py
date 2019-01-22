import array


numbers = array.array('h', [-2, -1, 0, 1, 2])
print(numbers)

memv = memoryview(numbers)
print(memv)
print(len(memv))
print(memv[0])

memv_oct = memv.cast('B')
print(memv_oct.tolist())
print(memv_oct)

memv_oct[5] = 4
print(numbers)
