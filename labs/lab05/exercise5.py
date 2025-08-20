# Getting input from users
mark1 = int(input("Enter mark 1:"))
mark2 = int(input("Enter mark 2:"))
mark3 = int(input("Enter mark 3:"))

# Calculating total_score, average
total_score = int(mark1 + mark2 + mark3)
average = float(total_score / 3)

# Displaying the output
print("Your mark 1 is " + str(mark1))
print("Your mark 1 is " + str(mark2))
print("Your mark 1 is " + str(mark3))
print("Your total mark is " + str(total_score))
print("Your average mark is " + str(round((average))))