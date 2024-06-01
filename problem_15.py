"""
Write a program that takes two numbers as input and prints:

"First number is greater" if the first number is greater than the second number.
"Second number is greater" if the second number is greater than the first number.
"Both numbers are equal" if the two numbers are equal.

"""

# SOLUTION :

no_1 = int(input("Enter first number:"))
no_2 = int(input("Enter second number:"))

if no_1 > no_2:
    print("First number is greater")
elif no_2 > no_1:
    print("Second number is greater")
else:
    print("Both numbers are equal")