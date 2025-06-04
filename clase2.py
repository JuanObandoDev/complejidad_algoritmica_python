import time
import sys

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def factorial_iterative(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if __name__ == "__main__":
    n = 1000
    sys.setrecursionlimit(n + 10)
    
    start_time = time.time()
    factorial_iterative(n)
    end_time = time.time()
    print(end_time - start_time)

    start_time = time.time()
    factorial(n)
    end_time = time.time()
    print(end_time - start_time)