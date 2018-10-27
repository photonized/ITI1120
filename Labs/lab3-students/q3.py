

def is_divisible(n,m):
    return n % m == 0

n = int(input("Enter an integer"))
def is_divisible23n8(n):
    if((is_divisible(n, 2) or is_divisible(n, 3)) and not is_divisible(n, 8)):
        return "yes"
    else:
        return "no"

if(is_divisible23n8(n) == "yes"):
    print(n, "is divisible by 2 or 3 but not 8")
else:
    print("It is not true that", n, "is divisible by 2 or 3 but not 8")