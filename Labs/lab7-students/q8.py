def lastfirst(l):
    a=[]
    b=[]
    c=[]
    for i in range(len(l)):
        n=l[i].index(",")
        o=l[i].index(" ")
        a+=[l[i][:n]]
        b+=[l[i][o+1:]]
    c+=[a]+[b]
    return c


def better(L):
    fnames = []
    lnames = []

    for name in L:
        l, f = name.split(', ')
        fnames.append(f)
        lnames.append(l)

    return fnames, lnames