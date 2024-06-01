# Write a program to check if year is leap year.
# Note: search on google of what leap year is.

year = int(input("Enter year to check its leap year or not:"))
if year % 4 == 0:
    print("This is leap year")
else:
    print("This is not a leap year")