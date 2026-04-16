age = int(input("What is your age? "))
is_working = True
amount= 0

if age >= 65 and not is_working:
    amount = 1000
elif age >= 65 and is_working:
    amount = 600
elif age >= 21 and not is_working:
    amount = 500
elif age >= 21 and is_working:
    amount = 200

print(f"You will receive ${amount}")

print("======Nested if statements========")

if age >= 65:
    if is_working:
        amount = 1000
    else:
        amount = 600
elif age >= 21:
    if is_working:
        amount = 500
    else:
        amount = 200