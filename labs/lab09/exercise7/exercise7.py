student_gpa = float(input())
total_score = int(input())
number_extracurricular = int(input())
completed_interview = input()

# TODO: Your code here
requirement_met = 0

if student_gpa >= 3.0:
    requirement_met += 1
if total_score >= 1200:
    requirement_met += 1
if number_extracurricular >= 1:
    requirement_met += 1
if completed_interview == "Yes":
    requirement_met += 1

if requirement_met == 4:
    admission_status = "Accepted"
elif requirement_met == 3:
    admission_status = "Waitlisted"
else:
    admission_status = "Rejected"


print(admission_status)