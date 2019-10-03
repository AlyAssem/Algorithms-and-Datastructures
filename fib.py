# Uses python3
def calc_fib(n):
    fib_list = []
    fib_list_0 = fib_list.insert(0,0)

    fib_list_1 = fib_list.insert(1,1)
    for i in range(2,n+1):
        fib_list_i = fib_list[i-1] + fib_list[i-2]
        fib_list.insert(i,fib_list_i)
    return fib_list[n]


n = int(input())

print(calc_fib(n))

