"""
内置类型的方法不会调用子类覆盖的方法。
例如，dict的子类覆盖的 __getitem__() 方法不会被内置类型的 get() 方法调用。
"""


class DoppelDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)


dd = DoppelDict(one=1)
print(dd)
dd['two'] = 2
print(dd)
dd.update(three=3)
print(dd)
