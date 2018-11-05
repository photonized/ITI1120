def mystery(n):
    c=0
    while n > 1:
        n=n//2
        c+=1
    return c