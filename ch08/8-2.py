class Gizmo:

    def __init__(self):
        print('Gizmo id: %d' % id(self))


x = Gizmo()

try:
    y = Gizmo() * 10
except Exception as err:
    print(err)

print(dir())
"""
创建对象之后才会把变量分配给对象

该示例证明赋值语句的右边先执行。

为了理解 Python 中的赋值语句，应该始终先读右边。
对象在右边创建或获取，在此之后左边的变量才会绑定到对象上，
这就像为对象贴上标注。

因为变量只不过是标注，所以无法阻止为对象贴上多个标注。
贴上多个标注，就是别名。
"""
