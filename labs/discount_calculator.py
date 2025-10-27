# Movie tickets discount calculation (simple version)

age_input = input("Enter your age: ")

# Check if age is numeric (allow negative sign)
if not age_input.lstrip('-').isdigit():
    print("Error: Age must be a number.")
    quit()

age = int(age_input)

ticket_input = input("Enter the price of the movie ticket: ")

# Check if ticket price is numeric (allow one decimal point and negative sign)
if not ticket_input.replace('.', '', 1).lstrip('-').isdigit():
    print("Error: Ticket price must be a number.")
    quit()

ticket_price = float(ticket_input)

# Validate values
if age < 0 or ticket_price < 0:
    print("Error: Age or ticket price cannot be negative.")
    quit()

# Determine discount
if age <= 12:
    discount_category = "Children"
    discount = 0.5
elif age <= 17:
    discount_category = "Teenagers"
    discount = 0.25
else:
    discount_category = "Adults"
    discount = 0.0

# Calculate and display
discount_price = ticket_price * (1 - discount)

if discount > 0:
    print(f"You are eligible for the {discount_category} discount ({int(discount * 100)}% off).")
else:
    print(f"You are in the {discount_category} category. No discount applies.")

print(f"Discounted ticket price: ${discount_price:.2f}")
