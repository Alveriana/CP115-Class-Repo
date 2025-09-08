import menu_data

print(f" Welcome to the : {menu_data.restaurant_name} ")
print(f" Customer Number : {menu_data.customer_number} ")
print(f" All menu : {menu_data.menu_item1}, {menu_data.menu_item2}, {menu_data.menu_item3}")
print(f" Today's special is : {menu_data.daily_special_number}")


if menu_data.daily_special_number == 1:
    special = menu_data.menu_item1
elif menu_data.daily_special_number == 2:
    special = menu_data.menu_item2
else:
    special = menu_data.menu_item3

print(f"Today's special is: {special}")