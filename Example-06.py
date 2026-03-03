# Simple Interest Calculator
# Time period is fixed at 5 years

# Input from user
principal = eval(input("Enter the principal amount: "))
rate = eval(input("Enter the rate of interest (% per annum): "))

# Fixed time period
time = 5

# Calculate simple interest
simple_interest = (principal * rate * time) / 100

# Calculate amount payable
amount = principal + simple_interest

# Display results
print(f"\nPrincipal Amount: Rs. {principal}")
print(f"Rate of Interest: {rate}% per annum")
print(f"Time Period: {time} years")
print(f"Simple Interest: Rs. {simple_interest}")
print(f"Amount Payable: Rs. {amount}")
