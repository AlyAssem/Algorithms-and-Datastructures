
def lis(arr):
    """calculates the number of elements in the biggest sub sequence in an array."""

    # creates a table with the default values of 1 for each sub problem.
    # LIS(for array with 1 element), LIS(for array with 2 elements), LIS(for array with 3 elements) etc..
    sub_problems_table = [1] * len(arr)

    # for all elements in the arr but the 1st elem.
    for j in range(1, len(arr)):
        for i in range(j):
            # check if any of the previous elements is less than the current element.
            # also if the previous element should be added to the longest sub sequence or not.
            if arr[j] > arr[i] and sub_problems_table[i] + 1 > sub_problems_table[j]:
                sub_problems_table[j] = sub_problems_table[i] + 1

    return max(sub_problems_table)





array = list(map(int, input().split()))

print(lis(array))