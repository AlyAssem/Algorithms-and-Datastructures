# Using python3.
def max_amount_gold(bag_weight, gold_bars):
    """Gets the maximum number of gold bars that could be stored in a bag of given weight."""
    # 2d array to store the solution to each sub problem, being the max amount of gold could be taken in the ith weight.
    dp_table = [[0 for _ in range(bag_weight + 1)] for _ in range(len(gold_bars))]

    # for each gold bar.
    for i in range(len(gold_bars)):
        # for each bag weight.(0, 1, 2....bag weight).
        for j in range(bag_weight + 1):
            # if the bar weight is less than or equal to the bag weight.
            if gold_bars[i] <= j:
                # the maximum amount that could be put into that bag is either the previous bar
                # or the current bar + 1 of the previous bars that could fit in with the current bar.
                dp_table[i][j] = max(
                    dp_table[i - 1][j],
                    dp_table[i - 1][j - gold_bars[i]] + gold_bars[i]
                )
                # if the bar weight is greater than the bag weight just take the previous bars that could fit into bag.
            else:
                dp_table[i][j] = dp_table[i - 1][j]

    # returns the maximum amount of gold bars that could fit into the bag of the given weight.
    return dp_table[i][j]


bag_weight, number_gold_bars = input().split()

gold_bars = list(map(int, input().strip().split()))[:int(number_gold_bars)]

print(max_amount_gold(int(bag_weight), gold_bars))
