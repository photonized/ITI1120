def longest_run(l):
    """
    (list) -> int
    Returns the count of the longest run in a list.
    Preconditions: the list can only contain floats and ints.
    """
    a = 1
    li = []
    if len(l) == 0:
        return 0
    if len(l) == 1:
        return 1
    for i in range(len(l)-1):
        if float(l[i]) == float(l[i+1]):
            a += 1
        else:
            li += [a]
            a = 1
    li += [a]
    return max(li)


number = input("Please input a list of numbers separated by space: ")
number = number.strip().split()
print(longest_run(number))
