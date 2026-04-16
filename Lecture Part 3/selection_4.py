height = int(input("Please enter your height in centimeters: "))

if height >= 400 or height <= 10:
    print("The height is invalid")
else:
    print(f"You are {height/100}m tall")