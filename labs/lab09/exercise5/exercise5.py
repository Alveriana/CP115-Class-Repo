main_course = input()
drink = input()
dessert = input()
customer_age = int(input())

# TODO: Your code here
if main_course == "Chicken":
    main_course_price = 10
elif main_course == "Beef":
    main_course_price = 12
elif main_course == "Fish":
    main_course_price = 11

if drink == "Soft Drink":
    drink_price = 2
elif drink == "Coffee":
    drink_price = 3

if dessert == "Ice Cream":
    dessert_price = 4
elif dessert == "Cake":
    dessert_price = 5

food_cost = main_course_price + drink_price + dessert_price
service_charge = 0.1 * food_cost
final_bill = food_cost + service_charge

if customer_age > 60:
    final_bill *= 1-0.15
elif customer_age < 18:
    final_bill *= 1-0.1
    
print(f"{final_bill:.2f}")