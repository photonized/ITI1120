import math
import turtle


###################################################################
# Question 1
###################################################################
def pythagorean_pair(a, b):
    """
    (int, int) -> boolean
    Returns True if two numbers form a pythagorean pair and False if not
    Precondition: The two numbers must be integers
    """

    c = a**2 + b**2

    return math.sqrt(c) % 1 == 0


###################################################################
# Question 2
###################################################################
def mh2kh(s):
    """
    (number) -> number
    Returns the number of miles per hour converted to miles per hour
    Preconditions: none
    """
    return s * 1.60934


###################################################################
# Question 3
###################################################################
def in_out(xs, ys, side):
    """
    (number, number, number) -> boolean
    Returns True if given query point is inside of the given square, False otherwise
    Preconditions: Side is a non-negative value
    """
    x = float(input("Enter a number for the x coordinate of a query point: "))
    y = float(input("Enter a number for the y coordinate of a query point: "))

    return xs <= x <= xs + abs(side) and ys <= y <= ys + abs(side)


###################################################################
# Question 4
###################################################################
def safe(n):
    """
    (int) -> boolean
    Returns True if n cannot be divided by 9 or contains a 9, False otherwise
    Preconditions: n is a non negative integer
    """
    return len(str(n))<=2 and abs(n) % 9 != 0 and "9" not in str(abs(n))


###################################################################
# Question 5
###################################################################
def quote_maker(quote, name, year):
    """
    (str, str, number) -> str
    Returns a produced sentence in the form of: In year, a person called name said: “quote”
    Preconditions: none
    """
    return "In " + str(year) + ", a person called " + str(name) + " said:" ' "' + str(quote) + '"'


###################################################################
#  Question 6
###################################################################
def quote_displayer():
    """
    (none) -> none
    Uses the functions quote_maker(quote, name, year) to print the string in human readable form after prompting user for the specific questions.
    Preconditions: none
    """
    quote = input("Give me a quote: ")
    name = input("Who said that? ")
    year = input("What year did she/he say that? ")

    print(quote_maker(quote, name, year))


###################################################################
# Question 7
###################################################################
def rps_winner():
    """
    (none) -> none
    Takes player 1 and player 2 input for Rock, Paper, Scissors and displays the result of the game.
    Preconditions: Input must only be rock, paper, or scissors, all in lower case.
    """
    x = input("What choice did player 1 make?\nType one of the following options: rock, paper, scissors: ")
    y = input("What choice did player 2 make?\nType one of the following options: rock, paper, scissors: ")

    print("Player 1 wins. That is", (x == "rock" and y == "scissors") or (x == "scissors" and y == "paper") or (x == "paper" and y == "rock"), "\nIt is a tie. That is not", x != y)


###################################################################
# Question 8
###################################################################
def fun(x):
    """
    (number) -> number
    Returns y = ln(x+3)/4ln10 as that is the isolated y variable from 10^(4y) = x + 3
    Preconditions: x must be a positive number
    """

    y = math.log(x + 3)/(4 * math.log(10))

    return y


###################################################################
# Question 9
###################################################################
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


