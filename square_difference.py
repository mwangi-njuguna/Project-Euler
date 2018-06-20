def sum_of_square(limit):
    my_list = []
    start = 1
    while start<=limit:
        square = start*start
        my_list.append(square)
        start+=1
        p = sum(my_list)
        if len(my_list)==limit:
            m = sum(my_list)
    return m

def square_of_sum(limit):
    list = []
    for a in range(1,limit +1):
        list.append(a)
        p = sum(list)
        if len(list)==limit:
		continue
    return p*p

def difference(limit):
    num_sum = square_of_sum(limit)-sum_of_square(limit)
    return num_sum

difference(10)
