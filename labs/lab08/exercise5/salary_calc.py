import employee_data

print(f" Basic Salary: {employee_data.basic_salary}")
print(f" Overtime Hours: {employee_data.overtime_hours}")
print(f" Overtime Rate: {employee_data.overtime_rate: .2f}")
overtime_pay = employee_data.overtime_hours * employee_data.overtime_rate
gross_salary = employee_data.basic_salary + overtime_pay

# Deduction
epf = gross_salary * 0.11
socso = gross_salary * 0.005
eis = gross_salary * 0.002
medical_insurance = 50
parking = 30
total_deduction = epf + socso + eis + medical_insurance + parking
net_salary = gross_salary - total_deduction

print(f" Overtime Pay: {overtime_pay:.2f}")
print(f" Total Salary: {gross_salary:.2f}")
print(f" EPF: {epf:.2f}")
print(f" SOCSO: {socso:.2f}")
print(f" EIS: {eis:.2f}")
print(f" Medical Insurance: {medical_insurance:.2f}")
print(f" Parking: {parking:.2f}")
print(f" Total Deduction: {total_deduction:.2f}")
print(f" Net Salary: {net_salary:.2f}")