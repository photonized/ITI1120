def count_pos(l):
    """
    (list) -> int
    Returns the number of positive numbers inside of a list of numbers.
    Preconditions: list has to only contains ints and floats.
    """
    a = 0
    for i in range(len(l)):
        if float(l[i]) > 0:
            a += 1
    return a


number = input("Please input a list of numbers separated by space: ")
number = number.strip().split()
print("There are " + str(count_pos(number)) + " positive numbers in your list.")
