correct_password = "python123"
login_successful = "False"

# TODO: Your code here
attempts_used = 0

while attempts_used < 3:
    password = input("Enter your password: ")
    attempts_used += 1

    if password == correct_password:
        login_successful = True
        break

print(login_successful)
print(attempts_used)
