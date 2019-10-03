#Using python3.
def maximum_loot(n,W,v,w):
    v_w_ratio = [x / y for x,y in zip(v,w)]
    value = 0

    while (W != 0) and (len(v_w_ratio) != 0):
        max_index = v_w_ratio.index(max(v_w_ratio))
        if (W - w[max_index]) >= 0:
            value += v[max_index]
            W -= w[max_index]
            v_w_ratio.pop(max_index)
            v.pop(max_index)
            w.pop(max_index)


        elif (W - w[max_index]) < 0:
            value += (v[max_index] / w[max_index]) * W
            W -= W
            v_w_ratio.pop(max_index)
            v.pop(max_index)
            w.pop(max_index)

    return value



number_of_items, knapsack_weight = map(int,input().strip().split())

values = []

weights = []

for i in range(number_of_items):
    values_i, weights_i = map(int,input().strip().split())
    values.insert(i,values_i)
    weights.insert(i,weights_i)

print(round(maximum_loot(number_of_items, knapsack_weight, values,weights),4))






