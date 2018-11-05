def four_letter(l):
    b=[]
    for i in range(len(l)):
        if len(l[i]) == 4:
            b+=[l[i]]
    return b