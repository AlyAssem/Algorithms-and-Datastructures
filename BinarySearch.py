#Using python3.
def binary_search(arr, low, high, key):# list, first element index, last element index, key searching for.
    # array is empty.
    if high < low:
        return -1
    # middle index of the array.
    mid_point = low + (high - low) // 2
    #check if the middle term of the array is the key we are searching for.
    if key == arr[mid_point]:
        #if yes return the middle term index.
        return mid_point
    #if the key is < than the middle term we decrease the problem with the array that is smaller than the middle term.
    elif key < arr[mid_point]:
        return binary_search(arr, low, mid_point - 1, key)
    #if the key is > than the middle term we decrease the problem with the array that is bigger than the middle term
    else:
        return binary_search(arr, mid_point + 1, high, key)

x =list(map(int,input().strip().split()))
x_size = x.pop(0)
x2 =list(map(int,input().strip().split()))
x2_size = x2.pop(0)
x3 = []
for elem in x2:
    x3.append(binary_search(x, 0, x_size - 1, elem))
print(*x3)

