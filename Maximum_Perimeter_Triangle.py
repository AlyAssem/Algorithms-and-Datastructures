"""Description"""
# It should return an array of  integers that represent the side lengths of the chosen triangle in non-decreasing order.
# maximumPerimeterTriangle has the following parameter(s):
# sticks: an integer array that represents the lengths of sticks available

def maximum_perimeter_triangle(sticks):
    #sort the array in a descending order.
    sticks.sort(reverse=True)
    #create a list that will contain the biggest 3 elements that could possibly be a non-degenerating triangle.
    non_degenerating_triangle = []
    for i in range(len(sticks) - 2): # keep iterating till the last 3 elements.
        # check whether the 2 numbers infront of the stick can form a non-degenerating triangle with it.
        if sticks[i] + sticks[i+1] > sticks[i+2]  and sticks[i+1] + sticks[i+2] > sticks[i] and sticks[i+2] + sticks[i] > sticks[i+1]:
            non_degenerating_triangle.append(sticks[i])
            non_degenerating_triangle.append(sticks[i+1])
            non_degenerating_triangle.append(sticks[i+2])
            # sort em in an ascending order.
            non_degenerating_triangle.sort()
            return " ".join(map(str, non_degenerating_triangle))  # join only works on string.

    return -1

#read the size of the array.
sticks_size = int(input())

#array of numbers that are candidates for creating a non-degenrating triangle
sticks = list(map(int,input().strip().split()))

print(maximum_perimeter_triangle(sticks))