def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply (a, b):
    return a * b
def divide(a, b):
    return a / b

while True:
    a = float(input("enter a number: "))
    b = float(input("enter a  number: "))
    
    addition = add(a, b)
    subtraction = subtract(a, b)
    multiplication = multiply(a, b)
    

    addition = 1
    subtraction = 2
    multiplication = 3
    division = 4

    operation = int(input("enter number between 1 to 5: 1 is for addition, 2 for subtraction, 3 for multiplying and 4 for division, 5 for exit: "))

    if operation == 1:
        print(" the sum is:", add(a, b))
    elif operation == 2:
        print("the difference is:", subtract(a, b))
    elif operation == 3:
        print("the product is:", multiply(a, b))
    elif operation == 4:
        if b == 0:
            print("Syntax Error")   
        else:
            print("the quotient is:", divide(a, b))
    elif operation == 5:
        print("Exiting calculator...")
        break
    else:
        print("invalid choice")





