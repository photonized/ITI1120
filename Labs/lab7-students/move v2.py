def move_zeros_v2(L):
    for i in L:
        if i == 0:
            L.append(0)
            L.remove(i)