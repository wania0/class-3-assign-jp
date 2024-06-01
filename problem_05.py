# Write a program to display the grade of the user in subject A, ask user marks obtained out of 100

# SOLUTION :

marks_obtained = int(input("Enter subject marks:"))
if marks_obtained >= 80:
    print("You got A-one garde")
elif marks_obtained >= 70:
    print("You got A grade")
elif marks_obtained >= 60:
    print("You got B grade")
elif marks_obtained >= 50:
    print("You got C grade")
elif marks_obtained >= 40:
    print("You got D grade")
else:
    print("Oops! You are fail.")