position = input()
overtime_hours = int(input())
is_weekend = input()

# Your code here
if position == "Manager":
    hourly_rate = 35
elif position == "Supervisor":
    hourly_rate = 25
elif position == "Staff":
    hourly_rate = 18

overtime_rate = 1.5 * hourly_rate

if is_weekend == "Yes":
    overtime_rate += 5

overtime_pay = overtime_hours * overtime_rate
total_pay = overtime_pay

print(hourly_rate)
print(overtime_pay)
print(total_pay)