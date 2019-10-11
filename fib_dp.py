def fib_dp(n):
    if n <= 1:
        return n
    else:
        prev, current = 0, 1
        for i in range(n - 1):
            new_current = prev + current
            prev, current = current, new_current
        return current


print(fib_dp(150))