# 0 1 2 3 4 5 6 7  8  9  10 ... <- index
# 0 1 1 2 3 5 8 13 21 34 55 ... <- Fibonacci number
# ^^^
# base cases
#
# fib(0): 0
# fib(1): 1
# fib(n): fib(n - 1) + fib(n - 2)

# Bottom-up dynamic programming
# Start from the base case and work up towards the number

def fib(n):
    f = [0,1]

    if n <= 1:
        return f[n]

    for i in range(2, n):
        # f[i] = f[i-1] + f[i-2]
        # f.append(f[i-1] +f[i-2])
        # next_fib = f[i-1] + f[i-2]
        next_fib = f[-1] + f[-2]
        f.append(next_fib)

    print(f)   
    return f[-1]

for i in range(0, 10):
    print(fib(i))