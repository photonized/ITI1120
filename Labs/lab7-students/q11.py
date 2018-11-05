def inversions(s):
    c=0
    for i in range(len(s)):
        for j in range(0, i):
            if s[i]<s[j]:
                c+=1
    return c