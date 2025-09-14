employee_name = input()
base_salary = float(input())
overtime_hours = int(input())
tax_status = input().lower()

overtime_pay = overtime_hours * 35
total_income = base_salary + overtime_pay

# TODO: Your code here
if tax_status == "single":
    if total_income >= 5000:
        tax_rate = 0.22
    else:
        tax_rate = 0.18
elif tax_status == "married":
    if total_income >= 6000:
        tax_rate = 0.20
    else:
        tax_rate = 0.15
elif tax_status == "head":
    if total_income >= 5500:
        tax_rate = 0.25
    else:
        tax_rate = 0.19
else:
    tax_rate = 0.0  # Default case if tax_status is invalid

after_tax = total_income * ( 1- tax_rate )
net_salary = after_tax * (1 - 0.11 - 0.005)

print(employee_name)
print(f"{int(tax_rate*100)}%")
print(f"{net_salary:.2f}")