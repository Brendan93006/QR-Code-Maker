
def main():

    print("Welcome to Calculator!")

    print(f"|{'Addition':^10}|{'Subtraction':^13}|{'Multiplication':^16}|{'Division':^10}|{'Square Root':^13}|{'Square':^8}|{'Cube':^6}|{'Exponential':^13}|{'Absolute Value':^16}|{'Percentage':^12}|")

    arithmetic = (input("Pick a mathematical operation: ")).lower()

    valid_ops = ["addition", "subtraction", "multiplication", "division", "square root", "square", "cube", "exponential", "absolute value", "percentage"]

    two_value_ops = ["addition", "subtraction", "multiplication", "division", "exponential", "percentage"]

    if arithmetic not in valid_ops:
        print("Error: invalid operation")

    else:

        if arithmetic in two_value_ops:
            num1 = float(input("First Number: "))
            num2 = float(input("Second Number: "))
            if arithmetic == "addition":
                print(addition(num1, num2))
            elif arithmetic == "subtraction":
                print(subtraction(num1, num2))
            elif arithmetic == "multiplication":
                print(multiplication(num1, num2))
            elif arithmetic == "division":
                print(division(num1, num2))
            elif arithmetic == "exponential":
                print(exponentiate(num1, num2))
            elif arithmetic == "percentage":
                print(percentage(num1, num2))
            
        else:
            num = float(input("Provide Number: "))
            if arithmetic == "square root":
                print(square_root(num))
            elif arithmetic == "square":
                print(square(num))
            elif arithmetic == "cube":
                print(cube(num))
            elif arithmetic == "absolute value":
                print(absolute_value(num))


def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y == 0:
        return "Can't divide by 0."
    else:
        return float(x / y)

def exponentiate(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Can't take the square root of a negative number."
    else:
        return float(x ** 0.5)
    
def percentage(x, y):
    if y == 0:
        return "Error: can't get percent of 0"
    else:
        return float((x / y) * 100)

def absolute_value(x):
    return (x * x) ** 0.5

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

main()