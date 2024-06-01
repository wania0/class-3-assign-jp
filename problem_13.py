# Write a program that accepts 3 input from user and check the second largest.
# for example:
# input1 is 5 and input2 is 10 and input3 is 15
# output should be 10 as this number is larger than 5 and smaller than 15

# SOLUTION:

no_1 = int(input("Enter first number:"))
no_2 = int(input("Enter second number:"))
no_3 = int(input("Enter third number:"))

if no_1 < no_2 < no_3:
    print("The second largest no is:", no_2 )

elif no_1 < no_3 < no_2:
    print("The second largest no is:",no_3 )

elif no_2 < no_1 < no_3:
    print("The second largest no is:",no_1 )

elif no_2 < no_3 < no_1:
    print("The second largest no is:", no_3 )

elif no_3 < no_1 < no_2:
    print("The second largest no is:", no_1 )

elif no_3 < no_2 < no_1:
    print("The second largest no is:", no_2)
else:
    print("All numbers are equal")
    