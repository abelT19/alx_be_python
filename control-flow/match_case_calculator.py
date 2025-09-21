number_1 = float(input("Enter the first number: "))
number_2 = float(input("Enter the second number: "))
operation = operation = input("Choose the operation (+, -, *, /): ")
match operation:
    case "+":
        print("The Result is", number_1 + number_2)
    case "-":
        print("The Result is", number_1 - number_2)
    case "*":
        print("The Result is", number_1 * number_2)
    case "/":
        if number_2 != 0:
            print("The Result is", number_1 / number_2)
        else:
            print("Error: Division by zero!")
    case _:
        print("Invalid operation")




