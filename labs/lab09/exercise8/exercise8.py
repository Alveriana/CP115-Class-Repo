monthly_income = int(input())
employment_status = input()
credit_rating = input()
employment_years = int(input())

# TODO: Your code here
number_approval = 0

if monthly_income >= 3000:
    number_approval += 1
if employment_status in ["permanent" , "contract"]:
    number_approval += 1
if credit_rating in ["good" , "excellent"]:
    number_approval += 1
if employment_years >= 2:
    number_approval += 1

if number_approval == 4:
    approval_status = "Approved"
elif number_approval == 3:
    approval_status = "Conditionally Approved"
else:
    approval_status = "Rejected"

print(approval_status)