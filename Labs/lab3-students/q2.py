x = int(input("Enter 1st integer:"))
y = int(input("Enter 2nd integer"))
def is_divisible(x,y):
    return x % y == 0

if(is_divisible(x,y)==True):
    print(x, "is divisible by", y)
else:
    print(x, "is not divisible by", y)

z = int(input("Enter an integer"))