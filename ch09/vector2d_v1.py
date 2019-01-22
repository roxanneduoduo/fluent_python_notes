from array import array
import math


class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:].cast(typecode))
        return cls(*memv)

"""
classmethod 装饰器，定义操作类，而不是操作实例的方法。
因此类方法的第一个参数是类本身，而不是实例。
classmethod 的常见用途是定义备选的构造方法，例如本实例中的 frombytes。

frombytes 方法是将字节序列转换成 Vector2d 实例。
从而它是一个从字节序列中构造 Vector2d 实例的 备选的构造方法。
"""
