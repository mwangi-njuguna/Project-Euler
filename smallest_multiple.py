def smallest_m():
    start = 1
    while True:
        if all(start % i == 0 for i in range(20, 1,-1)):
            print(start)
            break
        else:
            start+=1

smallest_m()
