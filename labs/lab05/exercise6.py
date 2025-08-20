#Get input from users
minutes_time = float(input("Enter time in minutes: "))

#Change minutes to hours
hours_time = int(minutes_time // 60)
excess_time = int(minutes_time % 60)

#Display the output
print(f"{hours_time} Hours {excess_time} Minutes")