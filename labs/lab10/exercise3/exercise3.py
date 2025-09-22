monthly_income = int(input())
credit_score = int(input())
loan_amount = int(input())

# Your code here
requirement_met = 0

if monthly_income >= 4000:
    requirement_met += 1
if credit_score >= 600:
    requirement_met += 1
if loan_amount <= 5*monthly_income:
    requirement_met += 1



print(interest_rate)
print(max_loan_amount)
print(approval_status)