applicant_age = int(input())
vision_test = input()
written_score = int(input())
driving_score = int(input())
medical_clearance = input()

# TODO: Your code here
requirement_met = 0

if applicant_age >= 18:
    requirement_met += 1
if vision_test == "Pass":
    requirement_met += 1
if written_score >= 80:
    requirement_met += 1
if driving_score >= 85:
    requirement_met += 1
if medical_clearance == "Pass":
    requirement_met += 1

if applicant_age < 18:
    if vision_test == "Pass" or written_score >= 80 or driving_score >= 85 or medical_clearance == "Pass":
        license_class = "Restricted License"
    else:
        license_class = "Application Denied"

elif vision_test == "Pass" and written_score >= 80 and driving_score >= 85:
    if applicant_age >= 21 and medical_clearance == "Pass":
        license_class = "Class A (Commercial)"
    else:
        license_class = "Class B (Regular)"

else:
    license_class = "Restricted License"


print(license_class)