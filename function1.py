#Excersise 1 Calculator
def Addition(a,b):
    return(a+b)
def Subtraction(a,b):
    return(a-b)
def Multiplication(a,b):
    return(a*b)
def Division(a,b):
    return(a / b)
num1 = int(input("Enter first number="))
num2 = int(input("Enter second number="))
print("please select your choice")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

while(True):
    choice = int(input("Enter your choice="))
    if choice == 1:
        result = num1 + num2
        print("Result", result)
    elif (choice == 2):
        result = num1 - num2
        print("Result", result)
    elif (choice == 3):
        result = num1 * num2
        print("Result", result)
    elif (choice == 4):
        result = num1 / num2
        print("Result", result)
    else:
        print("Wrong choice")
Addition(a,b)
Subtraction(a,b)
Multiplication(a,b)
Division(a,b)
