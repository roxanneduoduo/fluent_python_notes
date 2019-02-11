from functools import wraps


def coroutine(func):
    """
    decorator: executing forward to the first `yield` expression, prime `func`
    """
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return primer


