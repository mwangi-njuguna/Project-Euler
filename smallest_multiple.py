def smallest_m(limit):
    start = 1
    while True:
        if all(start % i == 0 for i in range(limit, 1,-1)):
            print(start)
            break
        else:
            start+=1

smallest_m(20)
