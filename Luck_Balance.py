"""Description"""
# The function should return an integer that represents the maximum luck balance achievable.
# luckBalance has the following parameter(s):
# k: the number of important contests Lena can lose
# contests: a 2D array of integers where each  contains two integers that represent the luck balance
# and importance of the ith contest.

def max_luck_balance(k, contests):
    # input: [[5,1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]] ...... output: 5 + 2 + 8 + 10 + 5 - 1
    #can only lose 3 important contests (k = 3)
    maximum_luck_balance = 0

    contests.sort(reverse=True)
    for contest in contests:
        # if it is an unimportant contest u can just add it to the maximum luck balance as a loss.
        if contest[1] == 0:
            maximum_luck_balance += contest[0]
        else: # if it is an important contest.
            if k != 0:
                maximum_luck_balance += contest[0]
                k -=1
            else:
                maximum_luck_balance -= contest[0]

    return maximum_luck_balance



#read a line containing number of contests and number of max times to lose important contests.
contests_number, max_allowed_lose_number  =  list(map(int,input().strip().split()))

#read a 2d array containing luck value for each contest and the importance of each contest.
contests_arr = []
for i in range(contests_number):
    contests_arr.append(list(map(int,input().strip().split())))


print(max_luck_balance(max_allowed_lose_number, contests_arr))