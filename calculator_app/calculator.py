# ➗ Simple Calculator App

def calculator():
    print("➗ Welcome to the Calculator App!")

    num1 = float(input("Enter first number: "))
    operation = input("Choose operation (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2 if num2 != 0 else "Cannot divide by zero"
    else:
        result = "Invalid operation"

    print(f"Result: {result}")

if __name__ == "__main__":
    calculator()