###################################################################
# Question 10
###################################################################
def draw_car():
    """
    (none) -> none
    Returns a turtle drawing of a coloured simple car
    Preconditions: none
    """
    t = turtle.Turtle()
    s = turtle.Screen()

    #t.speed("fastest")

    t.penup()
    t.goto(-200, 0)
    t.pendown()
    t.begin_fill()
    t.color("black", "red")
    t.forward(400)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(400)
    t.left(90)
    t.forward(100)
    t.end_fill()

    t.penup()
    t.goto(-150, 100)
    t.pendown()
    t.begin_fill()
    t.color("black", "cyan")
    t.left(135)
    t.forward(100)
    t.right(45)
    t.forward(150)
    t.right(45)
    t.goto(90, 100)
    t.end_fill()

    t.penup()
    t.right(45)
    t.goto(-210, 0)
    t.pendown()
    t.begin_fill()
    t.color("black", "gray")
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(10)
    t.end_fill()

    t.penup()
    t.goto(190, 0)
    t.pendown()
    t.begin_fill()
    t.color("black", "gray")
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(10)
    t.end_fill()

    t.penup()
    t.goto(-20, 70)
    t.pendown()
    t.begin_fill()
    t.color("black", "black")
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(12)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(12)
    t.end_fill()

    t.penup()
    t.goto(180, 65)
    t.pendown()
    t.begin_fill()
    t.color("black", "orange")
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(30)
    t.end_fill()

    t.penup()
    t.goto(-200, 65)
    t.pendown()
    t.begin_fill()
    t.color("black", "dark red")
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(30)
    t.end_fill()

    t.penup()
    t.goto(75, 0)
    t.pendown()
    t.begin_fill()
    t.color("black", "black")
    t.circle(50)
    t.end_fill()

    t.penup()
    t.goto(-175, 0)
    t.pendown()
    t.begin_fill()
    t.color("black", "black")
    t.circle(50)
    t.end_fill()

    t.penup()
    t.goto(-155, 0)
    t.pendown()
    t.begin_fill()
    t.color("black", "gray")
    t.circle(30)
    t.end_fill()

    t.penup()
    t.goto(95, 0)
    t.pendown()
    t.begin_fill()
    t.color("black", "gray")
    t.circle(30)
    t.end_fill()

    t.penup()
    t.goto(120, 0)
    t.pendown()
    t.begin_fill()
    t.color("black", "black")
    t.circle(5)
    t.end_fill()

    t.penup()
    t.goto(-130, 0)
    t.pendown()
    t.begin_fill()
    t.color("black", "black")
    t.circle(5)
    t.end_fill()

    t.penup()
    t.goto(-125, 0)
    t.pendown()
    t.right(180)
    t.forward(35)
    t.goto(-125, 0)
    t.right(72)
    t.forward(35)
    t.goto(-125, 0)
    t.right(72)
    t.forward(35)
    t.goto(-125, 0)
    t.right(72)
    t.forward(35)
    t.goto(-125, 0)
    t.right(72)
    t.forward(35)

    t.penup()
    t.goto(125, 0)
    t.pendown()
    t.forward(35)
    t.goto(125, 0)
    t.right(72)
    t.forward(35)
    t.goto(125, 0)
    t.right(72)
    t.forward(35)
    t.goto(125, 0)
    t.right(72)
    t.forward(35)
    t.goto(125, 0)
    t.right(72)
    t.forward(35)

    t.penup()
    t.goto(-50, 0)
    t.pendown()
    t.right(144)
    t.forward(170.71)

    t.penup()
    t.goto(90, 0)
    t.pendown()
    t.right(0)
    t.forward(100)

    t.penup()
    t.goto(300, -50)
    t.pendown()
    t.left(90)
    t.forward(600)

    t.screen.exitonclick()


###################################################################
# Question 11
###################################################################
def alogical(n):
    """
    (number) -> number
    Returns the number of times that n has to be divided by two to be less or equal to 1 by using logarithmic functions
    Preconditions: number must be positive
    """
    return math.ceil(math.log(n, 2))


###################################################################
# Question 12
###################################################################
def time_format(h, m):
    """
    (int, int) -> str
    Returns detailed explanation of time using time notations such as "half past" and "o'clock" and rounds to the nearest 5 minutes
    Preconditions: h must be int between 0 and 23 and m must be int between 0 and 59
    """
    if(h>23 or m>59):
        return "Make sure that your hours are 0-23 and your minutes are 0-59"

    m = ((m+2)//5) * 5

    if (m == 30):
        return ("Half past " + str(h) + " o'clock")
    elif(m == 0):
        return (str(h) + " o'clock")
    elif(m > 30):
        if(h == 23):
            return (str(60 - m) + " minutes to " + str(0) + " o'clock")
        else:
            return (str(60 - m) + " minutes to " + str(h + 1) + " o'clock")
    elif(m < 30):
        return (str(m) + " minutes past " + str(h) + " o'clock")


###################################################################
# Question 13
###################################################################
def cad_cashier(price, payment):
    """
    (number, number) -> number
    Returns change to give back when given the price and the payment rounded to the nearest 5 cents
    Precondtions: payment must be bigger than price and both must be positive numbers with only 2 decimal points
    """
    change = ((payment - price + 0.02) // 0.05) * 0.05
    return (change)


###################################################################
# Question 14
###################################################################
def min_CAD_coins(price, payment):
    """
    (number, number) -> int, int, int, int, int
    Returns the change to give back to customer using the cad_cashier(price, payment) function to return the amount of each canadian coin to give back
    Preconditions: price must be less than payment and both must be positive numbers with 2 decimal places
    """

    dif = cad_cashier(price, payment) * 100

    toonie = (dif // 200)
    loonie = ((dif - (toonie * 200)) // 100)
    quarter = ((dif - (toonie * 200 + loonie * 100)) // 25)
    dime = ((dif - (toonie * 200 + loonie * 100 + quarter * 25)) // 10)
    nickel = ((dif - (toonie * 200 + loonie * 100 + quarter * 25 + dime * 10)) // 5)

    return int(toonie), int(loonie), int(quarter), int(dime), int(nickel)


