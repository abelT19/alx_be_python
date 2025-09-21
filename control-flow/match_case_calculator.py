# Get user input
number_1 = float(input("Enter the first number: "))
number_2 = float(input("Enter the second number: "))
operation = input("Choose an operation (+, -, *, /): ")

# Use match-case to perform the operation
match operation:
    case "+":
        print("Result:", number_1 + number_2)
    case "-":
        print("Result:", number_1 - number_2)
    case "*":
        print("Result:", number_1 * number_2)
    case "/":
        if number_2 != 0:
            print("Result:", number_1 / number_2)
        else:
            print("Error: Division by zero!")
    case _:
        print("Invalid operation")
