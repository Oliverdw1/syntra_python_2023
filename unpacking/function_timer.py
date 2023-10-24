import time


def func1(a, b):
    a = a**2
    b = b**3
    return a**b


def func2(a, b, c):
    return a+b+c


def time_it(func, rep, *args, **kwargs):
    start = time.perf_counter()
    for i in range(rep):
        func(*args, **kwargs)
    stop = time.perf_counter()
    print(stop-start)


time_it(func2, 100_000_000, 1, 2, c=3)
