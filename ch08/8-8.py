"""
为任意对象做深复制和浅复制

copy 模块提供的 deepcopy 和 copy 函数能为任意对象做深复制和浅复制
"""
import copy


class Bus:

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
bus2 = copy.copy(bus1)

bus3 = copy.deepcopy(bus1)
print([id(bus) for bus in (bus1, bus2, bus3)])

bus1.drop('Bill')
print(bus2.passengers)
print([id(bus.passengers) for bus in (bus1, bus2, bus3)])
print(bus3.passengers)
