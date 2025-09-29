# The smart way - let Python count for you
print("Printing 5 receipts:")
for receipt_number in range(5):
    print(f"Receipt #{receipt_number + 1} printed")


# Single parameter: range(stop)
print("Basic range counting:")
for count in range(4):
    print(f"Count: {count}")


# Two parameters: range(start, stop)
print("Custom start and stop:")
for number in range(10, 15):
    print(f"Number: {number}")


# Three parameters: range(start, stop, step)
print("Counting by 3s:")
for value in range(0, 12, 3):
    print(f"Value: {value}")


# Counting by 5s
print("Counting by 5s:")
for value in range(0, 25, 5):
    print(f"Value: {value}")


# Basic while loop counter pattern
attempt = 1                    # Step 1: Initialize
while attempt <= 3:            # Step 2: Condition
    print(f"Attempt number: {attempt}")
    attempt += 1               # Step 3: Update