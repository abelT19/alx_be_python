##Arithmetic Operations





   



# take inputs
num_1 = float(input("Enter first number: "))
num_2 = float(input("Enter second number: "))
operation = input("Enter operation (adder, substractor, multiplication, division): ")

# define functions
def adder(num_1, num_2):
    return num_1 + num_2

def substractor(num_1, num_2):
    return num_1 - num_2

def multiplication(num_1, num_2):
    return num_1 * num_2

def division(num_1, num_2):
    if num_2 != 0:
        return num_1 / num_2
    else:
        return "Error: Division by zero!"

# choose operation
if operation == "adder":
    print(adder(num_1, num_2))
elif operation == "substractor":
    print(substractor(num_1, num_2))
elif operation == "multiplication":
    print(multiplication(num_1, num_2))
elif operation == "division":
    print(division(num_1, num_2))
else:
    print("Invalid operation")

