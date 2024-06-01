# Write a program that accepts 2 inputs from user and check which number is largest.
# for example:
# input1 is 5 and input2 is 10
# output should be 10 as this number is larger than 5

# SOLUTION :

no_1 = int(input("Enter first number :"))
no_2 = int(input("Enter second number :"))

if no_1 > no_2:
    print(no_1, "is larger than", no_2)
elif no_2 > no_1:
    print(no_2, "is larger than", no_1)
else:
    print(no_1, "is equal to", no_2)