def merge(l_arr, r_arr):
    lnr_arr = []
    while (len(l_arr) != 0) and (len(r_arr) != 0):
        l1 = l_arr[0]
        r1 = r_arr[0]
        if l1 <= r1:
            lnr_arr.append(l1)
            l_arr.remove(l1)
        else:
            lnr_arr.append(r1)
            r_arr.remove(r1)

    while len(l_arr) != 0:
        lnr_arr.append(l_arr.pop(0))

    while len(r_arr) != 0:
        lnr_arr.append(r_arr.pop(0))


    return lnr_arr

def merge_sort(array):# 14 7 3 12
    if len(array) == 1:
        return array
    mid_point = len(array) // 2 # equals (2) at first
    left_array = merge_sort(array[:mid_point])
    right_array = merge_sort(array[mid_point:])
    lnr_array = merge(left_array, right_array)
    return lnr_array


print(merge_sort([14,7,3,12]))

