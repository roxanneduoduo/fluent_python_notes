class Demo:

    @classmethod
    def klassmeth(*args):
        return args

    @staticmethod
    def statmeth(*args):
        return args


print(Demo.klassmeth())
print(Demo.klassmeth('spam'))
print(Demo.statmeth())
print(Demo.statmeth('spam'))


"""
比较 classmethod 和 staticmethod

不管怎样调用 Demo.Klassmeth，它的第一个参数始终是 Demo 类

Demo.statmeth 的行为与普通的函数类似。
"""
