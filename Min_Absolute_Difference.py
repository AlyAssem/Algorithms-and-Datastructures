# The minimumAbsoluteDifference function below.
# It should return an integer that represents the minimum absolute difference between any pair of elements.
# minimumAbsoluteDifference has the following parameter(s):
# n: an integer that represents the length of arr
# arr: an array of integers

def min_absolute_difference(arr, n):
    arr.sort()
    min_difference = arr[-1] - arr[0]
    for i in range(1, n):
        if arr[i] - arr[i - 1] < min_difference:
            min_difference = arr[i] - arr[i - 1]
    return min_difference

array_size = int(input())

array = list(map(int,input().strip().split()))

print(min_absolute_difference(array, array_size))