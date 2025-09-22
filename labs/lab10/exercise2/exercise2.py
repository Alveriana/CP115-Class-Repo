age = int(input())
accident_count = int(input())

# Your code here
if age < 25:
    base_premium = 2400
elif age <= 50:
    base_premium = 1800
else:
    base_premium = 2000

discount_amount = 0
penalty_amount = 0

if accident_count == 0:
    discount_amount = 0.1 * base_premium
elif accident_count == 1 or accident_count == 2:
    penalty_amount = 300
elif accident_count >= 3:
    penalty_amount = 600

final_premium = base_premium - discount_amount + penalty_amount

print(int(base_premium))
print(int(final_premium))
print(int(discount_amount))