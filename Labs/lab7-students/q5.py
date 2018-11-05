def intersect(l1, l2):
    b=[]
    if len(l1) > len(l2):
        for i in range(len(l1)):
            if l1[i] in l2:
                b+=[l1[i]]
    else:
        for i in range(len(l2)):
            if l2[i] in l1:
                b+=[l2[i]]

    return b