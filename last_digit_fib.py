# Uses python3

def get_fibonacci_last_digit_naive(n):
    fib_list = []
    fib_list_0 = fib_list.insert(0,0)

    fib_list_1 = fib_list.insert(1,1)
    for i in range(2,n+1):
        fib_list_i = (fib_list[i-1] + fib_list[i-2]) % 10
        fib_list.insert(i,fib_list_i)
    return fib_list[n]



n = int(input())
print(get_fibonacci_last_digit_naive(n))