# Write a program that accepts 3 input from user and check which number is largest.
# for example:
# input1 is 5 and input2 is 10 and input3 is 15
# output should be 15 as this number is larger than 5 and 10

# SOLUTION :

no_1 = int(input("Enter first number :"))
no_2 = int(input("Enter second number :"))
no_3 = int(input("Enter third number :"))

if no_1 > no_2 and no_1 > no_3:
    print(no_1, "is larger than", no_2, "and", no_3)
elif no_2 > no_1 and no_2 > no_3:
    print(no_2, "is larger than", no_1, "and", no_3)
elif no_3 > no_1 and no_3 > no_2:
    print(no_3, "is larger than", no_1, "and", no_2)
else:
    print(no_1, "is equal to", no_2, "and", no_3)