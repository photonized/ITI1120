def two_length_run(l):
    """
    (list) -> boolean
    Returns True if the list contains a series of repetitive numbers (run) and False if the list does not contain a
    series of repetitive numbers (run).
    Preconditions: the list can only contain floats and ints.
    """
    if len(l) < 2:
        return False
    for i in range(len(l)-1):
        if float(l[i]) == float(l[i+1]):
            return True
    return False


number = input("Please input a list of numbers separated by space: ")
number = number.strip().split()
print(two_length_run(number))
