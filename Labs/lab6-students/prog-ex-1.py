def sum_odd_while_v2(n):
    """
    (int)->int
    Returns the sum of all odd integers between 5 and n
    """
    i=5
    c=0

    if n<5:
        return None
    while i<=n:
         c+=i
         i+=2
    return c


