def pair(l1, l2, num):
    for i in range(len(l1)):
        if num - l1[i] in l2:
            print(str(l1[i]) +" "+ str((num - l1[i])))
