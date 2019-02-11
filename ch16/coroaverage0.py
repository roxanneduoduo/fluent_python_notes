def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total/count


coro_avg = averager()
next(coro_avg)    # prime coroutine

for value in (10, 30, 5):
    avg = coro_avg.send(value)
    print(avg)

