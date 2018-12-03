def is_palindrome(a):
    if len(a)==0:
        return False
    if len(a)==1:
        return True
    elif len(a)==2 and a.lower()[0]==a.lower()[-1]:
        return True
    else:
        return is_palindrome(a[1:-1]) and a.lower()[0]==a.lower()[-1]


def is_palindrome_v2(a):

    if len(a)==0:
        return True
    if not a[0].isalpha():
        return is_palindrome_v2(a[1:])
    if not a[-1].isalpha():
        return is_palindrome_v2(a[:-1])
    if a[0].lower()!=a[-1].lower():
        return False

    return is_palindrome_v2(a[1:-1])



def is_palindrome_ashwin(a):
    if len(a)==0:
        return True
    if a[0] != a[-1]:
        return False

    else:
        return is_palindrome(a)


def gcd(a,b):
    if b==0:
        return a
    return gcd(b, a%b)
