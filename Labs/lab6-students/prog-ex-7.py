def inner_product(x, y):
    if len(x)!=len(y) or len(x)==0 and len(y)==0:
        return None
    i=0
    a=0
    while i<len(x):
        a+=x[i]*y[i]
        i+=1
    return a