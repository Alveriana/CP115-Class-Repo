import math

#Get input from user
number = int(input("Enter a number: "))

#Calculate square and cubes
square_root = math.sqrt(number)
square = number ** 2
cube = number ** 3
sine_value = math.sin(number)

#Display the results
print(f"Square root of {number} is {square_root:.2f}")
print(f"Square of {number} is {square}")
print(f"Cube of {number} is {cube}")
print(f"Sine of {number} is {sine_value:.2f}")