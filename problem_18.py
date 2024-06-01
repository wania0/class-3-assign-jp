"""
Write a program that takes the total amount of a purchase as input and applies a discount:

If the amount is less than $100, no discount.
If the amount is between $100 and $500, apply a 10% discount.
If the amount is more than $500, apply a 20% discount.
Print the final amount after the discount.

"""

# SOLUTION:

amount_of_purchase =input("Enter total amount of a purchase:(e.g $100):")
updated_amount = amount_of_purchase.replace("$","")
amount = int(updated_amount)

if amount < 100:
    print("No Discount")
elif amount >=100 and amount <= 500:
    current_amount = amount * 0.1
    discount = amount - current_amount
    print("Discount is 10%:", discount)
elif amount > 500:
    current_amount = amount * 0.2
    discount = amount - current_amount
    print("Discount is 20%:", discount)
else:
    print("Invalid amount of purchase")