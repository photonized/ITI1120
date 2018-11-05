def subsetSum(l, target):
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if target-l[i]-l[j] in l:
                return True
    return False