def sublist(l1, l2):
    tf=""
    for i in range(len(l2)):
        if l1[0] == l2[i]:
            for j in range(i, len(l1)):
                if l1[j] in l2[i:]:
                    tf+="t"
                else:
                    tf+="f"
    if "f" in tf:
        return False
    return True