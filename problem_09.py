# Write a program that accepts 3 inputs from user. input 1 and input 2 should be numbers and the third input should be mathematical operator.
# Perform operation accordingly
# for example
# input1 is 5 and input2 is 10 and input3 is +
# then output should be 15
# input1 is 5 and input2 is 10 and input3 is *
# then output should be 50

no_1 = int(input("Enter first no:"))
no_2 = int(input("Enter second no:"))
operator = input("Enter an operator:(+ , - , * , /):")

if operator == "+":
    print(no_1 + no_2)
elif operator == "*":
    print(no_1 * no_2)
elif operator == "-":
    print(no_1 - no_2)
elif operator == "/":
    print(no_1 / no_2)
else:
    print("Invalid operator")