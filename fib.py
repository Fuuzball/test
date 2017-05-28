import numpy as np

def fib(n, x0 = 0, x1 = 1):
    if n <= 0:
        return x0
    if n == 1:
        return x1
    return fib(n-1) + fib(n-2)

print [ fib(n) for n in range(10) ]
print [ fib(n, 1, 1) for n in range(10) ]
