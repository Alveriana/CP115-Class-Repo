import random
import math

# Get input from user
name = input("Enter your name: ")
student_id = input("Enter your student ID: ")
age = int(input("Enter your age: "))
course_code = input("Enter your course code: ")
course_name = input("Enter your course name: ")

# Generate two random score (70-95 and 79-100)
score_1 = random.randint(70, 95)
score_2 = random.randint(79, 100)

# Calculate total 
total_score = score_1 + score_2

# String operations
name_upper = name.upper()
name_lower = name.lower()
name_length = len(name)

# Calculate square root of total score
square_root = math.sqrt(total_score)