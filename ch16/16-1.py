def simple_coroutine():                # 1
    print('-> coroutine started')
    x = yield                          # 2
    print('-> coroutine received:', x)


my_coro = simple_coroutine()
print(my_coro)                         # 3
print(next(my_coro))                   # 4
my_coro.send(42)                       # 5
# expect result:
"""
Trackback (most recent call last):     # 6
 ...
StopIteration
"""

# 1: define coroutine by generator function: 
#    there is yield keyword in function body

# 2: yield used in expression (right part of "="), 
#    if coroutine only accept value from customer, the generated value is None
#    this value is implicit appointed, 
#    because there is no expression in the right of yield.

# 3: the same way with creating generator, 
#    calling function get the generator object.

# 4: firstly call function next(...), because generator is not starting,
#    it doesn't stop in the yield sentence, 
#    so could not send value in the beginning

# 5: call this method, the yield expresion in coroutine definition body will 
#    calculate the value 42;
#    then the coroutine recover, executing until the next yield expression,
#    or the end of program

# 6: here, control flow to then end of coroutine definition body, 
#    throw StopIteration just like usual generator.

"""
coroutine can be one of 4 states.
current state can use inspect.getgeneratorstate(...) to get it,
this method can reply one of below strings:

'GEN_CREATED'
    waiting to be executed.

'GEN_RUNNING'
    the interpreter is running.

'GEN_SUSPENDED'
    stop in the yield expression

'GEN_CLOSED'
    executing end.

because the argument of method send() will become to the suspended yield expression's value,
so only when coroutine in GEN_SUSPENDED state, the method send can be called.

however, if the coroutine is not starting (that is, GEN_CLOSED state), the situation is different.
so always call next(my_coro) to activate the coroutine ---
also can call my_coro.send(None) to get the same effect.

after create coroutine, if send value except None to it immediately, will get below error:

>>> my_coro = simple_coroutine()
>>> my_coro.send(1729)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't send non-None value to a just-started generator


the first time call next(my_coro), this step usually is called "prime" the coroutine.
(that means, let  coroutine execute forward to the first yield expression, 
prepare for a staring coroutine using)


"""
