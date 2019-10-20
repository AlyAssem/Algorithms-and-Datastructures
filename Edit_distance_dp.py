def edit_distance(string_1, string_2):
    """gets the minimum number of operations needed to transform 1 string to another."""
    # you can either replace, insert or delete a character.

    # first string char array including if the string was empty.
    char_arr_1 = list(string_1)
    char_arr_1.insert(0,'')

    # second string char array including if the string was empty.
    char_arr_2 = list(string_2)
    char_arr_2.insert(0, '')

    # create a 2d array that stores the answers for each sub problem.
    # e.g. dp_table[0][0] says how to convert an empty string to another empty string.
    # e.g. dp_table[1][1] says how to convert a 1 element string to another 1 element string.
    dp_table = [[0 for row in range(len(char_arr_1))] for col in range(len(char_arr_2))]

    for i in range(len(char_arr_2)):
        for j in range(len(char_arr_1)):

            # if the u want to convert from a string to an empty string.
            # e.g. if u have 2 chars in ur string u would have 2 operations to delete the 2 chars to have an empty str.
            if i == 0:
                dp_table[i][j] = j

            # if the u want to convert from an empty string to a string with characters.
            # e.g. if u want ur empty string to be converted to a 2 chars string u would have to insert 2 chars.
            elif j == 0:
                dp_table[i][j] = i

            # if the 2 characters in both strings are the same, no operation is needed.
            # al -> ml no operation is needed for L so i will just need to take the number of operations needed to -
            # convert a to m.
            elif char_arr_1[j] == char_arr_2[i]:
                dp_table[i][j] = dp_table[i - 1][j - 1]

            # if the chars in both strings are not the same.
            elif char_arr_1[j] != char_arr_2[i]:
                # do 1 operation(insert, delete, replace) and add it to the min option.
                # for "al" to become "ml" it is just 1 operation which is(for 'a' to become 'm').

                # e.g. "aly" to "ml"
                dp_table[i][j] = 1 + min(dp_table[i - 1][j - 1],  # for "al" to become "m"(2 operations)
                                         dp_table[i - 1][j],  # for "aly" to become "m"(3 operations)
                                         dp_table[i][j - 1]   # for "al" to become "ml"(1 operation)
                                         # apparently 3rd option is the best.
                                         )

    # return the last element in the table which says the min number of operations to transform a whole string
    # to another string.
    return dp_table[i][j]






string_a = input()
string_b = input()
print(edit_distance(string_a, string_b))