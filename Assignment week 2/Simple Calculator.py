def add(num1: float, num2: float) -> float:
    return num1 + num2
def subtract(num1: float, num2: float) -> float:
    return num1 - num2
def multiply(num1: float, num2: float) -> float:
    return num1 * num2
def divide(num1: float, num2: float) -> float:
    try:
        return num1 / num2
    except ZeroDivisionError:
        return "\nError: Division by zero is not allowed."
def get_input(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("\nInvalid input. Please enter a number.")
def calculator():
    operations = {
        1: ("Add", add, '+'),
        2: ("Subtract", subtract, '-'),
        3: ("Multiply", multiply, '*'),
        4: ("Divide", divide, '/')
    }
    while True:
        print("\nPlease select operation -")
        for key, (name, _, symbol) in operations.items():
            print(f"{key}. {name} ({symbol})")
        
        try:
            select = int(input("\nSelect operations from 1, 2, 3, 4 (or 0 to exit): "))
        except ValueError:
            print("\nPlease enter a number between 1 and 4.")
            continue

        if select == 0:
            break
        if select in operations:
            number_1 = get_input("Enter first number: ")
            number_2 = get_input("Enter second number: ")
            operation_name, operation_func, symbol = operations[select]
            result = operation_func(number_1, number_2)
            print(f"{number_1} {symbol} {number_2} = {result}")
        else:
            print("\nPlease select a valid operation.")

calculator()