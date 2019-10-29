# Using python 3.
"""Gets the maximum value of an arithmetic operation."""


#  e.g. (5 - 8 + 7 * 4 - 8 + 9) = 200.


def get_operation(a, b, op):
    if op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        return a + b


def min_max(i, j, op, m, M):
    minimum = float("inf")
    maximum = float("-inf")
    for k in range(i, j):  # Try all possible last operations to do
        # e.g. (5 - 8 + 7) could be either((5 - 8) + 7) so last operation is + or (5-(8+7)) so last operation is -.

        # using all these patterns because if the last operation to be done is a multiplication for example,
        # you would want to have the minimum of the 2 numbers, or if it was a subtraction,
        # you would want to have the maximum of the first number and the minimum of the second number, etc...
        a = get_operation(M[i][k], M[k + 1][j], op[k])
        b = get_operation(M[i][k], m[k + 1][j], op[k])
        c = get_operation(m[i][k], M[k + 1][j], op[k])
        d = get_operation(m[i][k], m[k + 1][j], op[k])
        minimum = min(minimum, a, b, c, d)
        maximum = max(maximum, a, b, c, d)
    return minimum, maximum


def max_arithmetic_expression(expression):
    # The 2 at the end of the slice makes u skip 1 element.
    operations = expression[1: len(expression):2]

    numbers = expression[0:len(expression):2]

    size = len(numbers)

    # minimum values for sub problems (being the minimum value of applying an operation to 2 numbers).
    m = [[0 for _ in range(size)] for _ in range(size)]

    # max values for sub problems.
    M = [[0 for _ in range(size)] for _ in range(size)]

    # filling the main diagonal in both dp_tables.
    for i in range(size):
        # meaning that a number on it's own doesn't have any operation so it just gives the same number.
        m[i][i] = int(numbers[i])
        M[i][i] = int(numbers[i])

    # number of diagonals to fill above the main diagonal to get the max value for operations(0, size).
    for s in range(1, size):
        # number of rows in each diagonal.
        for i in range(size - s):
            # so that i can move in a stair case manner(diagonally).
            # meaning at s = 1 , first 2 elements then 2nd 2 elements then 3rd 2 elements (0, 1), (1, 2), (2, 3).
            j = i + s

            # calculating the minimum and maximum to each sub problem.
            m[i][j], M[i][j] = min_max(i, j, operations, m, M)

    return M[0][size - 1]



expression = input()

print(max_arithmetic_expression(expression))
