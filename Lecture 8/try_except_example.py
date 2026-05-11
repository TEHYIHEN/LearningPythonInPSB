
try:
    height = float(input("Please enter your height: "))
    print("Your height is {}".format(height))
except ValueError:
    print("Please enter a number")