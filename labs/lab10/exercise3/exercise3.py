monthly_income = int(input())
credit_score = int(input())
loan_amount = int(input())

# Your code here
interest_rate = 0.0
credit_tier = ""
max_loan_amount = 5 * monthly_income
approval_status = "Rejected"

#Approval Status
if monthly_income >= 4000 and credit_score >= 600 and loan_amount <= 5*monthly_income:
    approval_status = "Approved"

    if credit_score >= 700:
        credit_tier = "Excellent"
        interest_rate = 3.5
    elif credit_score >= 600:
         credit_tier = "Good"
         interest_rate = 5.5
    else:
        credit_tier = "Poor"

print(interest_rate)
print(max_loan_amount)
print(approval_status)