"""
Write a program that takes an employee's salary and years of service as input. Calculate the bonus as follows:

If the years of service are less than 5, no bonus.
If the years of service are between 5 and 10, bonus is 10% of the salary.
If the years of service are more than 10, bonus is 20% of the salary.
Print the bonus amount.

"""

# SOLUTION :

salary = int(input("Enter salary:"))
years_of_service = int(input("Enter years of service:"))

if years_of_service < 5:
    print("No bonus")

elif years_of_service >= 5 and years_of_service <= 10:
    print("bonus is 10% of the salary:", salary * 0.1)

elif years_of_service > 10:
    print("bonus is 20% of the salary:", salary * 0.2)
else:
    print("Invalid years of service")