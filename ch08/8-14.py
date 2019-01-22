"""
防御可变参数

如果定义的函数接收可变参数，应该谨慎考虑调用方是否期望修改传入的参数。
例如，如果函数传入一个字典，而且在处理的过程中要修改它，
那么这个副作用要不要体现在函数的外部？
具体情况具体分析，这其实需要函数的编写者和调用方达成共识。

"""


class TwilightBus:

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


basketball_team = ['Sue', 'Tina', 'Maya', 'Diana', 'Pat']
bus = TwilightBus(basketball_team)
bus.drop('Tina')
bus.drop('Pat')
print(basketball_team)

"""
正确的做法是，校车自己维护乘客列表。
如 8-8 示例所示那样：

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

这句 self.passengers = list(passengers), 
创建 passengers 列表的副本；如果不是列表，就把它转换为列表。


"""