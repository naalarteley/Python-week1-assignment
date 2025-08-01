# Super Simple Calculator

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Enter +, -, *, or /: ")

if operation == "+":
    print("Answer:", a + b)
elif operation == "-":
    print("Answer:", a - b)
elif operation == "*":
    print("Answer:", a * b)
elif operation == "/":
    if b != 0:
        print("Answer:", a / b)
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid operation.")
