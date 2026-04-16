response = "y"

while response.lower() == "y":
    print("In the loop.")

    #
    sales = float(input("Enter your sales: "))
    comm_rate = float(input("Enter the commission rate:")) / 100
    commission = sales * comm_rate
    print("Your commission is: $", commission)
    #

    response = input("Continue?(y/n): ")

print("Thank you.")