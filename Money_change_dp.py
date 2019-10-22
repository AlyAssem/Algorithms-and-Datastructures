#Using python3.
import math
def money_change(money):
    """changes an amount of money with the minimum number of coins."""

    denominations = [1, 3, 4]

    # an array containing the solution to each of the sub problem.
    dp_arr = [0] * (money + 1)
    # loop through all elements of dp except for 0th element since min number of coins needed are 0 anyways.
    for i in range(1, len(dp_arr)):
        dp_arr[i] = math.inf
        # loop through the denominations for each sub problem to get the best denomination to pick.
        for j in range(len(denominations)):
            if i >= denominations[j]:
                # for each coin num_coins is the answer for each denomination - money and adding 1 for the coin used.
                num_coins = dp_arr[i - denominations[j]] + 1

                # use the if to get the min. number of denomination for each sub problem.
                if num_coins < dp_arr[i]:
                    dp_arr[i] = num_coins

    return dp_arr[len(dp_arr) - 1]



money = int(input())

print(money_change(money))
