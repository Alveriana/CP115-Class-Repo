## Lab 10 - Test 3
monthly_usage = int(input())

discount = 0

#code
if monthly_usage < 50:
    discount = 0
elif monthly_usage <= 100:
    discount = 0.05
else:
    discount = 0.2

amount_paid = monthly_usage * (1-discount)

print(amount_paid)