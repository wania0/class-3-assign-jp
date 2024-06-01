"""
create the same ATM machine program that we do in last class.
features:
    allow only affiliated_card if age < 60
    allow govt employee regardless of age and affiliated_card
    charge 10 Rs more if grade is less than 18

# hint: filename: if_statement/if_with_nested_if.py
"""

# SOLUTION :

balance = 0
affiliated_card = True
senior_citizen = True
govt_employee = True
my_profit = 10

print("Your Current balance is :", balance)

deposit_amount = int(input("Enter the amount you want to deposit:"))
balance += deposit_amount

print("Now you can withdraw some amount. The total balance is:", balance)
withdraw_amount = int(input("Enter the amount you want to withdraw!"))

if withdraw_amount <= balance and senior_citizen:
    balance -= withdraw_amount
    print("After withdraw remaining balance is:", balance)
elif withdraw_amount <= balance and govt_employee:
    high_grade = int(input("Enter Your Grade:"))
    if high_grade < 18:
        withdraw_amount += my_profit
        print("Additional charge of 10 Rs is applied due to grade being less than 18.\n Now the withdraw amount is:",
              withdraw_amount)
        remaining_balance = balance - withdraw_amount
        print("Your remaining balance is:", remaining_balance)
    else:
        balance -= withdraw_amount
        print("after withdraw:", balance)
else:
    print("You are not allowed to withdraw this amount")
















        
    
    
    











