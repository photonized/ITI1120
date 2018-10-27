def ascii_name_plaque(name: str):
    """
    (str) -> none
    Takes string as input and creates a printed "plaque" for the string in ASCII
    Preconditions: none
    """
    st = "*" + str("  __" + name + "__  ") + "*\n"
    star = "*" * (len(st)-1) + "\n"
    space = "*" + (" " * (len(st)-3)) + "*\n"
    print(star + space + st + space + star)


def split_tester(N:str, d:str):
    """
    (str, str) -> bool
    Takes two strings as a input, splits the first value into int(d) sized bits. Returns True if the bits are
    increasing every time, and False otherwise.
    Preconditions: N and d must be able to be converted to positive integers.
    """
    cont1 = ''
    tf = ''
    n = str(N)
    d = int(d)

    for i in range(len(n) // d):
        accum = n[d * i:(d * i) + d]

        if int(d) == len(n):
            print(n)
            return True
        else:

            if i == len(n) // d - 1:
                accum = n[d * i:(d * i) + d]
                print(accum, end='\n')

                if cont1 < int(accum):
                    tf += "f"
                elif cont1 > int(accum):
                    tf += "t"

                if "f" in tf:
                    return False
                else:
                    return True
            else:

                cont1 = int(n[d * i + d: d * i + 2 * d])
                print(accum, end=", ")

                if cont1 < int(accum):
                    tf += "f"
                elif cont1 > int(accum):
                    tf += "t"
                elif cont1 == int(accum):
                    tf += "f"


ascii_name_plaque("Welcome to my increasing-splits tester")
name = input("What is your name? ")
name = name.strip()
message = name + ", welcome to my increasing-splits tester."
ascii_name_plaque(message)
ta = "Try again."
flag = True

while flag:

    question = input(name + ", would you like to test if a number admits an increasing-split of give size? ")
    question = (question.strip()).lower()

    if question == 'no':
        ascii_name_plaque("Good bye " + name)
        flag = False

    elif question == 'yes':

        N = input("Good choice!\nEnter a positive integer: ")
        N = N.strip()
        accumu = ""

        for char in N:

            if char in "-":
                accumu += ""
            else:
                accumu += char

        if not accumu.isdigit() or "-" in N[1:]:
            flag = True
            print("The input can only contain digits. " + ta)

        elif "-" in N[0] or int(accumu) == 0:
            flag = True
            print("The input has to be a positive integer. " + ta)

        else:
            d = input("Input the split. The split has to divide the length of " + N + " i.e. " + str(len(N)) + "\n")
            d = d.strip()

            accumu = ""

            for char in d:
                if char in "-":
                    accumu += ""
                else:
                    accumu += char

            if not accumu.isdigit() or "-" in d[1:]:
                flag = True
                print("The input can only contain digits. " + ta)

            elif "-" in d[0] or int(accumu) == 0:
                flag = True
                print("The input has to be a positive integer. " + ta)

            else:
                if len(str(N)) % int(d) == 0:
                    if split_tester(N, d):
                        flag = True
                        print("The sequence is increasing")
                    else:
                        flag = True
                        print("The sequence is not increasing")
                else:
                    flag = True
                    print(d + " does not divide " + str(len(N)) + " " + ta)
    else:
        print("Please enter either yes or no. " + ta)

