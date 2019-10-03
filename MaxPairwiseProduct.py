#using python 3
import unittest

input_number = int(input())
input_list = list(map(int, input().split()))

if len(input_list) == input_number :
    max1 = max(input_list)
    input_list.remove(max1)
    max2 = max(input_list)
    out = max1 *max2

    print(out)

else:
    print("Enter a list with the proper number of elements")



if __name__ == '__main__':
    unittest.main()