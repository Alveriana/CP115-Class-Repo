
# Getting user input (always returns a string)
item_name = input("Enter item name: ")

# Getting user input (always returns a float)
price = input("Enter price: ")

# Creates variables for quantity (3 items) and tax rate (6%)
quantity = 3
tax_rate = 0.06 

# Calculating subtotal, tax amount, and total cost
subtotal = float(price) * quantity
tax_amount = subtotal * tax_rate
total_cost = subtotal + tax_amount

# Formatted output using string concatenation
print()
print("Subtotal: " + str(subtotal))
print("Tax amount: " + str(tax_amount))
print("Total cost: " + str(total_cost))