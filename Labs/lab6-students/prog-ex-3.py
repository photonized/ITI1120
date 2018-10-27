def first_neg(l):
    i=0

    while i <= (len(l)-1):
        if l[i] < 0:
            return i
        i+=1
    return None