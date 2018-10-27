

def blue_collar():
    """
    string -> (number)
    :return:
    """


    y = float(input("How much do you get paid per hour?"))
    x = float(input("How many hours did you work?"))

    if(x <= 40):
        answer = x * y
    elif(x > 40 and x <= 60):
        answer = (y * (x - 40) * 1.5) + (y * 40)
    elif(x > 60):
        answer = (y * (x - 60) * 2) + (y * 20 * 1.5) + (y * 40)

    return answer


def rps(x, y):
    if(x != "R".lower() and x != "S".lower() and x != "P".lower()):
        print("Player 1 has to be P S or R!")
        return -1

    if (y != "R".lower() and y != "S".lower() and y != "P".lower()):
        print("Player 2 has to be P S or R!")
        return -1

    if(x == "R".lower() and y == "P".lower()):
        return 1
    elif(x == "P".lower() and y == "R".lower()):
        return -1
    elif (x =="S".lower() and y == "R".lower()):
        return 1
    elif(x == "R".lower and y == "S".lower()):
        return -1
    elif(x == "P".lower() and y == "S".lower()):
        return 1
    elif(x == "S".lower() and y == "P".lower()):
        return -1
    elif(x==y):
        return 0
