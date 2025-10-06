age_count = 0
total_age = 0
average = 0

age_input = input(" Enter age (or 'done' to end): ")

# TODO: Your code here
while age_input != "done":
    age = float(age_input)
    total_age += age
    age_count += 1
    age_input = input(" Enter age (or 'done' to end): ")

average_age = total_age / age_count

print(age_count)
print(total_age)
print(f"{average_age:.2f}")
