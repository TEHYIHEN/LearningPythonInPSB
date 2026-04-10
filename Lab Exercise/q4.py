SALES_TAX_RATE = 0.07

item_1_price = float(input("Enter the item price: "))
item_2_price = float(input("Enter the item price: "))
item_3_price = float(input("Enter the item price: "))
item_4_price = float(input("Enter the item price: "))
item_5_price = float(input("Enter the item price: "))

total_amount = (item_1_price + item_2_price + item_3_price + item_4_price + item_5_price)

sales_tax = total_amount * SALES_TAX_RATE
nett_amount = total_amount + sales_tax

print(f"Total amount before tax: {total_amount:.2f}")
print(f"Sales tax: {sales_tax:.2f}")
print(f"Nett amount: {nett_amount:.2f}")