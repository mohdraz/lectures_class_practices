import time
from functools import lru_cache


@lru_cache(maxsize=16)
def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


t1 = time.time()
# print([fib(x) for x in range(10000)])
t2 = time.time()
# print(f"time took: {t2-t1} ")


def bunnyEars(bunnies):
    if bunnies == 0:
        return 0
    return 2 + bunnyEars(bunnies-1)

print(bunnyEars(10))
