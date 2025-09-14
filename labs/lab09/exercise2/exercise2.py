employee_name = input()
total_income = float(input())
base_salary = int(input())
overtime_hours = int(input())
tax_status = input()

overtime_pay = overtime_hours * 35
total_income = base_salary + overtime_pay

# TODO: Your code here
if tax_status == "single":
    if total_income >= 5000:
        tax_rate = 0.22
    else:
        tax_rate = 0.12
elif tax_status == "married":
    if total_income >= 6000:
        tax_rate = 0.20
    else:
        tax_rate = 0.15
else:
    tax_status == "head"
    if total_income >= 5500:
        tax_rate = 0.25
    else:
        tax_rate = 0.19

tax_amount = total_income * tax_rate
epf = total_income * 0.11
socso = total_income * 0.005
net_salary = total_income - (tax_amount + epf + socso)

print(employee_name)
print(tax_rate)
print(f"{net_salary:.2f}")