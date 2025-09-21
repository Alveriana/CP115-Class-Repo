position = input()
overtime_hours = int(input())
is_weekend = input()

# TODO: Your code here
if position == "Manager":
    base_hourly_rate = 30
elif position == "Supervisor":
    base_hourly_rate = 20
elif position == "Staff":
    base_hourly_rate = 15
elif position == "Intern":
    base_hourly_rate = 8

if overtime_hours <= 8:
    overtime_pay = overtime_hours * base_hourly_rate * 1.5
else:
    overtime_pay = (8 * base_hourly_rate * 1.5) + ((overtime_hours - 8) * base_hourly_rate * 2.0)

if is_weekend == "Yes":
    overtime_pay += 5 * overtime_hours

print(overtime_pay)