#Program to calculate the factorial of an inputted number using for while loop

# Input from user
num = int(input("Enter a number to calculate its factorial: "))

# Calculate factorial using while loop
factorial = 1
i = 1
while i <= num:
    factorial *= i
    i += 1

# Display the result
print(f"Factorial of {num} is: {factorial}")