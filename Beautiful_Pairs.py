"""Description"""
# The function below should return an integer that represents the maximum-
# number of pairwise disjoint beautiful pairs that can be formed.
# beautifulPairs has the following parameters:
# A: an array of integers
# B: an array of integers
def beautiful_pairs(n, a, b):
    disjoint_pairs = []
    not_in_b = 0
    #looping through all elements in a and check if that element in list b.
    for i in range(n):
        if a[i] in b:
            # add the index of the 2 elements as a tuple in the disjoint_pairs.
            disjoint_pairs.append(("it is there"))
            b.remove(a[i])
        else: # if it is not in b list.
            not_in_b = a[i]
            continue
    if (len(b) != 0):
        b[0] = not_in_b
        disjoint_pairs.append("it is there")
    else:
        return len(disjoint_pairs) - 1

    return len(disjoint_pairs)


# size of 2 arrays and their elements as input.
n = int(input())
a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))

print(beautiful_pairs(n, a, b))
