# TODO: Your code here
found_number = False

for num in range (1, 101):
    if num % 7 == 0 and num % 13 == 0:
        found_number = num
        break

print(found_number)
