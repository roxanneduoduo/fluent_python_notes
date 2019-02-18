class Class:
    data = 'the class data attr'

    @property
    def prop(self):
        return 'the prop value'


obj = Class()
print(vars(obj))
print(obj.data)
obj.data = 'bar'
print(vars(obj))
print(obj.data)
print(Class.data)
print()

print(Class.prop)
print(obj.prop)
try:
    obj.prop = 'foo'
except AttributeError as exc:
    print('AttributeError: {}'.format(exc))
obj.__dict__['prop'] = 'foo'
print(vars(obj))
print(obj.prop)
Class.prop = 'baz'
print(obj.prop)
print()

print(obj.data)
print(Class.data)
Class.data = property(lambda self: 'the "data" prop value')
print(obj.data)
del Class.data
print(obj.data)
print()
