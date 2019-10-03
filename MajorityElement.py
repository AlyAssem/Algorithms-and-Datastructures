#Using python3.
from collections import Counter
def majority_element(array):
    array_count = Counter(array)# a counter object of the given array.
    count_listing = array_count.most_common()#gives me a list of tuples containing elem and it's count
    for tuple in count_listing:
        if tuple[1] > len(array) // 2:
            return 1
    return 0
array_size = int(input())
array = list(map(int,input().strip().split()))
print(majority_element(array))

