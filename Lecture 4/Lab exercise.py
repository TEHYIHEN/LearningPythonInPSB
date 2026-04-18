while True:
    number_a = float(input("Enter a number: "))
    number_b = float(input("Enter another number: "))
    total = number_a + number_b

    print("The sum is", total)

    response = input("Would you like to continue (y/n)? ").lower()

    if response != "y":
        break

print("Thank you.")

