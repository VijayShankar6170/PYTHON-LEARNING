# Program to calculate income tax based on salary and savings using nested if...else

# Input from user
basic_salary = int(input("Enter basic salary (in lakhs): "))
total_savings = int(input("Enter total savings (in lakhs): "))

# Tax calculation based on income slabs
if basic_salary < 2.5:
    # No tax for income less than 2.5 lakh
    tax = 0
    print(f"Income: {basic_salary} lakh")
    print(f"Tax: {tax}")
    
elif basic_salary >= 2.5 and basic_salary <= 5:
    # 0-5% tax for income 2.5 to 5 lakh (based on age groups)
    age = int(input("Enter age: "))
    
    if age < 30:
        tax_rate = 0
        tax = 0
    elif age >= 30 and age < 40:
        tax_rate = 2
        tax = (basic_salary * tax_rate) / 100
    elif age >= 40 and age < 50:
        tax_rate = 3
        tax = (basic_salary * tax_rate) / 100
    else:  # age >= 50
        tax_rate = 5
        tax = (basic_salary * tax_rate) / 100
    
    print(f"Income: {basic_salary} lakh")
    print(f"Age: {age}")
    print(f"Tax Rate: {tax_rate}%")
    print(f"Tax: {tax} lakh")

elif basic_salary > 5 and basic_salary <= 10:
    # 20% tax for income 5 to 10 lakh
    tax = (basic_salary * 20) / 100
    print(f"Income: {basic_salary} lakh")
    print(f"Tax Rate: 20%")
    print(f"Tax before savings deduction: {tax} lakh")
    
    # Tax savings under Sec 80C (up to 1.5 lakh investment saves up to 45,000)
    if total_savings > 0:
        if total_savings <= 1.5:
            # Savings up to 1.5 lakh: tax deduction = savings * 30% (approx)
            tax_saving = (total_savings * 30) / 100
        else:
            # Maximum savings of 45,000 (1.5 lakh * 30%)
            tax_saving = 0.45
        
        tax = tax - tax_saving
        print(f"Savings under Sec 80C: {total_savings} lakh")
        print(f"Tax saving: {tax_saving} lakh")
        print(f"Tax after savings deduction: {tax} lakh")
    else:
        print(f"Tax: {tax} lakh")

else:  # basic_salary > 10
    # Income above 10 lakh
    tax = (basic_salary * 30) / 100
    print(f"Income: {basic_salary} lakh")
    print(f"Tax Rate: 30%")
    print(f"Tax before savings deduction: {tax} lakh")
    
    # Tax savings under Sec 80C
    if total_savings > 0:
        if total_savings <= 1.5:
            tax_saving = (total_savings * 30) / 100
        else:
            tax_saving = 0.45
        
        tax = tax - tax_saving
        print(f"Savings under Sec 80C: {total_savings} lakh")
        print(f"Tax saving: {tax_saving} lakh")
        print(f"Tax after savings deduction: {tax} lakh")
    else:
        print(f"Tax: {tax} lakh")

print(f"\nFinal Payable Tax: {tax} lakh")
