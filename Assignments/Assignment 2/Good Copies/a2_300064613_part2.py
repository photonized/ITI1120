import math


def min_enclosing_rectangle(radius, x, y):
    """
    (float, float, float) -> float, float
    Returns the x and y coordinates of the minimum sized rectangle that can cover
    a circle when given the radius and the coordinates of the center of the circle.
    Preconditions: radius must be a positive float
    """
    xrecb = x-radius
    yrecb = y-radius

    xrect = x+radius
    yrect = y+radius

    if (xrect - xrecb < 0) or (yrect - yrecb < 0):
        return None

    return xrecb, yrecb


def series_sum():
    """
    (none) -> float
    Returns the series sum up to a given number. Series sum is 1000 + 1/1 + 1/2 + ... + 1/n
    Preconditions: Input must be a non negative integer.
    """
    n = input("Please enter a non negative integer: ")

    if not n.isdigit():
        return None

    a = 1000
    for i in range(1, int(n)+1):
        a += 1/(int(i)**2)

    return a


def pell(n: int):
    """
    (int) -> int
    Returns the Pell number of the given integer. For more information on how to calculate the Pell number,
    refer to https://en.wikipedia.org/wiki/Pell_number
    Preconditions: n must be a non negative integer.
    """
    if not str(n).isdigit():
        return None

    fpell = ((1+math.sqrt(2))**(n-2)-(1-math.sqrt(2))**(n-2))/(2*math.sqrt(2))

    spell = (((1+math.sqrt(2))**(n-1))-((1-math.sqrt(2))**(n-1)))/(2*math.sqrt(2))
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return round(2*spell + fpell)


def countMembers(s: str):
    """
    (str) -> int
    Returns the number of characters of s that are a part of a 'member' string.
    Preconditions: none
    """
    e = "efghijFGHIJKLMNOPQRSTUVWX23456!\,"

    a = 0
    for i in s:
        if i in e:
            a += 1

    return a


def casual_number(s):
    """
    (str) -> int
    Returns none if the string cannot be converted to an integer. Returns the integer without commas to
    show a bank balance.
    Preconditions: s must be able to convert to an integer.
    """
    a = ""
    for i in s:
        if i in ",":
            a += ""
        else:
            a += i

    if not a[1:].isdigit() or "-" in s[1:]: return None

    return int(a)


def alienNumbers(s):
    """
    (str) -> int
    Returns a string converted into alien numbers. Alien number chart provided on the assignment manual.
    Single line function challenge completed :)
    Preconditions: none
    """
    return s.count("T") * 1024 + s.count("y") * 598 + s.count("!") * 121 + s.count("a") * 42 + s.count("N") * 6 + s.count("U")


def alienNumbersAgain(s):
    """
    (str) -> int
    Returns a string converted into alien numbers using no string methods. Alien number chart provided on the assignment manual.
    :param s:
    :return:
    """
    t = "T"
    y = "y"
    e = "!"
    a = "a"
    n = "N"
    u = "U"

    c = 0
    for i in s:
        if i in t:
            c += 1024
        elif i in y:
            c += 598
        elif i in e:
            c += 121
        elif i in a:
            c += 42
        elif i in n:
            c += 6
        elif i in u:
            c += 1
    return c


def encrypt(s:str):
    """
    (str) -> str
    Returns an encrypted version of the string.
    Preconditions: none
    """
    p = len(s)-1
    a = ""
    for i in range((len(s)+1)//2):
        if i == (len(s)+1)//2-1 and not (len(s)) % 2 == 0:
            a += s[p]
        else:
            a += s[p]+s[i]
        p -= 1
    return a


def oPify(s):
    """
    (str) -> str
    Returns the OP version of the string provided. Returns a string with the letters o and p between
    every character of the string. The capitalization of the o and p is dependant on the capitalization of
    the character that it is next to. If the character is a non alphabet character, there is no oPifying.
    Preconditions: none
    """
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = upper.lower()
    a = ""

    for i in range(len(s)):
        if len(s) > 1 and i < len(s)-1:
            if (s[i] in upper or s[i] in lower) and (s[i+1] in lower or s[i+1] in upper):
                if s[i] in upper and s[i+1] in upper:
                    a += s[i]+"OP"
                elif s[i] in upper and s[i+1] in lower:
                    a += s[i]+"Op"
                elif s[i] in lower and s[i+1] in upper:
                    a += s[i]+"oP"
                elif s[i] in lower and s[i+1] in lower:
                    a += s[i]+"op"
            else:
                a += s[i]
        else:
            a += s[i]
    return a


def nonrepetitive(s):
    """
    (str) -> bool
    Returns False if the string of characters contains any length of substring that repeats itself. True if otherwise.
    Preconditions: none
    """
    tf=""
    for i in range(len(s)):
        for a in range(len(s)):
            s1 = s[i:a]
            s2 = s[a:a*2-i]
            if s1 == s2 and s2 != "" and s1 != "":
                tf += "t"
            else:
                tf += "f"
    if "t" in tf:
        return False
    return True
