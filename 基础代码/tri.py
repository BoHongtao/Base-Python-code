    L=[1]
    while True:
        yield L
        L = [1] + [L[i-1]+L[i] for i in range(1,len(L))] +[1]

