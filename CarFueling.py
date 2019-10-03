#Using Python3.
def min_refills(total_distance, full_tank, number_stops, stops):
    x = []
    x.insert(0, 0)
    x.extend(stops)
    x.append(total_distance)
    num_refills = 0
    current_refill = 0
    while current_refill <= number_stops:
        last_refill = current_refill
        while ((current_refill <= number_stops) and (x[current_refill+1] - x[last_refill] <= full_tank)):
            current_refill +=1
        if current_refill == last_refill:
            return -1
        if current_refill <= number_stops:
            num_refills +=1
    return num_refills




total_distance =  int(input())
full_tank = int(input())
number_stops = int(input())
stops = list(map(int,input().strip().split()))


print(min_refills(total_distance, full_tank, number_stops, stops))























































