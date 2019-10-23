def lcs(string_1, string_2):
    """Gets the longest common sub sequence for 2 Strings."""
    #  create a list of chars for each string that contains even an empty string.
    char_arr_1 = list(string_1)
    char_arr_1.insert(0, "")

    char_arr_2 = list(string_2)
    char_arr_2.insert(0, "")

    # create a dp table for the answers to each sub problem.
    dp_table = [[0 for row in range(len(char_arr_1))] for col in range(len(char_arr_2))]

    # for each row.
    for i in range(1, len(char_arr_2)):
        # fill all the columns.
        for j in range(1, len(char_arr_1)):
            # if the element in string 2 is equal to any of the elements in string 1.
            if char_arr_1[j] == char_arr_2[i]:

                # the cell value would be to remove the 2 chars from the array + 1 element added to the common sub seq.
                dp_table[i][j] = dp_table[i - 1][j - 1] + 1

            # if the element in string 2 does not match with the element in string 1.
            elif char_arr_1[j] != char_arr_2[i]:
                # the cell value would be to get the max of either removing last element of string 1 or last
                # element in string 2.

                dp_table[i][j] = max(
                    dp_table[i][j - 1], dp_table[i - 1][j]
                )

    # return the value of the longest common sub sequence of the whole 2 strings.

    return dp_table[i][j]


string_1 = input()
string_2 = input()

print(lcs(string_1, string_2))

"""Gets the longest common sub sequence for 2 arrays of numbers."""
# def lcs(arr_1, arr_2):
#     #  create a list of chars for each string that contains even an empty string.
#     char_arr_1 = list(arr_1)
#     char_arr_1.insert(0, "")
#
#     char_arr_2 = list(arr_2)
#     char_arr_2.insert(0, "")
#
#     # create a dp table for the answers to each sub problem.
#     dp_table = [[0 for row in range(len(char_arr_1))] for col in range(len(char_arr_2))]
#
#     # for each column.
#     for i in range(1, len(char_arr_2)):
#         # fill the entire row.
#         for j in range(1, len(char_arr_1)):
#             if char_arr_1[j] == char_arr_2[i]:
#                 dp_table[i][j] = dp_table[i - 1][j - 1] + 1
#
#             elif char_arr_1[j] != char_arr_2[i]:
#                 dp_table[i][j] = max(
#                     dp_table[i][j - 1], dp_table[i - 1][j]
#                 )
#
#     return dp_table[i][j]
#
#
# size_1 = int(input())
#
# arr_1 = list(map(int, input().strip().split()))[:size_1]
#
# size_2 = int(input())
#
# arr_2 = list(map(int, input().strip().split()))[:size_2]
#
# print(lcs(arr_1, arr_2))
