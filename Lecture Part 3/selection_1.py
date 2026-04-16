print("-- Cashier --")

amount = float(input("How much spent?"))

if amount > 200:
    print("Oh you spend more than $200")
    print("Applying discount...")
    amount = round(amount * 0.95 ,2)
print(f"You need to pay: ${amount}")