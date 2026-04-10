balance = 5000
annual_return = 0.10

num_years = 7

new_balance = balance * ((1 + annual_return) ** num_years)

print(f"Original balance  : ${balance:,.2f}")
print(f"My project balance: ${new_balance:,.2f}")
print()
print(f"Original balance  : ${balance:13,.2f}")
print(f"My project balance: ${new_balance:13,.2f}")
print()
print()

label_1 = "Original Investment"
label_2 = "Project Balance"
title = "My Investment"

print("=" * 56)
print(f"| {title:^52} |")   # ^ caret, circum accent
print("=" * 56)
print(f"| {label_1:24} | ${balance:24,.2f} |")
print("-" * 56)
print(f"| {label_2:24} | ${new_balance:24,.2f} |")
print("=" * 56)
print()
#make the title align to right
print(f"| {label_1:>24} | ${balance:,.2f} |")
print(f"| {label_2:>24} | ${new_balance:,.2f} |")