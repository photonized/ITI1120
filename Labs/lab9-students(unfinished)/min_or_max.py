def min_or_max_index(l, b):

    value=l[0]
    ct=0
    if b==False:
        for i in range(len(l)-1):
            if l[i]>value:
                value=l[i]
                ct+=1
    elif b==True:
        for i in range(len(l)-1):
            if l[i]<value:
                value=l[i]
                ct+=1
    return (value, ct)
