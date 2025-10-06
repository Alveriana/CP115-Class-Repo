num_days = int(input())
danger_threshold = float(input())

# TODO: Your code here
# Use input() inside the loop to get each day's temperature
danger_days = 0
total_temp = 0

for i in range (num_days):
    temp_reading = float(input())
    if temp_reading > danger_threshold:
        danger_days +=1

    total_temp += temp_reading

average_temp = total_temp/num_days


print(danger_days)
print(f"{average_temp:.1f}")