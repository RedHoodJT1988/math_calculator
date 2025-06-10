import math

def add(*args):
    return sum(args)

def subtract(a, b):
    return a - b

def multiply(*args):
    result = 1
    for num in args:
        result *= num

    return result

def divide(a, b):
    if b == 0:
        return ValueError("Error: Division by zero. This is not allowed")
    return a / b

def percentage(a, b):
    return (a * b) / 100

def square_root(a):
    if a < 0:
        return ValueError("Error: Negative value for square root")
    return math.sqrt(a)

def power(a, b):
    return a ** b

def validate_input(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def calculator():
    print("Simple Python Calculator")
    while True:
        print("\n Options:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Percentage")
        print("6. Square root")
        print("7. Power")
        print("8. Exit")

        choice = input("\n Choose an Operation ( 1 - 8): ")

        if choice == "1":
            numbers = input("Enter numbers to add, seperated by space: ").split()
            if all(validate_input(num) for num in numbers):
                print(f"Result: {add(*map(float, numbers))}")
            else:
                print("Invalid input. Please enter numbers")
        elif choice == "2":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print(f"Result: {subtract(a, b)}")
        elif choice == "3":
            numbers = input("Enter numbers to multiply, separated by space: ").split()
            if all(validate_input(num) for num in numbers):
                print(f"Result: {multiply(*map(float, numbers))}")
            else:
                print("Invalid input. Please enter numbers")
        elif choice == "4":
            a = float(input("Enter numerator: "))
            b = float(input("Enter denominator: "))
            print(f"Result: {divide(a, b)}")
        elif choice == "5":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print(f"Result: {percentage(a, b)}")
        elif choice == "6":
            a = float(input("Enter number: "))
            print(f"Result: {square_root(a)}")
        elif choice == "7":
            a = float(input("Enter base: "))
            b = float(input("Enter exponent: "))
            print(f"Result: {power(a, b)}")
        elif choice == "8":
            print("Goodbye")
            break
        else:
            print("Invalid choice. Please select a valid option")

calculator()
