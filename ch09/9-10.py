from vector2d_v3 import Vector2d

v1 = Vector2d(3, 4)
print(v1.__dict__)
print(v1._Vector2d__x)

v1._Vector2d__x = 123
v1._Vector2d__y = 321

print(v1.x, v1.y)
print(v1)


"""
私有属性：以 __mood 形式, 即以两个前导下划线，尾部没有或最多一个下划线，以这种形式定义的属性

“受保护的”属性： 使用一个下划线前缀的属性

但是实质上，无论“私有属性”或者“受保护的属性”， 都是加引号的，因为并不能真正的实现私有和不可变。

"""
