# Fitness Membership
membership_cost = 120
personal_training_sessions = 80
num_of_session = 6
locker_rental = 25
towel_service = 15
registration_fee = 50

# Total cost calculation
first_month_cost = membership_cost + (personal_training_sessions * num_of_session) + locker_rental + towel_service + registration_fee
monthly_cost = membership_cost + (personal_training_sessions * num_of_session) + locker_rental + towel_service
annual_cost = first_month_cost + (11 * monthly_cost)

print(f" First Month Cost = RM{first_month_cost}")
print(f" Monthly Cost = RM{monthly_cost}")
print(f" Annual Cost = RM{annual_cost}")