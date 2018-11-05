def doubles(l):
    for i in range(1, len(l)):
        if l[i] == l[i-1] * 2:
            print(l[i])

