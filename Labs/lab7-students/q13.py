def mssl(l):
    max=0
    for i in range(len(l)):
        count=0
        for j in range(i+1, len(l)):
            count+=l[j]
            if count>max:
                max=count
    return max