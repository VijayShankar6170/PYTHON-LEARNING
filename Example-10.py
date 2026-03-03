# Four-function calculator using nested if...else

print("Four-Function Calculator")
print("-" * 40)

# Input numbers and operation
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

# if...elif...else to determine operation and calculate result
if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed!")
else:
    print(f"Error: '{operation}' is not a valid operation!")
