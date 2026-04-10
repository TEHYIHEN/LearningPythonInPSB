# #1
# your_name = input("What is your name:")
# your_street = input("Key in your street:")
# your_city = input("Key in your city:")
# your_state = input("Key in your state:")
# your_zipcode = input("Key in your zipcode:")
# your_phone_number = input("Key in your phone number:")
# your_college_major = input("Key in your college major:")
#
# print(your_name)
# print(f"{your_street},\n{your_zipcode} {your_city},\n{your_state}")
# print(your_phone_number)
# print("Your college major:",your_college_major)
#
# print()
# print()
# #2
# pound = 0.454
#
# mass_of_object = int(input("Key in your mass of object:"))
# total_kg = mass_of_object * pound
#
# print(f"Total mass equal to {total_kg}kg")
#
#
# print()
# print()
# #3
# mile_driven = int(input("Key in your mile driven:"))
# gallons = int(input("Key in your gallons:"))
#
# MPG = mile_driven / gallons
# print(f"Result MPG is {MPG}")

#4
item = ["Apple", "Banana" , "Cherry" , "Donut" , "Egg" ]
print(f"We have 5 item: {item}")
#customer_selected = input("Key in for check price:")

apple_price = 1
banana_price = 2
cherry_price = 3
donut_price = 4
egg_price = 5

print(f"Apple price: {apple_price} \n"
      f"Banana price: {banana_price} \n"
      f"Cherry price: {cherry_price} \n"
      f"Donut price: {donut_price} \n"
      f"Egg price: {egg_price} \n")
# if customer_selected == "Apple" :
#     print(apple_price)
# elif customer_selected == "Banana" :
#     print(banana_price)
# elif customer_selected == "Cherry" :
#     print(cherry_price)
# elif customer_selected == "Donut" :
#     print(donut_price)
# elif customer_selected == "Egg" :
#     print(egg_price)

customer_buy_item = []
def buy_item():
    customer_buy_item.append(item)

buy_item()


