# Uses python3
import random


def partition3(a, l, r):
    #  write your code here
    x = a[l]
    j = l
    z = 0
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    for k in range(j-1, -1, -1):
        if a[k] == a[j]:
            continue
        else:
            z = k
            break
    #  now we have regions that are at most x  and greater than x.

    return z, j

def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m1, m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1);
    randomized_quick_sort(a, m2 +1, r);
    return a

n = int(input())
a = list(map(int,input().strip().split()))
answer = randomized_quick_sort(a, 0, n-1)

for number in answer:
    print(number, end=" ")


