def fractional_knapsack(value, weight, capacity):
    # index = [0, 1, 2, ..., n - 1] for n items
    index = list(range(len(value)))
    # contains ratios of values to weight
    ratio = [v/w for v, w in zip(value, weight)]
    # index is sorted according to value-to-weight ratio in decreasing order
    index.sort(key=lambda i: ratio[i], reverse=True)
    max_value = 0
    fractions = [0]*len(value)
    
    for i in index:
        if weight[i] <= capacity:    #15<=20                        #10<=5
            fractions[i] = 1         #1  output
            max_value += value[i]    #24
            capacity -= weight[i]    #20-15= 5 remaining capacity
        else:
            fractions[i] = capacity/weight[i]                       #5/10 = 0.5 output
            max_value += value[i]*capacity/weight[i]                #15*0.5 = 7.5 + 24 = 31.5 output
            break
    
    return max_value, fractions

n = int(input('Enter number of items: '))  #3
value = input('Enter the values of the {} item(s) in order: '.format(n)).split() #24 15 25
value = [int(v) for v in value]
weight = input('Enter the positive weights of the {} item(s) in order: '.format(n)).split() #15 10 18
weight = [int(w) for w in weight]
capacity = int(input('Enter maximum weight: ')) #20

max_value, fractions = fractional_knapsack(value, weight, capacity) 
print('The maximum value of items that can be carried:', max_value)    #ans 31.5
print('The fractions in which the items should be taken:', fractions)  #ans 1, 0.5, 0