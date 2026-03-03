# Program to illustrate implicit type conversion from int to float

# Declare an integer variable
num_int = 10

# Declare a float variable
num_float = 3.5

# Implicit type conversion: int is converted to float when added with float
result = num_int + num_float

print("Integer value:", num_int)
print("Type of num_int:", type(num_int))
print("\nFloat value:", num_float)
print("Type of num_float:", type(num_float))
print("\nSum:", result)
print("Type of result:", type(result))
