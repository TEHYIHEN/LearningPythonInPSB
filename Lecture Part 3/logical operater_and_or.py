from urllib import response

per_head_income = float(input("Please enter your per-head income: "))
POOR_THRESHOLD = 1643.5
housing_type = input("Public or Private : ")

#per_head_income < POOR_THRESHOLD
#if condition is true, continue the next rules #and housing_type.lower()
##if 2nd condition is true, then print the 1st result
#if condition is false, break the circuit, result to else print
if per_head_income < POOR_THRESHOLD and housing_type.lower() == "private":
    print("You are eligible for financial aid of $500 per head per month.")
else:
    print("Unfortunately you do not meet the requirements for aid")

print()
print("========Other Case==========")

response_1 = input("Are you a student in PSB (Y/N): ")
response_2 = input("Are you a staff in Marina Center (Y/N): ")

if response_1.upper() == "Y" or response_2.upper() == "Y":
    print("You are entitled to 15% discount")
else:
    print("Sorry, the discount is for student and staff only")