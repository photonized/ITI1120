def pairSum(l, num):
    for i in range(len(l)):
        if num-l[i] in l:
            for j in range(i+1, len(l)):
                if l[j] == num-l[i]:
                    print(str(i) +" "+ str(j))