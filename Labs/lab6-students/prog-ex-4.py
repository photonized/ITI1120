def sum_5_consecutive(l):
    if len(l) < 5:
        return False
    c=0
    for i in range(len(l)):
        if not i+4 > len(l):
            c+=l[i]
            if c == 0:
                return True
    return False


def sum_5_consecutive_v2(l):
    if len(l) < 5:
        return False
    i=0
    while i < len(l):
        c=0
        if not i+4 > len(l):
            c+=l[i]
            if c == 0:
                return True
        i+=1

    return False
