# Program to generate the table of a number using for loop

num = int(input("Enter a number: "))

print(f"Table of {num}:")
for i in range(1, 11):
    print(f"{num} × {i} = {num * i}")
