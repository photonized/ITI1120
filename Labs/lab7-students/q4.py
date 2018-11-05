def inBoth(l1, l2):
    if len(l1) > len(l2):
        for i in range(len(l1)):
            if l1[i] in l2:
                return True
    return False