def count_digits(n):

    if n<10:
        return 1
    else:
        return count_digits(n//10)+1