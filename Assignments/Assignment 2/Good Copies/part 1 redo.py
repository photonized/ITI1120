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


def split_tester(number: str, divisor: str):
    """
    (str, str) -> bool
    Takes two strings as a input, splits the first value into int(d) sized bits. Returns True if the bits are
    increasing every time, and False otherwise.
    Preconditions: N and d must be able to be converted to positive integers.
    """
    cont1 = ''
    tf = ''
    n = str(number)
    div = int(divisor)

    for i in range(len(n) // div):
        accum = n[div * i:(div * i) + div]

        if int(div) == len(n):
            print(n)
            return True
        else:

            if i == len(n) // div - 1:
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

                cont1 = int(n[div * i + div: div * i + 2 * div])
                print(accum, end=", ")

                if cont1 < int(accum):
                    tf += "f"
                elif cont1 > int(accum):
                    tf += "t"
                elif cont1 == int(accum):
                    tf += "f"


def num_checker(num):
    """
    (string) -> boolean
    Returns True if a given string is an integer and False if otherwise. Checks the number for any negative symbols at position
    0 of the string, and checks if the string is a digit. Prints error messages accordingly.
    Preconditions: input must be a string
    """
    ta = "Try again."
    accumu = ""

    for char in num:

        if char in "-":
            accumu += ""
        else:
            accumu += char

    if not accumu.isdigit() or "-" in num[1:]:
        print("The input can only contain digits. " + ta)
        return False
    elif "-" in num[0] or int(accumu) == 0:
        print("The input has to be a positive integer. " + ta)
        return False
    return True


def input_numbers():
    """
    (none) -> none
    Takes user input and then calls a function to check the numbers, and then calls a different function
    if the number checker returns true.
    Preconditions: none
    """
    number = input("Good choice!\nEnter a positive integer: ")
    number = number.strip()

    if num_checker(number):
        d = input("Input the split. The split has to divide the length of " + number + " i.e. " + str(len(number)) + "\n")
        d = d.strip()

        if num_checker(d):
            increase_tester(number, d)


def increase_tester(number, divisor):
    """
    (str, str) -> none
    Tests if a sequence of numbers is increasing based on what the split_tester returns and if the number inputs are
    of correct format. Prints messages according to the numbers being inputted from the string.
    Preconditions: input must be two strings
    """
    ta = "Try again."
    if len(str(number)) % int(divisor) == 0:
        if split_tester(number, divisor):
            print("The sequence is increasing")
        else:
            print("The sequence is not increasing")
    else:
        print(divisor + " does not divide " + str(len(number)) + ". " + ta)


def yes_or_no():
    """
    (none) -> none
    Prints a message.
    Preconditions: none
    """
    ta = "Try again."
    print("Please enter either yes or no. " + ta)


ascii_name_plaque("Welcome to my increasing-splits tester")
nm = input("What is your name? ")
nm = nm.strip()
message = nm + ", welcome to my increasing-splits tester."
ascii_name_plaque(message)
flag = True

while flag:

    question = input(nm + ", would you like to test if a number admits an increasing-split of give size? ")
    question = (question.strip()).lower()

    if question == 'no':
        ascii_name_plaque("Good bye " + nm)
        flag = False
    elif question == 'yes':
        input_numbers()
    else:
        yes_or_no()
