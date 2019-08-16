def sushu():
    leaps = 1
    for i in range(101,200):
        for j in range(2,i):
            if (i % j == 0):
                leaps = 0
                break
        if leaps :
            print(i)
        leaps = 1



sushu()
