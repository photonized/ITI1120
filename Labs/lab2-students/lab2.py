import math


def repeater(s1: str, s2: str, n: int):

    result = "_" + (s1 + s2) * n + "_"

    return result


def roots(a: float, b: float, c: float):

    discrim = (b**2) - (4*a*c)

    x1 = (-b + math.sqrt(discrim)) / (2*a)
    x2 = (-b - math.sqrt(discrim)) / (2*a)

    print("The quadratic equation with the coefficients a = " + str(a) + ", b = " + str(b) + ", c = " + str(c) +
          " has the following solutions (i.e roots):\n" + str(x1) + " and " + str(x2))


def real_roots(a: float, b: float, c: float):

    discrim = (b**2) - (4*a*c) > 0

    return discrim


def reverse(x: int):

    first = (x % 10)
    second = (x - first) // 10

    return first * 10 + second


