# Program to calculate product of two integers using repeated addition

# Input two integers
num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))

# Calculate product using repeated addition
product = 0
for i in range(abs(num2)):
    product += num1

# Handle negative numbers
if num2 < 0:
    product = -product

# Display the result
print(f"Product of {num1} and {num2} is: {product}")
