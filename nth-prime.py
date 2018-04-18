def prime(num):
    listy = []
    for i in range(1,num+1):
        if i > 1:
            for x in range(2,i):
                if i % x == 0:
                    break
            else:
                listy.append(i)
    print(listy[-1])
prime(10001)
