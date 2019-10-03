#Using python3.
def money_change(m):
    change = [1,5,10]
    counter = 0
    while m != 0:
        if (m - change[-1]) >= 0:
            m -= change[-1]
            counter +=1

        elif (m - change[1]) >= 0:
            m -= change[1]
            counter +=1

        elif (m - change[0]) >= 0:
            m -= change[0]
            counter +=1
    return counter



m = int(input())

print(money_change(m))