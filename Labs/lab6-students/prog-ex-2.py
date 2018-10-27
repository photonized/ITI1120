flag = True
while flag:
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")

    if not num1.isdigit() or not num2.isdigit():
        print("You need to input an integer.")
    else:
        print(int(num1) + int(num2))

    again = input("Do you want to continue this and try again? ")
    again = again.lower().strip()

    if not again == "yes":
        flag = False