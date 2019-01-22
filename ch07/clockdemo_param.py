import time


DEFAULT_FMT = '[{elapsed:0.8f}s {name}({args}) -> {result}]'


def clock(fmt=DEFAULT_FMT):
    def decorate(func):
        def clocked(*_args):
            t0 = time.time()
            _result = func(*_args)
            elapsed = time.time() - t0
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args)
            result = repr(_result)
            print(fmt.format(**locals()))   # locals(): clocked 中的局部变量
            return _result
        return clocked
    return decorate


if __name__ == '__main__':

    @clock()                # 这里的调用必须带括号，因为它是装饰器工厂函数
    def snooze(seconds):
        time.sleep(seconds)

    for i in range(3):
        snooze(.123)

"""
clock 是参数化装饰器工厂函数
decorate 是真正的装饰器
clocked 包装被装饰的函数，clocked会取代被装饰的函数，因此它必须返回被装饰函数的值
decorate 返回 clocked
clock 返回 decorate
"""
