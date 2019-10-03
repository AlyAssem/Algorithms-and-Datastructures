"""Description"""
#The function should return a long integer that represents the minimum miles necessary.
# marcsCakewalk has the following parameter(s):
# calorie: an integer array that represents calorie count for each cupcake

def marc_cake_walk(n, cupcakes): #number of cupcakes and array of them
    #input = [5, 10, 7]   #ouput = 10*(2^0) + 7*(2^1) + 5*(2^2) miles to walk
    minimum_miles = 0
    #sort the list from biggest to smallest.
    cupcakes.sort(reverse = True)
    for i in range(0, n):
        #take the biggest element in the list and multiply it by the smallest power.
        miles_to_add = cupcakes.pop(0) * (2 ** i)

        minimum_miles += miles_to_add
    return minimum_miles


number_cupcakes = int(input())

cupcakes = list(map(int,input().strip().split()))

print(marc_cake_walk(number_cupcakes, cupcakes))