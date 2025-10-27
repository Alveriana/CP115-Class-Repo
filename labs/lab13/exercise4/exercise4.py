number = float(input())

# TODO: Your code here
positive_count = 0
positive_sum = 0.0

while number > 0:
    if number == 0:
        break

    if number > 0:
         positive_sum += number
        positive_count += 1

print(positive_count)
print(f"{positive_sum:.2f}")