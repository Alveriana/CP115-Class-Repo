passing_count = 0
failing_count = 0
pass_rate = 0

score_input = input("Enter score (or 'end' to stop): ")

# TODO: Your code here
while score_input != "end":
    score = float(score_input)
    if score >= 60:
        passing_count += 1
        score_input = input("Enter score (or 'end' to stop): ")
    else:
        failing_count += 1
        score_input = input("Enter score (or 'end' to stop): ")

pass_rate = ( passing_count / (passing_count + failing_count) ) * 100


print(passing_count)
print(failing_count)
print(f"{pass_rate:.2f}")