"""
Write a program that checks if a customer is eligible for a discount based on their membership status
and purchase amount:

If the customer is a member:
    If the purchase amount is $50 or more, print "Eligible for 10% discount".
    Otherwise, print "Eligible for 5% discount".
If the customer is not a member:
    If the purchase amount is $100 or more, print "Eligible for 5% discount".
    Otherwise, print "No discount".
"""

# SOLUTION:

membership_status = input("Enter membership status(yes or no):")
purchase_amount = input("Enter purchase amount:(e.g $100):")
update_amount = purchase_amount.replace("$","")
amount = int(update_amount)

if membership_status == "yes":
    if amount >= 50:
        print("Eligible for 10% discount")
    else:
        print("Eligible for 5% discount")
elif membership_status == "no":
    if amount >= 100:
        print("Eligible for 5% discount")
    else:
        print("No discount")
else:
    print("Invalid membership status")