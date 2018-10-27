def fib(n):
    a=[1,1]
    i=2
    while i < n:
        a+=[a[i-1]+a[i-2]]
        i+=1
    return a