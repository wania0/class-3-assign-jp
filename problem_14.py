# Write a python program that accept user an input. The valid input should be of following
# - GREEN or gREEN or green etc
# - RED or red or rEd etc
# - YELLOW or yellow or yELlOw etc
# program should display the following message on checking above input
# Car is allowed to go
# Car has to wait
# Car has to stop
# invalid input

# SOLUTION :

color = input("Enter color(red , green , yellow):").lower()
if color == "green":
    print("Car is allowed to go")
elif color == "red":
    print("Car has to stop")
elif color == "yellow":
    print("Car has to wait")
else:
    print("Invalid input")