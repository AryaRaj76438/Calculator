import art

def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(art.logo)
    num1 = float(input("What's your first number?: "))

    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation from line above: ")
        num2 = float(input("Next number: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"type 'y' to continue calculating with {answer}, type 'n' to start a new calculation: ") == "y":
            num1 = answer
        else:
            should_continue = False
            print(f"Your final answer = {answer}")
            calculator()

calculator()