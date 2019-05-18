import time, timeit


def clock(func):
    def clocked(*args):
        t0 = timeit.default_timer()
        result = func(*args)
        elapsed = timeit.default_timer() - t0
        name = func.__name__
        print('[%0.8fs] %s' % (elapsed, name))
        return result

    return clocked
