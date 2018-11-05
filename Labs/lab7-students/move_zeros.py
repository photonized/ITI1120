def move_zeros_v1(L):
    tmp=[]
    for num in L:
        if not num==0:
            tmp+=[num]
    for num in L:
        if num==0:
            tmp+=[num]
    return tmp