def m(i):

    if i==1:
        return i/((i*2)+1)
    else:
        return m(i-1)+(i/((i*2)+1))