# Write a program that accepts 1 input from user and check if the number is divisible by 2 and 3 both.
# for example
# input1 is 10
# output should be "10 is only divisible by 2"
# input1 is 9
# output should be "9 is only divisible by 3"
# input1 is 12
# output should be "12 is divisible by 2 and 3"

# SOLUTION :

number = int(input("Enter any Number to check it is divisible by 2 and 3:"))

if number % 2 == 0 and number % 3 == 0:
    print("Number is divisible by 2 and 3")
elif number % 2 == 0:
    print("Number is only divisible by 2")
elif number % 3 == 0:
    print("Number is only divisible by 3")
else:
    print("Number is not divisible by 2 and 3")