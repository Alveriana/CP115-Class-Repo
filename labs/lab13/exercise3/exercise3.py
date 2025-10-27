
valid_count = 0
total = 0.0

while True:
    grade = float(input())

    if grade < 0:      # stop when a negative number is entered
        break

    if 0 <= grade <= 100:   # count only valid grades
        total += grade
        valid_count += 1
    # invalid grades are skipped automatically

# calculate average safely (avoid division by zero)
if valid_count > 0:
    average = total / valid_count
else:
    average = 0.0

print(valid_count)
print(f"{average:.2f}")