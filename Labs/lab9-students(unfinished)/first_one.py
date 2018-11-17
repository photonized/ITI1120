def first_one(L):
    s=0
    e=len(L)-1
    avg = (s + e) // 2

    if L[0]==1:
        return 0

    if L[len(L)-1]==0:
        return -1

    while L[avg]!=1 or L[avg-1]!=0 or L[avg+1]!=1:

        if L[avg]==0 and L[avg+1]==0:
            s=avg+1
        elif L[avg]==1 and L[avg-1]==1:
            e=avg-1
        else:
            return avg+1
        avg = (s + e) // 2
    return avg
