def partition(arr, low, high):
    x = arr[low]
    j = low

    for i in range(low + 1, high + 1):
        if arr[i] <= x:
            j += 1
            arr[j], arr[i] = arr[i], arr[j]

    arr[low], arr[j] = arr[j], arr[low]
    return j


def quick_sort(array, low, high):
    if low >= high:
        return
    mid_pivot = partition(array, low, high)

    quick_sort(array, low, mid_pivot - 1)
    quick_sort(array, mid_pivot + 1, high)
    return array



array = [2,3,9,2,2]
print(quick_sort(array, 0, len(array) - 1))