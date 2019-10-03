import math

def change_problem(money, coins):
    # Use this variable to fill the stack with a temporary value.
    infinity_value = money + 1

    # dynamic programming stack that is filled first with big numbers.
    dp_stack = [infinity_value] * (money + 1)
    # have a value of 0 in the first element of the array.
    dp_stack.insert(0, 0)

    # get minimum coins needed for a change for each number from 1 till the amount of money given.
    for i in range(1, money + 1):
        # for each coin in the coins list.
        for j in range(len(coins)):
            # if the coin is less than the money of the sub problem in the dp_stack.
            if coins[j] <= i:
                num_coins = dp_stack[i - coins[j]] + 1
                if num_coins < dp_stack[i]:
                    dp_stack[i] = num_coins
    return dp_stack[money]



print(change_problem(11, [1, 2, 5]))



