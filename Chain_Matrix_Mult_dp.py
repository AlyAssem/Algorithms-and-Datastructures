def matrix_chain_mult(m):
    """Gets the minimum cost of multiplying a chain of matricies together."""
    # number of matrices.
    n = len(m) - 1
    cost_table = [[float("inf")] * (n + 1) for _ in range(n + 1)]

    # multiplying 1 matrix dimensions have no cost.
    for i in range(n):
        # e.g. cost_table[0][1] means the first matrix of size(40 * 20).
        cost_table[i][i + 1] = 0

    # starting from having 3 dimensions of minimum 2 matrices to multiply together.
    for s in range(2, n + 1):
        # looping for the first and 2nd matrix.
        # then for 3 matrices.
        # then for 4 matrices ..... etc..
        for i in range(n - s + 1):
            # setting an end point to the looping of k.
            j = i + s
            # start from having 3 dimensions(2 matrices)
            for k in range(i + 1, j):
                cost_table[i][j] = min(cost_table[i][j],
                                       cost_table[i][k] + cost_table[k][j] + m[i] * m[j] * m[k]
                                       )
    # returns the min cost of multiplying all dimensions together.
    return cost_table[0][n]


# There are 4 matrices in this array.(40 * 20), (20 * 30), (30 * 10), (10 * 30) sizes.
m = [40, 20, 30, 10, 30]
print(matrix_chain_mult(m))
